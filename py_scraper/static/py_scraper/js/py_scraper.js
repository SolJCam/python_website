console.log("scripts are being read");




// async function url(url) {
// 	const response = await fetch(url);
// 	return await response.json();
// }

function loadImage(wrdCld, scrape_url, id){

	async function url(url) {
		const response = await fetch(url);
		return await response.json();
	}

	url(scrape_url)
		.then((first_json)=>{return first_json})
		.then((json)=>{
			// debugger
			try{
				// debugger
				$('#'+wrdCld).attr('src', '/static/imgs/'+wrdCld+'.png');
				$('#'+wrdCld).load('#'+wrdCld);
				if ($('#'+wrdCld)[0].width != 0 || $('#'+wrdCld)[0].width != 147){
				// if ($('#'+wrdCld)[0].width > 0){
					// debugger
					// $('#'+wrdCld).load('#'+wrdCld);
					for(let i=0;i<=4;i++){
						$(`#${id}-${i}`).text(`${json[i][0]} : ${json[i][1]}`);
						console.log($(`#${id}-${i}`).text(`${json[i][0]} : ${json[i][1]}`), $(`#${id}-${i}`).text());
					}
					console.log($('#'+wrdCld).attr('src', '/static/imgs/'+wrdCld+'.png')[0], $('#'+wrdCld)[0]);
					console.log(`Success scrapeing ${wrdCld}!`)
					// debugger
					fetch('del_clds')
						.then(response => response.json())
						.then(data => console.log(data));
				}else{
					console.log(`Failure scrapeng ${wrdCld}!`)
					// setTimeout(url, 180000, scrape_url)
				}
				// debugger
			}catch{
				console.log("error")
			}
		})
		.catch((error)=>{
			alert(error+" : Please try again");
		});
}

$(document).ready(() => {

	// debugger
    $("#scrape_msnbc").click(e=>{
		e.preventDefault();

		loadImage("msnbcwrdcld","scrape_msnbc","ms");
		// url("scrape_msnbc")
		// 	.then((json)=>{
		// 		// debugger
		// 		$('#msnbcwrdcld').attr('src', '/static/imgs/msnbcwrdcld.png');
		// 		$('#msnbcwrdcld').load(" #msnbcwrdcld");
		// 		for(let i=0;i<=4;i++){
		// 			$(`#ms-${i}`).text(`${json[i][0]} : ${json[i][1]}`);
		// 		}
		// 	})
		// 	.catch((error)=>{
		// 		alert(error+" : Please try again");
		// 	})
	})


    $("#scrape_cnn").click(e=>{
		e.preventDefault();
		
		loadImage("cnnwrdcld","scrape_cnn","cnn");
		// url("scrape_cnn")
		// 	.then((json)=>{
		// 		$('#cnnwrdcld').attr('src', '/static/imgs/cnnwrdcld.png');
		// 		$('#cnnwrdcld').load(" #cnnwrdcld");
		// 		for(let i=0;i<=4;i++){
		// 			$(`#cnn-${i}`).text(`${json[i][0]} : ${json[i][1]}`);
		// 		}
		// 	})
		// 	.catch((error)=>{
		// 		alert(error+" : Please try again");
		// 	})
	})
	

    $("#scrape_fox").click(e=>{
		e.preventDefault();
		
		loadImage("foxwrdcld","scrape_fox","fox");
		// url("scrape_fox")
		// 	.then((json)=>{
		// 		debugger
		// 		$('#foxwrdcld').attr('src', '/static/imgs/foxwrdcld.png');
		// 		$('#foxwrdcld').load(" #foxwrdcld");
		// 		for(let i=0;i<=4;i++){
		// 			$(`#fox-${i}`).text(`${json[i][0]} : ${json[i][1]}`);
		// 		}
		// 	})
		// 	.catch((error)=>{
		// 		alert(error+" : Please try again");
		// 	})
    })
})


