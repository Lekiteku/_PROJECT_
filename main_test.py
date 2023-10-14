import individuals as cc

# Example usage:

checkpoint1 = cc.Checkpoint("Bus Stop A", 37.1234, -122.3456)
checkpoint2 = cc.Checkpoint("Bus Stop B", 38.5678, -121.6789)

parent1 = cc.Parent("John", "Doe", "Male", "Mary Doe", "555-555-5555")
parent2 = cc.Parent("Jane", "Smith", "Female", "Bob Smith", "555-555-5556")

student1 = cc.Student("Alice", "Doe", "Female", "12345", checkpoint1, [parent1])
student2 = cc.Student("Bob", "Smith", "Male", "67890", checkpoint2, [parent2])

# Simulate registration by marking the persons as registered

student1.register()
student2.register()
parent1.register()
parent2.register()

# Print information about registered persons

print("Registered Students:")
print(f"Student 1: {student1.first_name} {student1.last_name}, Student ID: {student1.student_id}")
print(f"Student 2: {student2.first_name} {student2.last_name}, Student ID: {student2.student_id}")

print("\nRegistered Parents:")
print(f"Parent 1: {parent1.first_name} {parent1.last_name}, Guardian Name: {parent1.guardian_name}")
print(f"Parent 2: {parent2.first_name} {parent2.last_name}, Guardian Name: {parent2.guardian_name}")