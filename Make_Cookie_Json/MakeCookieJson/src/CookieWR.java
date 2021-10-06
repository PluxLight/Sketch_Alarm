import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.Reader;

import java.io.IOException;
import java.text.ParseException;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

public class CookieWR {

}


    // public static JSONObject editjson(String cmd, String val) throws ParseException {
    //     // cmd
    //     // = all_ : false
    //     // = pid : put pixiv id
    //     // = pdel : delete pixiv id
    //     // = plist : pixiv id list return
    //     JSONObject returnobj = new JSONObject();

    //     try (Reader reader = new FileReader("./liver.json")) {

    //         System.out.println(reader);
    //         // JSONParser parser = new JSONParser();        
    //         // JSONObject liverjson = (JSONObject) parser.parse(reader);
    //         // // Iterator<String> iter = liverjson.keySet().iterator();

    //         // if (cmd.equalsIgnoreCase("all_")) {
    //         //     while(iter.hasNext()) {
    //         //         String key = iter.next();
    //         //         liverjson.replace(key, "false");
    //         //     }
    //         // }
    //         // else if (cmd.equalsIgnoreCase("pid")) {
    //         //     liverjson.put(val, "false");
    //         // }
    //         // else if (cmd.equalsIgnoreCase("pdel")) {
    //         //     liverjson.remove(val);                
    //         // }
    //         // else if (cmd.equalsIgnoreCase("plist")) {
    //         //     returnobj = liverjson;
    //         // }
    //         // else ;

    //         // FileWriter file = new FileWriter("./liver.json");
    //         // file.write(liverjson.toJSONString());
    //         // file.flush();
    //         // file.close();

    //     } catch (IOException e) {
    //         e.printStackTrace();
    //     } catch (Exception e) {
    //         e.printStackTrace();
    //     }

    //     return returnobj;

    // }
