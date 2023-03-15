import socket
import time
import base64

bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "irc.root-me.org"
port = 6667
channel = "#root-me_challenge"
contact = "candy"
bot_name = "m3taaaIsBot"

print("connect to " + host)
bot.connect((host, port))
print("connect is ok")

bot.send(bytes("USER " + bot_name + " "+bot_name + " " + host + " " + bot_name + "\r\n", "UTF-8"))
bot.send(bytes("NICK "+ bot_name + "\n", "UTF-8"))
bot.send(bytes("JOIN " + channel + "\r\n", "UTF-8"))
time.sleep(2)
bot.send(bytes("PRIVMSG " + contact + " !ep2" + "\r\n", "UTF-8"))

end_script = False

while(end_script == False):
	msg = bot.recv(2048).decode("UTF-8")
	print(msg)
	if(msg.startswith(":Candy!Candy@root-me.org PRIVMSG")):
		string_to_decode = msg.replace(":Candy!Candy@root-me.org PRIVMSG m3taaaIsBot :", "")
		end_script = True
string_decode = str(base64.b64decode(string_to_decode))
string_decode = string_decode.replace("b'", "")
string_decode = string_decode.replace("'", "")
bot.send(bytes("PRIVMSG " + contact + " !ep2 -rep " + string_decode + "\r\n", "UTF-8"))
msg = bot.recv(2048).decode("UTF-8")
print(msg)
