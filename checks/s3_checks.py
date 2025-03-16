import boto3


def check_s3_security():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()['Buckets']

    results = []
    for bucket in buckets:
        bucket_name = bucket['Name']

        # Check Encryption
        try:
            s3.get_bucket_encryption(Bucket=bucket_name)
            encryption_status = "✅ Encrypted"
        except:
            encryption_status = "❌ NOT Encrypted"

        # Check HTTPS enforcement
        try:
            policy = s3.get_bucket_policy(Bucket=bucket_name)['Policy']
            if "s3:SecureTransport" in policy:
                https_status = "✅ HTTPS Enforced"
            else:
                https_status = "❌ HTTPS NOT Enforced"
        except:
            https_status = "❌ No Policy Set"

        results.append([bucket_name, encryption_status, https_status])

    return results
