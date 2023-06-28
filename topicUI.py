import PySimpleGUI as sg  # GUI库，pip安装一下

from topic import insert_topic, update_topic, delete_topic, bind_topic, get_all_topics, topic_status_up, topic_status_is


def input_topic_info():
    layout = [
        [sg.Text('论文标题:'), sg.InputText(size=(17, 1))],
        [sg.Text('论文描述:'), sg.InputText(size=(17, 1))],
        [sg.Text('学生ID:'), sg.InputText(size=(17, 1))],
        [sg.Text('指导老师'), sg.InputText(size=(17, 1))],
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


def update_topic_info():
    layout = [
        [sg.Text('选题 ID:'), sg.InputText(size=(17, 1))],
        [sg.Text('论文标题:'), sg.InputText(size=(17, 1))],
        [sg.Text('论文描述:'), sg.InputText(size=(17, 1))],
        [sg.Text('学生ID:'), sg.InputText(size=(17, 1))],
        [sg.Text('指导老师'), sg.InputText(size=(17, 1))],
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


def delete_topic_info():
    layout = [
        [sg.Text('选题 ID:'), sg.InputText(size=(17, 1))],
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
        [sg.Text('课题id:'), sg.InputText(size=(17, 1))],
        [sg.Text('学生id:'), sg.InputText(size=(17, 1))],
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


def query_topic_info():
    topics = get_all_topics()
    if topics:
        layout = [
            [sg.Text('选题ID\t选题标题\t论文标题\t指导老师\t学生ID')],
            [sg.Multiline('\n'.join([f'{t[0]}\t{t[1]}\t{t[2]}\t{t[3]}\t'
                                     f'{t[4]}\t{"未绑定" if t[4] is None else t[4]}' for t in topics]), size=(70, 10),
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


def topic_status_up_info():
    layout = [
        [sg.Text('学生id:'), sg.InputText(size=(17, 1))],
        [sg.Text('课题id:'), sg.InputText(size=(17, 1))],
        [sg.Button('确定'), sg.Button('退出')]
    ]
    window = sg.Window('输入信息', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '退出':
            break
        elif event == '确定':
            topic_status_up(values[0], values[1])
            sg.popup('课题状态更新成功.')
            break
    window.close()


def topic_status_is_info():
    layout = [
        [sg.Text('学生id:'), sg.InputText(size=(17, 1))],
        [sg.Text('课题id:'), sg.InputText(size=(17, 1))],
        [sg.Radio('未提交', 'status', default=True, key='0'),
         sg.Radio('已提交', 'status', key='1'),
         sg.Radio('已完成', 'status', key='2'),
         sg.Radio('在修改', 'status', key='3')],
        [sg.Button('确定'), sg.Button('退出')]
    ]
    window = sg.Window('输入信息', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '退出':
            break
        elif event == '确定':
            status = int(values[2]) + int(values[3]) * 2 + int(values[4]) * 3 + int(values[5]) * 4
            sg.popup('您选择的状态值是：', status)
            topic_status_is(values[0], values[1], status)
            sg.popup('课题状态更新成功')
            break
    window.close()
