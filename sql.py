import csv
import sqlite3
import PySimpleGUI as sg

from student import get_all_students
from topic import get_all_topics


# 数据库操作等函数
# 新建数据库文件，初始化程序数据库
def create_tables():
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    # 创建学生表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        sid INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        major TEXT NOT NULL,
        year INTEGER DEFAULT 2023,
        title_id INTEGER,
        state INTEGER DEFAULT 0,
        FOREIGN KEY (title_id) REFERENCES thesis_topics (tid)
    )
    ''')
    # 创建课题表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS topics (
        tid INTEGER PRIMARY KEY AUTOINCREMENT,
        title_name TEXT NOT NULL,
        description TEXT NOT NULL,
        teacher TEXT NOT NULL,
        student_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES students (sid)
    )
    ''')
    # 创建用户表用来登录
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    userid  INTEGER
    )
    ''')
    # 创建账户学生关系表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS student_user_relation (
    student_id INTEGER,
    user_id TEXT,
    name TEXT,
    username TEXT,
    FOREIGN KEY (student_id) REFERENCES students (sid),
    FOREIGN KEY (username) REFERENCES users (username),
    FOREIGN KEY (name) REFERENCES students (name),
    FOREIGN KEY (user_id) REFERENCES users (userid)
    )''')
    # 初始一个超级管理员
    cursor.execute("INSERT INTO users (username, password, userid) VALUES ('admin', 'admin123', 0)")

    # 初始一个普通用户
    cursor.execute("INSERT INTO users (username, password, userid) VALUES ('feng', 'fengyushun', 1)")
    conn.commit()
    conn.close()


# 数据库导出函数
def export_data_to_csv():
    students = get_all_students()
    topics = get_all_topics()

    with open('students.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['学生ID', '名字', '专业', '毕业年份'])
        writer.writerows(students)

    with open('topics.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['选题ID', '选题', '论文标题', '学生ID'])
        writer.writerows(topics)

    sg.popup('数据保存为 students.csv 和 topics.csv 成功.')


# 添加测试数据
def test_data():
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, major, year) VALUES ('张三', '法学', 2022)")
    cursor.execute("INSERT INTO students (name, major, year) VALUES ('李四', '计算机网络', 2022)")
    cursor.execute("INSERT INTO students (name, major, year) VALUES ('王五', '机电一体化', 2022)")
    cursor.execute("INSERT INTO topics (title, description, teacher) VALUES ('论怎么实现完美犯罪', '在法律边缘疯狂试探', '罗翔')")
    cursor.execute("INSERT INTO topics (title, description, student_id, teacher) VALUES (?, ?, ?, ?)")
    cursor.execute("INSERT INTO topics (title, description, student_id, teacher) VALUES (?, ?, ?, ?)")
    conn.commit()
    conn.close()
