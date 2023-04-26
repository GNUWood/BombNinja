import cloudscraper
import requests
import re
import fake_useragent
import random
import sys
import threading
import os
if os.name == 'nt':
    import ctypes
 
    # https://docs.microsoft.com/en-us/windows/console/setconsolemode?redirectedfrom=MSDN
    ENABLE_PROCESSED_OUTPUT = 0x0001
    ENABLE_WRAP_AT_EOL_OUTPUT = 0x0002
    ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
    MODE = ENABLE_PROCESSED_OUTPUT + ENABLE_WRAP_AT_EOL_OUTPUT + ENABLE_VIRTUAL_TERMINAL_PROCESSING
 
    kernel32 = ctypes.windll.kernel32
    handle = kernel32.GetStdHandle(-11)
    kernel32.SetConsoleMode(handle, MODE)


def request_data_gen(ua,content):
    header = {
        "User-Agent": ua,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "ja,en-US;q=0.7,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://www.ninjar.jp",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Sec-GPC": "1",
    }
    body = {
        "theme_form[title]":content,
        "theme_form[redirect_url]":"",
        "commit":"%E5%8C%BF%E5%90%8D%E3%81%A7%E8%B3%AA%E5%95%8F%E3%82%92%E9%80%81%E3%82%8B"
    }
    return header, body

def ninjar_spammer(url,txt,randomstr):
    session=cloudscraper.CloudScraper()
    result=session.get(url).text
    uname=re.findall("users/(.*)/themes",url)
    ua = fake_useragent.FakeUserAgent.safari
    content=random.choice(txt)
    if randomstr in ["yes","y"]:
        content += "\n" + "".join(random.choices("ABCDWFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",k=8))
    header, data=request_data_gen(ua=ua, content=content)
    r = session.post(url,headers=header,data=data)
    if r.status_code in (200, 201, 305):
        print(f"送信に成功しました。\nステータスコード:{r.status_code}\nメッセージ:{content}\nUser-Agent:{ua}\nユーザー名:{uname}\n\n\n")
    else:
        print(f"送信に失敗した可能性があります。\nステータスコード:{r.status_code}\nメッセージ:{content}\nUser-Agent:{ua}\nユーザー名:{uname}\n\n\n")


print("""
                   \033[31m*█.*\033[0m
                  ▄▄█
                 ██
\033[36m▀█████████▄   ▄██████▄    ▄▄▄▄███▄▄▄▄   ▀█████████▄  ███▄▄▄▄    ▄█  ███▄▄▄▄        ▄█    ▄████████
  ███    ███ ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███▀▀▀██▄ ███  ███▀▀▀██▄     ███   ███    ███
  ███    ███ ███    ███ ███   ███   ███   ███    ███ ███   ███ ███▌ ███   ███     ███   ███    ███
 ▄███▄▄▄██▀  ███    ███ ███   ███   ███  ▄███▄▄▄██▀  ███   ███ ███▌ ███   ███     ███   ███    ███
\033[34m▀▀███▀▀▀██▄  ███    ███ ███   ███   ███ ▀▀███▀▀▀██▄  ███   ███ ███▌ ███   ███     ███ ▀███████████
  ███    ██▄ ███    ███ ███   ███   ███   ███    ██▄ ███   ███ ███  ███   ███     ███   ███    ███
  ███    ███ ███    ███ ███   ███   ███   ███    ███ ███   ███ ███  ███   ███     ███   ███    ███
▄█████████▀   ▀██████▀   ▀█   ███   █▀  ▄█████████▀   ▀█   █▀  █▀    ▀█   █▀  █▄ ▄███   ███    █▀
                                                                              ▀▀▀▀▀
                                    Simple Ninjar spammer
\033[0m                                         \033[35m1 . 0 . 0\033[0m

""")
username=input("Ninjarユーザー名: ")
randomstr=input("文末にランダムな文字列を追加しますか？(y/n): ")
amount=int(input("送信数: "))
url="https://www.ninjar.jp/users/" + username + "/themes"
try:
    with open("ninjar.txt", encoding="utf-8") as f:
        txt = [i for i in f.read().splitlines() if i != None]
    for i in range(amount):
        threading.Thread(target=ninjar_spammer,args=(url,txt,randomstr)).start()
except:
    print("テキストファイル（ninjar.txt）が見つかりませんでした。")
    sys.exit()
