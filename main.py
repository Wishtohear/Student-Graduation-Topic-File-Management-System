import sqlite3
import csv
import PySimpleGUI as sg  # GUI库，pip安装一下
import os.path


def create_tables():
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        sid INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        major TEXT NOT NULL,
        title_id INTEGER,
        state TEXT NOT NULL,
        FOREIGN KEY (title_id) REFERENCES thesis_topics (id)
    )
    ''')
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
    conn.commit()
    conn.close()


def insert_student(name, major, year):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, major, year) VALUES (?, ?, ?)", (name, major, year))
    conn.commit()
    conn.close()


def insert_topic(title, description, student_id):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO topics (title, description, student_id) VALUES (?, ?, ?)",
                   (title, description, student_id))
    conn.commit()
    conn.close()


def update_student(student_id, name, major, year):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name=?, major=?, year=? WHERE id=?", (name, major, year, student_id))
    conn.commit()
    conn.close()


def update_topic(topic_id, title, description, student_id):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE topics SET title=?, description=?, student_id=? WHERE id=?",
                   (title, description, student_id, topic_id))
    conn.commit()
    conn.close()


def delete_student(student_id):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    conn.close()


def delete_topic(topic_id):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM topics WHERE id=?", (topic_id,))
    conn.commit()
    conn.close()


def get_all_students():
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return students


def get_all_topics():
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM topics")
    topics = cursor.fetchall()
    conn.close()
    return topics


def input_student_info():
    layout = [
        [sg.Text('名字:'), sg.InputText()],
        [sg.Text('专业:'), sg.InputText()],
        [sg.Text('毕业年份:'), sg.InputText()],
        [sg.Button('确定'), sg.Button('退出')]
    ]
    window = sg.Window('输入学生信息', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '退出':
            break
        elif event == '确定':
            insert_student(values[0], values[1], values[2])
            sg.popup('学生录入成功.')
            break
    window.close()


def input_topic_info():
    layout = [
        [sg.Text('选题:'), sg.InputText()],
        [sg.Text('论文标题:'), sg.InputText()],
        [sg.Text('学生ID:'), sg.InputText()],
        [sg.Button('确定'), sg.Button('退出')]
    ]
    window = sg.Window('录入论文信息', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '退出':
            break
        elif event == '确定':
            insert_topic(values[0], values[1], int(values[2]))
            sg.popup('录入论文信息成功.')
            break
    window.close()


def update_student_info():
    layout = [
        [sg.Text('学生ID:'), sg.InputText()],
        [sg.Text('名字:'), sg.InputText()],
        [sg.Text('专业:'), sg.InputText()],
        [sg.Text('毕业年份:'), sg.InputText()],
        [sg.Button('确定'), sg.Button('退出')]
    ]
    window = sg.Window('更改学生信息', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '退出':
            break
        elif event == '确定':
            update_student(int(values[0]), values[1], values[2], values[3])
            sg.popup('学生信息更改成功.')
            break
    window.close()


def update_topic_info():
    layout = [
        [sg.Text('选题 ID:'), sg.InputText()],
        [sg.Text('选题:'), sg.InputText()],
        [sg.Text('论文标题:'), sg.InputText()],
        [sg.Text('学生ID:'), sg.InputText()],
        [sg.Button('确定'), sg.Button('退出')]
    ]
    window = sg.Window('更新课题信息', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '退出':
            break
        elif event == '确定':
            update_topic(int(values[0]), values[1], values[2], int(values[3]))
            sg.popup('课题更新成功.')
            break
    window.close()


def delete_student_info():
    layout = [
        [sg.Text('学生ID:'), sg.InputText()],
        [sg.Button('确定'), sg.Button('退出')]
    ]
    window = sg.Window('删除学生', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '退出':
            break
        elif event == '确定':
            delete_student(int(values[0]))
            sg.popup('学生删除成功.')
            break
    window.close()


def delete_topic_info():
    layout = [
        [sg.Text('选题 ID:'), sg.InputText()],
        [sg.Button('确定'), sg.Button('退出')]
    ]
    window = sg.Window('删除选题', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '退出':
            break
        elif event == '确定':
            delete_topic(int(values[0]))
            sg.popup('选题删除成功.')
            break
    window.close()


def query_student_info():
    students = get_all_students()
    if students:
        layout = [
            [sg.Text('ID\t姓名\t专业\t毕业年份')],
            [sg.Multiline('\n'.join([f'{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}' for s in students]), size=(50, 10),
                          disabled=True)],
            [sg.Button('看完了')]
        ]
        window = sg.Window('学生信息', layout)
        while True:
            event, _ = window.read()
            if event == sg.WIN_CLOSED or event == '看完了':
                break
        window.close()
    else:
        sg.popup('没有学生信息.')


def query_topic_info():
    topics = get_all_topics()
    if topics:
        layout = [
            [sg.Text('选题ID\t选题标题\t论文标题\t学生ID')],
            [sg.Multiline('\n'.join([f'{t[0]}\t{t[1]}\t{t[2]}\t{t[3]}' for t in topics]), size=(50, 10),
                          disabled=True)],
            [sg.Button('看完了')]
        ]
        window = sg.Window('选题信息', layout)
        while True:
            event, _ = window.read()
            if event == sg.WIN_CLOSED or event == '看完了':
                break
        window.close()
    else:
        sg.popup('没有选题信息.')


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


def ad_main():
    # 检查数据库文件是否存在，如果不存在则创建表
    if not os.path.isfile('graduation_topics.db'):
        create_tables()

    layout = [
        [sg.Text('           欢迎使用毕业选题管理系统          ')],
        [sg.Button('添加学生'), sg.Button('添加课题')],
        [sg.Button('更新学生信息'), sg.Button('更新课题信息')],
        [sg.Button('删除学生信息'), sg.Button('删除课题信息')],
        [sg.Button('查询学生信息'), sg.Button('查询课题信息')],
        [sg.Button('保存数据'), sg.Button('退出')],
        [sg.Text('             毕业设计，仅供学习')]
    ]
    window = sg.Window('毕业选题管理系统', layout)

    while True:
        event, _ = window.read()
        if event == sg.WIN_CLOSED or event == '退出':
            break
        elif event == '添加学生':
            input_student_info()
        elif event == '添加课题':
            input_topic_info()
        elif event == '更新学生信息':
            update_student_info()
        elif event == '更新课题信息':
            update_topic_info()
        elif event == '删除学生信息':
            delete_student_info()
        elif event == '删除课题信息':
            delete_topic_info()
        elif event == '查询学生信息':
            query_student_info()
        elif event == '查询课题信息':
            query_topic_info()
        elif event == '保存数据':
            export_data_to_csv()

    window.close()


if __name__ == '__main__':
    main()
