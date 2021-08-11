import os
import requests
from bs4 import BeautifulSoup

class prac:
    def __init__(self):
        self.first = 1
        self.send = 2
        self.crawl_count = 1

        self.title = "방송 시작 알림"
        self.contents = "님의 방송을 하는 중입니다."

        self.check_cookie_page = 'https://www.pixiv.net/'
        self.check_user_page = 'https://sketch.pixiv.net/@user_name'  #https://sketch.pixiv.net/@'user_name'
        self.live_page = 'https://sketch.pixiv.net' #https://sketch.pixiv.net/@'user_name'/lives/'ch_id'
        self.path_icon = 'icon.ico'
        self.crawl_count = 1

        # self.pixiv_cookie = {'PHPSESSID' : '7937790_pPfJxt7dIt26vd7Z3zFEp0c3urZcx8Um'} #Cookie.json에서 값을 읽어온다
        self.pixiv_cookie = {'PHPSESSID' : ''}
        self.userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.277 Whale/2.9.118.38 Safari/537.36"
        self.user_header = {
                            'user-agent' : self.userAgent, 
                            'authority' : 'www.pixiv.net', 
                            'scheme' : 'https', 
                            'accept' : 'application/vnd.sketch-v4+json',
                            'accept-encoding' : 'gzip, deflate, br',
                            'accept-language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
                            }

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

        except:
            print('user.txt를 읽지 못했습니다.\nuser.txt 파일이 실행 프로그램과 같은 폴더에 있는지 확인하세요.')
            self.end_program()

        print(f'현재 등록된 작가는 {len(self.artists)}명이며 다음과 같습니다.')

        for artist in self.artists:
            print(f'{cnt}. {artist}')
            cnt += 1

        print('\n')

    def plus(self):
        self.first += 1
        self.send += 12

    def amnu_key(self):
        # print('계속하려면 아무키나 누르세요')
        os.system("pause")

    def filewr(self):

        for self.artist in self.artists:
            split_url = self.check_user_page.split('@')[0]
            self.check_user_page = split_url + '@' + self.artist

            req = requests.get(self.check_user_page, cookies=self.pixiv_cookie, headers=self.user_header)

            if req.status_code == 200:
                html = req.text
                
                if 'Live broadcasting' in html and self.artists_status[self.artist] == 'False':
                    print(f'\n{self.artist}님이 방송중입니다.') #콘솔에서 보일거
                    self.artists_status[self.artist] = 'True'
                    soup = BeautifulSoup(html, 'html.parser')
                    self.ch_id = soup.select('div > div.UserHeaderBody > div > div.live-button > a')
                    self.ch_id = self.ch_id[0].get('href')
                    self.nick = soup.select('div.UserHeaderBody > div > div.user > div.name')
                    self.nick = self.nick[0].text
                    print(self.nick)
                    print(f'URL = {self.live_page}{self.ch_id}\n')
                    # with open(str(self.crawl_count) + 'sketch_html_' + str(self.artist) + '.txt',
                    #             'w', encoding='utf8') as file:
                    #     file.write(html)

                    # with open(str(self.crawl_count) + 'sketch_soup_' + str(self.artist) + '.txt',
                    #             'w', encoding='utf8') as file:
                    #     file.write(soup.text)

                elif 'Live broadcasting' in html and self.artists_status[self.artist] == 'True':
                    print(f'{self.artist}님이 방송중입니다.') #콘솔에서 보일거

                else:
                    print(f'{self.artist}님은 휴식중입니다.') #콘솔에서 보일거
                    self.artists_status[self.artist] = 'False'
                    #알람 메세지로도 보이게끔

    # def read_cookie(self):
    #     try:
    #         with open('Cookie.txt', 'r', encoding='utf8') as file:
    #             lines = file.readlines()
    #             for line in lines:
    #                 # print(line)
    #                 if 'PHPSESSID' in line.upper().strip():
    #                     temp = line.split('\t')
    #                     print(f'{temp[-1]}')
    #                     self.pixiv_cookie['PHPSESSID'] = temp[-1]
    #         if self.pixiv_cookie['PHPSESSID'] == '':
    #             print('end game')
    #     except Exception as e:
    #         print(f'\n{e}\n')

    def printprac(self):
        print(f'개행문자\
            \n연습중입니다\
            \n이거은근\
            \n어렵네요')


    def main(self):
        # print('alpa')
        # print(f'{self.first}\n{self.send}')
        # self.plus()
        # print(f'{self.first}\n{self.send}')
        # self.amnu_key()
        # self.clear_artist_status()
        # self.filewr()
        # self.read_cookie()
        self.printprac()


if __name__ == "__main__":
    temp = prac()
    temp.main()