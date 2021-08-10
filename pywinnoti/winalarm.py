import webbrowser
from win10toast_click import ToastNotifier

import requests
from bs4 import BeautifulSoup

import schedule
import time

import json

import sys

class WinAlarm():

    
    def __init__(self):
        self.check_cookie_page = 'https://www.pixiv.net/'
        self.check_user_page = 'https://sketch.pixiv.net/@user_name'  #https://sketch.pixiv.net/@'user_name'
        self.live_page = 'https://sketch.pixiv.net' #https://sketch.pixiv.net/@'user_name'/lives/'ch_id'


        self.pixiv_cookie = {'PHPSESSID' : '7937790_pPfJxt7dIt26vd7Z3zFEp0c3urZcx8Um'} #이게 진짜 값
        # pixiv_cookie = {'PHPSESSID' : '7937790_pPfJxt7dIt26vd7Z3zFEp0c3urZcx8a'} #테스트용 가짜 값
        #실제로는 cookie.json에서 읽어와야함
        self.userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.277 Whale/2.9.118.38 Safari/537.36"
        self.user_header = {
                            'user-agent' : self.userAgent, 
                            'authority' : 'www.pixiv.net', 
                            'scheme' : 'https', 
                            'accept' : 'application/vnd.sketch-v4+json',
                            'accept-encoding' : 'gzip, deflate, br',
                            'accept-language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
                            }


    def check_cookie(self):
        try:
            req = requests.get(self.check_cookie_page, cookies=self.pixiv_cookie, headers=self.user_header)
            if req.status_code == 200:
                html = req.text
                if "login: 'yes'" in html:
                    print("픽시브 로그인 성공\n")
                else:
                    print("픽시브 로그인 실패. 쿠키값을 갱신하고 다시 실행해주세요.") #콘솔에서 보일거
                    sys.exit('program end...')
                    #알람 메세지로도 보이게끔
        except:
            print("픽시브 로그인 실패. 쿠키값을 갱신하고 다시 실행해주세요.") #콘솔에서 보일거
            sys.exit('program end...')
            #알람 메세지로도 보이게끔


    def clear_artist_status(self):

        self.artists = []
        self.artists_status = dict()
        cnt = 1
        
        f = open('user.txt', 'r', encoding='utf8')
        while True:
            line = f.readline().strip()
            if not line: #더이상 읽을 줄이 없거나 줄이 있어도 공백이면
                break
            self.artists.append(line)
            self.artists_status[line] = 'False'
        f.close()
        print(f'현재 등록된 작가는 {len(self.artists)}명이며 다음과 같습니다.')
        for artist in self.artists:
            print(f'{cnt}. {artist}')
            cnt += 1
        print('\n')
        # print()
        # for arts in self.artist_status.keys():
        #     print(f'key={arts} value={self.artist_status[arts]}')
        

    def crawl(self):

        if len(self.artists) == 0:
            print(f'등록한 작가가 없습니다. user.txt 파일에 한 줄에 한명씩 작가를 입력해주세요.')
        else:
            for self.artist in self.artists: #self.check_user_page = 'https://sketch.pixiv.net/@user_name'
                split_url = self.check_user_page.split('@')[0]
                self.check_user_page = split_url + '@' + self.artist

                try:
                    req = requests.get(self.check_user_page, cookies=self.pixiv_cookie, headers=self.user_header)
                    if req.status_code == 200:
                        html = req.text
                        
                        if 'Live broadcasting' in html and self.artists_status[self.artist] == 'False':
                            print(f'{self.artist}님이 방송중입니다.')
                            self.artists_status[self.artist] == 'True'
                            soup = BeautifulSoup(html, 'html.parser')
                            self.ch_id = soup.select('div > div.UserHeaderBody > div > div.live-button > a')
                            # print(ch_id)
                            self.ch_id = self.ch_id[0].get('href')

                            print(f'URL = {self.live_page}{self.ch_id}')
                            self.notice()
                        else:
                            print(f'{self.artist}님은 휴식중입니다.') #콘솔에서 보일거
                            self.artists_status[self.artist] == 'False'
                            #알람 메세지로도 보이게끔
                except:
                    print("픽시브 로그인 실패. 쿠키값을 갱신하고 다시 실행해주세요.") #콘솔에서 보일거
                    sys.exit('program end...')
                    #알람 메세지로도 보이게끔
                time.sleep(1)
        
        


    def open_url(self):
        live_url = self.live_page+self.ch_id
        try:
            webbrowser.open(live_url)
            print('open url...')
        except:
            print('Failed open URL')


    def notice(self):
        toaster = ToastNotifier()

        toaster.show_toast("라이브 시작 알림", 
                            self.artist+"님의 방송이 시작됐습니다",
                            icon_path=None,
                            duration=3,
                            threaded=False,
                            callback_on_click=self.open_url)


    # def schedul():
    #     schedule.every(1).minutes.do(printtime)
    #     while True:
    #         schedule.run_pending()
    #         time.sleep(1)


    # def printtime(self):
    #     print('im print')

    def main(self):
        self.clear_artist_status()
        self.check_cookie()
        self.crawl()





if __name__ == "__main__":
    do_class = WinAlarm()
    do_class.main()
    

# req = requests.get(visit_url, cookies=self.pixiv_cookie, headers=self.user_header)

        # html = req.text
        # header = req.headers
        # status = req.status_code

        # isok = req.ok

        # soup = BeautifulSoup(html, 'html.parser')


        # print()
        # print()
        # print(status, isok)

        
        # live_check = soup.select(
        # 'div > div.live-button > a > button > span > span'
        # )

        # if live_check != []:
        #     print('now live!')
        # else:
        #     print('no live')          