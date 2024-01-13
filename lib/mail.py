# gw edit dikit doang gan :'v
import requests
import json
import random
import time
from datetime import datetime

class Email(requests.Session):
	
	def __init__(self, session=None):
		super().__init__()
		self.session = session
	
	@property
	def Mail(self):
		self.buildses = user = "".join(random.SystemRandom().choice("qwertyuiopasdfghjklzxcvbnm0987654321") for i in range(26))
		self.create = self.get(f"https://10minutemail.net/address.api.php?new=1&sessionid={self.buildses}&_={int(datetime.now().timestamp() * 1000)}").json()
		return {"mail": self.create["permalink"]["mail"], "session": self.create["session_id"]}

	def inbox(self, loop=False):
		time.sleep(1)
		self.sessinbox = self.session if self.session else self.buildses
		self.data = self.get(f"https://10minutemail.net/address.api.php?sessionid={self.sessinbox}&_={int(datetime.now().timestamp() * 1000)}").json()
		if len(self.data["mail_list"]) !=1:
			self.address = self.data["mail_list"][0]["subject"]
			self.id = self.data["mail_list"][0]["mail_id"]
			self.box = self.get(f"https://10minutemail.net//mail.api.php?mailid={self.id}&sessionid={self.sessinbox}").json()
			self.plain = self.box["plain_link"]
			self.datetime = self.box["datetime"]
			self.to = self.box["to"]
			self.name = self.box["header_decode"]["replylist"][0]["name"]
			self.amli = self.box["header_decode"]["replylist"][0]["address"]
			return {"topic": self.address, "name": self.name, "from": self.amli, "to": self.to, "message": self.plain[0], "datetime": self.datetime}