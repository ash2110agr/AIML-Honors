import sqlite3

DB_FILE = "employee.db"


def get_conn():
    return sqlite3.connect(DB_FILE)


def setup():
    conn = get_conn()
    conn.execute(
        "CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY, name TEXT, salary INTEGER)"
    )
    conn.commit()
    conn.close()


def add_emp():
    eid = int(input("ID: "))
    name = input("Name: ")
    sal = int(input("Salary: "))
    conn = get_conn()
    conn.execute("INSERT INTO employee VALUES(?,?,?)", (eid, name, sal))
    conn.commit()
    conn.close()
    print("Added.")


def show_all():
    conn = get_conn()
    rows = conn.execute("SELECT * FROM employee").fetchall()
    conn.close()
    if not rows:
        print("No records.")
    else:
        for r in rows:
            print(r)


def update_sal():
    eid = int(input("ID: "))
    new_sal = int(input("New salary: "))
    conn = get_conn()
    conn.execute("UPDATE employee SET salary=? WHERE id=?", (new_sal, eid))
    conn.commit()
    conn.close()
    print("Updated.")


def remove_emp():
    eid = int(input("ID: "))
    conn = get_conn()
    conn.execute("DELETE FROM employee WHERE id=?", (eid,))
    conn.commit()
    conn.close()
    print("Deleted.")


setup()

while True:
    print("\n1) Add  2) Show  3) Update salary  4) Delete  5) Quit")
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
        print("Invalid.")
