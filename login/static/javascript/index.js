// Select of elements from DOM
const burgerIcon = document.querySelector("#burger");
const navbarMenu = document.querySelector("#nav-link");

// Add a clic from menu icon (burgerIcon)
burgerIcon.addEventListener("click", () => { 
    // Toggle "is-active" class in navigation menu
    navbarMenu.classList.toggle("is-active");
});