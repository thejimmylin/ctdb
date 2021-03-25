document.addEventListener("DOMContentLoaded", function() {
    const textareas = document.querySelectorAll('textarea.ckeditor4');
    for (const textarea of textareas) {
        CKEDITOR.replace(textarea.id, {
            customConfig: 'custom_config.js'
        });
    }
})
