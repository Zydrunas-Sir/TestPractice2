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



