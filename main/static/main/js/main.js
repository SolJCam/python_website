console.log("scripts are being read");

//fade in my image and blurb
$(document).ready(function (e) {

  $("#me").fadeIn(2e3);
  $("#blurb").fadeIn(2e3);
  // $("#projects-page").fadeIn(2e3);
    
  console.log('2ndplz!');


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


 
  // nav project link BASIC functionality to scroll to individual projects
  $('#project_link2').click(function(e){
    e.preventDefault();
    $("#project2")[0].scrollIntoView({ behavior: 'smooth', block: 'center' }); 
    console.log("woohoo!!!");
  })
  $('#project_link3').click(function(e){
    e.preventDefault();
    $("#project3")[0].scrollIntoView({ behavior: 'smooth', block: 'center' }); 
    console.log("woohoo!!!");
  })


  // display options to add word to dictionary
  $('#add_word').click(function(e){
    console.log("woohoo!!!");
    e.preventDefault();
    $( "#new_word" ).slideDown("slow", function() {
      // Animation complete.
    });
  })


  // SHOULD WORK ONCE "CLICK" EVENT IS SORTED OUT

  // function setValue(){
  //   $('#id_Enter_Word').attr("value", this.innerHTML)
  //   $('#dict_form').submit();
  // }
  
  // BREAKS CODE

  // $('.suggestion').on("click", setValue())

  // WORKS FOR FIRST SUGGESTION ONLY
  $('.suggestion').click((e)=>{
    console.log("hittin\'");
    e.preventDefault();
    // for(let i=0;i<=$('.suggestion').length;i++){
      $('#id_Enter_Word').attr("value", $('.suggestion')[0].innerHTML)
      $('#dict_form').submit();
    // }
  })


  // return button behavior
  let thirty; let scroll;

  window.onscroll =   () => { 
    thirty = $('body').height() * .3; 
    scroll = window.scrollY; 
    if(scroll >= thirty) {
      // console.log(`${scroll} and ${thirty}`);
      $("#return-btn").css("visibility", "visible");
    }else{
      $("#return-btn").css("visibility", "hidden");
    }
  }

  $("#return-btn").click(function(e){
    $("#title")[0].scrollIntoView({ behavior: 'smooth', block: 'center' });
  });

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
      $("#proj-link").toggleClass('d-lg-block');
    },
    function(){
      $("#P").toggleClass('d-lg-none');
      $("#proj-link").toggleClass('d-lg-block');
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
    }, 500)
  });

  //toggle email position; DO NOT REMOVE. Bootstrap works from small to larg views. The below function is the only way to remove this class for larger viewports  
  $(".email").toggleClass('mr-3 ml-3');

}




if (window.matchMedia("(max-width:992px)").matches) {
  
  // nav connect link functionality to scroll to social media links on small viewports: wip
  $('#C').click(function(e){
    e.preventDefault();
    $("html,body").animate({
      scrollTop: 964
    }, 215)
  });

  // nav project link BASIC functionality to scroll to individual projects on small viewports
  // $('#C').click(function(e){
  //   e.preventDefault();
  //   $("html,body").animate({
  //     scrollTop: 1655
  //   }, 215)
  // });
}