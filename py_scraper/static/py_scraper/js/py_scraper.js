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
    fetch("https://textvis-word-cloud-v1.p.rapidapi.com/v1/textToCloud", {
	"method": "POST",
	"headers": {
		"x-rapidapi-host": "textvis-word-cloud-v1.p.rapidapi.com",
		"x-rapidapi-key": "b61f4c9fc0msh384299504cd20a5p19e082jsnede2583ed2ed",
		"x-api-key": "qLn10OtYwY8MILjfYAIH11rx6yVWaGMOUNh0NZQh",
		"content-type": "application/json",
		"accept": "application/json"
	},
	"body": {
		"text": "This is a test. I repeat, this is a test. We are only testing the functionality of this api, nothing else. End of test.",
		"scale": 0.5,
		"width": 800,
		"height": 800,
		"colors": [
			"#375E97",
			"#FB6542",
			"#FFBB00",
			"#3F681C"
		],
		"font": "Tahoma",
		"use_stopwords": true,
		"language": "en",
		"uppercase": false
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
        // debugger
    })
})