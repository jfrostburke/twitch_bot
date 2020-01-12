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
# Start with goomba
xs = [2, 3, 4, 5, 6, 8, 9, 10, 11, 8, 7, 1, 2, 3, 4, 5, 6, 10, 11, 12, 1, 2, 3, 4, 5, 11, 12, 13, 13, 2, 3, 7, 8, 9, 6, 7, 8, 9, 10, 6, 4, 5, 7, 8, 9, 10, 11, 4, 5, 6, 7, 8, 9, 10, 11, 5, 6, 7, 8, 9, 10, 9, 10, 11, 6, 5, 4, 4, 6, 9, 11, 4, 4, 11, 11, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10, 10, 10, 11, 12, 10, 1, 2, 3, 4, 2, 3, 4, 11, 12, 13, 14, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 7, 8, 12, 13, 14, 15, 0, 1, 2, 3, 7, 8, 12, 13, 14, 15, 1, 2, 3, 12, 13, 14, 1, 2, 3, 12, 3, 14, 13, 6, 7, 8, 9, 2, 5, 6, 7, 8, 9, 10, 13, 3, 12, 4, 5, 6, 7, 8, 9, 10, 11, 4, 11, 5, 6, 7, 8, 9, 10, 5, 10, 6, 7, 8, 9, 6, 7, 8, 9]
ys = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9, 10, 9, 10, 11, 11, 10, 9, 8, 9, 9, 9, 9, 9, 8, 12, 11, 11, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15]
cs = ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', '#FEDFA6', '#FEDFA6', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'white', 'black', 'black', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', '#FEDFA6', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', '#A81100', 'black', 'black', 'black', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100', '#A81100']
for i in range(len(xs)):
    x = xs[i]
    y = ys[i]
    color = cs[i]
    rect = Rectangle(xy=(x,y),width=1,height=1,color=color,lw=0,alpha=1.0,zorder=10)
    ax.add_patch(rect)
while True:
    msg_raw = str(server.recv(2048))
    try:
        msg_clean = msg_raw.split(' ')[3:]
        msg_clean[-1] = msg_clean[-1][:-2] # clean newline chars
        if msg_clean[0] != ':!draw':
            print msg_clean
            print "not drawing"
            plt.pause(1)
            continue
        else:
            x = int(msg_clean[1])-1
            y = int(msg_clean[2])-1
            color = msg_clean[3]
    except:
        print "something else went wrong"
        # So I can save my place
        # TODO: automatically restart plot on _tkinter.TclError
        print xs
        print ys
        print cs
        plt.pause(1)
        continue

    try:
        xs.append(x)
        ys.append(y)
        cs.append(color)
        rect = Rectangle(xy=(x,y),width=1,height=1,color=color,lw=0,alpha=1.0,zorder=10)
        ax.add_patch(rect)
    except:
        print "couldn't draw"
        plt.pause(1)
        continue
    plt.pause(1)
    
