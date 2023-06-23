import PySimpleGUI as sg  # GUI库，pip安装一下

from student import insert_student, get_all_students, get_student_me, bind_student


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


def get_student_info():
    layout = [
        [sg.Text('名字:'), sg.InputText()],
        [sg.Button('确定'), sg.Button('退出')]
    ]
    window = sg.Window('查询学生信息', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '退出':
            break
        elif event == '确定':
            student = get_student_me(values[0])
            return student
        get_student_info_next()
    window.close()


def get_student_info_next():
    students = get_student_info()
    if students:
        layout = [
            [sg.Text('ID\t姓名\t专业\t毕业年份\t课题状态')],
            [sg.Multiline('\n'.join([
                f'{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]}\t{s[7]}'
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


def query_student_info():
    students = get_all_students()
    if students:
        layout = [
            [sg.Text('ID\t姓名\t专业\t毕业年份\t课题状态')],
            [sg.Multiline('\n'.join([
                f'{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{"已完成" if s[4] == 0 else "已做完" if s[4] == 1 else "在修改" if s[4] == 2 else "未提交"}'
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
