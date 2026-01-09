# 📄 Invoice Scanner — Azure Document Intelligence

Aplikasi ini digunakan untuk melakukan **scanning dan ekstraksi data invoice** menggunakan metode **Azure AI Document Intelligence**.
Project ini berjalan menggunakan **Python + Flask**, dan membutuhkan koneksi ke layanan Azure Document Intelligence.

---

## 🚀 Fitur Utama

* Upload invoice (JPG/PNG/PDF)
* Pemrosesan invoice menggunakan Azure Document Intelligence
* Menampilkan hasil ekstraksi dalam format JSON
* Endpoint API siap digunakan

---

## 📦 Persiapan & Instalasi

### 1. Clone / Download Project

```bash
git clone https://github.com/namaproject/invoice-scanner.git
cd invoice-scanner
```

### 2. Buat Virtual Environment (Opsional tapi disarankan)

```bash
python -m venv venv
```

Aktifkan:

**Windows**

```bash
venv\Scripts\activate
```

**Mac / Linux**

```bash
source venv/bin/activate
```

---

## 📚 Instalasi Dependencies

Untuk install semua kebutuhan:

```bash
pip install -r requirements.txt
```

## 🔑 Setup Azure Credentials

Aplikasi ini menggunakan layanan **Azure Document Intelligence**, jadi kamu perlu menyiapkan:

* **AZURE_ENDPOINT**
* **AZURE_KEY**

Buat file `.env` di root project:

```
AZURE_ENDPOINT=https://xxx.cognitiveservices.azure.com/
AZURE_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## ▶️ Cara Menjalankan Aplikasi

Setelah semua dependencies terinstall, jalankan:

```bash
cd backend
python app.py
```

Jika berhasil, akan muncul:

```
Running on http://127.0.0.1:5000
```

Buka browser dan akses URL tersebut.

---

## 🔍 Cara Menggunakan Scanning (Azure Method)

1. Buka halaman **upload** di aplikasi.
2. Pilih file invoice (gambar atau PDF).
3. Sistem akan mengirim file ke Azure Document Intelligence.
4. Azure mengekstrak data (nama barang, harga, tanggal, dsb).
5. Hasil dikembalikan ke app dalam format JSON.

---

## 🛠 Teknologi yang Digunakan

* Python 3
* Flask
* Azure AI Document Intelligence
* Azure Key Credential
* JSON Formatter

