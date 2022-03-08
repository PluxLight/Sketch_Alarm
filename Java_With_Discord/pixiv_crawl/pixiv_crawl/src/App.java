import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

import org.jsoup.Jsoup;

import org.jsoup.Connection;
import org.jsoup.Connection.Base;
import org.jsoup.Connection.Method;
import org.jsoup.Connection.Response;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import org.jsoup.select.Evaluator.AttributeKeyPair;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import java.net.CookieManager;

public class App {
    public static void nomain(String[] args) throws Exception {

        String url = "https://sketch.pixiv.net/api/lives.json";
        String liveurl = "https://sketch.pixiv.net/lives";
        String api_lives = "https://sketch.pixiv.net/lives?sort_by=created_at";
        String userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.277 Whale/2.9.118.38 Safari/537.36";

        //일단 접속해서 쿠키부터 얻어보자
        // Connection.Response livepage=Jsoup.connect(liveurl)
        //                                 .header("referer", "https://sketch.pixiv.net/")
        //                                 .userAgent(userAgent)
        //                                 .method(Connection.Method.GET)
        //                                 .execute();

        // Map<String, String> PHPSESSID=livepage.cookies();
        // Document firstweb=livepage.parse();

        // System.out.println(PHPSESSID);
        
        // txtout(firstweb, "./firstweb.txt");



        Document doc = Jsoup.connect(url)
                            
                            .header("authority", "sketch.pixiv.net")
                            // .header("path", "/api/lives.json?count=500&order_by=audience_count")
                            .header("scheme", "https")
                            .header("accept", "application/vnd.sketch-v4+json")
                            .header("accept-encoding", "gzip, deflate, br")
                            .header("accept-language", "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7")

                            //쿠키 PHPSESSID 값이 있어야 모든 방송 유저의 정보를 얻을 수 있음
                            .cookie("PHPSESSID", "7937790_Vmr8mfVXA5FeaKvIMCgkkhPuj80JcbA1")
                            // .cookie("__cf_bm", "0b0879e7ef78ffbca5610c3300946b0a95d2def0-1627622858-1800-ARqyjlrT/+FxGrK8YJGUg1uucf+dDGAZsr+8WXXX/b7/P4kZ0g7zOpT2gpTQeZ+JtcYrh9U3N8RRFxjvM60qzxr26hZy9BqiKHAlAEFjWHwTCf+Igl1gNShQPlrvZqgb95hr7MRbtyta3HhIrp4NG5QTvFX9bSGDckc7g66fOzqnm6JHz1hz+k/lZ+MAEf2I8A==")
                            // .cookie("device_token", "42e0d38a29bf95200c4c20d156ac0373")

                            .header("referer", "https://sketch.pixiv.net/")
                            .header("X-Requested-With", api_lives)
                            .userAgent(userAgent)
                            // 요청 count 수가 500을 초과하면 에러 발생
                            .data("count", "500", "order_by", "created_at") //최근 라이브 시작한 순서
                            // .data("count", "100", "order_by", "total_audience_count") // 시청자 합계가 많은 순서
                            // .data("count", "50", "order_by", "audience_count") // 현재 시청자 수가 많은 순서                        


                            .method(Connection.Method.GET)
                            .ignoreContentType(true)
                            .get();

    
            txtout(doc.body(), "./jsonorigin.txt");

            JSONParser parser = new JSONParser();
            // Object obj = parser.parse(doc.text());
            txtout(doc.text(), "./whyerror.txt");
            JSONObject obj = (JSONObject)parser.parse(doc.text());
            JSONObject datajson = (JSONObject)obj.get("data");

            txtout(datajson, "./datajson.txt");

            String htmlString = datajson.toString();

            JSONObject obj2 = (JSONObject)parser.parse(htmlString);
            JSONArray datajson2 = (JSONArray)obj2.get("lives");
            String all_data = "";
            String exclive = "";

            txtout(datajson2, "./datajson2.txt");

            for(int i=0;i<datajson2.size();i++){
                JSONObject temp = (JSONObject)datajson2.get(i);
                String unique_name =  (String)((JSONObject)temp.get("user")).get("unique_name");
                String name =  (String)((JSONObject)temp.get("user")).get("name");
                String channel_id = (String)temp.get("id");

                // System.out.println("No." + i + " unique_name : " + unique_name + " / channel_id : " + channel_id + " / name : " + name);
                all_data =  all_data + "No." + i + 
                                        " unique_name : " + unique_name + 
                                        " / channel_id : " + channel_id + 
                                        " / name : " + name + "\n";

                exclive = exclive + ".data(\"exclude_live_ids[]\", \"" + channel_id + "\")\n";
            }

            txtout(all_data, "./all_data.txt");
            // txtout(exclive, "./exclive.txt");


            /*

            txtout(datajson2, "./datajson2.txt");

            JSONObject obj3 = (JSONObject)datajson2.get(0);

            txtout(obj3, "./obj3.json");

            // JSONObject obj4 = (JSONObject)obj3.get("user");

            String obj4 = (String)((JSONObject)obj3.get("user")).get("unique_name");

            // System.out.println(obj4);

            // txtout(obj4, "./obj4.json");

            txtout(obj4, "./obj4.text");

            */


    }

    public static void txtout(Object temp, String filename) throws IOException {

        OutputStream output = new FileOutputStream(filename);

        String htmlString = temp.toString();    
        byte[] by=htmlString.getBytes();
        output.write(by);
    }
}

