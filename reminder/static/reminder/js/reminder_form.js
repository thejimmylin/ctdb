document.addEventListener("DOMContentLoaded", function() {
    const inputPolicy = document.querySelector("#id_policy");
    const inputAdvancedPolicy = document.querySelector("#id_advanced_policy");
    const formRowAdvancedPolicy = document.querySelector("#id_form_row_advanced_policy");
    function useAdvancedPolicy() {
        return inputPolicy.value === 'advanced policy';
    }
    function toggleDisplay(target, condition) {
        target.style.display = condition ? "" : "none";
    }
    inputPolicy.addEventListener("change", function(event) {
        toggleDisplay(formRowAdvancedPolicy, useAdvancedPolicy());
        if (!useAdvancedPolicy()) {
            inputAdvancedPolicy.value = "";
        }
    })
    toggleDisplay(formRowAdvancedPolicy, useAdvancedPolicy());
})
