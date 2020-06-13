console.log("scripts are being read");



$(document).ready(() => {

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

	function loadImage(scrape_url, wrdCld, id){

		url(scrape_url)
			.then((json)=>{
				// debugger
				try{
					// debugger
					$('#'+wrdCld).attr('src', '/static/imgs/'+wrdCld+'.png');
					$('#'+wrdCld).load('#'+wrdCld);
					if ($('#'+wrdCld)[0].width != 0 || $('#'+wrdCld)[0].width != 147){
						for(let i=0;i<=4;i++){
							$(`#${id}-${i}`).text(`${json[i][0]} : ${json[i][1]}`);
							// $(`#${id}-${i}`).text(`${json['t5w'][i][0]} : ${json['t5w'][i][1]}`);	//herokuS3
							// console.log($(`#${id}-${i}`).text(`${json['t5w'][i][0]} : ${json['t5w'][i][1]}`), $(`#${id}-${i}`).text());
						}
						// console.log($('#'+wrdCld).attr('src', '/static/imgs/'+wrdCld+'.png')[0], $('#'+wrdCld)[0]);
						console.log(`Success scraping ${wrdCld}!`)
						
						// debugger
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
				fetch('del_'+id+'_files')
					.then(response => console.log("Delete "+id+" file http response: "+response.status))
				console.log(error);
				alert("Woops! There was an error. Please reload page and try again");
			});
	}

    $("#scrape_msnbc").click(e=>{
		e.preventDefault();

		loadImage("scrape_msnbc","msnbcwrdcld","ms");
	})


    $("#scrape_cnn").click(e=>{
		e.preventDefault();
		
		loadImage("scrape_cnn","cnnwrdcld","cnn");
	})
	

    $("#scrape_fox").click(e=>{
		e.preventDefault();
		
		loadImage("scrape_fox","foxwrdcld","fox");
	})
})


