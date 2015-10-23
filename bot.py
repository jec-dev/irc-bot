import socket

server = "irc.freenode.net"
channel = "#jec-dev"
botnick = "Mybot"

def ping(): # responds to server pings
  ircsock.send("PONG :pingis\n")

def sendmsg(chan , msg):
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n")

def joinchan(chan):
  ircsock.send("JOIN "+ chan +"\n")

def hello():
  ircsock.send("PRIVMSG "+ channel +" :Hello! Welcome to jec-dev! Happy \
          Hacking! :D\n")

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" Test Bot\n") # user authentication
ircsock.send("NICK "+ botnick +"\n") # here we actually assign the nick to the bot

joinchan(channel)

while 1:
  ircmsg = ircsock.recv(2048)
  ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
  print(ircmsg) # server messages

  if ircmsg.find(":Hello "+ botnick) != -1:
    hello()

  if ircmsg.find(":PING ") != -1:
    ping()
