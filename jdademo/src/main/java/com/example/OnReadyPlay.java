package com.example;

import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.util.List;

import java.text.SimpleDateFormat;

import org.jetbrains.annotations.NotNull;

import net.dv8tion.jda.api.JDA;
import net.dv8tion.jda.api.entities.TextChannel;
import net.dv8tion.jda.api.events.ReadyEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;


public class OnReadyPlay extends ListenerAdapter {

    public void onReady(@NotNull ReadyEvent event) {
        long time1 = System.currentTimeMillis();
        SimpleDateFormat simpl = new SimpleDateFormat("yyyy년 MM월 dd일 aa hh시 mm분 ss초");
        String timestr1 = simpl.format(time1);

        System.out.println(timestr1 + " 이건 void onReady 에서 출력한 것");

        Runnable runnable = new Runnable() {
            int cnt = 0;
            @Override
            public void run() {
                long time2 = System.currentTimeMillis();
                SimpleDateFormat simpl = new SimpleDateFormat("yyyy년 MM월 dd일 aa hh시 mm분 ss초");
                String timestr2 = simpl.format(time2);

                ZonedDateTime now = ZonedDateTime.now(ZoneId.of("Asia/Seoul"));
                String nowstr = now.toString();
                JDA jda = event.getJDA();
                long rn = event.getResponseNumber();
                List<TextChannel> channels = jda.getTextChannelsByName("알람", true);
                for(TextChannel ch : channels)
                {
                    ch.sendMessage(nowstr + "\ni'm here !!!").queue();
                }
                System.out.printf("rn :  %d\n", rn);
                System.out.println(cnt + " 회");

                cnt += 1;
                System.out.println(timestr2 + " 이건 runnable - void run 에서 출력한 것");
            }
        };
        ScheduledExecutorService service = Executors.newSingleThreadScheduledExecutor();
        service.scheduleAtFixedRate(runnable, 30, 60, TimeUnit.SECONDS);

            

    }

}