"""Фукция Сбора информации о книге"""


def book_data():
    data = {}
    data.update(dict(name=input('Введите наименование книги: '),
                     author=input('Введите автора книги: '),
                     year=input('Введите год издания книги: '),
                     genre=input('Введите жанр книги: ')))
    print(data)


book_data()


"""Фукция Учёта оценок студентов"""


def students_grade():
    grades = {}
    for i in range(int(input('Введите кол-во студентов: '))):
        student_name = input('Введите Имя студента: ')
        grade = int(input('Введите Оценку студента: '))
        grades[student_name] = grade
    print(f'Средниц балл класса: {float(sum(grades.values()) / len(grades))}')


students_grade()