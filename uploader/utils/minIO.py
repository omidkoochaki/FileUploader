from minio import Minio
from accounts.models import User
ACCESS_KEY = "H8TSA9VXWKA8UXP1CL4N"
SECRET_KEY = "VdVmPkzmY7sXslLg+yxByNK7S9Q9Q7jSY1ytSqO7"

MINIO_API_HOST = "localhost:9000"

# def MinIO2():
#     client = Minio(MINIO_API_HOST, access_key=ACCESS_KEY, secret_key=SECRET_KEY, secure=False, )
#     return True

# MINIO_CLIENT =


class UserStorage:

    def __init__(self, user: User):
        self.client = Minio(MINIO_API_HOST, access_key=ACCESS_KEY, secret_key=SECRET_KEY, secure=False,)
        self.user = user

    def uploade(self, filename, path):
        try:
            bn = self.bucket()
            print("?????")
            # result2 = self.client.make_bucket(bucket_name='omid')
            # print(result2)
            result = self.client.fput_object(bn, filename, path)
            print(result)
            return result
        except Exception as e:
            print()
            print("---------------------------")
            print(e)
            # raise Exception("cant uploade file")

    def bucket(self):
        bucket_name = self.user.first_name + self.user.last_name + str(self.user.id)
        if self.client.bucket_exists(bucket_name):
            print("*****  Yes")
            return bucket_name
        else:
            print("*****  No")
            try:
                result = self.client.make_bucket(bucket_name=bucket_name)
                print('========')
                print(result)
            except:
                raise Exception("cant make bucket for this user")
            return result

    def delete(self, filename):
        self.client.remove_object(self.bucket(), filename)

