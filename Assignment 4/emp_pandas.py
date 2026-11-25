import pandas as pd
import os

CSV_PATH = "employee.csv"


def load():
    if os.path.exists(CSV_PATH):
        return pd.read_csv(CSV_PATH)
    return pd.DataFrame(columns=["id", "name", "salary"])


def save(df):
    df.to_csv(CSV_PATH, index=False)


def add_emp():
    df = load()
    eid = int(input("ID: "))
    name = input("Name: ")
    sal = int(input("Salary: "))
    new_row = pd.DataFrame({"id": [eid], "name": [name], "salary": [sal]})
    df = pd.concat([df, new_row], ignore_index=True)
    save(df)
    print("Added.")


def show_all():
    df = load()
    if df.empty:
        print("No records yet.")
    else:
        print(df.to_string(index=False))


def update_sal():
    df = load()
    eid = int(input("ID: "))
    if eid not in df["id"].values:
        print("Not found.")
        return
    new_sal = int(input("New salary: "))
    df.loc[df["id"] == eid, "salary"] = new_sal
    save(df)
    print("Updated.")


def remove_emp():
    df = load()
    eid = int(input("ID: "))
    if eid not in df["id"].values:
        print("Not found.")
        return
    df = df[df["id"] != eid]
    save(df)
    print("Deleted.")


while True:
    print("\n1-Add  2-Show  3-Update  4-Delete  5-Exit")
    ch = int(input("> "))

    if ch == 1:
        add_emp()
    elif ch == 2:
        show_all()
    elif ch == 3:
        update_sal()
    elif ch == 4:
        remove_emp()
    elif ch == 5:
        break
    else:
        print("Nope.")
