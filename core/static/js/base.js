// Load these codes after DOM loaded
document.addEventListener("DOMContentLoaded", function() {
    // Function definition
    const setLanguage = function(language) {
        fetch(i18nUrl, {
            method: "POST",
            body: new URLSearchParams({
                "csrfmiddlewaretoken": csrfMiddlewareToken,
                "language": language,
            }),
        }).then(function() {location.reload();});
    };
    // Django i18n/setlang
    const btns = document.querySelectorAll("a.set-language-item");
    for (const btn of btns) {
        btn.addEventListener("click", function(event) {
            setLanguage(event.currentTarget.textContent);
        });
    }
    // Scroll-sensitive things
    document.addEventListener("scroll", function() {
        let scrollSensitive = document.querySelector(".scroll-sensitive");
        scrollSensitive.classList.toggle('scrolled', window.scrollY > 0);
    })
});