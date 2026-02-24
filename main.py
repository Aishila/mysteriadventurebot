import time
import random

# ANSI color codes
RESET = "\u001b[0m"
GREEN = "\u001b[32m"
RED = "\u001b[31m"
YELLOW = "\u001b[33m"
CYAN = "\u001b[36m"

# Probabilities for success per choice (configurable)
PROB_LEMBAH_A = 0.85
PROB_LEMBAH_B = 0.75
PROB_GUNUNG_A = 0.80
PROB_GUNUNG_B = 0.70


def cetak(teks, delay=0.5, warna=None, emoji=None):
    """Print with optional color, emoji and delay."""
    pref = warna if warna else ""
    suf = RESET if warna else ""
    em = f" {emoji}" if emoji else ""
    print(f"{pref}{teks}{em}{suf}")
    time.sleep(delay)


# ASCII art
SWORD = r'''
        /\
       ||
       ||
       ||
       ||
       ||
      /||\
     //||\\
    // || \\
   ||  ||  ||
   ||  ||  ||
    \\_||_//
      `--'
'''

SKULL = r"""
  .-''''-.
 /  .--.  \
/  /    \  \
|  |    |  |
|  |.-""-.|
///`.::::.`\\\
||| ::/  \:: |||
||; ::\__/:: ;||
 \\\'::::'//'
  `='----'=`
"""


def game_utama():
    nyawa = 100
    cetak("--- MEMULAI PETUALANGAN DIGITAL ---", warna=CYAN, emoji="🎮")
    nama = input("Siapa namamu? ")
    cetak(f"Selamat datang, {nama}! Pilih jalur petualanganmu:", warna=GREEN, emoji="✨")
    cetak("1. Lembah Coding", warna=YELLOW, emoji="💻")
    cetak("2. Gunung Bug", warna=YELLOW, emoji="🐛")
    pilihan = input("Ketik 1 atau 2: ").strip()

    if pilihan == "1":
        cetak("\nKamu memasuki Lembah Coding — baris-baris kode berkilau di padang.", warna=CYAN, emoji="💡")
        cetak("Di sana ada teka-teki sintaks yang menunggu. Apa yang akan kamu lakukan?", warna=CYAN)
        # Validasi input: hanya terima 'a' atau 'b'
        attempts = 0
        aksi = ""
        while attempts < 3:
            aksi = input("a) Membaca dokumentasi\nb) Menulis tes\nPilih a atau b: ").strip().lower()
            if aksi in ("a", "b"):
                break
            attempts += 1
            cetak("Input tidak valid. Ketik 'a' atau 'b'.", warna=YELLOW, emoji="⚠️")

        if aksi in ("a", "b"):
            prob = PROB_LEMBAH_A if aksi == "a" else PROB_LEMBAH_B
            if random.random() < prob:
                cetak("Keberuntungan berpihak padamu! Kamu berhasil menyelesaikan tantangan.", warna=GREEN, emoji="🏆")
                cetak(SWORD, delay=0.2, warna=CYAN)
            else:
                nyawa -= 20
                cetak(f"Sayang sekali, gagal kali ini. Nyawa -20. Sisa nyawa: {nyawa}", warna=RED, emoji="💥")
                if nyawa <= 0:
                    cetak("Nyawa habis. Game over.", warna=RED, emoji="💀")
                    cetak(SKULL, delay=0.2, warna=RED)
                    return nyawa
        else:
            nyawa -= 20
            cetak(f"Terlalu banyak input tidak valid. Nyawa -20. Sisa nyawa: {nyawa}", warna=RED, emoji="❓")

    elif pilihan == "2":
        cetak("\nKamu mendaki Gunung Bug — kabut error memenuhi udara.", warna=YELLOW, emoji="🌫️")
        cetak("Sebuah stack trace menghalangi jalan. Apa yang kamu lakukan?", warna=YELLOW)
        # Validasi input: hanya terima 'a' atau 'b'
        attempts = 0
        aksi = ""
        while attempts < 3:
            aksi = input("a) Debug langkah demi langkah\nb) Menggunakan log\nPilih a atau b: ").strip().lower()
            if aksi in ("a", "b"):
                break
            attempts += 1
            cetak("Input tidak valid. Ketik 'a' atau 'b'.", warna=YELLOW, emoji="⚠️")

        if aksi in ("a", "b"):
            prob = PROB_GUNUNG_A if aksi == "a" else PROB_GUNUNG_B
            if random.random() < prob:
                cetak("Berhasil! Kamu menaklukkan bug itu.", warna=GREEN, emoji="🛠️")
                cetak(SWORD, delay=0.2, warna=CYAN)
            else:
                nyawa -= 20
                cetak(f"Usahamu belum cukup. Nyawa -20. Sisa nyawa: {nyawa}", warna=RED, emoji="😵")
                if nyawa <= 0:
                    cetak("Nyawa habis. Game over.", warna=RED, emoji="💀")
                    cetak(SKULL, delay=0.2, warna=RED)
                    return nyawa
        else:
            nyawa -= 20
            cetak(f"Terlalu banyak input tidak valid. Nyawa -20. Sisa nyawa: {nyawa}", warna=RED, emoji="❓")

    else:
        nyawa -= 20
        cetak(f"Pilihan tidak dikenali. Nyawa -20. Sisa nyawa: {nyawa}", warna=RED, emoji="❓")

    if nyawa <= 0:
        cetak("Nyawa habis. Game over.", warna=RED, emoji="💀")
        cetak(SKULL, delay=0.2, warna=RED)
        return nyawa

    cetak("\nTerima kasih telah bermain!", warna=CYAN, emoji="🎉")
    return nyawa


if __name__ == "__main__":
    while True:
        game_utama()
        while True:
            lagi = input("\nMain lagi? (y/n): ").strip().lower()
            if not lagi:
                continue
            c = lagi[0]
            if c == 'y':
                play_again = True
                break
            if c in ('n', 't'):
                play_again = False
                break
            cetak("Masukan tidak dikenali. Ketik y/yes/ya atau n/no/tidak.", warna=YELLOW, emoji="⚠️")
        if not play_again:
            cetak("Sampai jumpa!", warna=GREEN, emoji="👋")
            break
