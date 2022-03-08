package com.testjda;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

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


import javax.annotation.Nonnull;

import net.dv8tion.jda.api.entities.Guild;
import net.dv8tion.jda.api.entities.Member;
import net.dv8tion.jda.api.events.user.update.UserUpdateActivityOrderEvent;
import net.dv8tion.jda.api.events.user.update.UserUpdateOnlineStatusEvent;
import net.dv8tion.jda.internal.requests.Route.Guilds;
import net.dv8tion.jda.api.events.user.UserActivityEndEvent;
import net.dv8tion.jda.api.events.user.UserActivityStartEvent;

public class UserActivity extends ListenerAdapter {
    
    @Override
    public void onUserActivityStart(UserActivityStartEvent event) {
        System.out.println("user ActivityStart");
    }
    
    @Override
    public void onUserUpdateOnlineStatus(UserUpdateOnlineStatusEvent event) {
        System.out.println("user UpdateOnlineStatus");
    }

    public void onUserUpdateActivityOrderEvent(UserUpdateActivityOrderEvent event) {
        System.out.println("user ActivityOrder");
    }

    public void onUserActivityEndEvent(UserActivityEndEvent event) {
        System.out.println("user ActivityEnd");
    }


    
}

        // JDA jda = event.getJDA();

        // List<Guild> gds = jda.getGuilds();
        // for (Guild gd : gds) {
        //     pr(gd);
        //     List<Member> mers = gd.getMembers();
        //     for (Member mer : mers) {
        //         pr(mer);
        //     }

        // }