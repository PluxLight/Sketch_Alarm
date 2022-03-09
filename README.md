# Sketch_Alarm
Sketch 사이트를 크롤링하여 별도의 알람을 보내는 프로그램

## 프로젝트

### 1. Java_With_Discord

#### SketchAlarmBot : Main

- 메인 코드
- Discord에서 Bot을 통해 Sketch에서 방송중인 작가가 있으면 알람을 받을 수 있다.
- 봇에게 내릴 수 있는 명령
  - 알람 받을 작가 추가
  - 알람 받을 작가 삭제
  - 추가한 작가 목록 확인



#### pixiv_crawl, Make_Cookie_Json : Sub

- 테스트용 코드
  - 방송중인 작가 확인
  - 쿠키값 읽어서 json 파일로 변경



### 2. Python_With_EXE

- Sketch에서 방송중인 작가를 확인해 알람을 보내주는 프로그램
