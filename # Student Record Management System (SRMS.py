# Student Record Management System (SRMS)
# PROG211 - Object-Oriented Programming 1

class Student:
	def __init__(self, student_id, name, age, course, grade):
		self.student_id = student_id
		self.name = name
		self.age = age
		self.course = course
		self.grade = grade

	def display_details(self):
		print("\n--- Student Details ---")
		print("Student ID:", self.student_id)
		print("Name:", self.name)
		print("Age:", self.age)
		print("Course:", self.course)
		print("Grade:", self.grade)


class StudentRecordManagementSystem:
	def __init__(self):
		# Dictionary used to store student records
		self.students = {}

	@classmethod
	def system_name(cls):
		return "Student Record Management System"

	def add_student(self):
		student_id = input("Enter Student ID: ")

		if student_id in self.students:
			print("Student ID already exists!")
			return

		name = input("Enter Student Name: ")

		try:
			age = int(input("Enter Student Age: "))
		except ValueError:
			print("Invalid age. Please enter a number.")
			return

		course = input("Enter Student Course: ")
		grade = input("Enter Student Grade: ")

		student = Student(student_id, name, age, course, grade)

		self.students[student_id] = student

		print("Student record added successfully!")

	def view_students(self):
		if not self.students:
			print("No student records available.")
			return

		print("\n===== ALL STUDENT RECORDS =====")

		for student in self.students.values():
			student.display_details()

	def search_student(self):
		student_id = input("Enter Student ID to search: ")

		student = self.students.get(student_id)

		if student:
			student.display_details()
		else:
			print("Student not found!")

	def update_student(self):
		student_id = input("Enter Student ID to update: ")

		student = self.students.get(student_id)

		if not student:
			print("Student not found!")
			return

		print("Leave a field blank to keep its current value.")

		name = input("Enter New Name: ")
		if name:
			student.name = name

		age = input("Enter New Age: ")
		if age:
			try:
				student.age = int(age)
			except ValueError:
				print("Invalid age. Keeping the previous age.")

		course = input("Enter New Course: ")
		if course:
			student.course = course

		grade = input("Enter New Grade: ")
		if grade:
			student.grade = grade

		print("Student record updated successfully!")

	def delete_student(self):
		student_id = input("Enter Student ID to delete: ")

		if student_id in self.students:
			del self.students[student_id]
			print("Student record deleted successfully!")
		else:
			print("Student not found!")

	def run(self):
		print("\nWelcome to", self.system_name())

		while True:
			print("\n===== MAIN MENU =====")
			print("1. Add Student")
			print("2. View All Students")
			print("3. Search Student")
			print("4. Update Student")
			print("5. Delete Student")
			print("6. Exit")

			choice = input("Enter your choice (1-6): ")

			if choice == "1":
				self.add_student()

			elif choice == "2":
				self.view_students()

			elif choice == "3":
				self.search_student()

			elif choice == "4":
				self.update_student()

			elif choice == "5":
				self.delete_student()

			elif choice == "6":
				print("Thank you for using the Student Record Management System!")
				break

			else:
				print("Invalid choice. Please select between 1 and 6.")


# Main program
if __name__ == "__main__":
	system = StudentRecordManagementSystem()
	system.run()