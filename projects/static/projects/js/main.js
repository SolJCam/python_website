console.log("scripts are being read");

//fade in my image
$(window).on("load", function (e) {
  $(".me").fadeIn(1e3);
    
  console.log('2ndplz!');
});

//toggle between nav links and buttons based on viewport width
window.matchMedia("(max-width:992px)").matches ? $(".links").toggle() : window.matchMedia('(min-width:993px)').matches ? $(".btn-info").toggle() : null;

// $(document).ready(function() {
//     function o() {
//         const o = [$("#About"), $(".abt"), $("#SkillsExperience"), $(".skills"), $(".xp"), $("#Projects"), $(".p1"), $(".p2"), $(".p3")];
//         for ( const l = 0; l < o.length; l++) o[l].css("display", "inline");
//     }
// })

