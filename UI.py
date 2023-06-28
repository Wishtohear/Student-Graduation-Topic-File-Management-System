import PySimpleGUI as sg  # GUI库，pip安装一下
import os.path

from sql import create_tables, export_data_to_csv, test_data
from studentUI import input_student_info, query_student_info, bind_student_info, update_student_info, \
    delete_student_info
from topicUI import input_topic_info, update_topic_info, delete_topic_info, bind_topic_info, query_topic_info, \
    topic_status_up_info, topic_status_is_info
from user import register_user, register_admin, validate_user


# UI界面操作的一些函数
def register_ui():
    layout = [
        [sg.Text('           欢迎使用毕业选题管理系统          ')],
        [sg.Text('                  用户注册                ')],
        [sg.Text('请输入用户名'), sg.InputText(size=(15, 1), key="USERNAME")],
        [sg.Text('请输入密码'), sg.InputText(size=(17, 1), password_char="*", key="PASSWORD")],
        [sg.Text('请确认密码'), sg.InputText(size=(17, 1), password_char="*", key="PASSWORDOK")],
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
            if values["PASSWORD"] == values["PASSWORDOK"]:
                register_user(values["USERNAME"], values["PASSWORD"])
            else:
                sg.popup('两次密码不对，你在搞什么')
                break

        elif event == "注册管理员":
            if values["PASSWORD"] == values["PASSWORDOK"]:
                register_admin(values["USERNAME"], values["PASSWORD"])
            else:
                sg.popup('两次密码不对，你在搞什么')
                break
        window.close()
        main()


def main():
    # 检查数据库文件是否存在，如果不存在则创建表
    if not os.path.isfile('graduation_topics.db'):
        create_tables()
    layout = [
        [sg.Text('           欢迎使用毕业选题管理系统          ')],
        [sg.Text('                  用户登录                ')],
        [sg.Text('请输入用户名：'), sg.InputText(size=(15, 1), key="USERNAME")],
        [sg.Text('请输入密码：'), sg.InputText(size=(17, 1), password_char="*", key="PASSWORD")],
        [sg.Button('登录'), sg.Button('取消'), sg.Button('导入测试数据')],
        [sg.Text('没有用户？立即注册！'), sg.Button('注册')]
    ]
    window = sg.Window('登录毕业选题管理系统', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "取消":
            break
        elif event == "登录":
            login_result = validate_user(values["USERNAME"], values["PASSWORD"])
            if login_result == 1:
                sg.popup("管理员登录成功！")
                window.close()
                ad_main()
                break
            elif login_result == 2:
                sg.popup("用户登录成功！")
                window.close()
                us_main()
                break
            else:
                sg.popup("用户名或密码错误，请重试。")
        elif event == "注册":
            register_ui()
            window.close()
        elif event == "导入测试数据":
            test_data()
            sg.popup('数据导入成功')


def ad_main():
    layout = [
        [sg.Text('           欢迎使用毕业选题管理系统          ')],
        [sg.Button('添加学生'), sg.Button('添加课题')],
        [sg.Button('更新学生信息'), sg.Button('更新课题信息')],
        [sg.Button('删除学生信息'), sg.Button('删除课题信息')],
        [sg.Button('查询学生信息'), sg.Button('查询课题信息')],
        [sg.Button('保存数据'), sg.Button('退出登录')],
        [sg.Text('             毕业设计，仅供学习')]
    ]
    window = sg.Window('管理员界面', layout)

    while True:
        event, _ = window.read()
        if event == sg.WIN_CLOSED or event == '退出登录':
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
    main()


def us_main():
    layout = [
        [sg.Text('           欢迎使用毕业选题管理系统后门程序          ')],
        [sg.Button('绑定学生'), sg.Button('绑定课题')],
        [sg.Button('更新学生信息'), sg.Button('更新课题信息')],
        [sg.Button('论文状态提交'), sg.Button('论文状态修改')],
        [sg.Button('查询学生信息'), sg.Button('查询课题信息')],
        [sg.Button('保存数据'), sg.Button('退出登录')],
        [sg.Text('             毕业设计，仅供学习')]
    ]
    window = sg.Window('学生界面', layout)

    while True:
        event, _ = window.read()
        if event == sg.WIN_CLOSED or event == '退出登录':
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
            sg.popup("不是管理员怎么导出？")

    window.close()
    main()


def test_main():
    # 检查数据库文件是否存在，如果不存在则创建表
    if not os.path.isfile('graduation_topics.db'):
        create_tables()
    layout = [
        [sg.Text('           欢迎使用毕业选题管理系统          ')],
        [sg.Button('绑定学生'), sg.Button('绑定课题')],
        [sg.Button('更新学生信息'), sg.Button('更新课题信息')],
        [sg.Button('论文状态提交'), sg.Button('论文状态修改')],
        [sg.Button('查询学生信息'), sg.Button('查询课题信息')],
        [sg.Button('添加学生'), sg.Button('添加课题')],
        [sg.Button('保存数据'), sg.Button('退出登录'),sg.Button('导入测试数据')]
    ]
    window = sg.Window('登录毕业选题管理系统', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "取消":
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
        elif event == "导入测试数据":
            test_data()
            sg.popup('数据导入成功')
        elif event == '添加学生':
            input_student_info()
        elif event == '添加课题':
            input_topic_info()
        elif event == '论文状态提交':
            topic_status_up_info()
        elif event == '论文状态修改':
            topic_status_is_info()
