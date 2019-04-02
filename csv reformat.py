import csv

filename = input("Filename: ")
massive_array = []
with open(filename, "r") as file:
    reader = csv.reader(file, delimiter=input("Delimiter: "), quotechar=input("Quotechar: "))
    for row in reader:
        massive_array.append(row)
    print(massive_array)
with open(filename, "w") as file:
    writer = csv.writer(file, delimiter=input("Delimiter: "), quotechar=input("Quotechar: "))
    for row in massive_array:
        writer.writerow(row)
