console.log("scripts are being read");


async function url(url) {
	const response = await fetch(url);
	// debugger
	return await response.json();
}


$(document).ready(() => {


    $("#scrape_msnbc").click(e=>{
		e.preventDefault();

		url("scrape_msnbc")
			.then((json)=>{
				// debugger;
				$('#msnbcwrdcld').attr('src', '/static/imgs/msnbcwrdcld.png');
				$('#msnbcwrdcld').load(" #msnbcwrdcld");
				for(let i=0;i<=4;i++){
					$(`#ms-${i}`).text(`${json[i][0]} : ${json[i][1]}`);
				}
			})
			.catch((error)=>{
				alert(error+" : Please try again");
			})
	})


    $("#scrape_cnn").click(e=>{
		e.preventDefault();
		
		url("scrape_cnn")
			.then((json)=>{
				$('#cnnwrdcld').attr('src', '/static/imgs/cnnwrdcld.png');
				$('#cnnwrdcld').load(" #cnnwrdcld");
				for(let i=0;i<=4;i++){
					$(`#cnn-${i}`).text(`${json[i][0]} : ${json[i][1]}`);
				}
			})
			.catch((error)=>{
				alert(error+" : Please try again");
			})
	})
	

    $("#scrape_fox").click(e=>{
		e.preventDefault();
		
		url("scrape_fox")
			.then((json)=>{
				$('#foxwrdcld').attr('src', '/static/imgs/foxwrdcld.png');
				$('#foxwrdcld').load(" #foxwrdcld");
				for(let i=0;i<=4;i++){
					$(`#fox-${i}`).text(`${json[i][0]} : ${json[i][1]}`);
				}
			})
			.catch((error)=>{
				alert(error+" : Please try again");
			})
    })
})


