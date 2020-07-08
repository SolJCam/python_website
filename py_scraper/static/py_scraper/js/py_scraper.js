$(document).ready(() => {

	console.log("scripts are being read");
	counter = null;
	dwnldngImg = null;
	
	// only seems to work when written as async function
	async function fetchScraperUrl(url) {
		const response = await fetch(url);
		return response.json();
	}


	// code to acquire the CSRF cookie token to post
	function getCookie(name) {
	//   var cookieValue = null;
	  let cookieValue = null;
	  if (document.cookie && document.cookie !== '') {
		//   var cookies = document.cookie.split(';');
		  let cookies = document.cookie.split(';');
		  for (var i = 0; i < cookies.length; i++) {
			//   var cookie = cookies[i].trim();
			  let cookie = cookies[i].trim();
			  // Does this cookie string begin with the name we want?
			  if (cookie.substring(0, name.length + 1) === (name + '=')) {
				  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				  break;
			  }
		  }
	  }
	  return cookieValue;
	}


	function dwnldImg(id,wrdCld){
		fetch(id+'_img')
		.then(response => {
			// debugger
			if(response.status == 200){
				console.log(id+" img file http response: "+response.status)
				$('#'+wrdCld).attr('src', '/static/imgs/'+wrdCld+'.png');
				counter = null
				clearTimeout(dwnldngImg);
				// Deleting files. May be unnecessary in production
				// fetch('del_'+id+'_files')
				// .then(response => console.log("Delete "+id+" file http response: "+response.status+", Counter: "+counter));
			}else if(response.status == 500 && counter < 6){
				// debugger
				counter += 1
				dwnldngImg = setTimeout(dwnldImg,30000,id,wrdCld);
				console.log(id+" img file http response: "+response.status+". Counter: "+counter+" clearTimeout id: "+dwnldngImg);
			}else{
				console.log("Sorry, wrdcloud img failed to generate. Please refresh page and try again")
				alert("Sorry, "+wrdCld+" img failed to generate. Please refresh page and try again")
				counter = null
			}      
		})
	}


	function runScraper(scrape_url, wrdCld, id){
		fetchScraperUrl(scrape_url)
		.then((stw)=>{
			// debugger
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
                // console.log(wrds);
                try{
					dwnldImg(id,wrdCld);
                    for(let i=0;i<=4;i++){
                        $(`#${id}-${i}`).text(`${wrds[i][0]} : ${wrds[i][1]}`);
                        // $(`#${id}-${i}`).text(`${json['stw'][i][0]} : ${json['stw'][i][1]}`);	//herokuS3
                    }
                    console.log(`Success scraping ${wrdCld}!`);
                }catch(error){
                    console.log(error);
                    alert("Woops! There was an error. Please reload page and try again"); 
                }
			})
            .catch((error)=>{
                console.log(error);
                alert("Woops! There was an error. Please reload page and try again");
            });
		});
	}




    $("#scrape_msnbc").click(e=>{
		e.preventDefault();

		runScraper("scrape_msnbc","msnbcwrdcld","msnbc");
	})


    $("#scrape_cnn").click(e=>{
		e.preventDefault();
		
		runScraper("scrape_cnn","cnnwrdcld","cnn");
	})
	

    $("#scrape_fox").click(e=>{
		e.preventDefault();
		
		runScraper("scrape_fox","foxwrdcld","fox");
	})

})

