const imageInput = document.getElementById("imageInput");
const fileName = document.getElementById("fileName");

imageInput.addEventListener("change", () => {
    if (imageInput.files.length > 0) {
        fileName.textContent = imageInput.files[0].name;
    }
});

document.getElementById("generateBtn").addEventListener("click", async () => {

    const fileInput = document.getElementById("imageInput");

    if (!fileInput.files.length) {
        alert("Please select an image");
        return;
    }

    const formData = new FormData();
    formData.append("image", fileInput.files[0]);

    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "✨ Generating captions...";

    const response = await fetch("/generate", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    resultDiv.innerHTML = `
    <div class="caption-output">
    ${data.result.replace(/\n/g, "<br>")}
    </div>
    `;
});