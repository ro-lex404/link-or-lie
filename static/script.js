let images = ["/static/ocean.png", "/static/ocean2.png"];
let index = 0;
setInterval(() => {
    index = (index + 1) % images.length;
    document.getElementById("giantBox").style.backgroundImage = `url(${images[index]})`;
}, 1000); // switch every 500ms