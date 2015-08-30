/**
 * Created by MillerB on 8/30/2015.
 */

$(".sub-nav-clickable").click(function(event) {
    event.preventDefault();
    var elements = $(".sub-nav-clickable");
    for(var i=0; i<elements.length; i++) {
        if (elements[i] !== $(this)) {
            var thing = elements[i];
            $(thing).addClass("not-selected");
            $(thing).removeClass("selected");
            $(thing).parent().removeClass("active");
        }
    }
    if ($(this).hasClass("not-selected")) {
        $(this).addClass("selected");
        $(this).removeClass("not-selected");
        $(this).parent().addClass("active");
    }
    $.ajax({
        type: 'GET',
        url: "/search/",
        data: {
            'search_text': $('#search-data').val(),
            'sort_text': $('.selected').text()
        },
        success: searchSuccess,
        dataType: 'html'
    });
});

function searchSuccess(response) {
    $('#results').html(response)
}