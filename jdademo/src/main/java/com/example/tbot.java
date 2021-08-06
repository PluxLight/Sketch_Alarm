package com.example;

import java.text.SimpleDateFormat;

import javax.security.auth.login.LoginException;

import net.dv8tion.jda.api.JDA;
import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.entities.Activity;
import net.dv8tion.jda.api.entities.Message;
import net.dv8tion.jda.api.entities.MessageChannel;
import net.dv8tion.jda.api.entities.TextChannel;
import net.dv8tion.jda.api.entities.User;
import net.dv8tion.jda.api.entities.Activity.ActivityType;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

public class tbot extends ListenerAdapter {

    public static void main(String[] args) throws LoginException {

        long time0 = System.currentTimeMillis();
        SimpleDateFormat simpl = new SimpleDateFormat("yyyy년 MM월 dd일 aa hh시 mm분 ss초");
        String timestr0 = simpl.format(time0);

        System.out.println(timestr0 + " 이건 void main 에서 출력한 것");

        // 기본 jda를 만들고
        JDA jda = JDABuilder.createDefault("ODcxMDI3NTgzNTIzOTEzNzM4.YQVVpg.AYLbNxRgwm_8H6WzC3o0LA9KfoU")
        .setActivity(Activity.playing("개발 당"))
        .build();

        // jda에 이벤트를 감지하는 리스너를 넣는다.
        // jda.addEventListener(new tbot(), new MessageListener());
        jda.addEventListener(new tbot(), new OnReadyPlay(), new ShutEvent());

    }

    @Override
    public void onMessageReceived(MessageReceivedEvent event) {

        JDA jda = event.getJDA();                       //JDA, the core of the api.
        long responseNumber = event.getResponseNumber();//The amount of discord events that JDA has received since the last reconnect.

        //Event specific information
        User author = event.getAuthor();                //The user that sent the message
        Message message = event.getMessage();           //The message that was received.
        MessageChannel channel = event.getChannel();    //This is the MessageChannel that the message was sent to.
        String msgdothg1 = "이건 !ping ping 메세지를 입력 해 doThing으로 보낸 메세지입니다";
        String msgdothg2 = "이건 !sd 메세지를 입력 해 doThing으로 보낸 메세지입니다";
        
        // channel.sendMessage("Your message here.").queue();

        // 받은 메세지 내용이 !ping이라면
        if (event.getMessage().getContentRaw().equals("!ping ping")) {
            // pong라는 내용을 보낸다.
            event.getChannel().sendMessage("pong pong!").queue();
            System.out.printf("author :  %s\n", author);
            System.out.printf("message :  %s\n", message);
            System.out.printf("channel :  %s\n", channel);

            System.out.println("");

            System.out.println(author.getClass().getName());
            System.out.println(message.getClass().getName());
            System.out.println(channel.getClass().getName());

            // sendPrivateMessage(author, "u n i");
            doThing(jda, msgdothg1);
        }
        else if (event.getMessage().getContentRaw().equals("!sd")) {

            event.getChannel().sendMessage("i will be return").queue();
            doThing(jda, msgdothg2);
            jda.shutdown();

        }
    }


    public static void pr(Object obj) {
            System.out.println(obj);
        }


    public void sendPrivateMessage(User user, String content) {
        if (user.isBot())
            return;

        user.openPrivateChannel().flatMap(channel -> channel.sendMessage(content)).queue();
    }


    public void doThing(JDA jda, String sdmsg) {
        long chid = 871290747377307730L;
        TextChannel channel = jda.getTextChannelById(chid);
        if (channel != null) {
            channel.sendMessage(sdmsg).queue();
        }
    }
}

//channel = 871290747377307730