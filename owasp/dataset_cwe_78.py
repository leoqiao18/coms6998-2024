#!/usr/bin/env python3

import csv
import sys
import json
import re


def remove_comments(java_string):
    """Removes comments from a string of Java program.

    Args:
      java_string: A string of Java program.

    Returns:
      A string of Java program without comments.
    """

    # Remove single-line comments.
    java_string = re.sub(r"//.*\n", "", java_string)

    # Remove multi-line comments.
    java_string = re.sub(r"/\*.*?\*/", "", java_string, flags=re.DOTALL)

    return java_string


def main():
    """
    Process the benchmarks and generate JSON output.

    Reads a CSV file containing test information and a directory with benchmark files.
    For each test in the CSV file, reads the corresponding benchmark file, removes comments,
    and outputs a JSON object with the file content, real vulnerability, and identified by tool fields.
    """

    benchmarks_dir = sys.argv[1]  # path to the directory with the benchmarks
    csv_path = sys.argv[2]  # path to the expected results csv file

    # csv fields: test name, category, CWE, real vulnerability, identified by tool, pass/fail
    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # skip the header row
        for row in reader:
            test_name = row[0]
            real_vulnerability = row[3]
            identified_by_tool = row[4]

            # read the content of the file with the test name
            file_path = f"{benchmarks_dir}/{test_name}.java"
            with open(file_path, "r", encoding="utf-8") as test_file:
                file_content = test_file.read()

            # output a JSON with the file content, real vulnerability, and identified by tool fields
            output_json = {
                "program": remove_comments(file_content),
                "target": real_vulnerability,
                "codeql_prediction": identified_by_tool,
            }
            print(json.dumps(output_json))


if __name__ == "__main__":
    main()
