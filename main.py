from Database.Advert import *
from Database.Category import *
from Database.Comments import *
from Database.User import *


def join_advert_by_user(user_id):
    query = """SELECT User.first_name, Advert.item,date  FROM Advert
                JOIN User ON User.id = Advert.admin_id
                JOIN Categories ON Categories.id = Advert.category_id
                WHERE user_id = %s"""
    params = [user_id]
    select_query(query, params)


def join_comments_by_advert(advert_id):
    query = """SELECT Advert.item, Comments.comment FROM Comments
                    JOIN Advert ON Advert.id = Comments.advert_id
                    JOIN Categories ON Categories.id = Advert.category_id
                    WHERE advert_id = %s"""
    params = [advert_id]
    select_query(query, params)


def update_advert_item_if_creator(new_item, user_id, item_id):
    query = """UPDATE Advert SET item = %s WHERE admin_id = %s AND id = %s"""
    params = [new_item, user_id, item_id]
    CUD_query(query, params)


def update_comment_if_creator(comment_id, user_id, advert_id, new_comment):
    query = """UPDATE Comments SET comment = %s WHERE id = %s AND user_id = %s AND advert_id = %s"""
    params = [new_comment, comment_id, user_id, advert_id]
    CUD_query(query, params)
