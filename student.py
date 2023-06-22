import sqlite3


# 基本实现曾删改查
# 添加学生函数
def insert_student(name, major, year):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, major, year) VALUES (?, ?, ?)", (name, major, year))
    conn.commit()
    conn.close()


# 更新学生函数
def update_student(student_id, name, major, year):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name=?, major=?, year=? WHERE id=?", (name, major, year, student_id))
    conn.commit()
    conn.close()


# 删除学生函数
def delete_student(student_id):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    conn.close()


# 查询所有学生
def get_all_students():
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return students


def insert_student_my(name, major, year):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, major, year) VALUES (?, ?, ?)", (name, major, year))
    conn.commit()
    conn.close()


# 绑定学生
def bind_student(name, username):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO student_user_relation (name, username) VALUES (?, ?)", (name, username))
    conn.commit()
    conn.close()
