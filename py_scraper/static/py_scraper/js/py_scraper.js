console.log("scripts are being read");



$(document).ready(() => {


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

	async function url(url) {
		const response = await fetch(url);
		return response.json();
	}

	function updatePage(wrds, wrdCld, id){
		$('#'+wrdCld).attr('src', '/static/imgs/'+wrdCld+'.png');
		$('#'+wrdCld).load('#'+wrdCld);
		// debugger;
		for(let i=0;i<=4;i++){
			$(`#${id}-${i}`).text(`${wrds[i][0]} : ${wrds[i][1]}`);
			// $(`#${id}-${i}`).text(`${json['stw'][i][0]} : ${json['stw'][i][1]}`);	//herokuS3
			// console.log($(`#${id}-${i}`).text(`${json['stw'][i][0]} : ${json['stw'][i][1]}`), $(`#${id}-${i}`).text());
		}
		// console.log($('#'+wrdCld).attr('src', '/static/imgs/'+wrdCld+'.png')[0], $('#'+wrdCld)[0]);
		console.log(`Success scraping ${wrdCld}!`)
		
		// Deleting files. May be unnecessary in production
		fetch('del_'+id+'_files')
			.then(response => console.log("Delete "+id+" file http response: "+response.status));
	}

	function topWrds(id,stw,wrdCld){
		fetch('top_'+id+'_wrds', {
			method: 'POST',
			credentials: "same-origin",
			headers: {
				"X-CSRFToken": getCookie("csrftoken"),
				'X-Requested-With':'XMLHttpRequest',
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(Array(stw)[0])
		})
		.then(res => { return res.json() })
		.then(wrds => { 
			// debugger
			console.log(wrds);
			try{
				// debugger
				setTimeout(updatePage, 30000, wrds, wrdCld, id);
				// updatePage(wrds, wrdCld, id);
			}catch(error){
				console.log(error);
				alert("Woops! There was an error. Please reload page and try again"); 
			};
		})
		.catch((error)=>{
			fetch('del_'+id+'_files')
				.then(response => console.log("Delete "+id+" file http response: "+response.status))
			console.log(error);
			alert("Woops! There was an error. Please reload page and try again");
		});
	}

	function loadImage(scrape_url, wrdCld, id){

		url(scrape_url)
		.then((stw)=>{
			// debugger
			setTimeout(topWrds, 30000, id, stw, wrdCld);
		});
	}

    $("#scrape_msnbc").click(e=>{
		e.preventDefault();

		loadImage("scrape_msnbc","msnbcwrdcld","msnbc");
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


