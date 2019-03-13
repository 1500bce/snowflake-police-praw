import pymysql

def connect_to_db():
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        db='praw_db',
        user='praw_sys',
        password='xxx'
    )

    return connection

def close_connection(connection):
    connection.close()

def execute_query(connection, query, isInsert):
    cur = connection.cursor()
    cur.execute(query)

    if isInsert:
        connection.commit()

    cur.close()

    return cur

def get_bot_history(connection):
    query = "SELECT * FROM bot_history"
    return execute_query(connection, query, False)

def get_data():
    connection = connect_to_db()
    result = get_bot_history(connection)
    close_connection(connection)
    return result

def insert_data(data):
    connection = connect_to_db()
    query = f'''
        INSERT INTO bot_history(submission_id, submission_title, submission_text, 
        submission_created_utc, comment_id, comment_author, comment_body)
        VALUES('{data.submission_id}', '{data.submission_title}', '{data.submission_text}',  
        '{data.submission_created_utc}','{data.comment_id}','{data.comment_author}','{data.comment_body}')
    '''
    # print(query)
    return execute_query(connection, query, True)


