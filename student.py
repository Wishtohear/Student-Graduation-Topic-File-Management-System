import sqlite3


# 性别转换函数
def gender_to_number(six):
    if six == "男":
        return 0
    else:
        return 1


# 学生类函数
# 基本实现曾删改查
# 添加学生函数
def insert_student(name, major, year, six):
    six_number = gender_to_number(six)
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, major, year, six) VALUES (?, ?, ?, ?)", (name, major, year, six_number))
    conn.commit()
    conn.close()


# 更新学生函数
def update_student(student_id, name, major, year, six):
    six_number = gender_to_number(six)
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name=?, major=?, year=? WHERE id=?, six=?", (name, major, year, student_id, six_number))
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


def get_student_me(name):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name = '?'"), name
    result1 = cursor.fetchall()
    cursor.execute("SELECT * FROM topics WHERE student_id = '?'"), result1[4]
    result2 = cursor.fetchall()
    var = result1 + result2
    conn.commit()
    conn.close()
    return var


# 绑定学生
def bind_student(name, username):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO student_user_relation (name, username) VALUES (?, ?)", (name, username))
    conn.commit()
    conn.close()
