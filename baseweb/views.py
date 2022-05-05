from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import DocumentUpload
from .forms import DocumentUploadForm

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
