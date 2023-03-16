import socket
import time
import zlib
import base64

bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "irc.root-me.org"
port = 6667
channel = "#root-me_challenge"
contact = "candy"
bot_name = "OneSimpleBot"

bot.connect((host, port))
print("Connected to " + host)
bot.send(bytes("USER " + bot_name + " " + bot_name + " " + host + " " + bot_name + "\r\n", "UTF-8"))
bot.send(bytes("NICK " + bot_name + "\n", "UTF-8"))
bot.send(bytes("JOIN " + channel + "\r\n", "UTF-8"))
time.sleep(3)
bot.send(bytes("PRIVMSG " + contact + " !ep4" + "\r\n", "UTF-8"))
end_script = False
while(end_script == False):
    msg = bot.recv(2048).decode("UTF-8")
    print(msg)
    if (msg.startswith(":Candy!Candy@root-me.org PRIVMSG")):
        string_to_decode = msg.replace(":Candy!Candy@root-me.org PRIVMSG OneSimpleBot :", "")
        end_script = True
print(string_to_decode)
txt=zlib.decompress(base64.b64decode(string_to_decode))
txt_string = str(txt)
txt_string = txt_string.replace("b'", "")
txt_string = txt_string.replace("'", "")
bot.send(bytes("PRIVMSG " + contact + " !ep4 -rep " + txt_string + "\r\n", "UTF-8"))
msg = bot.recv(2048).decode("UTF-8")
print(msg)