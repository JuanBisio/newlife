// Reemplaza $(".open") con document.querySelector(".open")
// Reemplaza $(".c-hamburger") con document.querySelectorAll(".c-hamburger")

var toggles = document.querySelectorAll(".c-hamburger");

for (var i = toggles.length - 1; i >= 0; i--) {
  var toggle = toggles[i];
  toggleHandler(toggle);
}

function toggleHandler(toggle) {
  toggle.addEventListener("click", function (e) {
    e.preventDefault();
    if (this.classList.contains("is-active") === true) {
      this.classList.remove("is-active");
      document.querySelector(".open").classList.remove("oppenned");
    } else {
      this.classList.add("is-active");
      document.querySelector(".open").classList.add("oppenned");
    }
  });
}

document.querySelectorAll(".sub-menu li a").forEach(function (element) {
  element.addEventListener("click", function (event) {  
    document.querySelector(".open").classList.remove("oppenned");
    document.querySelectorAll(".c-hamburger").forEach(function (toggle) {
      toggle.classList.remove("is-active");
    });
  });
});
