from entity_person import Person
from employee_dao import PersonDatabase

# Connect to the SQLite database
db = PersonDatabase("employee_db.sqlite")  # make sure the DB exists

# Create a person object (Aidai Totoeva)
aidai = Person(203, "Aidai Totoeva", "UI/UX Designer", 98000, "2022-08-12")

# Insert Aidai into the database
try:
    db.insert_employee(aidai)
    print("Aidai Totoeva was successfully added to the team.")
except Exception as error:
    print("Employee already exists in the database.")

# Fetch by ID
print("\nFetching employee by ID:")
print(db.fetch_by_id(203))

# Show all records
print("\nAll employees:")
db.fetch_all()

# Update position
print("\nUpdating position for Aidai...")
aidai.role = "Lead Product Designer"
db.update_employee(aidai)
print("Updated successfully.")

# Delete
# Delete Aidai from database
db.delete_employee(203)
print("Aidai has been removed from the employee list.")

