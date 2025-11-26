document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("uploadForm");
    const resultBox = document.getElementById("result");
    const button = form.querySelector("button");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const fileInput = document.getElementById("image");
        const file = fileInput.files[0];

        if (!file) {
            alert("Please upload an image");
            return;
        }

        // ===== Disable tombol & tampilkan loading =====
        button.disabled = true;
        button.textContent = "Processing... ⏳";
        resultBox.innerHTML = "<p>Processing invoice. Please wait...</p>";

        const formData = new FormData();
        formData.append("file", file);

        try {
            const res = await fetch("http://localhost:5000/scan", {
                method: "POST",
                body: formData,
            });

            if (!res.ok) throw new Error("Server error");

            const data = await res.json();
            console.log("📦 Received OCR:", data);

            // Simpan data untuk form.html
            localStorage.setItem("invoice_data", JSON.stringify(data));

            // ===== Redirect ke form =====
            window.location.href = "form.html";

        } catch (error) {
            console.error("❌ Fetch / OCR error:", error);
            resultBox.innerHTML = "<p>Error processing invoice. Please try again.</p>";
        } finally {
            // Kembalikan tombol (kalau user mau retry)
            button.disabled = false;
            button.textContent = "Upload & Scan";
        }
    });
});
