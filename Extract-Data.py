import csv

def Extract(filename):
    data = []
    try:
        with open(filename, 'r') as file:
            reader= csv.DictReader(file)
            for row in reader:
                data.append(row)

    except FileNotFoundError:
        print('file not found')

    return data



data = Extract(r"C:\Users\ss\.vscode\student.csv")  
for row in data:
    print(row)

