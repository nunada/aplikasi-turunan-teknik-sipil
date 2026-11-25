# Aplikasi Turunan untuk Teknik Sipil

Kumpulan contoh soal dan latihan aplikasi turunan (optimisasi terapan, kinematika, laju yang berkaitan)
untuk mahasiswa S1 Teknik Sipil, dengan gambar dan penyelesaian yang dapat dibuka-tutup.

| Sumber | Optimisasi | Laju berkaitan | Kinematika |
|---|---|---|---|
| Hass, Heil & Weir, *Thomas' Calculus: Early Transcendentals* (SI), ed. 15 | 4.6 | 3.10 | |
| Stewart, Clegg & Watson, *Calculus: Early Transcendentals*, ed. 9 | 4.7 | 3.9 | |
| Larson & Edwards, *Calculus*, ed. 12 | 3.7 | 2.6 | |
| Trim, *Calculus for Engineers*, ed. 4 | 4.7 | 4.9 | 4.8 |

Contoh 1–5 Larson §2.6 diambil dari edisi 11 karena halaman tersebut kosong pada berkas edisi 12 yang dipakai.

Soal diringkas dengan kata-kata sendiri, sedangkan penyelesaian dan gambar dibuat ulang untuk keperluan belajar.
Teks asli dan hak cipta tetap milik penulis serta penerbit. Penyelesaian belum ditelaah dosen;
jika menemukan kekeliruan, silakan buka *issue*.

## Menyunting

- Soal dan penyelesaian: `src/content/*.md`
- Grafik pada penyelesaian: `src/content/*.grafik.txt` (titik maksimum/minimum diperiksa saat build)
- Gambar: `src/figs_*.py` (SVG, tanpa pustaka tambahan)

Bangun ulang situs (Python 3, tanpa dependensi):

```
python build.py
```

Hasilnya ada di folder `docs/`, yang disajikan oleh GitHub Pages. Rumus dirender dengan KaTeX dari CDN.
