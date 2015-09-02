$(document).ready(function() {
    $.getScript('/static/noraebook/js/norae-favorite.js');
    var inProgress = false;

    $('#search-data').keyup(function() {
        if (!inProgress && ($(window).scrollTop() > 1)) {
            inProgress = true;
            $("html, body").animate({ scrollTop: 1 });
        }
        searchAjax(0, searchSuccess, true)
    });

    $(".sub-nav-clickable").click(function(event) {
        event.preventDefault();
        if (!inProgress && ($(window).scrollTop() > 1)) {
            inProgress = true;
            $("html, body").animate({ scrollTop: 1 });
        }
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
        searchAjax(0, searchSuccess, false)
    });

    $(window).scroll(function() {
        if(($(window).scrollTop() + $(window).height() >= $(document).height()) && (!inProgress)) {
            if (!($("#dvloader").length) && ($("#scroll-div").length)) {
                var loadHtml = '<div class="small-12 columns" id="dvloader"><img src="/static/noraebook/gif/loading.gif" id="gif-loader" height="36" width="36" /></div>';
                $('#results').append(loadHtml);
                inProgress = true;
                searchAjax($('.result').length, scrollSuccess, true)
            }
        }
    });

    function searchAjax(resultsLength, successFunction, asyncBool) {
        $.ajax({
            type: 'GET',
            url: "/search/",
            data: {
                'search_text': $('#search-data').val(),
                'sort_text': $('.selected').text(),
                'results_length': resultsLength
            },
            async: asyncBool,
            success: successFunction,
            dataType: 'html'
        });
    }

    function searchSuccess(response) {
        $('#results').html(response);
        $.getScript('/static/noraebook/js/norae-favorite.js');
        inProgress = false
    }

    function scrollSuccess(response) {
        $("#dvloader").remove();
        var scrollDiv = document.getElementById('scroll-div');
        if (scrollDiv) {
            scrollDiv.removeAttribute('id');
        }
        $('#results').append(response);
        inProgress = false
    }

});
/*
function searchAjax(resultsLength, successFunction, asyncBool) {
    $.ajax({
        type: 'GET',
        url: "/search/",
        data: {
            'search_text': $('#search-data').val(),
            'sort_text': $('.selected').text(),
            'results_length': resultsLength
        },
        async: asyncBool,
        success: successFunction,
        dataType: 'html'
    });
}

function searchSuccess(response) {
    $('#results').html(response);
    $.getScript('/static/noraebook/js/norae-favorite.js');
    inProgress = false
}

function scrollSuccess(response) {
    $("#dvloader").remove();
    var scrollDiv = document.getElementById('scroll-div');
    if (scrollDiv) {
        scrollDiv.removeAttribute('id');
    }
    $('#results').append(response);
    inProgress = false
}
*/