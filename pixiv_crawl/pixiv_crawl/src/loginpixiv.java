import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

import org.jsoup.Jsoup;
import org.jsoup.Connection;
import org.jsoup.Connection.Method;
import org.jsoup.Connection.Response;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import org.jsoup.select.Evaluator.AttributeKeyPair;;

public class loginpixiv {
    public static void main(String[] args) throws Exception {
    /*
String login_url = "https://accounts.pixiv.net/login";
        String ID = "aeoragy";
        String PW = "dgdh49@pixiv";

        Connection.Response initial=Jsoup.connect(login_url)
                                        .method(Connection.Method.GET)
                                        .execute();

        Document key=initial.parse();

        // // 로그인 페이지에서 로그인에 함께 전송하는 토큰 얻어내기
        String post_key = key.select("input[name=post_key]").val();

        // 쿠키 얻어내기
        String phpsessid=initial.cookies().get("PHPSESSID");
        String p_ab_id=initial.cookies().get("p_ab_id");
        String p_ab_id_2=initial.cookies().get("p_ab_id_2");
        String p_ab_d_id=initial.cookies().get("p_ab_d_id");
        String  __cf_bm=initial.cookies().get("__cf_bm");



        // System.out.printf(phpsessid + "," + p_ab_id + "," + p_ab_id_2 + "," + p_ab_d_id + "," + __cf_bm);

        // 로그인 페이지에서 얻은 쿠키
        // Map<String, String> loginTryCookie = initial.cookies();

        // System.out.println(loginTryCookie);
        // System.out.println(phpsessid);

        // // System.out.println(post_key);

        // // // 전송할 폼 데이터
        Map<String, String> data = new HashMap<>();
        data.put("pixiv_id", ID);
        data.put("password", PW);
        data.put("return_to", "https://www.pixiv.net");
        data.put("lang", "en");
        data.put("post_key", post_key);
        data.put("source", "accounts");
        data.put("ref", "");
        // data.put("PHPSESSID", "7937790_i6nyEoZoVLXqBgwno2ccqUifs8O8CU36");

        Map<String, String> ck = new HashMap<>();
        ck.put("PHPSESSID", phpsessid);
        ck.put("p_ab_id", p_ab_id);
        ck.put("p_ab_id_2", p_ab_id_2);
        ck.put("p_ab_d_id", p_ab_d_id);
        ck.put("__cf_bm", __cf_bm);

        Connection.Response login=Jsoup.connect(login_url)
                            // .cookies(initial.cookies())
                            .data(data) 
                            .data(ck)

                            // add other values 

                            .method(Connection.Method.POST)

                            .timeout(5000)

                            .execute();

        // System.out.println(loginCookie);

        Document mypage=Jsoup.connect("https://sketch.pixiv.net/@suika2119")
                                        .cookies(login.cookies())
                                        .timeout(3000000).get();


        // System.out.println(mypage);

        Elements element = mypage.select("div.body");
        System.out.println(element);
*/
    }
}
