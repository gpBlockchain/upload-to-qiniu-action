import argparse
from qiniu import Auth, put_file, etag
import qiniu.config

def upload_file_to_qiniu(access_key, secret_key, bucket_name, key, local_file):

    q = Auth(access_key, secret_key)
    token = q.upload_token(bucket_name, key, 3600)
    ret, info = put_file(token, key, local_file, version='v2')
    print(info)
    assert ret['key'] == key
    assert ret['hash'] == etag(local_file)


 # python3 update.py --access_key xxx_key \
 #         --secret_key xxx_key \
 #         --bucket_name acceptance-test \
 #         --key ckb/demo/demo2.tar.gz \
 #         --local_file xxx/config/update.tar.gz
 #

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Upload a file to qiniu.')
    parser.add_argument('--access_key', required=True, help='Access Key')
    parser.add_argument('--secret_key', required=True, help='Secret Key')
    parser.add_argument('--bucket_name', required=True, help='Name of the bucket')
    parser.add_argument('--key', required=True, help='Key of the file')
    parser.add_argument('--local_file', required=True, help='Path of the local file')

    args = parser.parse_args()
    upload_file_to_qiniu(args.access_key, args.secret_key, args.bucket_name, args.key, args.local_file)
