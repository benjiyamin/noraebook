$(document).ready(function() {
    $(".likable").click(function(event) {
        event.preventDefault();
        if ($(this).hasClass("not-liked")) {
            $(this).removeClass("not-liked");
            $(this).addClass("liked");
        } else {
            $(this).removeClass("liked");
            $(this).addClass("not-liked");
        }
        $.ajax({
            type: 'POST',
            url: "/like/",
            data: {
                'song_id': event.target.id
            }
        });
    });
});
