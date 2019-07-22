console.log("scripts are being read");

//fade in my image
$(window).on("load", function (e) {
  $(".me").fadeIn(2e3);
    
  console.log('2ndplz!');
});


//toggle between nav links and buttons based on viewport width
// window.matchMedia("(max-width:992px)").matches ? $(".pills").toggle() : window.matchMedia('(min-width:993px)').matches ? $(".btn-info").toggle() : null;


//nav link animated display
if (window.matchMedia("(min-width:992px)").matches) {

  $("#resume-nav").hover(
    function(){
      $("#R").toggleClass('d-lg-none');
      $("#res-nav").toggleClass('d-lg-block');
    },
    function(){
      $("#R").toggleClass('d-lg-none');
      $("#res-nav").toggleClass('d-lg-block');
    }
  );
  $("#project-nav").hover(
    function(){
      $("#P").toggleClass('d-lg-none');
      $("#proj-nav").toggleClass('d-lg-block');
    },
    function(){
      $("#P").toggleClass('d-lg-none');
      $("#proj-nav").toggleClass('d-lg-block');
    }
  );
  $("#connect-nav").hover(
    function(){
      $("#C",).toggleClass('d-lg-none');
      $("#conn-nav").toggleClass('d-lg-block');
    },
    function(){
      $("#C",).toggleClass('d-lg-none');
      $("#conn-nav").toggleClass('d-lg-block');
    }
  );  
}