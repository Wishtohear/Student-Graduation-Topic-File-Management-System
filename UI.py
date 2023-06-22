import PySimpleGUI as sg  # GUI库，pip安装一下
import os.path

from sql import create_tables, export_data_to_csv
from student import insert_student, update_student, delete_student, get_all_students, bind_student
from topic import update_topic, delete_topic, get_all_topics, insert_topic, bind_topic
from user import register_user, register_admin, validate_user


# UI界面操作的一些函数
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


def bind_student_info():
    layout = [
        [sg.Text('名字:'), sg.InputText()],
        [sg.Text('账号:'), sg.InputText()],
        [sg.Button('确定'), sg.Button('退出')]
    ]
    window = sg.Window('输入学生信息', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '退出':
            break
        elif event == '确定':
            bind_student(values[0], values[1])
            sg.popup('学生绑定成功.')
            break
    window.close()


def input_topic_info():
    layout = [
        [sg.Text('论文标题:'), sg.InputText()],
        [sg.Text('论文描述:'), sg.InputText()],
        [sg.Text('学生ID:'), sg.InputText()],
        [sg.Text('指导老师'), sg.InputText()],
        [sg.Button('确定'), sg.Button('退出')]
    ]
    window = sg.Window('录入论文信息', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '退出':
            break
        elif event == '确定':
            insert_topic(values[0], values[1], int(values[2]), values[3])
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
        [sg.Text('论文标题:'), sg.InputText()],
        [sg.Text('论文描述:'), sg.InputText()],
        [sg.Text('学生ID:'), sg.InputText()],
        [sg.Text('指导老师'), sg.InputText()],
        [sg.Button('确定'), sg.Button('退出')]
    ]
    window = sg.Window('更新课题信息', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '退出':
            break
        elif event == '确定':
            update_topic(int(values[0]), values[1], values[2], int(values[3]), values[4])
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


def bind_topic_info():
    layout = [
        [sg.Text('课题id:'), sg.InputText()],
        [sg.Text('学生id:'), sg.InputText()],
        [sg.Button('确定'), sg.Button('退出')]
    ]
    window = sg.Window('输入信息', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '退出':
            break
        elif event == '确定':
            bind_topic(values[0], values[1])
            sg.popup('课题绑定成功.')
            break
    window.close()


def query_student_info():
    students = get_all_students()
    if students:
        layout = [
            [sg.Text('ID\t姓名\t专业\t毕业年份\t课题状态')],
            [sg.Multiline('\n'.join([
                                        f'{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{"未提交" if s[4] == 0 else "已做完" if s[4] == 1 else "在修改" if s[4] == 2 else "已完成"}'
                                        for s in students]), size=(50, 10),
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
            [sg.Text('选题ID\t选题标题\t论文标题\t指导老师\t学生ID')],
            [sg.Multiline('\n'.join([f'{t[0]}\t{t[1]}\t{t[2]}\t{t[3]}\t{t[4]}' for t in topics]), size=(50, 10),
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


def register_ui():
    layout = [
        [sg.Text('           欢迎使用毕业选题管理系统          ')],
        [sg.Text('                  用户注册                ')],
        [sg.Text('请输入用户名'), sg.InputText(key="USERNAME")],
        [sg.Text('请输入密码'), sg.InputText(password_char="*", key="PASSWORD")],
        [sg.Button('注册用户'), sg.Button('注册管理员')],
        [sg.Text('有用户？立即登录！'), sg.Button('登录')]
    ]
    window = sg.Window('注册用户', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "取消":
            break
        elif event == "登录":
            main()
            window.close()
        elif event == "注册用户":
            register_user(values["USERNAME"], values["PASSWORD"])
        elif event == "注册管理员":
            register_admin(values["USERNAME"], values["PASSWORD"])


def main():
    # 检查数据库文件是否存在，如果不存在则创建表
    if not os.path.isfile('graduation_topics.db'):
        create_tables()
    layout = [
        [sg.Text('           欢迎使用毕业选题管理系统          ')],
        [sg.Text('                  用户登录                ')],
        [sg.Text('请输入用户名'), sg.InputText(key="USERNAME")],
        [sg.Text('请输入密码'), sg.InputText(password_char="*", key="PASSWORD")],
        [sg.Button('登录'), sg.Button('取消')],
        [sg.Text('没有用户？立即注册！'), sg.Button('注册')]
    ]
    window = sg.Window('登录毕业选题管理系统', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "取消":
            break
        elif event == "登录":
            login_result = validate_user(values["USERNAME"], values["PASSWORD"])
            if login_result == 2:
                sg.popup("管理员登录成功！")
                window.close()
                ad_main()
                break
            elif login_result == 0:
                sg.popup("用户登录成功！")
                window.close()
                us_main()
                break
            else:
                sg.popup("用户名或密码错误，请重试。")
        elif event == "注册":
            register_ui()
            window.close()


def ad_main():
    layout = [
        [sg.Text('           欢迎使用毕业选题管理系统          ')],
        [sg.Button('添加学生'), sg.Button('添加课题')],
        [sg.Button('更新学生信息'), sg.Button('更新课题信息')],
        [sg.Button('删除学生信息'), sg.Button('删除课题信息')],
        [sg.Button('查询学生信息'), sg.Button('查询课题信息')],
        [sg.Button('保存数据'), sg.Button('退出')],
        [sg.Text('             毕业设计，仅供学习')]
    ]
    window = sg.Window('管理员界面', layout)

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


def us_main():
    layout = [
        [sg.Text('           欢迎使用毕业选题管理系统          ')],
        [sg.Button('绑定学生'), sg.Button('绑定课题')],
        [sg.Button('更新学生信息'), sg.Button('更新课题信息')],
        [sg.Button('论文状态提交'), sg.Button('论文状态修改')],
        [sg.Button('查询学生信息'), sg.Button('查询课题信息')],
        [sg.Button('保存数据'), sg.Button('退出')],
        [sg.Text('             毕业设计，仅供学习')]
    ]
    window = sg.Window('学生界面', layout)

    while True:
        event, _ = window.read()
        if event == sg.WIN_CLOSED or event == '退出':
            break
        elif event == '绑定学生':
            bind_student_info()
        elif event == '绑定课题':
            bind_topic_info()
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
