console.log("scripts are being read");

//fade in my image
$(window).on("load", function (e) {
  $(".me").fadeIn(2e3);
    
  console.log('2ndplz!');
});

//toggle between nav links and buttons based on viewport width
window.matchMedia("(max-width:992px)").matches ? $(".pills").toggle() : window.matchMedia('(min-width:993px)').matches ? $(".btn-info").toggle() : null;


//nav link animated display
if (window.matchMedia("(min-width:992px)").matches) {
  $(".pills").hover(  
        function(){
          $(".nav-item").toggleClass('d-lg-none');
          $(".nav-img").toggleClass('d-lg-block');
      }, function(){
          $(".nav-item").toggleClass('d-lg-none');
          $(".nav-img").toggleClass('d-lg-block');
      });
}
