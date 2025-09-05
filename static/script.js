let images = ["/static/ocean.png", "/static/ocean2.png"];
let index = 0;
let score = 0;
let roundCount = 0;
let scoreVal = document.getElementById("scoreVal");

setInterval(() => {
    index = (index + 1) % images.length;
    document.getElementById("giantBox").style.backgroundImage = `url(${images[index]})`;
}, 1000); // switch every 500ms

async function loadLinks() {
  let res = await fetch("/get-links");
  let links = await res.json(); // [["real","https://..."], ["fake","http://..."]]

  document.querySelectorAll(".fish").forEach((fish, i) => {
    fish.dataset.type = links[i][0]; // "real" or "fake"
    fish.querySelector(".link-text").innerText = links[i][1];
  });
}

document.querySelectorAll(".fish").forEach(fish => {
  fish.addEventListener("click", () => {
    if (fish.dataset.type === "real") {
      alert("✅ Correct! That’s the real site.");
      score += 1;
      scoreVal.innerText = score;
    } else {
      alert("❌ Phish! You got tricked.");
    }
    roundCount += 1;
    if (roundCount >= 5) {
      alert(`Game over! Your final score is ${score}/5.`);
      score = 0;
      roundCount = 0;
      scoreVal.innerText = score;
    }
    loadLinks(); // load new round
  });
});

loadLinks(); // start game
