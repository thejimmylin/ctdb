// Function definition
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
// Load these codes after DOM loaded
document.addEventListener("DOMContentLoaded", function () {
    // Django i18n/setlang
    const btns = document.querySelectorAll("a.set-language-item");
    for (const btn of btns) {
        btn.addEventListener("click", function (event) {
            setLanguage(event.currentTarget.textContent);
        });
    }
    // Scroll-sensitive things
    document.addEventListener("scroll", function () {
        let scrollSensitive = document.querySelector(".scroll-sensitive");
        scrollSensitive.classList.toggle('scrolled', window.scrollY > 0);
    })
});
