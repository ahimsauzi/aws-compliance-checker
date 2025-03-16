import os
from checks.iam_checks import check_iam_mfa
from checks.s3_checks import check_s3_security
from checks.ec2_checks import check_ec2_security_groups
from utils.report_generator import save_results_to_csv, save_results_to_json


def run_compliance_checks():
    """ Execute all compliance checks and save results """
    print("\n🔎 Running AWS Security Compliance Checks...\n")

    results = []
    results.extend(check_iam_mfa())  # IAM MFA Enforcement Check
    results.extend(check_s3_security())  # S3 Security Configurations
    results.extend(check_ec2_security_groups())  # EC2 Security Group Analysis

    # Ensure reports directory exists
    if not os.path.exists("reports"):
        os.makedirs("reports")

    # Save results in CSV and JSON format
    save_results_to_csv(results)
    save_results_to_json(results)

    print("\n✅ Compliance Check Completed!")


if __name__ == "__main__":
    run_compliance_checks()
