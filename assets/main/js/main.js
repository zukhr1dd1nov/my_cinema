var today = new Date();
var dd = today.getDate();
var mm = today.getMonth()+1; //January is 0 so need to add 1 to make it 1!
var yyyy = today.getFullYear();
if(dd<10){
  dd='0'+dd
}
if(mm<10){
  mm='0'+mm
}

today = yyyy+'-'+mm+'-'+dd;
document.getElementById("date").setAttribute("min", today);


var myCarousel = document.querySelector('#carouselExampleFade')
var carousel = new bootstrap.Carousel(myCarousel, {
  interval: 2000,
  wrap: false
})
