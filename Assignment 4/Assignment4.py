eren = {
  "name": "Eren",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
}
mikasa = {
 "name": "Mikasa",
 "homework": [100.0, 92.0, 98.0, 100.0],
 "quizzes": [82.0, 83.0, 91.0],
 "tests": [89.0, 97.0]
}
armin = {
"name": "Armin",
"homework": [0.0, 87.0, 75.0, 22.0],
"quizzes": [0.0, 75.0, 78.0],
"tests": [100.0, 100.0]
}

students = [eren, mikasa, armin]
for student in students:
    for key in student: # Iterate through each key in each student
        print(student.get(key)) # Prints each value in new lines

def average(numbers):
    total = sum(numbers)
    total = float(total)
    total = total / len(numbers)
    return total

def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return homework * 0.1 + quizzes * 0.3 + tests * 0.6 # Sum of all 3 variables with weight

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(get_letter_grade(get_average(armin))) # There was no information about lloyd in the word doc, so I used armin instead

def get_class_average(students):
    """
    Returns average score for a list of students

    Args:
        students (list): List containing all of the student' information in dictionary form

    Returns:
        (int): Average of the 3 students' average
    """
    results = []
    for student in students:
        results.append(get_average(student)) # Appends average of each student to results list
    return average(results) # Returns the average of the 3 students' average

print(get_class_average(students))
print(get_letter_grade(get_class_average(students)))