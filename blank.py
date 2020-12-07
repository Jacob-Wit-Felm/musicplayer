from audioplayer import AudioPlayer

import os
from time import sleep

def play(queue):
	global playing
	player = AudioPlayer(str(musicdir + '/' + queue[tracknumber])).play(loop=True)
	playing = True
	return player

dirname = os.path.dirname(__file__)
musicdir = os.path.join(dirname, '../Google/music247')
queue = [f for f in os.listdir(musicdir)]

global status
global playing
global track
global tracknumber
global maxtracks

status = True
playing = False
track = "current"
tracknumber = 0
maxtracks = len(queue)

while True:
	if status == True:
		if playing == False: player = play(queue)
		if track == 'next': 
			player.stop()
			player = play_next
		
		sleep(.5)
		print("loop")

AudioPlayer()