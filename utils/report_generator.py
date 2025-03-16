import csv
import json
import os


def save_results_to_csv(results, filename="reports/compliance_results.csv"):
    """ Save compliance check results to a CSV file. """
    if not os.path.exists("reports"):
        os.makedirs("reports")

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Check", "Status", "Details"])
        writer.writerows(results)

    print(f"✅ Results saved to {filename}")


def save_results_to_json(results, filename="reports/compliance_results.json"):
    """ Save compliance check results to a JSON file. """
    if not os.path.exists("reports"):
        os.makedirs("reports")

    with open(filename, mode='w') as file:
        json.dump(results, file, indent=4)

    print(f"✅ Results saved to {filename}")
