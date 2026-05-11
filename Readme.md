# README - Tubes DKA 2026

## Simulasi Pengangkutan Sampah Menggunakan AI

---

# Anggota Kelompok

| Nama      | Jobdesk                 |
| --------- | ----------------------- |
| Farrelino | Routing & Algoritma     |
| Chaesar   | Simulasi Operasional    |
| Valen     | Visualisasi & Integrasi |

---

# Struktur Project

```text
project/
│
├── data_generator.py
├── routing.py
├── operation.py
├── reporting.py
├── visualization.py
├── main.ipynb
├── requirements.txt
└── README.md
```

---

# Pembagian Jobdesk

## Farrelino

### File:

* `data_generator.py`
* `routing.py`

### Tugas:

* generate rumah
* hitung jarak
* greedy algorithm
* routing kendaraan

---

## Chaesar

### File:

* `operation.py`

### Tugas:

* simulasi waktu
* loading/unloading
* kapasitas kendaraan
* jam operasional
* sisa sampah

---

## Valen

### File:

* `visualization.py`
* `reporting.py`
* `main.ipynb`

### Tugas:

* visualisasi
* reporting
* integrasi sistem
* testing

---

# Cara Clone Project

```bash
git clone https://github.com/NAMA-REPO/tubes-dka.git
```

Masuk folder project:

```bash
cd tubes-dka
```

---

# Cara Membuat Branch

## Farrelino

```bash
git checkout -b feature/routing
```

---

## Chaesar

```bash
git checkout -b feature/operation
```

---

## Valen

```bash
git checkout -b feature/visualization
```

---

# Aturan Branch

## Jangan langsung push ke main

Semua pengerjaan dilakukan di branch masing-masing.

---

# Cara Pull Update Terbaru

Sebelum coding WAJIB pull dahulu.

```bash
git checkout main
git pull origin main
```

Lalu kembali ke branch masing-masing:

```bash
git checkout nama-branch
```

---

# Cara Commit

## Cek perubahan

```bash
git status
```

---

## Tambahkan file

```bash
git add .
```

---

## Commit

### Contoh commit Farrelino

```bash
git commit -m "Menambahkan greedy routing gerobak"
```

### Contoh commit Chaesar

```bash
git commit -m "Menambahkan simulasi waktu operasional"
```

### Contoh commit Valen

```bash
git commit -m "Menambahkan visualisasi jalur kendaraan"
```

---

# Cara Push

```bash
git push origin nama-branch
```

Contoh:

```bash
git push origin feature/routing
```

---

# Cara Merge ke Main

## 1. Pastikan code aman

* tidak error
* tidak merusak file orang lain

---

## 2. Pull latest main

```bash
git checkout main
git pull origin main
```

---

## 3. Merge branch

```bash
git merge nama-branch
```

Contoh:

```bash
git merge feature/routing
```

---

## 4. Push main

```bash
git push origin main
```

---

# Aturan Pengerjaan

## WAJIB

* pull sebelum coding
* commit jelas
* branch sesuai jobdesk

---

## DILARANG

* push langsung ke main
* mengubah file jobdesk orang lain tanpa izin
* commit dengan pesan:

  * `fix`
  * `update`
  * `hehe`
  * `test`

---

# Format Commit yang Benar

## Gunakan format:

```text
Menambahkan ...
Memperbaiki ...
Mengubah ...
```

---

# Contoh Commit yang Bagus

```bash
git commit -m "Menambahkan perhitungan jarak Euclidean"
```

```bash
git commit -m "Memperbaiki bug kapasitas gerobak"
```

```bash
git commit -m "Menambahkan visualisasi posisi TPS"
```

---

# Alur Kerja Kelompok

```text
1. Pull latest main
2. Masuk branch masing-masing
3. Coding
4. Commit
5. Push branch
6. Testing bersama
7. Merge ke main
```

---

# Library yang Digunakan

Install dependency:

```bash
pip install -r requirements.txt
```

---

# Library Utama

```text
numpy
pandas
matplotlib
math
random
```

---

# Tujuan Program

Program dibuat untuk:

* simulasi pengangkutan sampah
* optimasi rute kendaraan
* menghitung jarak dan waktu
* visualisasi sistem pengangkutan

---

# Catatan Penting

Jika terjadi conflict:

```bash
git pull origin main
```

Lalu selesaikan conflict sebelum commit kembali.

---

# Penanggung Jawab

| Bagian      | Penanggung Jawab |
| ----------- | ---------------- |
| Routing     | Farrelino        |
| Operation   | Chaesar          |
| Visualisasi | Valen            |
| Integrasi   | Bersama          |
| Testing     | Bersama          |
| Presentasi  | Bersama          |
