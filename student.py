FILENAME = 'student.txt'

# Read student data
def read_students():
    try:
        with open(FILENAME, 'r') as file:
            lines = file.readlines()
            if not lines:
                return [], []
            header = lines[0].strip().split(',')
            students = []
            for line in lines[1:]:
                values = line.strip().split(',')
                student = dict(zip(header, values))
                students.append(student)
        return header, students
    except FileNotFoundError:
        print(f"{FILENAME} not found. Please enter header fields (comma-separated):")
        header = input().strip().split(',')
        return header, []

# Write student data
def write_students(header, students):
    with open(FILENAME, 'w') as file:
        file.write(','.join(header) + '\n')
        for student in students:
            row = ','.join([student.get(col, "") for col in header])
            file.write(row + '\n')

# Add a new student with input validation
def add_student(header):
    new_student = {}
    for field in header:
        while True:
            value = input(f"Enter {field}: ").strip()
            if value == "":
                print(f"{field} cannot be empty. Please enter a value.")
            else:
                new_student[field] = value
                break
    return new_student

# Display students
def display_students(students):
    if not students:
        print("No students to display.")
        return
    header = list(students[0].keys())
    # Calculate the max width for each column
    col_widths = [max(len(str(s.get(col, ""))) for s in students + [dict(zip(header, header))]) for col in header]
    # Print header
    header_row = " | ".join(col.ljust(col_widths[i]) for i, col in enumerate(header))
    print(header_row)
    print("-" * len(header_row))
    # Print each student row
    for s in students:
        row = " | ".join(str(s.get(col, "")).ljust(col_widths[i]) for i, col in enumerate(header))
        print(row)

# Main menu
def main():
    header, students = read_students()
    while True:
        print("\n1. View Students\n2. Add Student\n3. Save & Exit")
        choice = input("Choose (1/2/3): ").strip()
        if choice not in {'1', '2', '3'}:
            print("Invalid option. Please enter 1, 2, or 3.")
            continue
        if choice == '1':
            display_students(students)
        elif choice == '2':
            students.append(add_student(header))
        elif choice == '3':
            write_students(header, students)
            print("Saved and exited.")
            break

if __name__ == '__main__':
    main()
