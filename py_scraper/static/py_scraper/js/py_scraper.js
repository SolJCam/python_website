console.log("scripts are being read");

// async function scrapeNews(){
//     let cnnResponse = await fetch(){

//     };

//     let msnbcResponse = await fetch(){

//     };

//     let foxResponse = await fetch(){

//     };
// }

async function generateCloud (){
	
	await fetch("https://wordcloudservice.p.rapidapi.com/generate_wc", {
		"method": "POST",
		"headers": {
			"x-rapidapi-host": "wordcloudservice.p.rapidapi.com",
			"x-rapidapi-key": "b61f4c9fc0msh384299504cd20a5p19e082jsnede2583ed2ed",
			"content-type": "application/json",
			"accept": "application/json"
		},
		"body": {
			"f_type": "png",
			"width": 800,
			"height": 500,
			"s_max": "4",
			"s_min": ".5",
			"f_min": 3,
			"r_color": "TRUE",
			"r_order": "FALSE",
			"s_fit": "FALSE",
			"fixed_asp": "TRUE",
			"rotate": "TRUE",
			"url": "https://en.wikipedia.org/wiki/Canada",
			"remove_words": "canada canadian original archived"
		}
	})
	.then(response => {
		console.log(response);
	})
	.catch(err => {
		console.log(err);
	});
}

$(document).ready(e => {
    $("#scrape").click(e=>{
        e.preventDefault();
		let cloud = generateCloud();
		console.log(cloud);
		// debugger
		// $("#wordcloud").attr("src", cloud);
    })
})


