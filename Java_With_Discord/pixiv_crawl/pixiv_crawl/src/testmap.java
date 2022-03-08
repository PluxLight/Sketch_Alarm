import java.text.SimpleDateFormat;
import java.util.Date;

public class testmap {
    public static void main(String[] args) {

        SimpleDateFormat format1 = new SimpleDateFormat ( "yyyy-MM-dd HH:mm:ss");
        Date time = new Date();
        String time1 = format1.format(time);
        System.out.println(time1);
               
    }
}
