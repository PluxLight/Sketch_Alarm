public class unuse {
    
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