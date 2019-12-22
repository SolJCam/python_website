console.log("scripts are being read");

var settings = {
	"async": true,
	"crossDomain": true,
	"url": "https://wordcloudservice.p.rapidapi.com/generate_wc",
	"method": "POST",
	"headers": {
		"x-rapidapi-host": "wordcloudservice.p.rapidapi.com",
		"x-rapidapi-key": "77632acd7emsh25a7f96161cc49cp19dd85jsnd720e55b6ed1",
		"content-type": "application/json",
		"accept": "application/json"
	},
	"processData": false,
	"data": "{  \"f_type\": \"png\",  \"width\": 800,  \"height\": 500,  \"s_max\": \"4\",  \"s_min\": \".5\",  \"f_min\": 3,  \"r_color\": \"TRUE\",  \"r_order\": \"FALSE\",  \"s_fit\": \"FALSE\",  \"fixed_asp\": \"TRUE\",  \"rotate\": \"TRUE\",  \"url\":\"https://www.npr.org/\",  \"remove_words\":\"\"}"
}


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


