from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .models import DocumentUpload
from .forms import DocumentUploadForm
from django.http import HttpResponseRedirect
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
            print(request.POST)
            form = DocumentUploadForm(request.POST, request.FILES)
            if form.is_valid():
                print("valid")
                form.save()
            else:

                print(form)
                print("Invalid Form")
                context = {}
                context['unprocessed_uploads'] = DocumentUpload.objects.filter(has_been_converted=False)
                context['form'] = form
                return render(request, self.template_name, context)


            return redirect('/uploads/')
