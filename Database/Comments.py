from Database.DataBaseContextManager import CUD_query, select_query


def create_comments_table():
    query = """CREATE TABLE IF NOT EXISTS Comments(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                advert_id INTEGER,
                user_id INTEGER,
                comment TEXT,
                FOREIGN KEY (user_id) REFERENCES User(id),
                FOREIGN KEY (advert_id) REFERENCES Advert(id))"""
    CUD_query(query)


def create_comment(advert_id, user_id, comment):
    query = """INSERT INTO Comments(advert_id, user_id, comment) VALUES (%s, %s, %s)"""
    params = [advert_id, user_id, comment]
    CUD_query(query, params)


def select_comment(comment_id):
    query = """SELECT * FROM Comments WHERE id = %s"""
    params = [comment_id]
    select_query(query, params)


def update_comment_text(comment_id, new_comment):
    query = """UPDATE Comments SET comment = %s WHERE id = %s"""
    params = [new_comment, comment_id]
    CUD_query(query, params)


def delete_comment_by_id(comment_id):
    query = """DELETE FROM Comments WHERE id = %s"""
    params = [comment_id]
    CUD_query(query, params)
