$(document).ready(function(){
  $("html").niceScroll({
    scrollspeed: 30, // scrolling speed
    mousescrollstep: 30 // scrolling speed with mouse wheel (pixel)
  });
  new WOW().init();
});
