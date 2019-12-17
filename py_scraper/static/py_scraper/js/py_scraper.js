console.log("scripts are being read");

// async function scrapeNews(){
//     let cnnResponse = await fetch(){

//     };

//     let msnbcResponse = await fetch(){

//     };

//     let foxResponse = await fetch(){

//     };
// }

function generateCloud (){
    fetch("https://wordcloudservice.p.rapidapi.com/generate_wc", {
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
			"s_max": "7",
			"s_min": "1",
			"f_min": 1,
			"r_color": "TRUE",
			"r_order": "TRUE",
			"s_fit": "FALSE",
			"fixed_asp": "TRUE",
			"rotate": "TRUE",
			"textblock": "generate word cloud generate word cloud awesome great png jpg pdf awesome generate word cloud"
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