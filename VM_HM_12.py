from requests import request
import time


class GetIp(object):

    def get_ip(self):
        s = request('GET', 'http://ip-api.com/json/')
        result = s.json()["query"]
        return result

    def timer(self):
        start_time = time.time()
        self.get_ip()
        return (time.time() - start_time)


info = GetIp()

ip = info.get_ip()
timecheck = info.timer()

print(ip)
print(timecheck)
