"""
Transform Module - Phase 2 of ETL Pipeline
Handles data cleaning, validation, and deduplication.
"""

import csv


def transform(data):
    """
    Clean and validate extracted data.
    
    Operations:
    - Remove records with invalid grades (> 100)
    - Remove records with missing age values
    - Deduplicate based on (name, age, grade)
    
    Args:
        data (list): List of dictionaries containing raw data
        
    Returns:
        list: List of cleaned and deduplicated records
    """
    clean_data = []
    seen = set()
    
    for row in data:
        try:
            # Validate grade
            grade = int(row.get('grade', 0))
            if grade > 100 or grade < 0:
                continue
            
            # Validate age
            if not row.get('age') or row.get('age').strip() == '':
                continue
            
            # Deduplicate
            student = (row['name'], row['age'], row['grade'])
            if student in seen:
                continue
            
            seen.add(student)
            clean_data.append(row)
            
        except (ValueError, KeyError) as e:
            print(f"Warning: Skipping invalid record - {e}")
            continue
    
    return clean_data


if __name__ == '__main__':
    from Extract import extract
    
    data = extract('student.csv')
    clean_data = transform(data)
    print(f"Original records: {len(data)}")
    print(f"Cleaned records: {len(clean_data)}")
    for row in clean_data:
        print(row)
