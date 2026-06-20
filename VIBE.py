#Alessandro De La Luz
#CIS261
#WK10 VIBE Coding - Student Grade Calculator

class Student:
    """Class to represent a student with test scores and grades."""
    
    def __init__(self, name, student_id, test1, test2, test3):
        """Initialize a student with name, ID, and three test scores."""
        self.name = name
        self.id = student_id
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()
    
    def calculate_average(self):
        """Calculate the average of the three test scores."""
        return (self.test1 + self.test2 + self.test3) / 3
    
    def calculate_grade(self):
        """Calculate the letter grade based on the average score."""
        if self.average >= 90:
            return 'A'
        elif self.average >= 80:
            return 'B'
        elif self.average >= 70:
            return 'C'
        elif self.average >= 60:
            return 'D'
        else:
            return 'F'
    
    def to_string(self):
        """Return the student data as a pipe-delimited string."""
        return f"{self.name}|{self.id}|{self.test1:.2f}|{self.test2:.2f}|{self.test3:.2f}|{self.average:.2f}|{self.grade}"
    
    @staticmethod
    def from_string(line):
        """Create a Student object from a pipe-delimited string."""
        parts = line.strip().split('|')
        if len(parts) >= 7:
            return Student(parts[0], parts[1], float(parts[2]), float(parts[3]), float(parts[4]))
        return None


def add_student(students):
    """Prompt user to add a new student record."""
    print("\n--- Add New Student ---")
    
    try:
        name = input("Enter student name: ").strip()
        if not name:
            print("Error: Name cannot be empty.")
            return
        
        student_id = input("Enter student ID: ").strip()
        if not student_id:
            print("Error: Student ID cannot be empty.")
            return
        
        test1 = float(input("Enter Test 1 score: "))
        test2 = float(input("Enter Test 2 score: "))
        test3 = float(input("Enter Test 3 score: "))
        
        # Validate test scores
        if not (0 <= test1 <= 100 and 0 <= test2 <= 100 and 0 <= test3 <= 100):
            print("Error: Test scores must be between 0 and 100.")
            return
        
        student = Student(name, student_id, test1, test2, test3)
        students.append(student)
        print(f"\nStudent {name} added successfully!")
        print(f"Average: {student.average:.2f}, Grade: {student.grade}")
    
    except ValueError:
        print("Error: Invalid input. Please enter numeric values for test scores.")


def display_all_students(students):
    """Display all students in a formatted table."""
    if not students:
        print("\nNo students in the database.")
        return
    
    print("\n" + "="*90)
    print(f"{'Name':<20} {'ID':<12} {'Test 1':<10} {'Test 2':<10} {'Test 3':<10} {'Average':<10} {'Grade':<5}")
    print("="*90)
    
    for student in students:
        print(f"{student.name:<20} {student.id:<12} {student.test1:<10.2f} {student.test2:<10.2f} {student.test3:<10.2f} {student.average:<10.2f} {student.grade:<5}")
    
    print("="*90)


def calculate_class_statistics(students):
    """Calculate and display class statistics."""
    if not students:
        print("\nNo students in the database.")
        return
    
    averages = [student.average for student in students]
    
    highest_avg = max(averages)
    lowest_avg = min(averages)
    class_avg = sum(averages) / len(averages)
    
    highest_student = next(s for s in students if s.average == highest_avg)
    lowest_student = next(s for s in students if s.average == lowest_avg)
    
    print("\n" + "="*50)
    print("CLASS STATISTICS")
    print("="*50)
    print(f"Total Students: {len(students)}")
    print(f"Highest Average: {highest_avg:.2f} ({highest_student.name})")
    print(f"Lowest Average: {lowest_avg:.2f} ({lowest_student.name})")
    print(f"Class Average: {class_avg:.2f}")
    print("="*50)


def search_student(students):
    """Search for a student by name (case-insensitive)."""
    if not students:
        print("\nNo students in the database.")
        return
    
    search_name = input("\nEnter student name to search: ").strip().lower()
    
    found_students = [s for s in students if s.name.lower() == search_name]
    
    if found_students:
        print("\n" + "="*90)
        print(f"{'Name':<20} {'ID':<12} {'Test 1':<10} {'Test 2':<10} {'Test 3':<10} {'Average':<10} {'Grade':<5}")
        print("="*90)
        for student in found_students:
            print(f"{student.name:<20} {student.id:<12} {student.test1:<10.2f} {student.test2:<10.2f} {student.test3:<10.2f} {student.average:<10.2f} {student.grade:<5}")
        print("="*90)
    else:
        print(f"No student found with name '{search_name}'.")


def save_students(students, filename="student_grades.txt"):
    """Save all student records to a file."""
    try:
        with open(filename, 'w') as file:
            for student in students:
                file.write(student.to_string() + '\n')
        print(f"\nSuccessfully saved {len(students)} student(s) to {filename}")
    except IOError as e:
        print(f"Error saving file: {e}")


def load_students(filename="student_grades.txt"):
    """Load student records from a file."""
    students = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.strip():
                    student = Student.from_string(line)
                    if student:
                        students.append(student)
        if students:
            print(f"Successfully loaded {len(students)} student(s) from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty student list.")
    except IOError as e:
        print(f"Error reading file: {e}")
    
    return students


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("STUDENT GRADE CALCULATOR")
    print("="*50)
    print("1. Add new student")
    print("2. Display all students")
    print("3. Display class statistics")
    print("4. Search for a student")
    print("5. Save students to file")
    print("6. Exit (or press ESC)")
    print("="*50)


def main():
    """Main program loop."""
    students = load_students()
    
    print("\nWelcome to the Student Grade Calculator!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_all_students(students)
        elif choice == '3':
            calculate_class_statistics(students)
        elif choice == '4':
            search_student(students)
        elif choice == '5':
            save_students(students)
        elif choice == '6':
            print("\nSaving and exiting...")
            save_students(students)
            print("Thank you for using the Student Grade Calculator!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()

