from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone
# Create your models here.
class DocumentUpload(models.Model):
    create_datetime = models.DateTimeField(default=timezone.now )
    document = models.FileField(upload_to="uploads/documents/",
                                validators=[FileExtensionValidator(["csv"])],
                                )
    has_been_converted = models.BooleanField(default=False)

    def __str__(self):

        return self.document.name.split("/")[-1]
