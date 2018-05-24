import redis
from tools.read_config import SysConfig


class RedisConn(object):
    def __init__(self):
        self.config = SysConfig()
        try:
            self.pool = redis.ConnectionPool(host=self.config.getValue('redis', 'host'),
                                             port=self.config.getInt('redis', 'port'),
                                             db=self.config.getInt('redis', 'db'),
                                             password=self.config.getPsw('redis', 'password'))
            self.redis_conn = redis.Redis(connection_pool=self.pool)
        except Exception as e:
            print(e)

    def get(self, key):
        return self.redis_conn.get(key)

    def set(self, key, word):
        return self.redis_conn.set(key, word)


if __name__ == '__main__':
    Re = RedisConn()
    res = Re.get('s')
    print(res)

