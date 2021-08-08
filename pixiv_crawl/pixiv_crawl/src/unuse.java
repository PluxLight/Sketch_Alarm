import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Set;

import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.OutputStream;
import java.io.Reader;





public class unuse {

    public static void main(String[] args) throws Exception {

        JSONObject obj1 = new JSONObject();
        JSONObject obj2 = new JSONObject();

        HashMap<String, String> map1 = new HashMap<String, String>();
        HashMap<String, HashMap<String, String>> map2 = new HashMap<String, HashMap<String, String>>();

        String hd = "hd";
        String ch = "ch";
        String nn = "nn";
        
        int idint = 1;

        for(int i=0; i<5; i++) {

            // String jsonstr = String.format("{\"name_0%d\" : {\"hd\" : \"%s\", \"ch\" : \"%s\", \"nn\" : \"%s\"}}", idint, hd+1, ch+1, nn+1);
            String jsonstr = String.format("{\"hd\" : \"%s\", \"ch\" : \"%s\", \"nn\" : \"%s\"}", hd+i, ch+i, nn+i);
            // System.out.println("jsonstr = "+jsonstr);

            JSONObject obj3 = (JSONObject) new JSONParser().parse(jsonstr);

            obj2.put("name_0"+i, obj3);
            


        }

        System.out.println(obj2+"\n\n");

        System.out.println(((JSONObject)obj2.get("name_02")).get("ch"));
        System.out.println(obj2.getClass().getName());

        System.out.println("\n\n");

        Iterator<String> iter = obj2.keySet().iterator();

        while(iter.hasNext()) {
            String key = iter.next();
            System.out.println(key + " : " + obj2.get(key));
        }

        try (Reader reader = new FileReader("./exampke.json")) {
            JSONParser parser = new JSONParser();        
            JSONObject liverjson = (JSONObject) parser.parse(reader);

            liverjson.put("name76", "kim");
            liverjson.remove("nameless");
            liverjson.replace("lastorder", "nonamed");
            liverjson.replace("name01", "aran");

            FileWriter file = new FileWriter("./exampke.json");
            file.write(liverjson.toJSONString());
            file.flush();
            file.close();

        } catch (IOException e) {
            e.printStackTrace();
        } catch (ParseException e) {
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }



    }


    
}

/*
            Element body = doc.body();

            String htmlString = body.toString();

            System.out.println(body);
    
            byte[] by=htmlString.getBytes();
    
            output.write(by);

            List<String> result = new ArrayList<>();

            JSONObject jsonObject = new JSONObject(htmlString);

            JSONArray arr = new JSONArray(body.text());

            JSONObject jsonObject = (JSONObject) parser.parse(htmlString);

            String lives = (String) jsonObject.get("lives");

            System.out.println(lives);

        try {
            Document doc = Jsoup.connect(url)
                            .header("authority", "sketch.pixiv.net")
                            .header("path", "/api/lives.json?count=20&order_by=created_at")
                            .header("scheme", "https")
                            .header("accept", "application/vnd.sketch-v4+json")
                            .header("accept-encoding", "gzip, deflate, br")
                            .header("accept-language", "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7")
                            .header("referer", "https://sketch.pixiv.net/")
                            .header("X-Requested-With", api_lives)
                            .userAgent(userAgent)
                            // 요청 count 수가 500을 초과하면 에러 발생
                            .data("count", "3", "order_by", "created_at") //최근 라이브 시작한 순서
                            // .data("count", "100", "order_by", "total_audience_count") // 시청자 합계가 많은 순서
                            // .data("count", "100", "order_by", "audience_count") // 현재 시청자 수가 많은 순서
                            .method(Connection.Method.GET)
                            .ignoreContentType(true)
                            .get();


            Element body = doc.body();

            String htmlString = body.toString();

            // System.out.println(body);
    
            // byte[] by=htmlString.getBytes();
    
            // output.write(by);

            // List<String> result = new ArrayList<>();

            // JSONObject jsonObject = new JSONObject(htmlString);

            // JSONArray arr = new JSONArray(body.text());

            JSONObject jsonObject = (JSONObject) parser.parse(htmlString);

            String lives = (String) jsonObject.get("lives");

            System.out.println(lives);


        } catch(Exception e) {
            System.out.println("Json load error");
        }
*/