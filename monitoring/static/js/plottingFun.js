function zoomablePlot(idPlaceholder, graphDatas, graphOptions, arrowLeft, arrowRight) {
    var placeholder = $(idPlaceholder)
    
    var plot = $.plot(placeholder, graphDatas, graphOptions, arrowLeft, arrowRight);
    

    // placeholder.bind("plotzoom", function (event, plot) {
    //     var axes = plot.getAxes();
    //     $(".message").html("Zooming to x: "  + axes.xaxis.min.toFixed(2)
    // 			   + " &ndash; " + axes.xaxis.max.toFixed(2)
    // 			   + " and y: " + axes.yaxis.min.toFixed(2)
    // 			   + " &ndash; " + axes.yaxis.max.toFixed(2));
    // });

    // // add zoom out button 
    // $("<div class='button' style='right:32px;top:15px'>zoom out</div>")
    //     .appendTo(placeholder)
    //     .click(function (event) {

    // 	    event.preventDefault();
    //         plot.zoomOut();
    // 	});

    // // and add panning buttons
    // function addArrow(src, right, top, offset) {
    //     $("<img class='button' src='" + src + "' style='right:" + right + "px;top:" + top + "px'>")
    //         .appendTo(placeholder)
    //         .click(function (e) {
    // 		e.preventDefault();
    // 		plot.pan(offset);
    //         });
    // }

    // addArrow(arrowLeft, 65, 40, { left: -100 })
    // addArrow(arrowRight, 30, 40, { left: 100 });


    // Make flot responsive-design
/*    window.onresize = function(event) {
        $.plot($(placeholder), [ d1, d2, d3 ]);
    }*/
}
