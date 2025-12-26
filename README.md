# Hand Gesture Audio Player

Proyek ini menggunakan OpenCV dan MediaPipe untuk mendeteksi gestur tangan secara real-time melalui kamera dan memicu pemutaran file audio yang sesuai. Aplikasi ini dirancang untuk mengenali tiga jenis gestur utama dengan respon audio yang berbeda.

## Fitur Utama

- Deteksi tangan real-time menggunakan MediaPipe Hands.
- Klasifikasi gestur berdasarkan posisi jari.
- Pemutaran audio otomatis menggunakan Pygame Mixer.
- Sistem cooldown untuk mencegah pemutaran audio berulang dalam waktu singkat.

## Gestur dan Respon Audio

Aplikasi ini diprogram untuk mengenali gestur berikut:

1. Berjuang: Terdeteksi saat tangan mengepal (semua jari tertutup). Memutar audio "Berjuang.mp3".
2. Selamat: Terdeteksi saat telapak tangan terbuka penuh (semua jari terbuka). Memutar audio "Selamat.mp3".
3. Sukses: Terdeteksi saat kedua tangan menunjukkan jempol (thumbs up). Memutar audio "Sukses.mp3".

## Prasyarat

Sebelum menjalankan proyek ini, pastikan Anda telah menginstal Python (versi 3.8 ke atas direkomendasikan).

### Library yang Dibutuhkan:
- OpenCV
- MediaPipe
- Pygame

## Instalasi dan Setup

1. Clone repositori ini:
   git clone https://github.com/username/hand-gesture-audio-player.git
   cd hand-gesture-audio-player

2. Buat Virtual Environment (venv):
   python -m venv venv

3. Aktifkan Virtual Environment:
   - Windows:
     venv\Scripts\activate
   - macOS/Linux:
     source venv/bin/activate

4. Instal library yang diperlukan:
   pip install opencv-python mediapipe pygame

5. Pastikan file audio berikut berada di folder root proyek:
   - Berjuang.mp3
   - Selamat.mp3
   - Sukses.mp3

## Cara Menjalankan

Jalankan skrip utama dengan perintah:
python custom_gesture_bot.py

Setelah jendela kamera terbuka:
- Tunjukkan gestur tangan sesuai daftar di atas.
- Tekan tombol 'q' pada keyboard untuk menghentikan aplikasi dan menutup kamera.

## Struktur File

- custom_gesture_bot.py: Skrip utama aplikasi.
- Berjuang.mp3: Audio untuk gestur kepalan tangan.
- Selamat.mp3: Audio untuk gestur telapak tangan terbuka.
- Sukses.mp3: Audio untuk gestur dua jempol.
- .gitignore: Daftar file yang tidak diunggah ke repositori.
- README.md: Dokumentasi proyek.
