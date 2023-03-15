import socket
import time
import math

host = "irc.root-me.org"
port = 6667
canal = "#root-me_challenge"
contact = "candy"
print("bot name : ")
name_bot =input()
#name_bot = "m3taaa"
bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Connect to server "+host)
bot.connect((host, port))
time.sleep(1)
bot.send(bytes("USER "+name_bot + " " + name_bot + " " + host + " " + name_bot + "\r\n", "UTF-8"))
bot.send(bytes("NICK " + name_bot + "\n", "UTF-8"))
time.sleep(1)
bot.send(bytes("JOIN " + canal + '\r\n', "UTF-8"))
time.sleep(2)
bot.send(bytes("PRIVMSG "+ contact +" :"+ "!ep1" + "\r\n", "UTF-8"))

end = False
while(end == False):
	resp = bot.recv(200000).decode("UTF-8")
	print(resp)
	if resp.startswith(":Candy!Candy@root-me.org PRIVMSG"):
		f1 = resp.replace(":Candy!Candy@root-me.org PRIVMSG " + name_bot + " :", "")
		print(f1)
		end = True

list_nb = f1.split("/")
nbOne = list_nb[0].replace(" ", "")
nbTwo = list_nb[1].replace(" ", "")
nbTwo = list_nb[1].replace("\r\n", "")
nb1 = int(nbOne)
nb2 = int(nbTwo)
nb1 = math.sqrt(nb1)
res = nb1 * nb2
res = round(res, 2)
print(res)
res_str = str(res)
bot.send(bytes("PRIVMSG " + contact + " !ep1 -rep "+res_str+"\r\n", "UTF-8"))
time.sleep(2)
resp = bot.recv(1024).decode("UTF-8")
print(resp)
print("END SCRIPT")
