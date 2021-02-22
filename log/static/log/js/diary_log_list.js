searchInput = document.querySelector("#searchInput");
searchInput.addEventListener("keyup", event => {
    var input, filter, table, tr, td, i, textValue;
    input = document.querySelector("#searchInput");
    filter = input.value.toLowerCase();
    table = document.querySelector("#diaryLogListTable");
    tbody = table.querySelector("tbody");
    tr = tbody.querySelectorAll("tr");
    var tds, textCreatedBy, textDailyRecord, textTodo;
    for (i = 0; i < tr.length; i++) {
        tds = tr[i].querySelectorAll("td");
        textCreatedBy = tds[1].textContent;
        textDailyRecord = tds[4].textContent;
        textTodo = tds[5].textContent;
        textValue = textCreatedBy + textDailyRecord + textTodo;
        if (textValue.toLowerCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
        } else {
            tr[i].style.display = "none";
        }
    }
})
