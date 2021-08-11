import webbrowser
from win10toast_click import ToastNotifier

import requests
from bs4 import BeautifulSoup

import schedule
import time

import json

import sys
import os


#pyinstaller -F -i icon.ico --additional-hooks-dir hooks


class WinAlarm():

    
    def __init__(self):

        self.title = "방송 시작 알림"
        self.contents = "님이 방송 중입니다.\n알림을 클릭하면 방송 페이지로 이동합니다."

        self.check_cookie_page = 'https://www.pixiv.net/'
        self.check_user_page = 'https://sketch.pixiv.net/@user_name'  #https://sketch.pixiv.net/@'user_name'
        self.live_page = 'https://sketch.pixiv.net' #https://sketch.pixiv.net/@'user_name'/lives/'ch_id'
        self.path_icon = 'icon.ico'
        self.crawl_count = 1

        self.pixiv_cookie = {'PHPSESSID' : ''} #Cookie.txt에서 값을 읽어온다
        self.userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.277 Whale/2.9.118.38 Safari/537.36"
        self.user_header = {
                            'user-agent' : self.userAgent, 
                            'authority' : 'www.pixiv.net', 
                            'scheme' : 'https', 
                            'accept' : 'application/vnd.sketch-v4+json',
                            'accept-encoding' : 'gzip, deflate, br',
                            'accept-language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
                            }


    def read_coookie(self):

        try:
            with open('Cookie.txt', 'r', encoding='utf8') as file:
                lines = file.readlines()

                for line in lines:
                    line = line.strip()

                    if 'PHPSESSID' in line.upper():
                        temp = line.split('\t')
                        self.pixiv_cookie['PHPSESSID'] = temp[-1]

            if self.pixiv_cookie['PHPSESSID'] == '':
                print(f'Cookie값을 읽는데 실패했습니다.\
                        \n다음 지시사항을 따라하십시오.\n')

                print(f'1. 크롬 확장 프로그램 Get Cookies.txt를 설치합니다.\n\
                        \nGet Cookies.txt DownLoad Link : https://chrome.google.com/webstore/detail/get-cookiestxt/bgaddhkoddajcdgocldbbfleckgcbcid\n\
                        \n2. 픽시브에 접속하고 로그인 후 메인페이지로 갑니다.\
                        \n3. 다운받은 Get Cookies.txt 확장프로그램을 클릭하고 Export를 클릭하여 텍스트 파일을 다운받습니다.\
                        \n4. 다운받은 텍스트 파일의 내용을 전부 실행중인 프로그램과 같은 폴더에 있는 Cookie.txt 파일에 전부 붙여넣고 저장합니다.\
                        \n5. 4번 과정을 마치고 나서 프로그램을 다시 실행하십시오.')

                self.end_program()

        except Exception as e:
            print(f'{e}\n')
            print('Cookie.txt 파일을 읽는데 실패했습니다. Cookie.txt 파일이 실행중인 프로그램과 같은 폴더에 있는지 확인하십시오.')
            self.end_program()


    def clear_artist_status(self):

        self.artists = []
        self.artists_status = dict()
        cnt = 1

        try:
            with open('user.txt', 'r', encoding='utf8') as file:

                 while True:
                    line = file.readline().strip()

                    if not line: #더이상 읽을 줄이 없거나 줄이 있어도 공백이면
                        break

                    self.artists.append(line)
                    self.artists_status[line] = 'False'

        except Exception as e:
            print(f'{e}\n')
            print('user.txt를 읽지 못했습니다.\nuser.txt 파일이 실행 프로그램과 같은 폴더에 있는지 확인하세요.')
            self.end_program()

        print(f'현재 등록된 작가는 {len(self.artists)}명이며 다음과 같습니다.')

        for artist in self.artists:
            print(f'{cnt}. {artist}')
            cnt += 1

        print('\n')


    def check_cookie(self):

        try:
            req = requests.get(self.check_cookie_page, cookies=self.pixiv_cookie, headers=self.user_header)

            if req.status_code == 200:
                html = req.text

                if "login: 'yes'" in html:
                    print("픽시브 로그인 성공\n")

                else:
                    print("픽시브 로그인 실패. 쿠키값을 갱신하고 다시 실행해주세요.")
                    self.end_program()

        except Exception as e:
            print(f'{e}\n')
            print("픽시브 접속 실패. 쿠키값을 갱신하거나 인터넷 상황을 확인하세요.")
            self.end_program()


    def crawl(self):

        if len(self.artists) == 0:
            print(f'등록한 작가가 없습니다. user.txt 파일에 한 줄에 한명씩 작가를 입력해주세요.')
            self.end_program()

        else:
            print(f'\n{self.crawl_count}번째 크롤링을 시작합니다.\n')

            for self.artist in self.artists:
                split_url = self.check_user_page.split('@')[0]
                self.check_user_page = split_url + '@' + self.artist

                try:
                    req = requests.get(self.check_user_page, cookies=self.pixiv_cookie, headers=self.user_header)

                    if req.status_code == 200:
                        html = req.text
                        
                        if 'Live broadcasting' in html and self.artists_status[self.artist] == 'False':
                            soup = BeautifulSoup(html, 'html.parser')
                            self.nick = soup.select('div.UserHeaderBody > div > div.user > div.name')
                            self.nick = self.nick[0].text
                            self.artists_status[self.artist] = 'True'
                            self.ch_id = soup.select('div > div.UserHeaderBody > div > div.live-button > a')
                            self.ch_id = self.ch_id[0].get('href')

                            print(f'\n{self.nick}({self.artist})님이 방송중입니다.')
                            print(f'URL = {self.live_page}{self.ch_id}\n')

                            self.notice(True)

                        elif 'Live broadcasting' in html and self.artists_status[self.artist] == 'True':
                            print(f'\n{self.artist}님이 방송중입니다.')
                            print(f'URL = {self.live_page}{self.ch_id}\n')

                        else:
                            print(f'{self.artist}님은 휴식중입니다.')
                            self.artists_status[self.artist] = 'False'

                    else: #404 등의 유저 오입력 경우
                        print("유저 정보 확인에 실패했습니다. user.txt에 입력한 유저값이 정상인지 확인하세요.")
                        self.end_program()

                except Exception as e:
                    print(f'{e}\n')
                    print("유저 정보 확인에 실패했습니다. user.txt에 입력한 유저값이 정상인지 확인하세요.")
                    self.end_program()
            
            print(f'\n{self.crawl_count}번째 작업이 끝났습니다.\n1분 후 작업을 다시 시작합니다.')
            self.crawl_count += 1


    def notice(self, bool):
        toaster = ToastNotifier()

        try:

            if bool == True:
                msg = f'{self.nick}({self.artist}) {self.contents}'
                toaster.show_toast(self.title, 
                                    msg,
                                    icon_path=self.path_icon,
                                    duration=3,
                                    threaded=False,
                                    callback_on_click=self.click_open_url)

            else:
                toaster.show_toast(self.title, 
                                    self.contents,
                                    icon_path=self.path_icon,
                                    duration=5,
                                    threaded=False)

        except  Exception as e:
            print(f'{e}\n')
            print('알림 메시지 전송에 실패했습니다.')
            self.end_program()


    def click_open_url(self):

        live_url = self.live_page+self.ch_id

        try:
            webbrowser.open(live_url)
            
        except Exception as e:
            print(f'{e}\n')
            print('URL을 여는데 실패했습니다.')
            self.end_program()


    def schedul(self):
        schedule.every(1).minutes.do(self.crawl)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def end_program(self):
        print('동일현상 중복 발생 시 개발자에게 문의 바랍니다.')
        self.title = "프로그램 종료"
        self.contents = "오류로 인해 프로그램을 종료합니다.\n프로그램 화면을 확인하세요"
        self.notice(False)
        os.system("pause")
        sys.exit(0)


    def main(self):
        self.read_coookie()
        self.clear_artist_status()
        self.check_cookie()
        self.crawl()
        self.schedul() #여기서 무한반복


if __name__ == "__main__":
    do_class = WinAlarm()
    do_class.main()