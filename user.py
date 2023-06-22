# 注册普通用户
import sqlite3
import PySimpleGUI as sg


def register_user(username, password):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password, userid) VALUES (?, ?, 1)", (username, password))
        conn.commit()
        sg.popup("注册成功！")
    except sqlite3.IntegrityError:
        sg.popup("用户名已存在，请尝试其他用户名。")


# 注册管理员
def register_admin(username, password):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password, userid) VALUES (?, ?, 0)", (username, password))
        conn.commit()
        sg.popup("注册成功！")
    except sqlite3.IntegrityError:
        sg.popup("用户名已存在，请尝试其他用户名。")


# 验证用户
def validate_user(username, password):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0] + 1
    else:
        return 0