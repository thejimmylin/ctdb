searchInput = document.querySelector("#searchInput");
searchInput.addEventListener("keyup", event => {
    var input, filter, table, tr, i, j, tds, textValue;
    input = document.querySelector("#searchInput");
    filter = input.value.toLowerCase();
    table = document.querySelector("#diaryListTable");
    tbody = table.querySelector("tbody");
    tr = tbody.querySelectorAll("tr");
    for (i = 0; i < tr.length; i++) {
        tds = tr[i].querySelectorAll("td");
        for (j = 0; j <tds.length; j++) {
            textValue += tds[j].textContent;
        }
        if (textValue.toLowerCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
        } else {
            tr[i].style.display = "none";
        }
    }
})
