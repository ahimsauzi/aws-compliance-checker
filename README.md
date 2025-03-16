# AWS NIST 800-53 Compliance Checker

## Overview

The **AWS NIST 800-53 Compliance Checker** is a Python-based tool designed to automate the assessment of AWS environments against selected NIST 800-53 security controls. This tool helps organizations ensure their AWS resources comply with specific security standards by performing checks and generating detailed reports.

## Features

- **Automated Compliance Checks**: Evaluates AWS resources against specific NIST 800-53 controls
- **Comprehensive Reporting**: Generates reports in both CSV and JSON formats
- **Extensible Design**: Modular architecture allows for easy addition of new compliance checks
- **Flexible Configuration**: Customizable settings via config.json

## NIST 800-53 Controls Implemented

The tool currently automates checks for the following NIST 800-53 controls:

- **Access Control (AC)**
  - **AC-2**: Account Management
  - **AC-6**: Least Privilege
  - **AC-17**: Remote Access (MFA Enforcement)
- **Audit & Accountability (AU)**
  - **AU-2**: Audit Events (CloudTrail Logging)
  - **AU-12**: Audit Generation (API Call Logging)
- **System & Communications Protection (SC)**
  - **SC-12**: Cryptographic Key Establishment and Management (S3 Bucket Encryption)
  - **SC-13**: Cryptographic Protection (HTTPS Enforcement)
  - **SC-28**: Protection of Information at Rest (RDS Encryption)
- **System & Information Integrity (SI)**
  - **SI-4**: Information System Monitoring (GuardDuty Findings)
  - **SI-7**: Software, Firmware, and Information Integrity (EC2 Security Group Configurations)

## Project Structure

```
aws_compliance_checker/
│
├── checks/
│   ├── __init__.py
│   ├── iam_checks.py          # IAM security checks
│   ├── s3_checks.py           # S3 security checks
│   ├── ec2_checks.py          # EC2 security group checks
│   └── cloudtrail_checks.py   # CloudTrail audit checks
│
├── reports/                   # Directory to store compliance reports
│
├── utils/
│   ├── __init__.py
│   └── report_generator.py    # Functions to generate reports
│
├── tests/                     # Unit tests for compliance checks
│
├── main.py                    # Script entry point
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── .gitignore                # Git ignore file
└── config.json               # Configuration file
```

## Prerequisites

- **AWS Account**: Active AWS account with appropriate access
- **AWS CLI**: Installed and configured with appropriate credentials
- **Python 3.8+**: Latest stable Python version
- **Required Permissions**: IAM role/user with the following permissions:
  - `iam:ListUsers`, `iam:GetUser`, `iam:ListAttachedUserPolicies`
  - `s3:ListBuckets`, `s3:GetBucketPolicy`, `s3:GetBucketEncryption`
  - `ec2:DescribeSecurityGroups`
  - `cloudtrail:DescribeTrails`
  - `guardduty:ListDetectors`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/aws_compliance_checker.git
   cd aws_compliance_checker
   ```

2. Create and activate virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Configure settings in `config.json`
2. Run the compliance checks:
   ```bash
   python main.py
   ```

## Reports

Reports are generated in the `reports/` directory:

- `compliance_results.csv`: CSV format report
- `compliance_results.json`: JSON format report

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

This project is licensed under the MIT License.

## Acknowledgements

Inspired by open-source AWS security assessment tools like Prowler and CloudMapper.
