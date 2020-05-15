window.onload = ()=>{
    (()=>{
      pdfjsLib
      .getDocument("/static/assets/SolDevRes5_16.pdf")
      .promise.then(pdfDoc => {
        // debugger 
        const page = pdfDoc.getPage(1);
          console.log(pdfDoc); // should be resolved
          console.log(page); // should be a promise
          return page; 
      })
      .then(page => {
        //   debugger 
          console.log(page); // should now be resolved
      
          const scale = 1;
          const viewport = page.getViewport({scale});
      
          // Apply page dimensions to the <canvas> element.
          const canvas = document.getElementById("pdf");
          const context = canvas.getContext("2d");
          canvas.height = viewport.height;
          canvas.width = viewport.width;
      
          // Render the page into the <canvas> element.
          const renderContext = {
              canvasContext: context,
              viewport: viewport
          };
          // page.render(renderContext);
  
          const pageCtxt = [
              page,
              renderContext
          ]
          return pageCtxt;
      })
      .then(pageCtxt => {
          // debugger
          pageCtxt[0].render(pageCtxt[1]);
      })
      .catch(err => {
          // Display error
          console.log(err);
      });
    })();
}