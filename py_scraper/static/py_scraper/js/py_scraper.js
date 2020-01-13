console.log("scripts are being read");


$(document).ready(e => {
    $("#scrape_msnbc").click(e=>{
		e.preventDefault();
		
		fetch("scrape_msnbc")
			.then((response)=>{
				debugger
				console.log(response)
			})
    })
})


