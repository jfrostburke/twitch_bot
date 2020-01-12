import os
import sys
import json
import socket
import requests
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection

connection_data = ('irc.twitch.tv', 6667)
user = os.getenv('twitchuser')
channel = os.getenv('twitchchannel') 
# Make sure channel has # as first character
token = os.getenv('twitchapikey')
# Token from http://twitchapps.com/tmi/
if not token:
    print("Error: invalid token")
    sys.exit()
readbuffer = ''

server = socket.socket()
server.connect(connection_data)
pass_string = 'PASS ' + token + '\r\n'
user_string = 'NICK ' + user + '\r\n'
join_string = 'JOIN ' + channel + '\r\n'
pass_string = pass_string.encode(encoding='UTF-8')
user_string = user_string.encode(encoding='UTF-8')
join_string = join_string.encode(encoding='UTF-8')
server.send(pass_string)
server.send(user_string)
server.send(join_string)

fig_size = 8
fig = plt.figure(figsize=(fig_size,fig_size),facecolor='white')
ax = fig.add_subplot(111)
# Twitch emote size is 28x28
# SMB1 sprite block is 16x16
length = 16
ax.set_xlim([0,length])
ax.set_ylim([0,length])
ax.set_xticks(np.arange(length)+0.5)
ax.set_xticklabels([str(x+1) for x in np.arange(length)])
ax.set_yticks(np.arange(length)+0.5)
ax.set_yticklabels([str(x+1) for x in np.arange(length)])
ax.xaxis.grid(ls='--',alpha=0.5,zorder=1)
ax.yaxis.grid(ls='--',alpha=0.5,zorder=1)
plt.ion()
plt.show()
while True:
    msg_raw = str(server.recv(2048))
    try:
        msg_clean = msg_raw.split(' ')[3:]
        msg_clean[-1] = msg_clean[-1][:-2] # clean newline chars
        if msg_clean[0] != ':!draw':
            print msg_clean
            print "not drawing"
            continue
        else:
            x = int(msg_clean[1])-1
            y = int(msg_clean[2])-1
            color = msg_clean[3]
    except:
        print "something else went wrong"
        continue

    try:
        rect = Rectangle(xy=(x,y),width=1,height=1,color=color,lw=0,alpha=1.0,zorder=10)
        ax.add_patch(rect)
    except:
        print "couldn't draw"
        continue
    plt.pause(0.1)
    
