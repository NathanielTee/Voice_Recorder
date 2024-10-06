# Voice Recorder

Voice Recorder adalah program Python yang memungkinkan pengguna untuk merekam audio menggunakan mikrofon, menyimpan rekaman ke dalam format WAV, dan memutar ulang rekaman. Pengguna dapat memulai dan menghentikan rekaman menggunakan tombol keyboard.

## Fitur

- Rekaman audio dengan sampling frequency 44100 Hz.
- Penyimpanan hasil rekaman dalam format WAV dengan normalisasi suara.
- Kontrol sederhana menggunakan keyboard: tekan 'S' untuk mulai merekam dan 'Enter' untuk menghentikan rekaman.
- Penyimpanan file rekaman ke dalam folder yang ditentukan.

## Persyaratan

Sebelum menjalankan program ini, pastikan kamu telah menginstal paket berikut:

- Python (versi 3.6 atau lebih baru)
- sounddevice
- scipy
- numpy
- keyboard

### Instalasi Paket

Kamu bisa menginstal semua paket yang diperlukan menggunakan pip:

```bash
pip install sounddevice scipy numpy keyboard
```

## Cara Menggunakan

1. **Clone repositori ini**:
   ```bash
   git clone https://github.com/NathanielTee/Voice_Recorder.git
   cd voice_recorder
   ```

2. **Jalankan program**:
   Pastikan untuk menjalankan program dalam terminal atau command prompt. Gunakan perintah berikut:
   ```bash
   python voice_recorder_2.py
   ```

3. **Rekam Suara**:
   - Tekan 'S' untuk memulai merekam suara.
   - Setelah selesai, tekan 'Enter' untuk menghentikan rekaman.

4. **Hasil Rekaman**:
   Rekaman akan disimpan dalam folder yang telah ditentukan di dalam kode. Nama file akan menggunakan timestamp saat rekaman dilakukan.

## Kontribusi

Jika kamu ingin berkontribusi pada proyek ini, silakan lakukan fork dan buat pull request.

## Lisensi

Proyek ini tidak memiliki lisensi khusus. Namun, kontribusi dan penggunaan yang baik sangat dihargai.


### Mengubah Pengaturan Folder (Opsional)

Jika kamu ingin mengubah folder tempat rekaman disimpan, ubah nilai dari `folder_path` dalam kode di bagian berikut:
```python
folder_path = "D:/Project Nathan/Recordings"  # Ganti dengan path folder yang diinginkan
```

Ganti dengan jalur folder yang kamu inginkan di komputermu.
