from django.db import models
from accounts.models import User
from .utils.storage import MinIO

# Create your models here.


class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    file_size = models.IntegerField(null=False, blank=False)
    file = models.FileField(null=True, blank=True, upload_to=".", storage=MinIO)

    def delete(self, using=None, keep_parents=False):
        """
        call delete from MinIO
        """
        storage = MinIO()
        storage.client.remove_object("test", self.file.name)
        return super().delete()