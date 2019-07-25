console.log("scripts are being read");

//fade in my image and blurb
$(window).on("load", function (e) {
  $("#me").fadeIn(2e3);
  $("#blurb").fadeIn(2e3);
    
  console.log('2ndplz!');
});
 
if (window.matchMedia("(min-width:992px)").matches) {

  //shift name and nav depending on screen size
  $(".two").toggleClass("offset-sm-1");
  $(".two").toggleClass("offset-sm-2");

  //nav links animated display
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
  
// toggle img layout
  $('#me').toggleClass("float-right")

}