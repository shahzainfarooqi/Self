class Student:
    def __init__(self, name, marks):
        self.name = name      # Assigning to instance variable using self
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

# Example usage
s1 = Student("Shahzain", 92)
s1.display()
