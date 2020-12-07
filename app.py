from flask import Flask, render_template, url_for, request
from apscheduler.scheduler import Scheduler

from multiprocessing import Process
import multiprocessing

from audioplayer import AudioPlayer
from mutagen.mp3 import MP3

import os
import time

global _Playing
global device
global tracknumber
global volume
global duration

_Playing = False
volume = 20

dirname = os.path.dirname(__file__)
musicdir = os.path.join(dirname, '../Google/music247')
queue = [f for f in os.listdir(musicdir)]
tracknumber = 0

app = Flask(__name__)

@app.route('/')
def index():
	current_volume_value = volume
	return render_template('index.html', current_volume_value=current_volume_value)

@app.route('/play/', methods = ['POST'])
def play():
	start_device()
	forward_message = "Playing"
	return render_template('index.html', forward_message=forward_message);

@app.route('/stop/', methods = ['POST'])
def stop():
	global device
	global _Playing

	try:
		_Playing = False
		device.terminate()
		device.join()
		forward_message = "Stoped"
	except:
		print("no device")
		forward_message = "Music it not playing"
	
	return render_template('index.html', forward_message=forward_message);

@app.route('/track/next/', methods = ['POST'])
def play_next_track():
	global device
	global tracknumber

	_Playing = False
	device.terminate()
	device.join()

	if tracknumber + 1 > len(queue)-1:
		tracknumber = 0
	else:
		tracknumber += 1
	
	start_device()

	forward_message = "Playing next"
	return render_template('index.html', forward_message=forward_message);

@app.route('/track/previous/', methods = ['POST'])
def play_previous_track():
	global device
	global tracknumber

	_Playing = False
	device.terminate()
	device.join()

	if tracknumber + 1 > len(queue)-1:
		tracknumber = 0
	else:
		tracknumber += 1

	start_device()

	forward_message = "Playing next"
	return render_template('index.html', forward_message=forward_message);

@app.route('/track/volume/', methods = ['POST'])
def change_volume():
	global _Playing
	global device
	global volume

	volume = int(request.form['volume'])
	print(volume)
	try:
		global device
		_Playing = False
		print("change_volume")
		print(_Playing)
		device.terminate()
		device.join()
		start_device()
		forward_message = "Volume set to " + str(volume)

	except:
		print("no device")
		forward_message = "Music it not playing"
	
	return render_template('index.html', forward_message=forward_message);

def device_play_app():
	audio = AudioPlayer(musicdir+"/"+queue[tracknumber])
	audio.volume = volume
	audio.play(block=True)

def start_device():
	global device
	global _Playing

	device = Process(name='audio1', target=device_play_app)
	device.start()
	_Playing = True


def if_device_dead():
	global tracknumber
	global device
	global _Playing
	
	print(_Playing)
	print(multiprocessing.active_children())

	if _Playing and not device.is_alive() and len(print(multiprocessing.active_children())) == 0:
		print(_Playing)
		_Playing = False
		device.join()

		if tracknumber + 1 > len(queue)-1:
			tracknumber = 0
		else:
			tracknumber += 1
		
		start_device()
		print("Next track auto")


if __name__ == "__main__":
	global device

	app.run(debug=True, host='192.168.1.179')
	audio1.terminate()
	audio1.join()
	device.terminate()
	device.join()