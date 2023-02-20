import boto3

s3 = boto3.resource('s3')
s3.create_bucket(Bucket='alex-tech201-python', CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})
bucket = s3.Bucket('alex-tech201-python')
bucket.upload_file('C:/Users/alexa/.ssh/test1.txt', 'test1.txt')
bucket.download_file('test1.txt', 'C:/Users/alexa/.ssh/test1.txt')
bucket.Object('test1.txt').delete()
s3.Bucket('alex-tech201-python').delete()