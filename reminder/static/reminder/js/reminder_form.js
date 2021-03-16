document.addEventListener("DOMContentLoaded", function() {
    // Declare
    const inputPolicy = document.querySelector("#id_policy");
    const inputAdvancedPolicy = document.querySelector("#id_advanced_policy");
    const formRowStartAt = document.querySelector("#id_form_row_start_at");
    const formRowEndAt = document.querySelector("#id_form_row_end_at");
    const formRowAdvancedPolicy = document.querySelector("#id_form_row_advanced_policy");
    // INIT
    formRowAdvancedPolicy.style.display = "";
    // Event
    inputPolicy.addEventListener("change", function(event) {
        if (inputPolicy.value === 'advanced policy') {
            formRowStartAt.style.display = "none";
            formRowEndAt.style.display = "none";
            formRowAdvancedPolicy.style.display = "";
        }
        else {
            formRowStartAt.style.display = "";
            formRowEndAt.style.display = "";
            formRowAdvancedPolicy.style.display = "none";
            inputAdvancedPolicy.value = "";
        }
    })
})
