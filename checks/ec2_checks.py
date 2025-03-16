import boto3


def check_ec2_security_groups():
    ec2 = boto3.client('ec2')
    security_groups = ec2.describe_security_groups()['SecurityGroups']

    results = []
    for sg in security_groups:
        for rule in sg['IpPermissions']:
            if rule.get('FromPort') in [22, 3389] and '0.0.0.0/0' in str(rule.get('IpRanges')):
                results.append([sg['GroupName'], "❌ Open SSH/RDP Detected"])

    return results
