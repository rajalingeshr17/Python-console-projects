import json
import os

DATA_FILE = "students.json"

class Student:
    def __init__(self, roll_no, name, age, grade):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.grade = grade

    def to_dict(self):
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }

class StudentManager:
    def __init__(self):
        self.students = []
        self.load_data()

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.students = [Student(**stu) for stu in data]

    def save_data(self):
        with open(DATA_FILE, "w") as f:
            json.dump([stu.to_dict() for stu in self.students], f, indent=4)

    def add_student(self):
        try:
            roll_no = int(input("Enter Roll Number: "))
            if any(s.roll_no == roll_no for s in self.students):
                print("❌ Student with this roll number already exists.")
                return
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grade = input("Enter Grade: ")
            self.students.append(Student(roll_no, name, age, grade))
            self.save_data()
            print("✅ Student added successfully.")
        except ValueError:
            print("❌ Invalid input. Please enter correct data types.")

    def view_students(self):
        if not self.students:
            print("⚠ No students found.")
        else:
            print("\n--- Student List ---")
            for stu in self.students:
                print(f"{stu.roll_no} - {stu.name}, Age: {stu.age}, Grade: {stu.grade}")

    def search_student(self):
        roll_no = input("Enter Roll Number to Search: ")
        for stu in self.students:
            if str(stu.roll_no) == roll_no:
                print(f"✅ Found: {stu.roll_no} - {stu.name}, Age: {stu.age}, Grade: {stu.grade}")
                return
        print("❌ Student not found.")

    def update_student(self):
        roll_no = input("Enter Roll Number to Update: ")
        for stu in self.students:
            if str(stu.roll_no) == roll_no:
                stu.name = input(f"Enter New Name ({stu.name}): ") or stu.name
                stu.age = int(input(f"Enter New Age ({stu.age}): ") or stu.age)
                stu.grade = input(f"Enter New Grade ({stu.grade}): ") or stu.grade
                self.save_data()
                print("✅ Student updated successfully.")
                return
        print("❌ Student not found.")

    def delete_student(self):
        roll_no = input("Enter Roll Number to Delete: ")
        for stu in self.students:
            if str(stu.roll_no) == roll_no:
                self.students.remove(stu)
                self.save_data()
                print("✅ Student deleted successfully.")
                return
        print("❌ Student not found.")

def main():
    manager = StudentManager()
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            manager.update_student()
        elif choice == "5":
            manager.delete_student()
        elif choice == "0":
            print("💾 Saving and exiting...")
            manager.save_data()
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
