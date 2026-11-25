import csv
import os

FILEPATH = "employee.csv"
COLS = ["ID", "Name", "Salary"]


def make_file():
    with open(FILEPATH, "w", newline="") as f:
        csv.writer(f).writerow(COLS)
    print("File created.")


def add_record():
    if not os.path.exists(FILEPATH):
        print("Create the file first.")
        return

    eid = input("ID: ")
    name = input("Name: ")
    sal = input("Salary: ")
    with open(FILEPATH, "a", newline="") as f:
        csv.writer(f).writerow([eid, name, sal])
    print("Added.")


def show_all():
    if not os.path.exists(FILEPATH):
        print("File doesn't exist yet.")
        return

    with open(FILEPATH, "r") as f:
        for row in csv.reader(f):
            print(row)


def update_record():
    if not os.path.exists(FILEPATH):
        print("File doesn't exist yet.")
        return

    with open(FILEPATH, "r") as f:
        rows = list(csv.reader(f))

    target = input("ID to update: ")
    matched = False

    for row in rows[1:]:
        if row[0] == target:
            row[1] = input("New name: ")
            row[2] = input("New salary: ")
            matched = True
            break

    if matched:
        with open(FILEPATH, "w", newline="") as f:
            csv.writer(f).writerows(rows)
        print("Updated.")
    else:
        print("ID not found.")


def remove_record():
    if not os.path.exists(FILEPATH):
        print("File doesn't exist yet.")
        return

    with open(FILEPATH, "r") as f:
        rows = list(csv.reader(f))

    target = input("ID to delete: ")
    filtered = [rows[0]] + [r for r in rows[1:] if r[0] != target]

    if len(filtered) == len(rows):
        print("ID not found.")
    else:
        with open(FILEPATH, "w", newline="") as f:
            csv.writer(f).writerows(filtered)
        print("Deleted.")


while True:
    print("\n1-Create  2-Add  3-Display  4-Update  5-Delete  6-Exit")
    try:
        ch = int(input("Choice: "))
    except ValueError:
        print("Enter a number.")
        continue

    if ch == 1:
        make_file()
    elif ch == 2:
        add_record()
    elif ch == 3:
        show_all()
    elif ch == 4:
        update_record()
    elif ch == 5:
        remove_record()
    elif ch == 6:
        break
    else:
        print("Invalid.")
