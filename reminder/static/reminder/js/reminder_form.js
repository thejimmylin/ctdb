document.addEventListener("DOMContentLoaded", function() {
    const inputPolicy = document.querySelector("#id_policy");
    const inputSpecialPolicy = document.querySelector("#id_special_policy");
    const formRowSpecialPolicy = document.querySelector("#id_form_row_special_policy");
    function useSpecialPolicy() {
        return inputPolicy.value === 'special policy';
    }
    function toggleDisplay(target, condition) {
        target.style.display = condition ? "" : "none";
    }
    inputPolicy.addEventListener("change", function(event) {
        toggleDisplay(formRowSpecialPolicy, useSpecialPolicy());
        if (!useSpecialPolicy()) {
            inputSpecialPolicy.value = "";
        }
    })
    toggleDisplay(formRowSpecialPolicy, useSpecialPolicy());
})
