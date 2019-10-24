import getpass
import psycopg2
import numpy as np
from psycopg2.extensions import adapt, register_adapter, AsIs

# Then connects to the DB
mypasswd = getpass.getpass()
connection = psycopg2.connect(database = 'nce', 
                              user = 'nce14', 
                              host = 'dbase.sgn.missouri.edu',
                              password = mypasswd)

del(mypasswd)
cursor = connection.cursor()

register_adapter(np.int64,AsIs)
register_adapter(np.float64,AsIs)


##Truncate tables to ensure old data is removed
SQL = "TRUNCATE TABLE reddit_title_authors CASCADE"
cursor.execute(SQL)

SQL = "TRUNCATE TABLE nce14.reddit_titles CASCADE"
cursor.execute(SQL)

SQL = "TRUNCATE TABLE nce14.reddit_subreddits CASCADE"
cursor.execute(SQL)

SQL = "TRUNCATE TABLE nce14.reddit_authors CASCADE"
cursor.execute(SQL)


##Ingest data into the db
SQL = "INSERT INTO nce14.reddit_authors "
SQL += "(author_id, author) VALUES "
SQL += "(%s,%s)"
with connection, connection.cursor() as cursor:
    for row in author.itertuples(index=False, name=None):  # pull each row as a tuple        
        cursor.execute(SQL, row)


SQL = "INSERT INTO nce14.reddit_subreddits "
SQL += "(subreddit_id, subreddit) VALUES "
SQL += "(%s,%s)"
with connection, connection.cursor() as cursor:
    for row in subreddit.itertuples(index=False, name=None):  # pull each row as a tuple  
        cursor.execute(SQL, row)
    
SQL = "INSERT INTO nce14.reddit_titles "
SQL += "(title_id, title, summary_text, link, dttm, subreddit_id) VALUES "
SQL += "(%s,%s,%s,%s,%s,%s)"
with connection, connection.cursor() as cursor:
    for row in title.itertuples(index=False, name=None):  # pull each row as a tuple        
        cursor.execute(SQL, row)
        
SQL = "INSERT INTO nce14.reddit_title_authors "
SQL += "(author_id, title_id) VALUES "
SQL += "(%s,%s)"
with connection, connection.cursor() as cursor:
    for row in title_author.itertuples(index=False, name=None):  # pull each row as a tuple        
        cursor.execute(SQL, row)
