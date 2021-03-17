document.addEventListener("DOMContentLoaded", function() {
    // Declare
    const inputPolicy = document.querySelector("#id_policy");
    const inputSpecifiedDates = document.querySelector("#id_specified_dates");
    const formRowStartAt = document.querySelector("#id_form_row_start_at");
    const formRowEndAt = document.querySelector("#id_form_row_end_at");
    const formRowSpecifiedDates = document.querySelector("#id_form_row_specified_dates");
    // INIT
    formRowSpecifiedDates.style.display = "";
    // Event
    inputPolicy.addEventListener("change", function(event) {
        if (inputPolicy.value === 'specified dates') {
            formRowStartAt.style.display = "none";
            formRowEndAt.style.display = "none";
            formRowSpecifiedDates.style.display = "";
        }
        else if (inputPolicy.value === 'once') {
            formRowStartAt.style.display = "";
            formRowEndAt.style.display = "none";
            formRowSpecifiedDates.style.display = "";
        }
        else {
            formRowStartAt.style.display = "";
            formRowEndAt.style.display = "";
            formRowSpecifiedDates.style.display = "none";
            inputSpecifiedDates.value = "";
        }
    })
})
