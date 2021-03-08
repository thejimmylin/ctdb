{
    let searchInput = document.querySelector("#searchInput");
    searchInput.addEventListener("keyup", function () {
        let inputValue, trs, tds, textValue, includeText;
        inputValue = document.querySelector("#searchInput").value;
        trs = document.querySelectorAll("#searchTable tbody tr");
        for (tr of trs) {
            tds = tr.querySelectorAll("td");
            textValue = ""
            for (td of tds) {
                textValue += td.textContent;
            }
            includeText = (textValue.toLowerCase().indexOf(inputValue.toLowerCase()) > -1);
            tr.style.display = includeText ? "" : "none";
        }
    })
}
