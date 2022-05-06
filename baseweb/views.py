from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .models import DocumentUpload
from .forms import DocumentUploadForm
from django.http import HttpResponseRedirect, JsonResponse
from .processing_toolkit import check_csv_eligibility
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
        if not status['column_names']['complete']:
            object.delete()



        return JsonResponse(status, safe=False)
