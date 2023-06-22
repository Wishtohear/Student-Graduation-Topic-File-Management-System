import sqlite3


def insert_topic(title, description, student_id, teacher):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO topics (title, description, student_id, teacher) VALUES (?, ?, ?, ?)",
                   (title, description, student_id, teacher))
    conn.commit()
    conn.close()


def update_topic(topic_id, title, description, student_id, teacher):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE topics SET title=?, description=?, student_id=? WHERE id=?, teacher=?",
                   (title, description, student_id, topic_id, teacher))
    conn.commit()
    conn.close()


def delete_topic(topic_id):
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM topics WHERE id=?", (topic_id,))
    conn.commit()
    conn.close()


def get_all_topics():
    conn = sqlite3.connect('graduation_topics.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM topics")
    topics = cursor.fetchall()
    conn.close()
    return topics
