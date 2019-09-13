import mysql.connector
from mysql.connector import Error

def connect(user_id, username, tweet, place, location):
    """
    connect to MySQL database and insert twitter data
    """
    try:
        con = mysql.connector.connect(host='remotemysql.com',
                                             database='zAgvpr43LA',
                                             user='zAgvpr43LA',
                                             password='vTrPIIHov2')

        if con.is_connected():
            """
            Insert twitter data
            """
            cursor = con.cursor()
            # twitter, golf
            cr_t= """CREATE TABLE IF NOT EXISTS USER_ACTIVITY(
    UserId VARCHAR(255),
    ScreenName VARCHAR(255),
    TweetText VARCHAR(255),
    Place VARCHAR(255),
    Location VARCHAR(255)
    )"""
            cursor.execute(cr_t)
            query = "INSERT INTO USER_ACTIVITY (UserId, ScreenName, TweetText, Place, Location) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (user_id, username, tweet, place, location))
            con.commit()


    except Error as e:
        print(e)

    cursor.close()
    con.close()
    print("MySQL connection is closed")
    return