
$("#analyze_text").on("click", function(){
    var comment_text = $("#comment_query").val();

    if(comment_text.length <= 0) return false;

    $.ajax({
        url: 'analyze',
        method: 'POST',
        data: {'text': comment_text},
        beforeSend: function() {
            $("#loader").fadeIn();

        },

        success: function(response){

            $("#loader").fadeOut();

            $("#results").html("");
            $("#result_text").html("");

            $("#result_text").html("<p>Watson is <span class='confidence'>"+
                (response['classes'][0]['confidence']*100).toFixed(2)+
                "%</span> confident that this comment is: <span class='class_name'>"+
                response['classes'][0]['class_name']+
                "</span></p>");
            
            response['classes'].forEach(function(element, index){
                $("#results").append(
                    "<a class='list-group-item' href='#'>"+
                        element['class_name']+
                        " ("+
                            (element['confidence']*100).toFixed(2)+
                        "%)</a>");
            });

            $(window).scrollTop($("#results").offset().top);

        }

    });

    return false;
});