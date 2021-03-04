// Django i18n/setlang
const setLanguage = function (language) {
    $.ajax({
        type: "POST",
        url: url,
        data: {
            csrfmiddlewaretoken: csrfmiddlewaretoken,
            language: language,
        },
        success: function () {
            location.reload();
        },
    });
};
document.addEventListener("DOMContentLoaded", function () {
    const btns = document.querySelectorAll("a.set-language-item");
    for (const btn of btns) {
        btn.addEventListener("click", function (event) {
            setLanguage(event.currentTarget.textContent);
        });
    }
});

// scroll-sensitive things
$(function () {
    $(document).scroll(function () {
        var scrollSensitive = $(".scroll-sensitive");
        scrollSensitive.toggleClass('scrolled', $(this).scrollTop() > scrollSensitive.height());
    });
});
