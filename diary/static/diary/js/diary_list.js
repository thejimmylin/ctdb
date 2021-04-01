document.addEventListener("DOMContentLoaded", function() {
    // Function definition
    const origin = window.location.origin;
    const urlApiDiaryList = `${origin}/api/diaries/`;
    fetch(urlApiDiaryList).then(r => r.json()).then(console.log);
    }
);