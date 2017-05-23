import socket
import time
import datetime


def ping():  # responds to server pings
    ircsock.send("PONG :pingis\n")


def sendmsg(chan, msg):
    ircsock.send("PRIVMSG " + chan + " :" + msg + "\n")


def joinchan(chan):
    ircsock.send("JOIN " + chan + "\n")


def hello():
    ircsock.send("PRIVMSG " + channel + " :Hello! Welcome to jec-dev! Happy \
          Hacking! :D\n")


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
            fname = 'logs/' + now.date().strftime('%d-%m-%y') + '.log'
            with open(fname, 'a') as log:
                log.write(now.time().strftime('%H:%M')+ircmsg+'\n')

            if ircmsg.find(":Hello " + botnick) != -1:
                hello()

            if ircmsg.find('PING') != -1:
                ping()
            time.sleep(2)
        except Exception:
            continue
