document.addEventListener("DOMContentLoaded", function() {
    // Declare
    const inputPolicy = document.querySelector("#id_policy");
    const inputSpecifiedDates = document.querySelector("#id_specified_dates");
    const inputStartAt = document.querySelector("#id_start_at");
    const initValueInputStartAt = inputStartAt.value;
    const formRowStartAt = document.querySelector("#id_form_row_start_at");
    const inputEndAt = document.querySelector("#id_end_at");
    const initValueInputEndAt = inputEndAt.value;
    const formRowEndAt = document.querySelector("#id_form_row_end_at");
    const formRowSpecifiedDates = document.querySelector("#id_form_row_specified_dates");
    // Initialize
    formRowSpecifiedDates.style.display = "none";
    // Event
    inputPolicy.addEventListener("change", function(event) {
        if (inputPolicy.value === 'specified dates') {
            formRowStartAt.style.display = "none";
            inputStartAt.value = initValueInputStartAt;
            formRowEndAt.style.display = "none";
            inputEndAt.value = initValueInputEndAt;
            formRowSpecifiedDates.style.display = "";
        }
        else if (inputPolicy.value === 'once') {
            formRowStartAt.style.display = "";
            formRowEndAt.style.display = "none";
            inputEndAt.value = initValueInputEndAt;
            formRowSpecifiedDates.style.display = "none";
            inputSpecifiedDates.value = "";
        }
        else {
            formRowStartAt.style.display = "";
            formRowEndAt.style.display = "";
            formRowSpecifiedDates.style.display = "none";
            inputSpecifiedDates.value = "";
        }
    })
})
