import MySQLdb
from mysql_conn import db_connect


cr_t_users = """CREATE TABLE IF NOT EXISTS USERS(

                                UserId VARCHAR(255),
                                ScreenName VARCHAR(255),
                                PRIMARY KEY (ScreenName)
                                )"""

cr_t_hash = """CREATE TABLE IF NOT EXISTS USER_HASHTAG_SEARCH(
                              UserId VARCHAR(255),
                              UserName VARCHAR(255),
                              ScreenName VARCHAR(255),
                              TweetText VARCHAR(255),
                              UserLocation VARCHAR(255),
                              PRIMARY KEY (ScreenName)
                              
                              )"""

cr_t_activity = """CREATE TABLE IF NOT EXISTS USER_ACTIVITY(
                                Created_at VARCHAR (255),
                                UserId VARCHAR(255),
                                ScreenName VARCHAR(255),
                                TweetText VARCHAR(255),
                                Place VARCHAR(255),
                                Location VARCHAR(255) ,
                                PRIMARY KEY (ScreenName)
                                    )"""

cr_t_tweets = """CREATE TABLE IF NOT EXISTS TWEETS(
                                ScreenName VARCHAR(255),
                                tweet_id VARCHAR(255),
                                Created_at VARCHAR (255),
                                TweetText VARCHAR(255),
                                PRIMARY KEY (tweet_id)
                                    )"""

con=db_connect()
con.set_character_set('utf8')
cursor = con.cursor()
cursor.execute(cr_t_tweets)
cursor.execute(cr_t_users)
cursor.execute(cr_t_activity)
cursor.execute(cr_t_hash)

alter_table1 = """ALTER TABLE USER_ACTIVITY ADD FOREIGN KEY (ScreenName) REFERENCES USERS(ScreenName)"""
alter_table2 = """ ALTER TABLE TWEETS ADD FOREIGN KEY (ScreenName) REFERENCES USERS(ScreenName)"""
alter_table3 = """ ALTER TABLE USER_HASHTAG_SEARCH ADD FOREIGN KEY (ScreenName) REFERENCES USERS(ScreenName)"""
alter_table4 = """ ALTER TABLE USER_ACTIVITY ADD FOREIGN KEY (ScreenName) REFERENCES USERS(ScreenName)"""

cursor.execute(alter_table1)
cursor.execute(alter_table2)
cursor.execute(alter_table3)
cursor.execute(alter_table4)
