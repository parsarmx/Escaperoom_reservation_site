let dailyProgram = document.querySelector("#daily-program");
let boxes = document.querySelectorAll(".date-section");
let changecolor = document.querySelectorAll(".date-section")
const responisveofthenav = () => {
  toggleButton.addEventListener('click', () => {
    navbarLinks.classList.toggle('active')
  });
  };
const visiblecalender = () => {
  boxes.forEach(items => {
    items.addEventListener("click",function(){
      dailyProgram.style.display = "block";
    });
  });

};







visiblecalender();
responisveofthenav();













