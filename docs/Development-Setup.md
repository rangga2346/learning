## Development Environment

Python        : 3.12.x
Dash          : Latest Stable
Plotly        : Latest Stable
Pandas        : Latest Stable
IDE           : VS Code / Cursor

Virtual Env   : venv

# Development Setup (macOS)

Panduan ini digunakan untuk melakukan setup project Morula pada Mac baru atau setelah melakukan clone project dari Git.

---

# Prerequisites

Install software berikut terlebih dahulu:

- Python 3.12
- Git
- VS Code (optional)

Verifikasi:

```bash
python3.12 --version
git --version
```

Expected:

```
Python 3.12.x
git version xx.xx
```

---

# 1. Clone Repository

Masuk ke folder Project

```bash
cd ~/Project
```

Clone repository

```bash
git clone https://git.pena.id/mtdlmii/morula-snowflake.git
```

Masuk ke project

```bash
cd morula-snowflake
```

---

# 2. Create Virtual Environment

Buat Virtual Environment

```bash
python3.12 -m venv .venv
```

---

# 3. Activate Virtual Environment

Aktifkan environment

```bash
source .venv/bin/activate
```

Terminal akan berubah menjadi

```
(.venv)
```

---

# 4. Install Dependencies

Install seluruh library

```bash
pip install -r requirements.txt
```

Pastikan selesai tanpa error.

---

# 5. Verify Python Version

```bash
python --version
```

Expected

```
Python 3.12.x
```

---

# 6. Verify Installed Packages

```bash
pip list
```

Pastikan package utama sudah tersedia.

Contoh

- dash
- dash-bootstrap-components
- pandas
- plotly
- duckdb
- openpyxl

---

# 7. Run Application

```bash
python app.py
```

atau

```bash
python3.12 app.py
```

Output

```
Dash is running...
```

Buka browser

```
http://127.0.0.1:8050
```

---

# Existing Project (Copy from Backup)

Apabila project berasal dari backup (Google Drive atau external storage):

1. Copy seluruh folder project.
2. Masuk ke folder project.

```bash
cd ~/Project/Morula
```

Hapus virtual environment lama.

```bash
rm -rf .venv
```

Buat virtual environment baru.

```bash
python3.12 -m venv .venv
```

Aktifkan.

```bash
source .venv/bin/activate
```

Install dependency.

```bash
pip install -r requirements.txt
```

Project siap dijalankan.

---

# Update Dependencies

Jika requirements berubah

```bash
pip install -r requirements.txt
```

---

# Generate requirements.txt

Jika ada package baru

```bash
pip freeze > requirements.txt
```

---

# Git Workflow

Pull terbaru

```bash
git pull
```

Commit perubahan

```bash
git add .
git commit -m "message"
```

Push

```bash
git push
```

---

# Re-create Virtual Environment

Jika environment rusak

```bash
rm -rf .venv

python3.12 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

---

# Common Problems

## python command not found

Gunakan

```bash
python3.12
```

atau

```bash
python3
```

---

## pip command not found

Gunakan

```bash
python3.12 -m pip install -r requirements.txt
```

---

## ModuleNotFoundError

Install ulang dependency

```bash
pip install -r requirements.txt
```

---

## Virtual Environment tidak aktif

Aktifkan kembali

```bash
source .venv/bin/activate
```

---

## Dash tidak bisa dijalankan

Pastikan

```bash
python app.py
```

dijalankan setelah Virtual Environment aktif.

---

# Folder Structure

```
Morula
│
├── app.py
├── requirements.txt
├── docs
├── pages
├── callbacks
├── repository
├── components
├── assets
├── database
├── data
└── .venv
```

---

# Development Checklist

- Python 3.12 terinstall
- Git terinstall
- Repository berhasil di-clone
- Virtual Environment aktif
- Dependency berhasil di-install
- `python app.py` berjalan tanpa error
- Dashboard dapat diakses melalui browser