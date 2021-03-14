document.addEventListener("DOMContentLoaded", function() {
    const e1 = document.querySelector("#id_policy");
    const e2 = document.querySelector("#id_form_row_special_policy");
    const useSepcialPolicy = function () {
        return (e1.value === "use special policy");        
    }
    e2.style.display = useSepcialPolicy() ? "" : "none";
    e1.addEventListener("change", function(event) {
        e2.style.display = useSepcialPolicy() ? "" : "none";
    })
})
