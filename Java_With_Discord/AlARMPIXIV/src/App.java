import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.OutputStream;

import org.jsoup.Jsoup;

import org.jsoup.Connection;
import org.jsoup.nodes.Document;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import java.text.SimpleDateFormat;
import java.util.Date;

public class App {
    public static void main(String[] args) throws Exception {

        String url = "https://sketch.pixiv.net/api/lives.json";
        String api_lives = "https://sketch.pixiv.net/lives?sort_by=created_at";
        String userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36";

        SimpleDateFormat format1 = new SimpleDateFormat("yyyy-MM-dd HH mm ss");

        int count = 0;

        while (true) {
            Document doc = Jsoup.connect(url)

                    .header("authority", "sketch.pixiv.net")
                    // .header("path", "/api/lives.json?count=100&order_by=created_at")
                    .header("scheme", "https").header("accept", "application/vnd.sketch-v4+json")
                    .header("accept-encoding", "gzip, deflate, br")
                    .header("accept-language", "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7")

                    // 쿠키 PHPSESSID 값이 있어야 모든 방송 유저의 정보를 얻을 수 있음
                    .cookie("PHPSESSID", "")

                    .header("referer", "https://sketch.pixiv.net/").header("X-Requested-With", api_lives)
                    .userAgent(userAgent)
                    // 요청 count 수가 500을 초과하면 에러 발생
                    .data("count", "500", "order_by", "created_at") // 최근 라이브 시작한 순서
                    // .data("count", "100", "order_by", "total_audience_count") // 시청자 합계가 많은 순서
                    // .data("count", "100", "order_by", "audience_count") // 현재 시청자 수가 많은 순서

                    .method(Connection.Method.GET).ignoreContentType(true).get();

            // txtout(doc.body(), "./jsonorigin.txt");

            JSONParser parser = new JSONParser();
            // Object obj = parser.parse(doc.text());
            JSONObject obj = (JSONObject) parser.parse(doc.text());
            JSONObject datajson = (JSONObject) obj.get("data");

            // txtout(datajson, "./datajson.txt");

            String htmlString = datajson.toString();

            JSONObject obj2 = (JSONObject) parser.parse(htmlString);
            JSONArray datajson2 = (JSONArray) obj2.get("lives");
            String all_data = "";
            String exclive = "";

            for (int i = 0; i < datajson2.size(); i++) {
                JSONObject temp = (JSONObject) datajson2.get(i);
                String unique_name = (String) ((JSONObject) temp.get("user")).get("unique_name");
                String name = (String) ((JSONObject) temp.get("user")).get("name");
                String channel_id = (String) temp.get("id");

                // System.out.println("No." + i + " unique_name : " + unique_name + " /
                // channel_id : " + channel_id + " / name : " + name);
                all_data = all_data + "No." + i + " unique_name : " + unique_name + " / channel_id : " + channel_id
                        + " / name : " + name + "\n";

                exclive = exclive + ".data(\"exclude_live_ids[]\", \"" + channel_id + "\")\n";
                count += 1;
            }

            Date time = new Date();
            String time1 = format1.format(time);

            txtout(all_data, "./df/" + time1 + " all_data.txt");
            // txtout(exclive, "./df/" + time1 + " exclive.txt");

            FileWriter fw2 = new FileWriter("./df/log.txt", true);
            String logdata = count + "명 " + time1 + "\n";
            fw2.write(logdata);
            fw2.close();

            count = 0;
            Thread.sleep(300000);
        }

    }

    public static void txtout(Object temp, String filename) throws IOException {

        OutputStream output = new FileOutputStream(filename);

        String htmlString = temp.toString();
        byte[] by = htmlString.getBytes();
        output.write(by);

        output.close();
    }
}