import sqlite3


def insert_student(name, major, year):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, major, year) VALUES (?, ?, ?)", (name, major, year))
    conn.commit()
    conn.close()


def update_student(student_id, name, major, year):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name=?, major=?, year=? WHERE id=?", (name, major, year, student_id))
    conn.commit()
    conn.close()


def delete_student(student_id):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    conn.close()


def get_all_students():
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return students
