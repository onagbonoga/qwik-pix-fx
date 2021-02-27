
var x = 2 //x is the value the width and height of the image will be divided by
lename = "placeholder filename"
function drawImage(filename){
	lename = filename
	f_name = "http://127.0.0.1:5000/static/pictures/".concat(filename)
	
	
	var imageContainer = document.getElementById("imageContainer");
	imageContainer.style.display = "none"
	var c = document.getElementById("myCanvas");
  	var ctx = c.getContext("2d");
  	
  	//trying to load the image so it dosent cache
  	var d = new Date(); 
  	var f_name= f_name + '?timestamp='+d.getTime(); //the timestamp is added so js reloads the image each time and wont use the cached version

  	console.log(f_name)
  	var img = new Image()
  	img.src = f_name
  	img.onload = function(){ //wait for image to load before drawing 
  		ctx.drawImage(img,5,5, img.width/x, img.height/x);
  	}
}

function ZoomOut(){
	
	var canvas = document.getElementById("myCanvas");
	const ctx = canvas.getContext('2d');
	ctx.clearRect(0, 0, canvas.width, canvas.height);
	x = x + 0.1;
	drawImage(lename);
}

function ZoomIn(){
	var canvas = document.getElementById("myCanvas");
	const ctx = canvas.getContext('2d');
	ctx.clearRect(0, 0, canvas.width, canvas.height);
	x = x - 0.1;
	drawImage(lename);
}

//function to make the scroll wheel zoom the image
function scrollZoom(){
	document.getElementById("myCanvas").addEventListener("wheel",function(canvasZoom)
{
	canvasZoom.preventDefault();
	if (canvasZoom.deltaY < 0)
	{
		ZoomIn();
	}
	else if (canvasZoom.deltaY > 0)
	{
		ZoomOut();
	}
});
}

function edit(selection){
	//make request to server to modify image
	var http = new XMLHttpRequest();
	var str1 = "http://127.0.0.1:5000/edit/";
	var str2 = selection.toString()
	var url = str1.concat(str2);
	console.log(url);
	//if the server already processed the request

	http.onreadystatechange = function(){
		if (this.readyState == 4 && this.status == 200){
		console.log(this.responseText);
		drawImage(lename)
		drawImage(lename)
		}
	}
	http.open("GET", url);
	http.send();

	//draw image
	drawImage(lename)
	drawImage(lename)
}