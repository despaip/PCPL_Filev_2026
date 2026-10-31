class Student:
    def __init__(self, id, name, average_grade, group_id):
        self.id = id
        self.name = name
        self.average_grade = average_grade
        self.group_id = group_id

class Group:
    def __init__(self, id, name):
            self.id = id
            self.name = name

class StudentGroup:
     def __init__(self, student_id, group_id):
                 self.student_id = student_id
                 self.group_id = group_id

students = [Student(1, "Ivanov", 3.3, 1), Student(2, "Petrov", 4.5, 1),
            Student(3, "Sidorov", 5.0, 2), Student(4, "Agrusev", 3.7, 3)]

groups = [Group(1, "AU5-31"), Group(2, "IU5-32"), Group(3, "AU5-33")]

students_groups = [StudentGroup(1, 1), StudentGroup(1, 2), StudentGroup(2, 1),
                   StudentGroup(3, 2), StudentGroup(4, 3)]

def main():
    one_to_many = [(student.name, student.average_grade, group.name)
                    for student in students for group in groups
                    if student.group_id == group.id]
    many_to_many = [(student.name, student.average_grade, group.name)
                    for student in students for group in groups
                    for student_group in students_groups
                    if student.id == student_group.student_id
                    and group.id == student_group.group_id]

    print("Задание 1:")
    students_ov = [(student[0], student[2]) for student in one_to_many
                   if student[0][-2:] == "ov"]
    print(students_ov)

    print("Задание 2:")
    groups_average_unsorted = [(group.name,
                                sum(student.average_grade
                                    for student in students
                                    if student.group_id == group.id) /
                                sum(1 for student in students
                                    if student.group_id == group.id))
                                for group in groups]
    groups_average_sorted = sorted(groups_average_unsorted, key = lambda x: x[1])
    print(groups_average_sorted)

    print("Задание 3:")
    groups_A = [(group.name, [student[0] for student in many_to_many
                              if student[2] == group.name])
                for group in groups if group.name[0] == "A"]
    print(groups_A)

if __name__ == "__main__":
      main()
