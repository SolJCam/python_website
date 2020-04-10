console.log("scripts are being read");

//fade in my image and blurb
$(document).ready(function (e) {

  $("#me").fadeIn(2e3);
  $("#blurb").fadeIn(2e3);
  // $("#projects-page").fadeIn(2e3);
    
  console.log('2ndplz!');

  // nav connect link functionality to scroll to social media links
  $('#C').click(function(e){
    e.preventDefault();
    $("#Message")[0].scrollIntoView({ behavior: 'smooth', block: 'center' }); 
  });


  $("#1").css("background-color", "yellow");

  $('#carousel').on('slide.bs.carousel', (relatedTarget) => {
    console.log(relatedTarget);
    let projToHighlight = relatedTarget.relatedTarget.classList[3];
    let arrayProjs = $('.proj_smry');
    let arrayProjsLen = arrayProjs.length;
    // debugger
    for(let i = 0; i < arrayProjsLen; i++){
      if(arrayProjs[i].id == projToHighlight){
        arrayProjs[i].style.backgroundColor = 'yellow';
        if(i == 0 ){
          arrayProjs[3].style.backgroundColor = 'white';
        }else{
          arrayProjs[i-1].style.backgroundColor = 'white';
        }
      }
    }
  });

  $('.proj_smry').hover(
    function(){
      let all_projs = $('.proj_smry')
      for(let i = 0; i < all_projs.length; i++){
        all_projs[i].style.backgroundColor = 'white';
      }
      let projs = $('.carousel-item');
      let proj_array = [];
      for(let i = 0; i < projs.length; i++){
        proj_array.push(projs[i].classList[2]);
      }
      // debugger
      let title = this.children[0].innerText // Keyword 'this' does not work with arrow functions!
      title_index = proj_array.indexOf(title);
      $('#carousel').carousel(title_index);
    },
    ()=>{
      $('#carousel').carousel(title_index);
    }
  );
  
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
      debugger
      var email = "mailto:scameron10@yahoo.com?from="+$('#inputEmail').val()+"&subject="+$('#inputSubject').val()+"&body=<"+$('#inputNameF').val()+" "+$('#inputNameS').val()+"><"+$('#inputEmail').val()+">"+$('#inputMessage').val()+"&target=_top";
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


 
  // nav Project link BASIC functionality to scroll to individual projects
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
  $('#project_link4').click(function(e){
    e.preventDefault();
    $("#project4")[0].scrollIntoView({ behavior: 'smooth', block: 'center' }); 
    console.log("woohoo!!!");
  })
  $('#project_link1').click(function(e){
    e.preventDefault();
    $("#project1")[0].scrollIntoView({ behavior: 'smooth', block: 'center' }); 
    console.log("woohoo!!!");
  })

  // on click, display options to add word to dictionary
  $('#add_word').click(function(e){
    console.log("woohoo!!!");
    e.preventDefault();
    $( "#word" ).slideDown("slow", function() {});
    $('#submit_word').toggle();
    $('#more_defs').toggle();
    $('#cancel').toggle();
  })
  $('#more_defs').click(function(e){
    console.log("woohoo!!!");
    e.preventDefault();
    $( "#definitions" ).slideDown("slow", function() {});
    $('#more_defs').toggle();
  })
  $('#cancel').click(function(e){
    console.log("woohoo!!!");
    e.preventDefault();
    $('[name="word_form"]')[0].reset();
    $( "#word" ).slideUp("slow", function() {});
    $( "#definitions" ).slideUp("slow", function() {});
    $("#id_word").css({"border-color":"grey", "border-width": "1px"});
    $("#id_definition").css({"border-color":"grey", "border-width": "1px"});
    if ($('#more_defs').attr("style") == "") {
      $('#more_defs').css('display', 'none');
    }
    $('#submit_word').toggle();
    $('#cancel').toggle();
  })

  // submit user selected suggestions 
  $('.suggestion').click((e)=>{
    e.preventDefault();
    $('#id_Enter_Word').attr("value", e.currentTarget.innerHTML)
    $('#dict_form').submit();
  })


  // highlight unfilled necessary fields when submitting new words
  $('#submit_wrd_btn').click(function(e){
    if($('#id_word').val()==""){
      e.preventDefault();
      alert("Please provide a word");
      $("#id_word").css({"border-color":"red", "border-width": "2px"});
    }
    if($('#id_definition').val()==""){
      e.preventDefault();
      alert("Please provide a definition");
      $("#id_definition").css({"border-color":"red", "border-width": "2px"});
    }
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

  // toggle margin for md/lg viewports
  $('.proj_smries').toggleClass('ml-4');
  $('.proj-imgs').toggleClass('ml-4');

  //toggle email position; DO NOT REMOVE. Bootstrap works from small to larg views. The below function is the only way to remove this class for larger viewports  
  $(".email").toggleClass('mr-3 ml-3');

}




if (window.matchMedia("(max-width:992px)").matches) {

  // toggle class on navbar to prevent hamburger bug
  $("#navbarSupportedContent").toggleClass("d-flex");

  // toggle project image sizes on small viewports
  $(".proj-img").toggleClass("h-100");
}