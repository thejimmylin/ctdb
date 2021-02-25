$(document).ready(function () {
    $("a.set-language-item").on("click", function () {
        var language = $(this).text();
        $.ajax({
            type: "POST",
            url: url,
            data: {
                csrfmiddlewaretoken: csrfmiddlewaretoken,
                language: language,
            },
            success: function () {
                location.reload();
            }
        });
    });
});

// scroll-sensitive things
$(function () {
    $(document).scroll(function () {
        var $scrollSensitive = $(".scroll-sensitive");
        $scrollSensitive.toggleClass('scrolled', $(this).scrollTop() > $scrollSensitive.height());
    });
});
