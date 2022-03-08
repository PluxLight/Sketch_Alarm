package com.example;

import java.text.SimpleDateFormat;

import net.dv8tion.jda.api.events.ShutdownEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

public class ShutEvent extends ListenerAdapter {

    public void sdEvent(ShutdownEvent event) {
        long time1 = System.currentTimeMillis();
        SimpleDateFormat simpl = new SimpleDateFormat("yyyy년 MM월 dd일 aa hh시 mm분 ss초");
        String timestr1 = simpl.format(time1);

        System.out.println(timestr1 + " 이건 sdEvent 에서 출력한 것");
        
        System.out.println(" ");
        System.exit(0);
    }
    
}

    
    