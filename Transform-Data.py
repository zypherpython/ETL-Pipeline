import csv

# DATA EXTRACTION
def extract(filename):
    data = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print('file not found')
    
    return data

# DATA TRANSFORMATION
def transformation(data):
    clean_data = []
    seen = set()
    
    for row in data:
        # Remove records with invalid grades
        if int(row['grade']) > 100:
            continue
        # Remove records with missing age
        elif row['age'] == '':
            continue
        
        # Deduplicate based on name, age, and grade
        student = (row['name'], row['age'], row['grade'])
        if student in seen:
            continue
        
        seen.add(student)
        clean_data.append(row)
    
    return clean_data

def main():
    data = extract('student.csv')
    clean_data = transformation(data)
    
    for row in clean_data:
        print(row)

if __name__ == '__main__':
    main()
