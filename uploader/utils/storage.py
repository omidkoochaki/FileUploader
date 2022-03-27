from django.core.files.storage import FileSystemStorage
from minio import Minio


ACCESS_KEY = "H8TSA9VXWKA8UXP1CL4N"
SECRET_KEY = "VdVmPkzmY7sXslLg+yxByNK7S9Q9Q7jSY1ytSqO7"

MINIO_API_HOST = "localhost:9000"


class MinIO(FileSystemStorage):
    def __init__(self):
        self.client = Minio(MINIO_API_HOST, access_key=ACCESS_KEY, secret_key=SECRET_KEY, secure=False)
        super(MinIO, self).__init__()

    def _open(self, name, mode="rb"):
        super(MinIO, self)._open(name, mode)

    def _save(self, name, content):
        res = super(MinIO, self)._save(name, content)
        full_path = self.path(name)
        result = self.uploade(name, full_path)

        self.delete(name)
        return res

    def uploade(self, filename, path):
        try:
            result = self.client.fput_object("test", filename, path)
            return result
        except Exception as e:
            raise Exception("cant uploade file")


