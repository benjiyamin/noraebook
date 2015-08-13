$(document).ready(function() {
  $('#search-data').keyup(function () {
    $.ajax({
      type: 'GET',
      url: "/search/",
      data: {
        'search_text': $('#search-data').val()
      },
      success: searchSuccess
    });
  });
});

function searchSuccess(response) {
  $('#results').html(response)
}