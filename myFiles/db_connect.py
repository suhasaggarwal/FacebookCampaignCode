import MySQLdb
from fb_app_config import *


class DBConnect:

    def __init__(self):
        conf_obj = AppConf()
        self.host = conf_obj.host
        self.username = conf_obj.username
        self.password = conf_obj.password
        self.db = conf_obj.db

    def db_connect_query(self, query, isupdate=0):
        error = False
        query_result = ((),)
        try:
            db = MySQLdb.connect(host=self.host,
                                 user= self.username,
                                 passwd= self.password,
                                 db= self.db)
            cur = db.cursor()
        except Exception as e:
            error = 'error in connecting to db is: %s' % (e)
            cur.close()
            db.close()

        if isupdate==0:
            try:
                cur.execute(query)
                query_result = cur.fetchall()
                cur.close()
                db.close()
            except Exception as e:
                error = 'error in fetching data  is: %s' % (e)
                cur.close()
                db.close()
        else:
            try:
                query_result = cur.execute(query)
                db.commit()
                cur.close()
                db.close()
            except Exception as e:
                error = 'error in inserting/updating data into db is: %s' % (e)
                cur.close()
                db.close()

        return query_result, error