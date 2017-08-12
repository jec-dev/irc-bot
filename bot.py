import socket
import time
import datetime
from dateutil import tz

from_zone = tz.gettz('UTC')
to_zone = tz.gettz('Asia/Kolkata')


def ping():  # responds to server pings
    ircsock.send("PONG :pingis\n")


def sendmsg(chan, msg):
    ircsock.send("PRIVMSG " + chan + " :" + msg + "\n")


def joinchan(chan):
    ircsock.send("JOIN " + chan + "\n")


def hello():
    ircsock.send("PRIVMSG " + channel + " :Hello! Welcome to jec-dev! Happy Hacking! :D\n")

def welcome():
	pass

if __name__ == '__main__':
    server = "irc.freenode.net"
    channel = "#jec-dev"
    botnick = "jec-dev-bot"

    ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Here we connect to the server using the port 6667
    ircsock.connect((server, 6667))

    ircsock.setblocking(False)

    ircsock.send("USER " + botnick + " " + botnick + " " +
                 botnick + " Test Bot\n")  # user authentication
    # here we actually assign the nick to the bot
    ircsock.send("NICK " + botnick + "\n")

    joinchan(channel)

    while 1:
        try:
            ircmsg = ircsock.recv(2048)
            ircmsg = ircmsg.strip('\n\r')  # removing any unnecessary linebreaks.

            now = datetime.datetime.now()
            utc = now.replace(tzinfo=from_zone)
            local = utc.astimezone(to_zone)

            fname = 'logging/logs/' + local.date().strftime('%d-%m-%y') + '.log'

            if ircmsg.find(":Hello " + botnick) != -1:
                hello()

			
            if ircmsg.find('PING') != -1:
                ping()
            else:
                with open(fname, 'a') as log:
                    split_message = ircmsg.split(' ')
                    user = split_message[0].split('!')[0]
                    ircmsg = local.time().strftime('%H:%M') + ' ' + user + ' ' + ' '.join(split_message[3:])
                    log.write(ircmsg+'\n')
            time.sleep(2)
        except Exception:
            continue

