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
				if ($('#'+wrdCld)[0].width > 0){
					$('#'+wrdCld).load('#'+wrdCld);
					for(let i=0;i<=4;i++){
						$(`#${id}-${i}`).text(`${json[i][0]} : ${json[i][1]}`);
					}
					console.log('Success!')
					fetch('del_clds')
						.then(response => response.json())
						.then(data => console.log(data));
				}else{
					// debugger
					console.log('Image failure. Resending request')
					setTimeout(url(url), 180,000)
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


