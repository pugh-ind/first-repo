#! /usr/bin/python3

#   Need python3 and boto3 installed...
#
#   This is using the 'high-level' Resource API calls. This is simpler than the
#   Client API (low-level) calls.
#

import sys
import boto3
import botocore

def main():

#   Connect to s3 service
    s3 = boto3.resource('s3')

#   Display all my buckets
    print ('Here are my S3 buckets:')
    for bucket in s3.buckets.all():
       print(bucket.name)

    print ('Here are contents:')
    for bucket in s3.buckets.all():
        for key in bucket.objects.all():
            print (bucket.name + ' ' + key.key)


#   Download file(s)
    s3.Bucket('pugh-cloud-2020-bucket-1').download_file('OTPCtoyotaebook.pdf', '/local/rpugh/data/dwnld.txt')
#    s3.Bucket('rpugh-s3-02').download_file('output.txt', '/local/rpugh/data/output.txt.down.02')


    sys.exit(0)

if __name__ == "__main__": main()

