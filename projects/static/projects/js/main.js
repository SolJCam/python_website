console.log("scripts are being read");

//fade in my image and blurb
$(document).ready(function (e) {

  // create id's for project nav link and parallax scroll behavior
  for(let i=0;i<=$(".parallax").length;i++){
    $(".parallax").eq(i).attr("id", `#projects${i}`); // learn about the eq() method here: https://api.jquery.com/eq/
    $(".proj-nav").eq(i).attr("id", `#proj-nav${i}`);
  }

  $("#me").fadeIn(2e3);
  $("#blurb").fadeIn(2e3);
    
  console.log('2ndplz!');
  
});


 



if (window.matchMedia("(min-width:992px)").matches) { 

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

  // nav connect link functionality to scroll to social media links on large viewports
  $('#C').click(function(e){
    e.preventDefault();
    $("html,body").animate({
      scrollTop: 1655
    }, 215)
  });

  //toggle email position; DO NOT REMOVE. Bootstrap works from small to larg views. The below function is the only way to remove this class for larger viewports  
  $(".email").toggleClass('mr-3 ml-3');

 
  // nav project link functionality to scroll to individual projects on large viewports
  $('#C').click(function(e){
    e.preventDefault();
    $("html,body").animate({
      scrollTop: 1655
    }, 215)
  });
  
  
  // PROJECT PAGE parallax behavior here
  $(window).on('scroll', function(){

    if (window.matchMedia('(min-width:900px)').matches){  

      // console.log("it's hittin")
      const scrolled = $(window).scrollTop();
      $('.parallax').css('top', 0 - scrolled);

    }
  })

}




if (window.matchMedia("(max-width:992px)").matches) {
  
  // nav connect link functionality to scroll to social media links on small viewports
  $('#C').click(function(e){
    e.preventDefault();
    $("html,body").animate({
      scrollTop: 964
    }, 215)
  });

  // nav project link functionality to scroll to individual projects on small viewports
  // $('#C').click(function(e){
  //   e.preventDefault();
  //   $("html,body").animate({
  //     scrollTop: 1655
  //   }, 215)
  // });
}








//Email submission functionality
$('#submit').click(function(e){
  if($('#inputNameF').val()==""){
    e.preventDefault();
    alert("Please provide a name");
    $("#inputNameF").css({"border-color":"red", "border-width": "3px"});
  }else if($('#inputEmail').val()==""){
    e.preventDefault();
    $("#inputEmail").css({"border-color":"red", "border-width": "3px"});
    alert("Please provide an email");
  }else if($('#inputSubject').val()==""){
    e.preventDefault();
    $("#inputSubject").css({"border-color":"red", "border-width": "3px"});
    alert("Please provide a subject");
  }else if($('#inputMessage').val()==""){
    e.preventDefault();
    $("#inputMessage").css({"border-color":"red", "border-width": "3px"});
    alert("Please provide a message");
  }else{
    var email = "mailto:scameron10@yahoo.com?from="+$('#inputEmail').val()+"&subject="+$('#inputSubject').val()+"&body=<"+$('#inputNameF').val()+" "+$('#inputNameS').val()+"><"+$('#inputEmail').val()+">"+$('#inputMessage').val();
    var href = email.replace(/ /g, "%20");
    console.log(href);
    $("#email").attr("action", href);
  }
});







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
);

$("#second").hover(
  function(){
    $("#first").fadeTo("fast", 0.3);
    $("#third").fadeTo("fast", 0.3);
  },
  function(){
    $("#first").fadeTo("fast", 1);
    $("#third").fadeTo("fast", 1);
  }
);

$("#third").hover(
  function(){
    $("#first").fadeTo("fast", 0.3);
    $("#second").fadeTo("fast", 0.3);
  },
  function(){
    $("#first").fadeTo("fast", 1);
    $("#second").fadeTo("fast", 1);
  }
);

// Not sure if this code is necessary. Browser resize suggests yes, Chrome dev tools suggests no. Will know after deployment

// if (window.matchMedia("(max-width:992px)").matches) {
//   $("#myname").toggleClass('offset-3');
//   $("#mydevtype").toggleClass('offset-3');
//   $(".pills").toggleClass('offset-2 mt-5');
// }