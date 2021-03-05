import datetime

from Database.DataBaseContextManager import CUD_query, select_query, select_function


def create_advert_table():
    query = """CREATE TABLE IF NOT EXISTS Advert(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                user_id INTEGER,
                category_id INTEGER,
                item TEXT,
                description TEXT,
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


def update_advert_description(description, advert_id, editing_user):
    get_advert_user_id_query = """Select user_id FROM Advert WHERE id = %s"""
    get_advert_user_id_params = [advert_id]
    advert_user_id = select_function(get_advert_user_id_query, get_advert_user_id_params)
    if editing_user == advert_user_id[0]:
        edit_advert_query = """ UPDATE Advert
        SET description = %s
        WHERE id = %s"""
        edit_advert_params = [description, advert_id]

        CUD_query(edit_advert_query, edit_advert_params)
    else:
        print("You cant edit this advert!!")


def delete_advert_by_id(advert_id):
    query = """DELETE FROM Advert WHERE id = %s"""
    params = [advert_id]
    CUD_query(query, params)
