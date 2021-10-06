package com.jsh.demo.cookierw;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;

import java.io.IOException;

import org.json.simple.*;

public class App 
{
	public static void main(String[] args) throws Exception {
        String cookie = null;
        String txtkie;
        String phpsessid = "PHPSESSID";
        String txtkieupper;
        String[] cookieline;

        System.out.println("1. 크롬 확장 프로그램 Get Cookies.txt를 설치합니다.\n");
        System.out.println("Get Cookies.txt DownLoad Link : https://chrome.google.com/webstore/detail/get-cookiestxt/bgaddhkoddajcdgocldbbfleckgcbcid\n");
        System.out.println("2. 픽시브에 접속하고 로그인 후 메인페이지로 갑니다.\n");
        System.out.println("3. Get Cookies.txt를 이용해 쿠키값을 얻습니다.\n");
        System.out.println("4. 압축해제한 폴더에 있는 Cookie.txt 파일에 전부 붙여넣고 저장합니다.\n");
        System.out.println("5. 4번 과정을 마치고 나서 Enter를 누르세요.\n");

        pause();

        try (BufferedReader reader = new BufferedReader(
                                             new FileReader("./Cookie.txt"))) {
            
            while ((txtkie = reader.readLine()) != null) {
                txtkieupper = txtkie.toUpperCase();
                if (txtkieupper.contains(phpsessid)) {
                    cookieline = txtkie.split(phpsessid);
                    // System.out.println(Arrays.toString(cookieline));
                    cookie = cookieline[1].trim();
                    // System.out.println(cookie);
                    break;
                }
            }
            reader.close();

        } catch (IOException e) {
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }

        if (cookie == null || cookie.isEmpty()) { //메모장을 불러오는데 실패했거나 phpsessid를 얻지 못한 경우
            System.out.println("프로그램의 지시사항대로 했는지 혹은 메모장을 저장 한 후 이 프로그램에서 Enter를 눌렀는지 다시 확인해주세요");
            System.out.println("동일현상 반복 발생시 개발자에게 문의하세요");
        }
        else {
            JSONObject obj = new JSONObject();

            obj.put(phpsessid, cookie);
            
            try (FileWriter file = new FileWriter("./Cookie.json")) {
            	
            	file.write(obj.toJSONString());
                file.flush();
                file.close();
                System.out.println("쿠키 값을 성공적으로 설정 파일에 저장했습니다.\n");
                
            } catch (IOException e) {
                e.printStackTrace();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        endProgram();

    }


    public static void pause() {
        try {
            System.in.read();
        } catch (IOException e) { }
    }


    public static void endProgram() throws InterruptedException {
        System.out.println("3초 후 종료합니다");
        Thread.sleep(800);
        System.out.println("2초 후 종료합니다");
        Thread.sleep(900);
        System.out.println("1초 후 종료합니다");
        Thread.sleep(1000);

        System.exit(0);
    }
}
