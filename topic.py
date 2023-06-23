import sqlite3


# 课题类函数
# 基本实现曾删改查
# 添加课题函数
def insert_topic(title, description, student_id, teacher):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO topics (title_name, description, student_id, teacher) VALUES (?, ?, ?, ?)",
                   (title, description, student_id, teacher))
    conn.commit()
    conn.close()


# 更新课题函数
def update_topic(topic_id, title, description, student_id, teacher):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE topics SET title=?, description=?, student_id=? topic_id=?, teacher=?",
                   (title, description, student_id, topic_id, teacher))
    conn.commit()
    conn.close()


# 删除课题函数
def delete_topic(topic_id):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM topics WHERE id=?", (topic_id,))
    conn.commit()
    conn.close()


# 查询所以课题函数
def get_all_topics():
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM topics")
    topics = cursor.fetchall()
    conn.close()
    return topics


# 绑定课题
def bind_topic(topic_id, sid):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO student_user_relation (name, username) VALUES (?, ?)", (topic_id, sid))
    conn.commit()
    conn.close()
