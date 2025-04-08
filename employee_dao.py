import sqlite3
from entity_person import Person

class PersonDatabase:
    """
    Class to interact with the employee database using Python.
    """

    def __init__(self, database_path):
        self.conn = sqlite3.connect(database_path)
        self.cur = self.conn.cursor()

    def insert_employee(self, person: Person):
        query = """
            INSERT INTO employee (id, name, position, salary, hire_date)
            VALUES (?, ?, ?, ?, ?)
        """
        self.cur.execute(query, (person.id, person.full_name,
                                 person.role, person.get_wage(), person.start_date))
        self.conn.commit()

    def fetch_by_id(self, person_id):
        query = "SELECT * FROM employee WHERE id = ?"
        self.cur.execute(query, (person_id,))
        record = self.cur.fetchone()
        if record:
            return Person(id=record[0], full_name=record[1], role=record[2],
                          wage=record[3], start_date=record[4])
        return None

    def fetch_all(self):
        query = "SELECT * FROM employee"
        self.cur.execute(query)
        records = self.cur.fetchall()
        people = []
        for row in records:
            person = Person(id=row[0], full_name=row[1], role=row[2],
                            wage=row[3], start_date=row[4])
            people.append(person)
        for p in people:
            print(p)

    def update_employee(self, person: Person):
        query = """
            UPDATE employee
            SET name = ?, position = ?, salary = ?, hire_date = ?
            WHERE id = ?
        """
        self.cur.execute(query, (person.full_name, person.role,
                                 person.get_wage(), person.start_date, person.id))
        self.conn.commit()

    def delete_employee(self, person_id):
        query = "DELETE FROM employee WHERE id = ?"
        self.cur.execute(query, (person_id,))
        self.conn.commit()


