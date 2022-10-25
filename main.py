class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

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

    def __str__(self):
        return f'Имя: {self.name}\n'\
               f'Surname: {self.surname}\n'\
               f'Средняя оценка за домашние задания: {self.gpa_student}\n' \
               f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {",".join(self.finished_courses)}'

    def __lt__(self, other):
        std_1 = self.gpa_student
        std_2 = other.gpa_student
        return std_1 < std_2

    def __le__(self, other):
        std_1 = self.gpa_student
        std_2 = other.gpa_student
        return std_1 <= std_2

    def __eq__(self, other):
        std_1 = self.gpa_student
        std_2 = other.gpa_student
        return std_1 == std_2

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nSurname: {self.surname}\nСредняя оценка за лекции: {self.gpa_lecturer}'

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

    def __lt__(self, other):
        ltr_1 = self.gpa_lecturer
        ltr_2 = other.gpa_lecturer
        return ltr_1 < ltr_2

    def __le__(self, other):
        ltr_1 = self.gpa_lecturer
        ltr_2 = other.gpa_lecturer
        return ltr_1 <= ltr_2

    def __eq__(self, other):
        ltr_1 = self.gpa_lecturer
        ltr_2 = other.gpa_lecturer
        return ltr_1 == ltr_2

class Reviewer(Mentor):
    pass

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


def count_gpa_grade(persons, course):
    if not isinstance(persons, list):
        return "Not list"
    count_gpa = []
    for person in persons:
        count_gpa.extend(person.grades.get(course, []))
    if not count_gpa:
        return "По такому курсу ни у кого нет оценок"
    return round(sum(count_gpa) / len(count_gpa), 2)

# Студенты
best_student_roy = Student('Roy', 'Eman', 'man')
best_student_roy.courses_in_progress += ['Python', 'Sql', 'HTML']

best_student_nicol = Student('Nicol', 'Jonson', 'woman')
best_student_nicol.courses_in_progress += ['Pyton', 'Git', 'HTML']

# Лекторы
lecturer_mentor_sam = Lecturer('Sam', 'Buddy')
lecturer_mentor_sam.courses_attached += ['Python', 'Git']

lecturer_mentor_nik = Lecturer('Nik', 'Popins')
lecturer_mentor_nik.courses_attached += ['HTML', 'Sql', 'Git']

# Проверяющие
reviewer_mentor_jack = Reviewer('Jack', 'Gibbs')
reviewer_mentor_jack.courses_attached += ['Python', 'Sql']

reviewer_mentor_bob = Reviewer('Bob', 'Simons')
reviewer_mentor_bob.courses_attached += ['HTML', 'Git']

# Оценки
best_student_roy.rate_lecturer(lecturer_mentor_sam, 'Python', 10)
best_student_nicol.rate_lecturer(lecturer_mentor_sam, 'Git', 10)
best_student_nicol.rate_lecturer(lecturer_mentor_nik, 'Git', 5)

reviewer_mentor_jack.rate_hw(best_student_roy, 'Sql', 10)
reviewer_mentor_bob.rate_hw(best_student_nicol, 'HTML', 10)

best_student_nicol.finished_courses += ['Git']
print(best_student_nicol)
print(best_student_roy.gpa_student)
print(count_gpa_grade([lecturer_mentor_sam, lecturer_mentor_nik], 'Git'))

