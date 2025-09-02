import csv

def write_csv():
    with open('data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'ad', 'yas'])
        writer.writerow([1, 'Təhminə', 25])
        writer.writerow([2, 'Elvin', 30])
        writer.writerow([3, 'Aysel', 22])

def read_csv():
    with open('data.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

if __name__ == "__main__":
    write_csv()
    print("CSV faylı yaradıldı və yazıldı.\n")
    print("CSV faylının məzmunu:")
    read_csv()
