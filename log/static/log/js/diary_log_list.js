searchInput = document.querySelector("#searchInput");
searchInput.addEventListener("keyup", event => {
    var input, filter, table, tr, td, i, textValue;
    input = document.querySelector("#searchInput");
    filter = input.value.toLowerCase();
    table = document.querySelector("#diaryLogListTable");
    tbody = table.querySelector("tbody");
    tr = tbody.querySelectorAll("tr");
    var tds, textAction, textData, textCreatedAt;
    for (i = 0; i < tr.length; i++) {
        tds = tr[i].querySelectorAll("td");
        textAction = tds[0].textContent;
        textData = tds[1].textContent;
        textCreatedAt = tds[2].textContent;
        textValue = textAction + textData + textCreatedAt;
        if (textValue.toLowerCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
        } else {
            tr[i].style.display = "none";
        }
    }
})
