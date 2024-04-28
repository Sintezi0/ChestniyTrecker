const fileInput = document.getElementById("file-input");
const uploadForm = document.getElementById("upload-form");

fileInput.addEventListener("change", () => {
    uploadForm.submit();
});