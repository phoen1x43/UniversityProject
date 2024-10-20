import sqlite3

def create_db():
    try:
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Students (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Surname TEXT NOT NULL,
                Department TEXT NOT NULL,
                DateOfBirth TEXT NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Teachers (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Surname TEXT NOT NULL,
                Department TEXT NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Courses (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Title TEXT NOT NULL,
                Description TEXT NOT NULL,
                TeacherID INTEGER,
                FOREIGN KEY (TeacherID) REFERENCES Teachers (ID)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Exams (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Date TEXT NOT NULL,
                CourseID INTEGER,
                MaxScore INTEGER NOT NULL,
                FOREIGN KEY (CourseID) REFERENCES Courses (ID)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Grades (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                StudentID INTEGER,
                ExamID INTEGER,
                Score INTEGER NOT NULL,
                FOREIGN KEY (StudentID) REFERENCES Students (ID),
                FOREIGN KEY (ExamID) REFERENCES Exams (ID)
            )
        ''')

        conn.commit()
        print("База данных создана!")
    except sqlite3.Error as e:
        print(f"Ошибка при создании базы данных: {e}")
    finally:
        if conn:
            conn.close()

def add_student(name, surname, department, date_of_birth):
    try:
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Students (Name, Surname, Department, DateOfBirth) VALUES (?, ?, ?, ?)', (name, surname, department, date_of_birth))
        conn.commit()
        print("Студент добавлен!")
    except sqlite3.Error as e:
        print(f"Ошибка добавления студента: {e}")

def add_teacher(name, surname, department):
    try:
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Teachers (Name, Surname, Department) VALUES (?, ?, ?)', (name, surname, department))
        conn.commit()
        print("Преподаватель добавлен!")
    except sqlite3.Error as e:
        print(f"Ошибка добавления преподавателя: {e}")

def add_course(title, description, teacher_id):
    try:
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Courses (Title, Description, TeacherID) VALUES (?, ?, ?)', (title, description, teacher_id))
        conn.commit()
        print("Курс добавлен!")
    except sqlite3.Error as e:
        print(f"Ошибка добавления курса: {e}")

def add_exam(date, course_id, max_score):
    try:
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Exams (Date, CourseID, MaxScore) VALUES (?, ?, ?)', (date, course_id, max_score))
        conn.commit()
        print("Экзамен добавлен!")
    except sqlite3.Error as e:
        print(f"Ошибка добавления экзамена: {e}")

def add_grade(student_id, exam_id, score):
    try:
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Grades (StudentID, ExamID, Score) VALUES (?, ?, ?)', (student_id, exam_id, score))
        conn.commit()
        print("Оценка добавлена!")
    except sqlite3.Error as e:
        print(f"Ошибка добавления оценки: {e}")

def update_student(student_id, name=None, surname=None, department=None):
    try:
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        if name:
            cursor.execute('UPDATE Students SET Name = ? WHERE ID = ?', (name, student_id))
        if surname:
            cursor.execute('UPDATE Students SET Surname = ? WHERE ID = ?', (surname, student_id))
        if department:
            cursor.execute('UPDATE Students SET Department = ? WHERE ID = ?', (department, student_id))
        conn.commit()
        print("Информация о студенте изменена!")
    except sqlite3.Error as e:
        print(f"Ошибка изменения информации о студенте: {e}")

def update_teacher(teacher_id, name=None, surname=None, department=None):
    try:
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        if name:
            cursor.execute('UPDATE Teachers SET Name = ? WHERE ID = ?', (name, teacher_id))
        if surname:
            cursor.execute('UPDATE Teachers SET Surname = ? WHERE ID = ?', (surname, teacher_id))
        if department:
            cursor.execute('UPDATE Teachers SET Department = ? WHERE ID = ?', (department, teacher_id))
        conn.commit()
        print("Информация о преподавателе изменена!")
    except sqlite3.Error as e:
        print(f"Ошибка изменения информации о преподавателе: {e}")

def update_course(course_id, title=None, description=None, teacher_id=None):
    try:
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        if title:
            cursor.execute('UPDATE Courses SET Title = ? WHERE ID = ?', (title, course_id))
        if description:
            cursor.execute('UPDATE Courses SET Description = ? WHERE ID = ?', (description, course_id))
        if teacher_id is not None:
            cursor.execute('UPDATE Courses SET TeacherID = ? WHERE ID = ?', (teacher_id, course_id))
        conn.commit()
        print("Информация о курсе изменена!")
    except sqlite3.Error as e:
        print(f"Ошибка изменения информации о курсе: {e}")

def delete_student(student_id):
    try:
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Students WHERE ID = ?', (student_id,))
        conn.commit()
        print("Студент удален!")
    except sqlite3.Error as e:
        print(f"Ошибка удаления студента: {e}")

def delete_teacher(teacher_id):
    try:
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Teachers WHERE ID = ?', (teacher_id,))
        conn.commit()
        print("Преподаватель удален!")
    except sqlite3.Error as e:
        print(f"Ошибка удаления преподавателя: {e}")

def delete_course(course_id):
    try:
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Courses WHERE ID = ?', (course_id,))
        conn.commit()
        print("Курс удален!")
    except sqlite3.Error as e:
        print(f"Ошибка удаления курса: {e}")

def delete_exam(exam_id):
    try:
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Exams WHERE ID = ?', (exam_id,))
        conn.commit()
        print("Экзамен удален!")
    except sqlite3.Error as e:
        print(f"Ошибка удаления экзамена: {e}")

def get_students_by_department(department):
    try:
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Students WHERE Department = ?', (department,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Ошибка получения студентов по факультету: {e}")

def get_courses_by_teacher(teacher_id):
    try:
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Courses WHERE TeacherID = ?', (teacher_id,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Ошибка получения курсов по преподавателю: {e}")

def get_students_in_course(course_id):
    try:
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        cursor.execute('''
                SELECT * FROM Students
                JOIN Grades ON Students.ID = Grades.StudentID
                JOIN Exams ON Grades.ExamID = Exams.ID
                WHERE Exams.CourseID = ?
            ''', (course_id,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Ошибка получения студентов по конкретному курсу: {e}")

def get_grades_by_course(course_id):
    try:
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        cursor.execute('''
                SELECT * FROM Grades
                JOIN Exams ON Grades.ExamID = Exams.ID
                WHERE Exams.CourseID = ?
            ''', (course_id,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Ошибка получения оценок по курсу: {e}")

def average_score_student(student_id, course_id):
    try:
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        cursor.execute('''
                SELECT AVG(Score) FROM Grades
                JOIN Exams ON Grades.ExamID = Exams.ID
                WHERE Grades.StudentID = ? AND Exams.CourseID = ?
            ''', (student_id, course_id))
        return cursor.fetchone()[0]
    except sqlite3.Error as e:
        print(f"Ошибка вычисления среднего балла студента по курсу: {e}")

def average_score_student_overall(student_id):
    try:
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        cursor.execute('SELECT AVG(Score) FROM Grades WHERE StudentID = ?', (student_id,))
        return cursor.fetchone()[0]
    except sqlite3.Error as e:
        print(f"Ошибка вычисления общего среднего балла студента: {e}")

def average_score_department(department):
    try:
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT AVG(Score) FROM Grades
            JOIN Students ON Grades.StudentID = Students.ID
            WHERE Students.Department = ?
        ''', (department,))
        return cursor.fetchone()[0]
    except sqlite3.Error as e:
        print(f"Ошибка вычисления среднего балла по факультету: {e}")

def main():
    while True:
        print("Выберите действие:")
        print("1. Добавить студента")
        print("2. Добавить преподавателя")
        print("3. Добавить курс")
        print("4. Добавить экзамен")
        print("5. Добавить оценку")
        print("6. Изменить информацию о студенте")
        print("7. Изменить информацию о преподавателе")
        print("8. Изменить информацию о курсе")
        print("9. Удалить студента")
        print("10. Удалить преподавателя")
        print("11. Удалить курс")
        print("12. Удалить экзамен")
        print("13. Получить список студентов по факультету")
        print("14. Получить список курсов, читаемых преподавателем")
        print("15. Получить список студентов, зачисленных на конкретный курс")
        print("16. Получить оценки студентов по курсу")
        print("17. Средний балл студента по курсу")
        print("18. Средний балл студента в целом")
        print("19. Средний балл по факультету")
        print("20. Выход")

        answer = input("Ваш выбор: ")

        if answer == '1':
            name = input("Имя: ")
            surname = input("Фамилия: ")
            department = input("Факультет: ")
            date_of_birth = input("Дата рождения (в формате YYYY-MM-DD): ")
            add_student(name, surname, department, date_of_birth)

        elif answer == '2':
            name = input("Имя: ")
            surname = input("Фамилия: ")
            department = input("Кафедра: ")
            add_teacher(name, surname, department)

        elif answer == '3':
            title = input("Название курса: ")
            description = input("Описание курса: ")
            teacher_id = int(input("ID преподавателя: "))
            add_course(title, description, teacher_id)

        elif answer == '4':
            date = input("Дата экзамена (в формате YYYY-MM-DD): ")
            course_id = int(input("ID курса: "))
            max_score = int(input("Максимальный балл: "))
            add_exam(date, course_id, max_score)

        elif answer == '5':
            student_id = int(input("ID студента: "))
            exam_id = int(input("ID экзамена: "))
            score = int(input("Оценка: "))
            add_grade(student_id, exam_id, score)

        elif answer == '6':
            student_id = int(input("ID студента: "))
            name = input("Новое имя (оставьте пустым, если не хотите изменять): ")
            surname = input("Новая фамилия (оставьте пустым, если не хотите изменять): ")
            department = input("Новый факультет (оставьте пустым, если не хотите изменять): ")
            update_student(student_id, name or None, surname or None, department or None)

        elif answer == '7':
            teacher_id = int(input("ID преподавателя: "))
            name = input("Новое имя (оставьте пустым, если не хотите изменять): ")
            surname = input("Новая фамилия (оставьте пустым, если не хотите изменять): ")
            department = input("Новая кафедра (оставьте пустым, если не хотите изменять): ")
            update_teacher(teacher_id, name or None, surname or None, department or None)

        elif answer == '8':
            course_id = int(input("ID курса: "))
            title = input("Новое название (оставьте пустым, если не хотите изменять): ")
            description = input("Новое описание (оставьте пустым, если не хотите изменять): ")
            teacher_id = input("Новый ID преподавателя (оставьте пустым, если не хотите изменять): ")
            update_course(course_id, title or None, description or None, int(teacher_id) if teacher_id else None)

        elif answer == '9':
            student_id = int(input("ID студента: "))
            delete_student(student_id)

        elif answer == '10':
            teacher_id = int(input("ID преподавателя: "))
            delete_teacher(teacher_id)

        elif answer == '11':
            course_id = int(input("ID курса: "))
            delete_course(course_id)

        elif answer == '12':
            exam_id = int(input("ID экзамена: "))
            delete_exam(exam_id)

        elif answer == '13':
            department = input("Введите факультет: ")
            students = get_students_by_department(department)
            for student in students:
                print(student)

        elif answer == '14':
            teacher_id = int(input("ID преподавателя: "))
            courses = get_courses_by_teacher(teacher_id)
            for course in courses:
                print(course)

        elif answer == '15':
            course_id = int(input("ID курса: "))
            students = get_students_in_course(course_id)
            for student in students:
                print(student)

        elif answer == '16':
            course_id = int(input("ID курса: "))
            grades = get_grades_by_course(course_id)
            for grade in grades:
                print(grade)

        elif answer == '17':
            student_id = int(input("ID студента: "))
            course_id = int(input("ID курса: "))
            avg_score = average_score_student(student_id, course_id)
            print(f"Средний балл студента по курсу: {avg_score}")

        elif answer == '18':
            student_id = int(input("ID студента: "))
            avg_score = average_score_student_overall(student_id)
            print(f"Средний балл студента в целом: {avg_score}")

        elif answer == '19':
            department = input("Введите факультет: ")
            avg_score = average_score_department(department)
            print(f"Средний балл по факультету: {avg_score}")

        elif answer == '20':
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Выберите существующий вариант.")

if __name__ == "__main__":
    create_db()
    main()



