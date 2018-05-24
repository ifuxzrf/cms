import pymongo
from tools.read_config import SysConfig


class MongoConn(object):
    def __init__(self):
        self.config = SysConfig()
        self.conn = pymongo.MongoClient(self.config.getValue('mongodb', 'host'), int(self.config.getInt('mongodb', 'port')))
        self.db = self.conn[self.config.getValue('mongodb', 'db_name')]  # connect db
        self.username = self.config.getValue('mongodb', 'username')
        self.password = self.config.getValue('mongodb', 'password')
        if self.username and self.password:
            self.connected = self.db.authenticate(self.username, self.password)
        else:
            self.connected = True


if __name__ == '__main__':
    my_conn = MongoConn()
    # users = [{"name": "cui", "age": "9"}, {"name": "cui", "age": "11"}]
    # my_conn.db['fx'].insert(users)
    for r in my_conn.db['fx'].find():
        print(r)
