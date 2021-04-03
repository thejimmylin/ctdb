document.addEventListener("DOMContentLoaded", function() {
    const pathname = window.location.pathname;
    const selectRoles = document.querySelector('#rolesSelect');
    if (selectRoles) {
        selectRoles.addEventListener("change", function(e) {
            const params = e.target.value ? {"dep": e.target.value} : {};
            const queryString = new URLSearchParams(params).toString();
            const url = queryString ? pathname + "?" + queryString : pathname;
            window.location.replace(url);
        })
    }
});