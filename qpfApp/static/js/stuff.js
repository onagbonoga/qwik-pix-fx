
var x = 2 //x is the value the width and height of the image will be divided by
function drawImage(){
	
	var imageContainer = document.getElementById("imageContainer");
	imageContainer.style.display = "none"
	var c = document.getElementById("myCanvas");
  	var ctx = c.getContext("2d");
  	var img = document.getElementById("myImage");
  	ctx.drawImage(img,5,5, img.width/x, img.height/x);
}

function ZoomOut(){
	//drawImage(5,5,2,2)
	var canvas = document.getElementById("myCanvas");
	const ctx = canvas.getContext('2d');
	ctx.clearRect(0, 0, canvas.width, canvas.height);
	x = x + 0.3;
	drawImage();
}

function ZoomIn(){
	var canvas = document.getElementById("myCanvas");
	const ctx = canvas.getContext('2d');
	ctx.clearRect(0, 0, canvas.width, canvas.height);
	x = x - 0.3;
	drawImage();
}