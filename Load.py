"""
Load Module - Phase 3 of ETL Pipeline
Handles data loading to target destinations.
"""

import csv


def load(data, filename):
    """
    Load cleaned data to a CSV file.
    
    Args:
        data (list): List of dictionaries to write
        filename (str): Output file path
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        if not data:
            print("Warning: No data to load")
            return False
            
        fieldnames = ['name', 'id', 'age', 'grade']
        
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        
        print(f"Successfully loaded {len(data)} records to '{filename}'")
        return True
        
    except Exception as e:
        print(f"Error loading data: {e}")
        return False


if __name__ == '__main__':
    from Extract import extract
    from Transform import transform
    
    data = extract('student.csv')
    clean_data = transform(data)
    load(clean_data, 'clean_data.csv')
