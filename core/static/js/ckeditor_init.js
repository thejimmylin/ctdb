// These codes is used to change the DOMs on the page to a CKeditor.
// CKeditor is a rich-text editor.
// https://ckeditor.com/ckeditor-4/
// To use a custom config: change the core\static\ckeditor\custom_config.js
// For more detail, see the official documentation.
// https://ckeditor.com/docs/ckeditor4/latest/guide/dev_configuration.html#configuration-loading-order

document.addEventListener("DOMContentLoaded", function() {
    const textareas = document.querySelectorAll('textarea.ckeditor4');
    for (const textarea of textareas) {
        CKEDITOR.replace(textarea.id, {
            customConfig: 'custom_config.js'
        });
    }
})
