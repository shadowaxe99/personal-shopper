```python
import boto3
from botocore.exceptions import NoCredentialsError

class BackendInfrastructure:
    def __init__(self, access_key, secret_key, region):
        self.s3_client = boto3.client('s3', aws_access_key_id=access_key,
                                      aws_secret_access_key=secret_key,
                                      region_name=region)

    def upload_to_s3(self, file_name, bucket, s3_file_name):
        try:
            self.s3_client.upload_file(file_name, bucket, s3_file_name)
            print("Upload Successful")
            return True
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False

    def download_from_s3(self, file_name, bucket, local_path):
        try:
            self.s3_client.download_file(bucket, file_name, local_path)
            print("Download Successful")
            return True
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False

    def create_bucket(self, bucket_name):
        try:
            response = self.s3_client.create_bucket(Bucket=bucket_name)
            print("Bucket created successfully")
            return True
        except Exception as e:
            print("Error in creating bucket: ", e)
            return False

backend = BackendInfrastructure('access_key', 'secret_key', 'region')
backend.create_bucket('ai-personal-shopper')
backend.upload_to_s3('userProfileData', 'ai-personal-shopper', 'userProfileData')
backend.upload_to_s3('productData', 'ai-personal-shopper', 'productData')
backend.upload_to_s3('wishlistData', 'ai-personal-shopper', 'wishlistData')
backend.upload_to_s3('affiliatePartners', 'ai-personal-shopper', 'affiliatePartners')
backend.upload_to_s3('premiumFeatures', 'ai-personal-shopper', 'premiumFeatures')
backend.upload_to_s3('sponsoredProducts', 'ai-personal-shopper', 'sponsoredProducts')
```