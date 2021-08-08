package com.example;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.text.SimpleDateFormat;

import org.jetbrains.annotations.NotNull;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import org.jsoup.Jsoup;
import org.jsoup.Connection;
import org.jsoup.nodes.Document;

import net.dv8tion.jda.api.JDA;
import net.dv8tion.jda.api.entities.TextChannel;
import net.dv8tion.jda.api.events.ReadyEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.OutputStream;
import java.io.Reader;


public class OnReadyPlay extends ListenerAdapter {

    public void onReady(@NotNull ReadyEvent event) {
        Runnable runnable = new Runnable() {          
            int cnt = 1;
            @Override
            public void run() {
                JSONParser parser = new JSONParser();
                JDA jda = event.getJDA();
                List<String> livers = new ArrayList<>();
                List<String> nonlivers = new ArrayList<>();

                try (Reader reader = new FileReader("./liver.json")) {
        
                    JSONObject liverjson = (JSONObject) parser.parse(reader);
                    Iterator<String> iter = liverjson.keySet().iterator();

                    JSONObject crawljson = search_live();

                    while(iter.hasNext()) {
                        String key = iter.next();
                        if(crawljson.containsKey(key)) { //방송중이면 livers 리스트로
                            livers.add(key);
                        }
                        else {
                            if(liverjson.get(key).equals("true")) { //방송중이 아니면서 값이 true로 된 유저는 nonlivers 리스트로
                                nonlivers.add(key);
                            }                             
                        }
                    }

                    // txtout(liverjson, "./liverjson.txt");
                    // txtout(iter, "./iter.txt");


                    List<TextChannel> channels = jda.getTextChannelsByName("알람", true);
                    for(TextChannel ch : channels) {
                        for(String liver : livers) {
                            System.out.println(liver);
                            if(liverjson.get(liver).equals("false")) {
                                String username = (String) ((JSONObject)crawljson.get(liver)).get("name");
                                String uniqname = (String) ((JSONObject)crawljson.get(liver)).get("unique_name");
                                String ch_id = (String) ((JSONObject)crawljson.get(liver)).get("channel_id");
                                String liveurl = "https://sketch.pixiv.net/@";
                                String alarmmsg = String.format("%s님이 방송을 시작했습니다!", username);
                                String linkmsg = String.format("%s%s/lives/%s", liveurl, uniqname, ch_id);

                                ch.sendMessage(alarmmsg).queue();
                                ch.sendMessage(linkmsg).queue();

                                liverjson.replace(liver, "true");
                            }
                        }
                        
                    }

                    if(nonlivers.size() > 0) {
                        for(String nonliver : nonlivers) {
                            liverjson.replace(nonliver, "false");
                        }
                    }
                    
                    FileWriter file = new FileWriter("./liver.json");
                    file.write(liverjson.toJSONString());
                    file.flush();
                    file.close();

                } catch (IOException e) {
                    e.printStackTrace();
                } catch (ParseException e) {
                    e.printStackTrace();
                } catch (Exception e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }

                System.out.println(cnt + " 회");
                cnt += 1;

                
            }
        };

        ScheduledExecutorService service = Executors.newSingleThreadScheduledExecutor();
        service.scheduleAtFixedRate(runnable, 10, 60, TimeUnit.SECONDS);

    }

    public static JSONObject search_live() throws Exception {

        String url = "https://sketch.pixiv.net/api/lives.json";
        String api_lives = "https://sketch.pixiv.net/lives?sort_by=created_at";
        String userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.277 Whale/2.9.118.38 Safari/537.36";

        Document doc = Jsoup.connect(url)
                            
                            .header("authority", "sketch.pixiv.net")
                            // .header("path", "/api/lives.json?count=500&order_by=audience_count")
                            .header("scheme", "https")
                            .header("accept", "application/vnd.sketch-v4+json")
                            .header("accept-encoding", "gzip, deflate, br")
                            .header("accept-language", "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7")

                            //쿠키 PHPSESSID 값이 있어야 모든 방송 유저의 정보를 얻을 수 있음
                            .cookie("PHPSESSID", "7937790_Vmr8mfVXA5FeaKvIMCgkkhPuj80JcbA1")

                            .header("referer", "https://sketch.pixiv.net/")
                            .header("X-Requested-With", api_lives)
                            .userAgent(userAgent)
                            // 요청 count 수가 500을 초과하면 에러 발생
                            .data("count", "500", "order_by", "created_at") //최근 라이브 시작한 순서                   
                            .method(Connection.Method.GET)
                            .ignoreContentType(true)
                            .get();


            JSONParser parser = new JSONParser();
            JSONObject return_obj = new JSONObject();
            
            JSONObject obj = (JSONObject)parser.parse(doc.text());
            JSONObject datajson = (JSONObject)obj.get("data");

            String htmlString = datajson.toString();

            JSONObject obj2 = (JSONObject)parser.parse(htmlString);
            JSONArray datajson2 = (JSONArray)obj2.get("lives");

            for(int i=0;i<datajson2.size();i++){
                JSONObject temp = (JSONObject)datajson2.get(i);
                String unique_name =  (String)((JSONObject)temp.get("user")).get("unique_name");
                String channel_id = (String)temp.get("id");
                String name =  (String)((JSONObject)temp.get("user")).get("name");
                String pixiv_id =  (String)((JSONObject)temp.get("user")).get("pixiv_user_id").toString();

                String jsonstr = String.format("{\"unique_name\" : \"%s\", \"channel_id\" : \"%s\", \"name\" : \"%s\"}", unique_name, channel_id, name);
                JSONObject obj3 = (JSONObject) new JSONParser().parse(jsonstr);
                return_obj.put(pixiv_id, obj3);
            }

            // txtout(return_obj, "./return_obj.txt");

        return return_obj;

    }

    public static void txtout(Object temp, String filename) throws IOException {

        OutputStream output = new FileOutputStream(filename);

        String htmlString = temp.toString();    
        byte[] by=htmlString.getBytes();
        output.write(by);
    }

}