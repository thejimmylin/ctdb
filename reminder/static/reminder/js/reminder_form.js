document.addEventListener("DOMContentLoaded", function() {
    // Declare
    const inputPolicy = document.querySelector("#id_policy");
    const inputAdvancedPolicy = document.querySelector("#id_advanced_policy");
    const formRowStartDate = document.querySelector("#id_form_row_start_date");
    const formRowStopDate = document.querySelector("#id_form_row_stop_date");
    const formRowAdvancedPolicy = document.querySelector("#id_form_row_advanced_policy");
    // INIT
    formRowAdvancedPolicy.style.display = "";
    // Event
    inputPolicy.addEventListener("change", function(event) {
        if (inputPolicy.value === 'advanced policy') {
            formRowStartDate.style.display = "none";
            formRowStopDate.style.display = "none";
            formRowAdvancedPolicy.style.display = "";
        }
        else {
            formRowStartDate.style.display = "";
            formRowStopDate.style.display = "";
            formRowAdvancedPolicy.style.display = "none";
            inputAdvancedPolicy.value = "";
        }
    })
})
