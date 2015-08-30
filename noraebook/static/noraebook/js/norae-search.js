$(document).ready(function() {
    $('#search-data').keyup(function () {
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
});

function searchSuccess(response) {
    $('#results').html(response)
}
