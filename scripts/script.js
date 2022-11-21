const bar = document.getElementById("bar");
const close = document.getElementById("close");
const nav = document.getElementById("navbar");
const mobileNav = document.getElementById("mobile-nav")

// Mobil Navbar Menu open-close

if (bar) {
  bar.addEventListener("click", () => {
    showMobileNavItems()
  })
}

if (close) {
  close.addEventListener("click", () => {
    nav.classList.remove("active");
  });
}

function showMobileNavItems() {
  console.log("hello!");
  nav.classList.add("active");
  const homeLink = document.createElement('a');
  homeLink.href = "../templates/index.html";
  homeLink.text = "Home";
  mobileNav.appendChild(homeLink);
}