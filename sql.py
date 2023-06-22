import sqlite3


def create_tables():
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    # 创建学生表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        sid INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        major TEXT NOT NULL,
        title_id INTEGER,
        state TEXT NULL,
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
    # 初始一个超级管理员
    cursor.execute("INSERT INTO users (username, password, userid) VALUES (admin, admin123, 0)")
    # 初始一个普通用户
    cursor.execute("INSERT INTO users (username, password, userid) VALUES (feng, fengyushun, 1)")
    conn.commit()
    conn.close()
