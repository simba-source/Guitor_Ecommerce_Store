const bar = document.getElementById("bar");
const close = document.getElementById("close");
const nav = document.getElementById("navbar");

// Mobil Navbar Menu open-close

if (bar) {
  bar.addEventListener("click", () => {
    nav.classList.add("active");
  });
}

if (close) {
  close.addEventListener("click", () => {
    nav.classList.remove("active");
  });
}

// Single Page- change to images

const mainImage = document.getElementById("MainImage");
const smallImage = document.getElementsByClassName("small-img");

function click1() {
  mainImage.src = smallImage[0].src;
  smallImage[0].classList.add("focus");
  smallImage[1].classList.remove("focus");
  smallImage[2].classList.remove("focus");
  smallImage[3].classList.remove("focus");
}

function click2() {
  mainImage.src = smallImage[1].src;
  smallImage[1].classList.add("focus");
  smallImage[0].classList.remove("focus");
  smallImage[2].classList.remove("focus");
  smallImage[3].classList.remove("focus");
}

function click3() {
  mainImage.src = smallImage[2].src;
  smallImage[2].classList.add("focus");
  smallImage[1].classList.remove("focus");
  smallImage[0].classList.remove("focus");
  smallImage[3].classList.remove("focus");
}

function click4() {
  mainImage.src = smallImage[3].src;
  smallImage[3].classList.add("focus");
  smallImage[1].classList.remove("focus");
  smallImage[2].classList.remove("focus");
  smallImage[0].classList.remove("focus");
}