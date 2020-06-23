console.log("scripts are being read");



$(document).ready(() => {


	// only seems to work when written as async function
	async function fetchScraperUrl(url) {
		const response = await fetch(url);
		return response.json();
	}


	// code to acquire the CSRF cookie token to post
	function getCookie(name) {
	  var cookieValue = null;
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
                console.log(wrds);
                try{
                    // debugger
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
                }catch(error){
                    console.log(error);
                    alert("Woops! There was an error. Please reload page and try again"); 
                }
            })
            .catch((error)=>{
                fetch('del_'+id+'_files')
                    .then(response => console.log("Delete "+id+" file http response: "+response.status))
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

