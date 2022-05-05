from django.forms import ModelForm, FileInput
from .models import DocumentUpload

class DocumentUploadForm(ModelForm):
    class Meta:
        model = DocumentUpload
        fields = ("document",)
        widgets = {
                'document':FileInput(attrs={'class': 'form-control'}),
        }
