var settings = {
    channels: ["#jec-dev"],
    server : "irc.freenode.net",
    port : "6667",
    secure : "false",
    nick : "botwayne",
    password: "oauth:randomNumbersAndLetters"
}

var admin_message = "Hackerrank contest on 29 Oct 2015 ... Register for the contest its free :) :) ... Happy Coding :) :)";

var irc = require('irc');

var bot = new irc.Client(settings.server,settings.nick,{
    channels: [settings.channels+" "+settings.password],
    debug : false,
    password:  settings.password,
    username:  settings.nick
});

var arr=[];
arr.push(settings.nick);
var regex = /vi*/

bot.addListener("join",function(channel,who){
    var match = who.match(regex);
    if(match)
        bot.say(channel,who+"...hello GSoCer ..");
    else if(who === settings.nick)
        bot.say(channel,who+" built by Node JS");
    else
        bot.say(channel,who+"...hello Coding enthusiast...");
})



bot.addListener("message",function(from,to,text,message){
var flag=true;
    arr.forEach(function(name){
        if(name===from)
            flag=false;        
        arr.push(from);  
    });

    if(flag==true)
        bot.say(settings.channels[0],"hi..."+from+"..."+admin_message);
    else
        console.log("exists");
});

