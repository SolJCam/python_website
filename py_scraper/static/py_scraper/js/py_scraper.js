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
    fetch("https://textvis-word-cloud-v1.p.rapidapi.com/v1/textToCloud?max_words=200&font=Tahoma&language=en&colors=%255B'%2523375E97'%252C%20'%2523FB6542'%252C%20'%2523FFBB00'%252C%20'%25233F681C'%255D&use_stopwords=true&scaling=0.5&width=800&height=800&text=This%20is%20a%20test.%20I%20repeat%252C%20this%20is%20a%20test.%20We%20are%20only%20testing%20the%20functionality%20of%20this%20api%252C%20nothing%20else.%20End%20of%20test.", {
	"method": "POST",
	"headers": {
		"x-rapidapi-host": "textvis-word-cloud-v1.p.rapidapi.com",
		"x-rapidapi-key": "77632acd7emsh25a7f96161cc49cp19dd85jsnd720e55b6ed1",
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