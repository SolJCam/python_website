console.log("scripts are being read");

//fade in my image and blurb
$(document).ready(function (e) {
  $("#me").fadeIn(2e3);
  $("#blurb").fadeIn(2e3);
    
  console.log('2ndplz!');
});


 



if (window.matchMedia("(min-width:992px)").matches) {

  //toggle email position; DO NOT REMOVE. Bootstrap works from small to larg views. The below function is the only way to remove this class for larger viewports  
  $(".email").toggleClass('mr-3 ml-3'); 

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
      $("#C").toggleClass('d-lg-none');
      $("#conn-nav").toggleClass('d-lg-block');
    },
    function(){
      $("#C").toggleClass('d-lg-none');
      $("#conn-nav").toggleClass('d-lg-block');
    }
  );

// toggle nav link width. Doesn't have breakpoint support
  $("#resume-nav").toggleClass("no-gutters");
  $("#project-nav").toggleClass("no-gutters");
  $("#connect-nav").toggleClass("no-gutters");

}






//Social Media Link Behaviour
$("#first").hover(
  function(){
    $("#second").fadeTo("fast", 0.3);
    $("#third").fadeTo("fast", 0.3);
  },
  function(){
    $("#second").fadeTo("fast", 1);
    $("#third").fadeTo("fast", 1);
  }
)

$("#second").hover(
  function(){
    $("#first").fadeTo("fast", 0.3);
    $("#third").fadeTo("fast", 0.3);
  },
  function(){
    $("#first").fadeTo("fast", 1);
    $("#third").fadeTo("fast", 1);
  }
)

$("#third").hover(
  function(){
    $("#first").fadeTo("fast", 0.3);
    $("#second").fadeTo("fast", 0.3);
  },
  function(){
    $("#first").fadeTo("fast", 1);
    $("#second").fadeTo("fast", 1);
  }
)

// Not sure if this code is necessary. Browser resize suggests yes, Chrome dev tools suggests no. Will know after deployment

// if (window.matchMedia("(max-width:992px)").matches) {
//   $("#myname").toggleClass('offset-3');
//   $("#mydevtype").toggleClass('offset-3');
//   $(".pills").toggleClass('offset-2 mt-5');
// }