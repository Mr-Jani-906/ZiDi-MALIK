exec(')"rotareneg-au llatsni pip"(metsys.so\t\n:tpecxe\nrotareneg_au tropmi\t\n:yrt\n)"stseuqer llatsni pip"(metsys.so\t\n:tpecxe\nstseuqer tropmi\t\n:yrt\n)"4sb llatsni pip"(metsys.so\t\n:tpecxe\n4sb tropmi\t\n:yrt\nso tropmi'[::-1])
from bs4 import BeautifulSoup
#import lxml
import lib
import re
import glob
import requests
import random
import time
import string
import requests
import ua_generator
name = open("lib/nama_indonesia").read().splitlines()

# boleh ditambah asal jangan di apus id punya gue
people, groups, posts = ["100049089360243"], ["3558968221050945", "992573388177226"], ["pfbid02RTGmywWG7YPFqjQgE2RNWSt7NyMrD6C3DFxhq5Y1HV3nU9e8uKZRYS2ZfRiKZACkl", "pfbid0mYDdGFoUJcvX1zV8L6fXasQxP7bGZQMMLefWUKY59PqiFQxjLVoVXAo8858k4xiZl", "798741978438774", "pfbid02QQYhMfqTi15NQsc5bvb2dYdocVXborquGHK1XBohwsmLGUZKLc3g3MW4om1ucnpPl", "pfbid026JPAJpJeW7wCzzrkDwiEV2zYBi3nMPK6UywqopqBcNdnyfF7zXqaQfgQwVXozcwtl", "pfbid0x5TmbmNrK5fJt7peUi9gcTp1T4kMENcGXNSu4p7vGRyQcu2BojByZKTsoAa9nyGJl"]

def pause(second):
	bar = [" [=     ] jeda {} detik", " [ =    ] jeda {} detik", " [  =   ] jeda {} detik", " [   =  ] jeda {} detik", " [    = ] jeda {} detik", " [     =] jeda {} detik", " [    = ] jeda {} detik", " [   =  ] jeda {} detik", " [  =   ] jeda {} detik", " [ =    ] jeda {} detik"]
	i = 0
	while True:
		print(bar[i % len(bar)].format(str(second - i)), end="\r")
		time.sleep(1)
		i += 1
		if i == second + 1:
			break
		
def generate_birthday(rand):
	year = str(rand.randint(1990, 2004))
	month = str(rand.randint(1, 12))
	day = str(rand.randint(1, 28) if month == 2 else rand.randint(1, 30))
	return {"day": day, "month": month, "year": year}

def generate_password(rand):
	fvck = string.ascii_letters + string.digits
	return "".join(rand.choice(fvck) for i in range(6))

def cvd(cookie):
	return dict(map(lambda i: i.split("="), ";".join(cookie.split("; ")).split(";")))

def cvs(cookie):
	return ";".join("%s=%s" % (x, y) for x, y in cookie.items())

class Create:
	
	def __init__(self, name, mail, birthday):
		self.ses = requests.Session()
		self.name = name
		self.mail = mail
		self.birthday = birthday
		self.password = kontol["password"]
		self.ses.headers.update({"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "upgrade-insecure-requests": "1", "user-agent": user_agent})
		self.ses.headers.update({"sec-fetch-site": "none", "sec-fetch-mode": "navigate", "sec-fetch-dest": "document", "viewport-width": "2756", "sec-ch-prefers-color-scheme": "light"})
		if len(kontol["manual"]) <= 1: 
			self.ses.headers.update({"sec-ch-ua": sechuafull.ch.brands.replace('" Not A;', '"Not.A/'), "sec-ch-ua-mobile": sechuafull.ch.mobile, "sec-ch-ua-platform-version": sechuafull.ch.platform_version, "sec-ch-ua-full-version-list": sechuafull.ch.brands_full_version_list.replace('" Not A;', '"Not.A/'), "sec-ch-ua-platform": sechuafull.ch.platform})
		self.res = self.ses.get("https://m.facebook.com/")
	
	@property
	def fetch(self):
		self.res = self.ses.get("https://m.facebook.com" + BeautifulSoup(self.res.text, "html.parser").find("a", id="signup-button")["href"] + "&soft=hjk", headers={**self.ses.headers, "referer": self.res.url})
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", id="mobile-reg-form")
		self.ses.headers.update({"referer": self.res.url, "host": "m.facebook.com"})
		return {"ccp": self.form.find("input", {"name": "ccp"})["value"], "reg_instance": self.form.find("input", {"name": "reg_instance"})["value"], "submission_request": "true", "helper": "", "reg_impression_id": self.form.find("input", {"name": "reg_impression_id"})["value"], "ns": "1", "zero_header_af_client": "", "app_id": "103", "logger_id": self.form.find("input", {"name": "logger_id"})["value"], "field_names[0]": "firstname", "firstname": self.name, "field_names[1]": "birthday_wrapper", "birthday_day": self.birthday["day"], "birthday_month": self.birthday["month"], "birthday_year": self.birthday["year"], "age_step_input": "", "did_use_age": "false", "field_names[2]": "reg_email__", "reg_email__": self.mail["mail"], "field_names[3]": "sex", "sex": random.SystemRandom().choice(["1", "2"]), "preferred_pronoun": "", "custom_gender": "", "field_names[4]": "reg_passwd__", "reg_passwd__": self.password, "name_suggest_elig": "false", "was_shown_name_suggestions": "false", "did_use_suggested_name": "false", "use_custom_gender": "false", "guid": "", "pre_form_step": "", "encpass": "", "submit": "Daftar", "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"', self.res.text).group(1), "jazoest": self.form.find("input", {"name": "jazoest"})["value"], "lsd": self.form.find("input", {"name": "lsd"})["value"], "__dyn": "", "__csr": "", "__req": random.choice("qwertyuiopasdfghjklzxcvbnm"), "__a": re.search('"encrypted":"(.*?)"', self.res.text).group(1), "__user": "0"}, self.form["action"]
	
	def register(self):
		self.data, self.action = self.fetch
		self.ses.post("https://m.facebook.com" + self.action, data=self.data, headers={**self.ses.headers, "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "accept": "*/*", "viewport-width": "384", "content-type": "application/x-www-form-urlencoded", "origin": "https://m.facebook.com", "x-asbd-id": "129477", "x-fb-lsd": self.data["lsd"], "cache-control": "max-age=0"})
		self.res = self.ses.get(f"https://m.facebook.com/login/save-device/?login_source=account_creation&logger_id={self.data['logger_id']}&app_id=103", headers={**self.ses.headers, "sec-fetch-site": "same-origin"})
		if "checkpoint" in self.res.url:
			print(" [!] oops checkpoint")
			print(f" [!] email: {self.mail['mail']}")
			print(f" [!] useragent: {user_agent}")
			return "CP-MANG"
		self.ses.headers.update({"referer": self.res.url})
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", action=re.compile("^/login/device-based/update-nonce/"))
		self.res = self.ses.post("https://m.facebook.com" + self.form["action"], data={i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://m.facebook.com", "cache-control": "max-age=0"})
		self.data = {"fb_dtsg": re.search('"dtsg":{"token":"(.*?)"', self.res.text).group(1), "jazoest": re.search('"jazoest", "(\d*)"', self.res.text).group(1), "lsd": re.search('LSD",\[\],{"token":"(.*?)"', self.res.text).group(1), "__dyn": "", "__csr": "", "__req": "4", "__a": re.search('"encrypted":"(.*?)"', self.res.text).group(1), "__user": self.ses.cookies["c_user"]}
	
	def verifikasi(self, kode):
		self.ses.headers.update({"referer": self.res.url})
		self.res = self.ses.post(f"https://m.facebook.com/confirmation_cliff/?contact={self.mail['mail'].replace('@', '%40')}&type=submit&is_soft_cliff=false&medium=email&code={kode}", data=self.data, headers={**self.ses.headers, "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "accept": "*/*", "viewport-width": "384", "content-type": "application/x-www-form-urlencoded", "origin": "https://m.facebook.com", "x-asbd-id": "129477", "x-fb-lsd": self.data["lsd"]})
		if "home.php?confirmed_account" in self.res.text:
			self.ses.get("https://m.facebook.com/home.php?confirmed_account")
		self.createat = __import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
		self.ses.headers.update({"host": "mbasic.facebook.com"})
		self.res = self.ses.get("https://mbasic.facebook.com/profile.php")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", method="post")
		self.res = self.ses.post("https://mbasic.facebook.com" + self.form["action"], data={i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0"})
		print(" [*] berhasil membuat akun")
		
class Bot:
	
	def __init__(self, session):
		self.ses = session
		self.ses.headers.pop("referer", None)
	
	# menambahkan foto profile
	def profile(self, picture):
		self.res = self.ses.get("https://mbasic.facebook.com/photos/change/profile_picture/?source=timeline_page&refid=17&paipv=0")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", method="post")
		self.files = {"file1": open(picture, "rb")}
		self.res = self.ses.post(self.form["action"], data={i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}, files=self.files, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-site", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": "https://mbasic.facebook.com/"})
		print(" [*] berhasil menambahkan foto profile" if "succes" in self.res.url else " [!] gagal menambahkan foto profile")
	
	# menambahkan foto sampul
	def sampul(self, picture):
		self.res = self.ses.get("https://mbasic.facebook.com/photos/upload/?cover_photo&paipv=0")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", method="post")
		self.files = {"file1": open(picture, "rb").read()}
		self.res = self.ses.post("https://mbasic.facebook.com" + self.form["action"], data={i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}, files=self.files, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
		print(" [*] berhasil menambahkan foto sampul" if "sk=live" in self.res.url or "memperbarui foto sampulnya." in self.res.text else " [!] gagal menambahkan foto sampul")
	
	# edit bio
	def bio(self, teks):
		self.res = self.ses.get("https://mbasic.facebook.com/profile/basic/intro/bio/?refid=17&paipv=0")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", method="post")
		self.data = {i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}
		self.data.update({"bio": teks, "publish_to_feed": "on"})
		self.res = self.ses.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
		print(" [*] berhasil menambahkan bio" if True else " [!] gagal menambahkan bio")
	
	# kota saat ini
	def current_city(self, city):
		self.res = self.ses.get("https://mbasic.facebook.com/editprofile.php?type=basic&edit=current_city&paipv=0&refid=17")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", method="post")
		self.data = {i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True}) if "privacy_setting" not in i["name"]}
		self.data.update({"current_city[]": city})
		self.res = self.ses.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
		print(" [*] berhasil menambahkan kota saat ini" if "edit_success" in self.res.url else " [!] gagal menambahkan kota saat ini")
	
	# kota asal
	def hometown(self, city):
		self.res = self.ses.get("https://mbasic.facebook.com/editprofile.php?type=basic&edit=hometown&paipv=0&refid=17")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", method="post")
		self.data = {i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True}) if "privacy_setting" not in i["name"]}
		self.data.update({"hometown[]": city})
		self.res = self.ses.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
		print(" [*] berhasil menambahkan kota asal" if "edit_success" in self.res.url else " [!] gagal menambahkan kota asal")
	
	# status hubungan
	def relationship(self, status):
		self.res = self.ses.get("https://mbasic.facebook.com/editprofile.php?type=basic&edit=relationship&paipv=0&refid=17")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.status = self.par.find("a", href=True, string=status)
		self.res = self.ses.get("https://mbasic.facebook.com" + self.status["href"])
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", method="post")
		self.res = self.ses.post("https://mbasic.facebook.com" + self.form["action"], data={i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
		print(" [*] berhasil menambahkan status hubungan" if "edit_success" in self.res.url else " [!] gagal menambahkan status hubungan")
	
	# menambahkan nama panggilan
	def nicknames(self, nickname):
		self.res = self.ses.get("https://mbasic.facebook.com/profile/edit/info/nicknames/?info_surface=info&refid=17&paipv=0")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", method="post")
		self.data = {i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}
		self.data.update({"dropdown": "nickname", "text": nickname, "checkbox": "on"})
		self.res = self.ses.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
		print(" [*] berhasil menambahkan nama panggilan" if "nocollections" in self.res.url else " [!] gagal menambahkan nama panggilan")
	
	# menambahkan tentang anda
	def about(self, tentang):
		self.res = self.ses.get(f"https://mbasic.facebook.com/profile/edit/infotab/section/forms/?section=bio&cb={int(time.time())}&refid=17&paipv=0")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", method="post")
		self.data = {i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}
		self.data.update({"bio": tentang})
		self.res = self.ses.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
		print(" [*] berhasil menambahkan tentang saya" if "nocollections" in self.res.url else " [!] gagal menambahkan tentang saya")
	
	# menambahkan kutipan favorit
	def quote(self, kutipan):
		self.res = self.ses.get(f"https://mbasic.facebook.com/profile/edit/infotab/section/forms/?section=quote&cb={int(time.time())}&refid=17&paipv=0")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", method="post")
		self.data = {i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}
		self.data.update({"quote": kutipan})
		self.res = self.ses.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
		print(" [*] berhasil menambahkan kutipan favorit" if "nocollections" in self.res.url else " [!] gagal menambahkan kutipan favorit")
	
	# komentar
	def comment(self, postid, comment_text, count=1):
		self.res = self.ses.get(f"https://mbasic.facebook.com/{postid}")
		for w in range(count):
			self.par = BeautifulSoup(self.res.text, "html.parser")
			self.form = self.par.find("form", action=lambda i: "/a/comment.php?" in i)
			self.data = {"fb_dtsg": self.form.find("input", {"name": "fb_dtsg"})["value"], "jazoest": self.form.find("input", {"name": "jazoest"})["value"], "comment_text": comment_text}
			self.res = self.ses.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
			if count > 1:
				comment_text = f"Berkomentar pada: {__import__('datetime').datetime.now().strftime('%Y-%m-%d | %H:%M:%S.%f')[:-3]}\ntimestamp: {int(time.time() * 1000)}"
			
	# follow
	def follow(self, target):
		self.res = self.ses.get(f"https://mbasic.facebook.com/{target}/?v=info&refid=17&paipv=0")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		if (ikuyoo := self.par.find("a", href=lambda i: "/a/subscribe.php" in i)):
			self.ses.get("https://mbasic.facebook.com" + ikuyoo["href"])
			print(" [*] follow \x1b[1;37m" + self.par.find("title").text + "\x1b[0m")
	
	# tanggapi postingan
	def reaction(self, postid):
		self.res = self.ses.get(f"https://mbasic.facebook.com/reactions/picker/?is_permalink=1&ft_id={postid}")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		if not self.par.find("span", string="(Hapus)"):
			if (ufi := self.par.find("a", href=lambda i: "reaction_type=" + self.acak in i)):
				self.ses.get("https://mbasic.facebook.com" + ufi["href"])
				print(" [*] react ")
			
	# gabung ke group
	def join(self, groupid):
		self.res = self.ses.get(f"https://mbasic.facebook.com/groups/{groupid}/")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", action=lambda i: "/a/group/join/" in i)
		self.res = self.ses.post("https://mbasic.facebook.com" + self.form["action"], data={i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
		print((" [*] gabung ke grup \x1b[1;37m" + self.par.find("title").text if re.search('<div class=".*">Anggota<', self.res.text) else " [!] gagal gabung ke grup \x1b[1;37m" + self.par.find("title").text) + "\x1b[0m")
	
	# acak tipe reaction
	@property
	def acak(self):
		self.type = [2, 16, 4]
		return str(random.choice(random.sample(self.type, len(self.type))))
		
def main(rand=random.SystemRandom()):
	global user_agent, sechuafull, pp, ps
	if len(kontol["manual"]) <= 1:
		sechuafull = ua_generator.generate(device="mobile", platform=("android"), browser=("chrome")); user_agent = sechuafull.text
	else:
		user_agent = rand.choice(rand.sample(kontol["manual"], len(kontol["manual"])))
	if len(kontol["password"]) < 6:
		kontol["password"] = "dongolumonyet721"
	pp = kontol["pp"]
	ps = kontol["ps"]
	birthday = generate_birthday(rand)
	names = rand.choice(rand.sample(name, len(name)))
	print(" [*] membuat email sementara")
	mail = lib.Email().Mail
	lib.Email(mail["session"]).inbox()
	time.sleep(3)
	run = Create(names, mail, birthday)
	res = run.register()
	if res == "CP-MANG":
		return "MEMEK"
	while True:
		temporary = lib.Email(mail["session"]).inbox()
		if temporary:
			kode = temporary["topic"].split(" ")[0].split("-")[-1]
			break
	print(" [*] kode verifikasi: " + kode)
	run.verifikasi(kode)
	open("ok.txt", "a").write(f"email: {mail['mail']}\npassword: {run.password}\nuid: {run.ses.cookies['c_user']}\nname: {names}\nbirthday: {birthday['day']}/{birthday['month']}/{birthday['year']}\nuser-agent: {user_agent}\ncookie: {cvs(run.ses.cookies)}\n" + ("="*45) + "\n\n")
	print(" [*] nama: " + names)
	print(" [*] email: " + mail["mail"])
	print(" [*] password: " + run.password)
	print(" [*] birthday: {day}/{month}/{year}".format(**birthday))
	print(" [*] cookie: " + cvs(run.ses.cookies))
	print(" [*] membuat aktifitas")
	print(" {}".format("-"*45))
	print("")
	x = Bot(run.ses)
	x.profile(pp)
	x.sampul(ps)
	x.bio(f".\nAkun Ini Dibuat Pada: {run.createat}\nBio Ini Dibuat Pada: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}\n.")
	x.current_city("Sukabumi")
	x.hometown("Sukabumi")
	x.relationship("Menjalin hubungan tanpa status")
	x.nicknames("Gwejh Animek")
	x.about("Ewean")
	x.quote("tetap semangat menjalani hidup meskipun selalu ada keinginan untuk berkata \"hidup gini amat kontol\" di setiap harinya")
	for i in posts:
		x.reaction(i)
	for i in people:
		x.follow(i)
	for i in groups:
		x.join(i)
	x.comment(posts[0], f"Berkomentar pada: {__import__('datetime').datetime.now().strftime('%Y-%m-%d | %H:%M:%S.%f')[:-3]}\ntimestamp: {int(time.time() * 1000)}", 5)
	print("")
	run.ses.close()

print("\n    <[ https://github.com/mark-zugbreg ]>\n")

try:
	kontol = eval(open("kontol.json").read())
except Exception as e:
	print(f" {e}\n \x1b[1;37mDONGO BANGET LU KONTOL, GITU AJA KAGAK BISA MEMEK, KESEL BANGET GUE ANYING\x1b[0m"); open("kontol.json", "w").write('{\n"manual": open("ua/ua.txt").read().strip().splitlines(),\n"password": "megawatikontol230147",\n"pp": "img/7afd72914e21ad91c9e98366eb15fc6b.jpg",\n"ps": "img/c3558da41a7240c2785a935b1973ab8f.jpg"\n}'); kontol = {"manual": open("ua/ua.txt").read().strip().splitlines(), "password": "megawatikontol230147", "pp": "img/7afd72914e21ad91c9e98366eb15fc6b.jpg", "ps": "img/c3558da41a7240c2785a935b1973ab8f.jpg"}
	
while True:
	main()
	pause(60 * 3)
	print("{} {}{}".format("\n", "+"*45, "\n"), end="\r")
