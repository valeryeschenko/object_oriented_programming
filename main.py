class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nSurname: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.gpa_student}\n' \
               f'Курсы в процессе изучения: {self.courses_in_progress}\n' \
               f'Завершенные курсы: {self.finished_courses}'

    @property
    def gpa_student(self):
        sum_num = 0
        count = 0
        for gpa in self.grades.values():
            sum_num += sum(gpa)
            count += len(gpa)
        if count == 0:
            return 0
        return sum_num / count


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self):
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\nSurname: {self.surname}\nСредняя оценка за лекции: {self.gpa_lecturer}"

    @property
    def gpa_lecturer(self):
        sum_num = 0
        count = 0
        for gpa in self.grades.values():
            sum_num += sum(gpa)
            count += len(gpa)
        if count == 0:
            return 0
        return sum_num / count


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nSurname: {self.surname}\n"

