class Person:
    def __init__(self, id, full_name, role, wage, start_date):
        self.id = id
        self.full_name = full_name
        self.role = role
        self.__wage = wage
        self.start_date = start_date

    def __str__(self):
        return f"ID: {self.id} | Name: {self.full_name} | Role: {self.role}"

    def get_wage(self):
        return self.__wage

    def update_wage(self, new_amount):
        self.__wage = new_amount
        print(f"Salary updated for {self.full_name}")
