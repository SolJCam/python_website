console.log("scripts are being read");



$(document).ready(() => {

	scraped_file = '';


  	// code to acquire the CSRF cookie token to post
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
	
	// testing for posting s3 data to amazon
	
	$("#s3_upload").click(e=>{
		e.preventDefault();
		// fetch(request)
		fetch('s3_upload', {
			method: 'POST',
			credentials: "same-origin",
			headers: {
			  "X-CSRFToken": getCookie("csrftoken"),
			  'X-Requested-With':'XMLHttpRequest',
			  'Content-Type': 'application/json',
			},
			body: JSON.stringify("msnbcnews.txt")
		})
		.then(response => {
			// console.log(response);
			// debugger
			return response.json();
		})
		.then(data => {
			// debugger
			return data;
		})
		.then(s3data => {
			// Retrieving txt files. For some reason this only worked after creating an async function
			fetch_file('fetch_MSNBC_file').then(file => { console.log(file); scraped_file = file; return scraped_file}).catch((error)=>{ console.log(error+" : Something went wrong"); });
			console.log('fetch_MSNBC_file: '+scraped_file);
			debugger
			return s3data
		})
		.catch((error)=>{
			console.log(error);
			alert("Woops! There was an error. Please reload page and try again");
		});
		console.log(scraped_file); 
	})
	


	async function fetch_file(url) {
		// debugger
		const response = await fetch(url);
		return await response.blob();
	}

	async function url(url) {
		const response = await fetch(url);
		const data = await response.json();
		return data
	}

	function loadImage(scrape_url, wrdCld, file_url, id){

		url(scrape_url)
			.then((json)=>{
				// debugger
				try{
					// debugger
					$('#'+wrdCld).attr('src', '/static/imgs/'+wrdCld+'.png');
					$('#'+wrdCld).load('#'+wrdCld);
					if ($('#'+wrdCld)[0].width != 0 || $('#'+wrdCld)[0].width != 147){
						for(let i=0;i<=4;i++){
							$(`#${id}-${i}`).text(`${json['t5w'][i][0]} : ${json['t5w'][i][1]}`);
							// console.log($(`#${id}-${i}`).text(`${json['t5w'][i][0]} : ${json['t5w'][i][1]}`), $(`#${id}-${i}`).text());
						}
						// console.log($('#'+wrdCld).attr('src', '/static/imgs/'+wrdCld+'.png')[0], $('#'+wrdCld)[0]);
						console.log(`Success scraping ${wrdCld}!`)

						// Retrieving txt files. For some reason this only worked after creating an async function
						// fetch_file(file_url).then(file => { console.log(file); scraped_file = file; return scraped_file}).catch((error)=>{ console.log(error+" : Something went wrong"); });
						// console.log(file_url+" : "+scraped_file);
						
						debugger
						// Deleting files. May be unnecessary in production
						fetch('del_'+id+'_files')
							.then(response => console.log("Delete "+id+" file http response: "+response.status))
					}else{
						console.log(`Failure scraping ${wrdCld}!`);
						// setTimeout(url, 180000, scrape_url)
					}
				}catch(error){
					console.log(error);
					// alert("Woops! There was an error. Please reload page and try again"); 
				};
			})
			.catch((error)=>{
				console.log(error);
				alert("Woops! There was an error. Please reload page and try again");
			});
	}

    $("#scrape_msnbc").click(e=>{
		e.preventDefault();

		loadImage("scrape_msnbc","msnbcwrdcld","fetch_MSNBC_file","ms");
	})


    $("#scrape_cnn").click(e=>{
		e.preventDefault();
		
		loadImage("scrape_cnn","cnnwrdcld","fetch_CNN_file","cnn");
	})
	

    $("#scrape_fox").click(e=>{
		e.preventDefault();
		
		loadImage("scrape_fox","foxwrdcld","fetch_FOX_file","fox");
	})
})


