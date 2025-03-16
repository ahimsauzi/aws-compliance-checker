import boto3


def check_iam_mfa():
    iam = boto3.client('iam')
    users = iam.list_users()['Users']

    results = []
    for user in users:
        mfa_devices = iam.list_mfa_devices(
            UserName=user['UserName'])['MFADevices']
        if not mfa_devices:
            results.append([user['UserName'], "❌ MFA NOT enabled"])
        else:
            results.append([user['UserName'], "✅ MFA enabled"])

    return results
