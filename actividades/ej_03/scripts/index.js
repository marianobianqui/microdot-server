var slider = document.getElementById("myRange");
var output = document.getElementById("ref");
var temp = document.getElementById("temp");
output.innerHTML = slider.value * 30 / 100;

slider.oninput = function() {
  output.innerHTML = this.value * 30 / 100;
  updateTemp(this.value)
}

setInterval(getTemp, 1000)

async function getTemp(){
  const get = await fetch(`/temp`)
  const formatted = await get.json()
  temp.innerHTML = formatted.temperature
}

async function updateTemp(ref){
  fetch(`/update/ref/${ref}`)
}