"""
Extract Module - Phase 1 of ETL Pipeline
Handles data ingestion from CSV files with error handling.
"""

import csv


def extract(filename):
    """
    Extract data from a CSV file.
    
    Args:
        filename (str): Path to the CSV file
        
    Returns:
        list: List of dictionaries containing parsed CSV rows
    """
    data = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")
    
    return data


if __name__ == '__main__':
    data = extract('student.csv')
    print(f"Extracted {len(data)} records")
    for row in data:
        print(row)
