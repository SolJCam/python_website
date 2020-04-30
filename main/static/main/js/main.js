console.log("scripts are being read");

//fade in my image and blurb
$(document).ready(function (e) {

  $("#me").fadeIn(2e3);
  $("#blurb").fadeIn(2e3);
  // $("#projects-page").fadeIn(2e3);
    
  console.log('2ndplz!');

  // acquire the CSRF token cookie token
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');

  // function to launch Resume pdf file
  function launchPdf (){
    pdfjsLib.getDocument("assets/Software Developer Resume 5_16.pdf")
    .promise.then(pdfDoc => { 
        // debugger 
        // Load information from the first page.
        const page = pdfDoc.getPage(1);
        console.log(pdfDoc); // should be resolved
        console.log(page); // should be a promise
        return page; 
    })
    .then(page => {
        // debugger 
        console.log(page); // should now be resolved
    
        const scale = 1;
        const viewport = page.getViewport({scale});
    
        // Apply page dimensions to the <canvas> element.
        const canvas = document.getElementById("pdf");
        const context = canvas.getContext("2d");
        canvas.height = viewport.height;
        canvas.width = viewport.width;
    
        // Render the page into the <canvas> element.
        const renderContext = {
            canvasContext: context,
            viewport: viewport
        };
        // page.render(renderContext);

        const pageCtxt = [
            page,
            renderContext
        ]
        return pageCtxt;
    })
    .then(pageCtxt => {
        debugger
        pageCtxt[0].render(pageCtxt[1]);
    })
    .catch(err => {
        // Display error
        console.log(err);
    });
};

// execute pdf function on click
$("#R").click(launchPdf);
    
  // nav connect link functionality to scroll to social media links
  $('#C').click(function(e){
    e.preventDefault();
    $("#Message")[0].scrollIntoView({ behavior: 'smooth', block: 'center' }); 
  });

  // carousel synced-image-info behavior
  $("#1").css("background-color", "yellow");

  $('#carousel').on('slide.bs.carousel', (relatedTarget) => {
    // console.log(relatedTarget);
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

  // carousel hover behavior
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
  

  // resume pdf format rendering
  // $('#R').click(function(e){
  //   e.preventDefault();
  //   (async () => {
  //     $("#pdf-cont").toggleClass('display')
  //     debugger
  //     const loadingTask = pdfjsLib.getDocument("/main/static/main/js/DevRes.pdf");
  //     // const loadingTask = PDFJS.getDocument("/Software Developer Resume 5_18.pdf");
  //     const pdf = await loadingTask.promise;
    
  //     // Load information from the first page.
  //     const page = await pdf.getPage(1);
    
  //     const scale = 1;
  //     const viewport = page.getViewport(scale);
    
  //     // Apply page dimensions to the <canvas> element.
  //     const canvas = document.getElementById("pdf");
  //     const context = canvas.getContext("2d");
  //     canvas.height = viewport.height;
  //     canvas.width = viewport.width;
    
  //     // Render the page into the <canvas> element.
  //     const renderContext = {
  //       canvasContext: context,
  //       viewport: viewport
  //     };
  //     await page.render(renderContext);
  //     console.log("Page rendered!");
  //   })();
  // })


  //Email submission functionality
  $('#submit').click(function(e){
    e.preventDefault();
    if($('#inputNameF').val()==""){
      alert("Please provide a name");
      $("#inputNameF").css({"border-color":"red", "border-width": "3px"});
    }else if($('#inputEmail').val()==""){
      $("#inputEmail").css({"border-color":"red", "border-width": "3px"});
      alert("Please provide an email");
    }else if($('#inputSubject').val()==""){
      $("#inputSubject").css({"border-color":"red", "border-width": "3px"});
      alert("Please provide a subject");
    }else if($('#inputMessage').val()==""){
      $("#inputMessage").css({"border-color":"red", "border-width": "3px"});
      alert("Please provide a message");
    }else{
      var email = {"Subject":$('#inputSubject').val(), "Body": [$('#inputEmail').val(), $('#inputNameF').val()+" "+$('#inputNameS').val(), $('#inputMessage').val()]};
      // debugger; 
      fetch('/', {
        method: 'POST',
        credentials: "same-origin",
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
          'X-Requested-With':'XMLHttpRequest',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(email),
      })
      .then(response => {return response.json()})
      .then(data => {
        console.log('Success:', data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
      
      // $(this).unbind('click').click();
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