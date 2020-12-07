class Devicetool:

def device_app(musicdir, queue, tracknumber):
	name = multiprocessing.current_process().name
	id = multiprocessing.current_process().pid

	audio = AudioPlayer(musicdir+"/"+queue(tracknumber))
	audio.volume = 30
	audio.play(block=True)

def start_device():
	global device
	device = Process(name='audio1', target=device_app)
	device.start()
