function onLoad() {
	volume_span = document.getElementById("volume_span")
	console.log(volume_span)
};

onLoad()

window.onload = function(){
	volume_span = document.getElementById("volume_span")
	console.log(volume_span)

	volumeRange = document.getElementById("volumeRange")
	volumeRange.addEventListener("change", function(){
		volume_span.innerText = volumeRange.value

	})
};