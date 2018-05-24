# import pymysql
# from tools.read_config import SysConfig
#
#
# class MysqlConn(object):
#     def __init__(self):
#         self.config = SysConfig()
#         self.db = pymysql.connect(host=self.config.getValue('db', 'host'), user=self.config.getValue('db', 'user'),
#                                   password=self.config.getPsw('db', 'password').decode(),
#                                   db=self.config.getPsw('db', 'database').decode(),
#                                   port=self.config.getInt('db', 'port'))
#         self.cur = self.db.cursor()
#

# if __name__ == '__main__':
#     r = MysqlConn()
