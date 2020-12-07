import audioplayer
import time


def play():
	audio = audioplayer.AudioPlayer("../Google/music247/test.mp3")
	audio.volume = 20

	audio.play(block=True)
	status = audio.trackstatus()
	print(status[1])
	audio.play()
	audio.stop()
	while True:
		status = audio.trackstatus()
		print(status[1])
		audio.resume()
		time.sleep(1)

class Player:
	def __init__(self, queue, tracknumber = -1, volume = 20):
		self.queue = self.update_queue()
		self.tracknumber = tracknumber
		self.volume = volume
		
		self.playing = False
		self.pause = False
		self.nextTrack = False
		self.queueRandom = False

	def update_queue():
		dirname = os.path.dirname(__file__)
		musicdir = os.path.join(dirname, '../Google/music247')
		queue = [f for f in os.listdir(musicdir)]
		return [musicdir, queue]

	def beginplaying():
		self.audio = audioplayer.AudioPlayer("../Google/music247/test.mp3")
		self.audio.play()

	def pause():
		self.audio.pause()

	def resume():
		self.audio.resume() 

	def next_track():
		self.audio.close()
		self.tracknumber = 

	def mainloop():

play()