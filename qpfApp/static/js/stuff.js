/*let canvas = document.getElementById('canvas')
let img = document.getElementById('img')

img.onload = function(){

	let x = -(img.width - canvas.offsetWidth)/2+"px"
	let y = -(img.height - canvas.offsetHeight)/2 + "px"
	console.log(x, "$$$$");
	console.log(y, "$$$$");
	let ratio = canvas.offsetWidth/img.width
	console.log(ratio, "$$$$");

	img.style.transform = `translate(${x}, ${y}) scale(${ratio})`
}*/
function drawImage(){
	var imageContainer = document.getElementById("imageContainer");
	imageContainer.style.display = "none"

	var c = document.getElementById("myCanvas");
  	var ctx = c.getContext("2d");
  	var img = document.getElementById("myImage");
  	ctx.drawImage(img,5,5, img.width/2, img.height/2);
}