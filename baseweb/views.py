from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .models import DocumentUpload
from .forms import DocumentUploadForm
from django.http import HttpResponseRedirect, JsonResponse
from .processing_toolkit import check_csv_eligibility
from existing_premiums_api.models import ExistingMedicalPremium
import pandas as pd
from decimal import Decimal

def create_entries_from_csv(csv):
    df = pd.read_csv(csv)

    # Drop any missing data
    df = df.dropna()

    # Change any yes or nos to booleans
    df['smoker'] = df['smoker'].replace({"yes":True, "Yes":True, "no": False, "No":False})


    # With the remaning data, add it to the database.
    for entry in df.iterrows():
        entry_data = entry[1]

        new_entry = ExistingMedicalPremium(
                                rf_age = entry_data.age,
                                rf_gender = entry_data.sex,
                                rf_bmi = entry_data.bmi,
                                rf_children = entry_data.children,
                                rf_is_smoker = entry_data.smoker,
                                rf_region = entry_data.region,
                                premium = entry_data.expenses,
                                )
        new_entry.save()
    return {}



class LandingPageView(TemplateView):
    template_name = "landing_page.html"

class UploadPageView(View):
    template_name = "upload_page.html"
    form_class = DocumentUploadForm

    def get(self, request):
        context = {}
        context['unprocessed_uploads'] = DocumentUpload.objects.filter(has_been_converted=False)
        context['form'] = self.form_class
        return render(request, self.template_name, context)

    def post(self, request):
        if request.method == "POST":
            form = DocumentUploadForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            else:
                context = {}
                context['unprocessed_uploads'] = DocumentUpload.objects.filter(has_been_converted=False)
                context['form'] = form
                return render(request, self.template_name, context)


            return redirect('/uploads/')

def GetDocumentStatusAjax(request):
    if request.method == "GET":
        object_id = request.GET.get("document_id")
        object = DocumentUpload.objects.get(id=object_id)
        status = check_csv_eligibility(object.document)

        # If column names are incorrect, delete the upload
        if not status['complete']:
            object.delete()



        return JsonResponse(status, safe=False)
def AddCheckedDocumentAjax(request):
    object_id = request.POST.get("document_id")
    object = DocumentUpload.objects.get(id=object_id)
    status = create_entries_from_csv(object.document)
    return JsonResponse({"success": "success"}, safe=False)
