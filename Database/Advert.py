import datetime

from Database.DataBaseContextManager import CUD_query, select_query


def create_advert_table():
    query = """CREATE TABLE IF NOT EXISTS Advert(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                admin_id INTEGER,
                category_id INTEGER,
                item TEXT,
                number TEXT,
                date DATETIME,
                FOREIGN KEY (admin_id) REFERENCES User(id),
                FOREIGN KEY (category_id) REFERENCES Categories(id))"""
    CUD_query(query)


def create_advert(admin_id, category_id, item, number):
    date = datetime.date.today()
    query = """INSERT INTO Advert(admin_id, category_id, item, number, date) VALUES (%s, %s, %s, %s, %s)"""
    params = [admin_id, category_id, number, item, date]
    CUD_query(query, params)


def select_advert(advert_id):
    query = """SELECT * FROM Advert WHERE id = %s"""
    params = [advert_id]
    select_query(query, params)


def update_advert_item(advert_id, new_item):
    query = """UPDATE Advert SET item = %s WHERE id = %s"""
    params = [new_item, advert_id]
    CUD_query(query, params)


def delete_advert_by_id(advert_id):
    query = """DELETE FROM Advert WHERE id = %s"""
    params = [advert_id]
    CUD_query(query, params)
