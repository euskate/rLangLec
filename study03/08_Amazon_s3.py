import boto3

# S3 클라이언트 생성
s3 = boto3.client('s3')

# 파일 업로드
s3.upload_file('localfile.txt', 'mybucket', 'localfile.txt')

# 파일 다운로드
s3.download_file('mybucket', 'localfile.txt', 'downloadedfile.txt')