import socket
import time
import codecs

bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hote = "irc.root-me.org"
port = 6667
channel = "#root-me_challenge"
contact = "candy"
bot_name = "m3taaa"

bot.connect((hote, port))
print("Connect to server : " + hote)
bot.send(bytes("USER " + bot_name + " " + bot_name + " " + hote + " " + bot_name + "\r\n", "UTF-8"))
bot.send(bytes("NICK " + bot_name + "\n", "UTF-8"))
bot.send(bytes("JOIN " + channel + "\r\n", "UTF-8"))
time.sleep(2)
bot.send(bytes("PRIVMSG " + contact + " !ep3" + "\r\n", "UTF-8"))



end_script = False
while(end_script == False):
    msg = bot.recv(2048).decode("UTF-8")
    print(msg)

    if(msg.startswith(":Candy!Candy@root-me.org PRIVMSG")):
       to_decrypt = msg.replace(":Candy!Candy@root-me.org PRIVMSG " + bot_name + " :", "")
       end_script = True

msg_to_send = codecs.encode(to_decrypt, "rot-13")
bot.send(bytes("PRIVMSG " + contact + " !ep3 -rep "+msg_to_send + "\r\n", "UTF-8"))
msg = bot.recv(2048).decode("UTF-8")
print(msg)