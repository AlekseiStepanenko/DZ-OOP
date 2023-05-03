class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        i = 0
        for val in self.grades.values():
            i += sum(val) / len(val)
        avg = i / len(self.grades)
        return avg

    def __str__(self):

        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):

        if not isinstance(other, Student):
            print('Not a Student')
            return
        else:
            return self._average_grade() < other._average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grade(self):
        i = 0
        for val in self.grades.values():
            i += sum(val) / len(val)
        avg = i / len(self.grades)
        return avg

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_grade()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        else:
            return self._average_grade() < other._average_grade()


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
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


dima_petrov = Student('Dima', 'Petrov', 'Men')
olya_ivanova = Student('Olya', 'Ivanova', 'Female')

vasiliy_titov = Lecturer('Vasiliy', 'Titov')
oleg_popov = Lecturer('Oleg', 'Popov')

igor_bobov = Reviewer('Igor', 'Bobov')
pavel_lukin = Reviewer('Pavel', 'Lukin')

dima_petrov.courses_in_progress.append('C++')
dima_petrov.courses_in_progress.append('C#')
dima_petrov.courses_in_progress.append('Python')
dima_petrov.courses_in_progress.append('Java')
dima_petrov.finished_courses.append('PHP')

olya_ivanova.courses_in_progress.append('C++')
olya_ivanova.courses_in_progress.append('Python')
olya_ivanova.courses_in_progress.append('Java')
olya_ivanova.finished_courses.append('PHP')

vasiliy_titov.courses_attached.append('C++')
vasiliy_titov.courses_attached.append('Python')
vasiliy_titov.courses_attached.append('Java')
vasiliy_titov.courses_attached.append('PHP')

oleg_popov.courses_attached.append('C++')
oleg_popov.courses_attached.append('Python')
oleg_popov.courses_attached.append('C#')
igor_bobov.courses_attached.append('C++')
igor_bobov.courses_attached.append('Python')
pavel_lukin.courses_attached.append('C++')
pavel_lukin.courses_attached.append('Python')
pavel_lukin.courses_attached.append('Java')
pavel_lukin.courses_attached.append('PHP')
igor_bobov.courses_attached.append('C#')

dima_petrov.rate_hw(vasiliy_titov, 'C++', 5)
dima_petrov.rate_hw(oleg_popov, 'Python', 8)
dima_petrov.rate_hw(oleg_popov, 'Python', 7)
dima_petrov.rate_hw(oleg_popov, 'C#', 10)
dima_petrov.rate_hw(vasiliy_titov, 'Java', 7)
dima_petrov.rate_hw(vasiliy_titov, 'PHP', 3)
olya_ivanova.rate_hw(oleg_popov, 'C++', 6)
olya_ivanova.rate_hw(vasiliy_titov, 'Python', 4)
olya_ivanova.rate_hw(vasiliy_titov, 'Python', 3)
olya_ivanova.rate_hw(oleg_popov, 'C#', 4)
olya_ivanova.rate_hw(vasiliy_titov, 'Java', 3)
olya_ivanova.rate_hw(vasiliy_titov, 'PHP', 1)

igor_bobov.rate_hw(dima_petrov, 'C++', 9)
igor_bobov.rate_hw(dima_petrov, 'C++', 8)
igor_bobov.rate_hw(dima_petrov, 'C++', 6)
igor_bobov.rate_hw(dima_petrov, 'Python', 8)
pavel_lukin.rate_hw(olya_ivanova, 'C++', 9)
pavel_lukin.rate_hw(olya_ivanova, 'C++', 4)
pavel_lukin.rate_hw(olya_ivanova, 'C++', 4)
pavel_lukin.rate_hw(olya_ivanova, 'Python', 8)
pavel_lukin.rate_hw(olya_ivanova, 'PHP', 6)
pavel_lukin.rate_hw(olya_ivanova, 'Java', 10)
pavel_lukin.rate_hw(olya_ivanova, 'C#', 9)
pavel_lukin.rate_hw(dima_petrov, 'PHP', 3)
pavel_lukin.rate_hw(dima_petrov, 'Java', 5)
pavel_lukin.rate_hw(dima_petrov, 'C#', 10)


def avg_dz(list_students, course):
    avg = 0
    for student in list_students:
        avg += sum(student.grades[course]) / len(student.grades[course])
    return avg / len(list_students)


def avg_lecture_grade(list_lecturers, course):
    avg = 0
    for lecturer in list_lecturers:
        avg += sum(lecturer.grades[course]) / len(lecturer.grades[course])
    return avg / len(list_lecturers)


print(dima_petrov)
print()
print(olya_ivanova)
print()
print(vasiliy_titov)
print()
print(oleg_popov)
print()
print(igor_bobov)
print()
print(pavel_lukin)
print()
print(dima_petrov < olya_ivanova)
print()
print(oleg_popov < vasiliy_titov)
print()
print(avg_dz([dima_petrov, olya_ivanova], 'C++'))
print()
print(avg_lecture_grade([vasiliy_titov, oleg_popov], 'Python'))
