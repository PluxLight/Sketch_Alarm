import java.io.File;
import java.io.FileNotFoundException;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.List;
import java.io.File;

public class datan {
    public static void main(String[] args) throws Exception {
        String fd = "C:\\Users\\sangha\\Documents\\pixiv_crawl\\pixiv_crawl\\참고자료\\크롤링 데이터";

        List<String> beforel = new ArrayList<>();

        File dir = new File(fd);
        File files[] = dir.listFiles();

        int count = 0;
        String temp = "";


        for (int i = 1; i < files.length; i++) {
            String rfn = files[i-1].toString();
            BufferedReader br = new BufferedReader(new FileReader(rfn));

            while(true) {
                String line = br.readLine();
                if (line==null) break;
                String un = line.split(" : ")[1].split(" / ")[0];
                // System.out.println(un);
                beforel.add(un);
            }

            rfn = files[i].toString();
            br = new BufferedReader(new FileReader(rfn));

            while(true) {
                String line = br.readLine();
                if (line==null) break;
                String un = line.split(" : ")[1].split(" / ")[0];
                // System.out.println(un);
                if (!beforel.contains(un)) count++;
            }

            temp = temp + files[i-1].toString().split("데이터")[1] + " -> " + files[i].toString().split("데이터")[1] + " " + count + "\n";
            count = 0;
            beforel = new ArrayList<>();
        }


        txtout(temp, "C:\\Users\\sangha\\Documents\\newhuman.txt");

    }

    public static void txtout(Object temp, String filename) throws IOException {

        OutputStream output = new FileOutputStream(filename);

        String htmlString = temp.toString();    
        byte[] by=htmlString.getBytes();
        output.write(by);
        output.close();
    }
}
