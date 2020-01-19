console.log("scripts are being read");


$(document).ready(e => {
    $("#scrape_msnbc").click(e=>{
		e.preventDefault();
		
		fetch("scrape_msnbc")
			.then((response)=>{
				$('#msnbcwrdcld').attr('src', '/static/imgs/msnbcwrdcld.png')
				$('#msnbcwrdcld').load(" #msnbcwrdcld")
			})
			.catch((error)=>{
				alert(error+" : Please try again")
			})
	})


    $("#scrape_cnn").click(e=>{
		e.preventDefault();
		
		fetch("scrape_cnn")
			.then((response)=>{
				$('#cnnwrdcld').attr('src', '/static/imgs/cnnwrdcld.png')
				$('#cnnwrdcld').load(" #cnnwrdcld")
			})
			.catch((error)=>{
				alert(error+" : Please try again")
			})
	})
	

    $("#scrape_fox").click(e=>{
		e.preventDefault();
		
		fetch("scrape_fox")
			.then((response)=>{
				$('#foxwrdcld').attr('src', '/static/imgs/foxwrdcld.png')
				$('#foxwrdcld').load(" #foxwrdcld")
			})
			.catch((error)=>{
				alert(error+" : Please try again")
			})
    })
})


