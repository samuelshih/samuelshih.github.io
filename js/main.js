$(document).ready(function(){
  $("html").niceScroll({
    scrollspeed: 30, // scrolling speed
    mousescrollstep: 30, // scrolling speed with mouse wheel (pixel)
    cursorcolor:"#00B277", // Set cursor color
    cursorwidth: "8" // Sety cursor width
  });

  new WOW().init();
});
