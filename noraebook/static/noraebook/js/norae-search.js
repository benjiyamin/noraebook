$(document).ready(function() {
    $('#search-data').keyup(function () {
        $.ajax({
            type: 'GET',
            url: "/search/",
            data: {
                'search_text': $('#search-data').val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
    });
});

function searchSuccess(response) {
    /*
    var songs_list = JSON.parse(response);
    var html_string = "";
    for(var i=0; i<songs_list.length; i++) {
        var song = songs_list[i];
        html_string += '<div class="result small-12 medium-12 large-12 columns">';
        html_string += '<div class="code-result small-4 medium-2 large-2 columns">';
        html_string += song.fields.code;
        html_string += '</div>';
        html_string += '<div class="song-result small-7 medium-9 large-9 columns">';
        html_string += '<div class="title-result small-12 large-12 columns">';
        html_string += song.fields.title;
        html_string += '</div>';
        html_string += '<div class="artist-result small-12 large-12 columns">';
        html_string += ' ' + song.fields.artist;
        html_string += '</div>';
        html_string += '</div>';
        html_string += '<div class="fav-result small-1 medium-1 large-1 columns">';
        html_string += '<a class="not-liked" href="/login/"><i class="fi-heart" id="song.fields.id"></i></a>';
        html_string += '</div>';
        html_string += '</div>';
        console.log(song.fields.title);
    }
    $('#results').html(html_string);
    */
    $('#results').html(response)
}
