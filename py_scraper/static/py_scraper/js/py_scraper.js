console.log("scripts are being read");


$(document).ready(e => {
    $("#scrape").click(e=>{
        e.preventDefault();

		$.ajax(settings).done(function (response) {
			// debugger
			console.log(response);
			$("#wordcloud").attr("src", response['url']);
		});
    })
})


