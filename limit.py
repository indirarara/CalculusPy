import sympy as sp

def hitung_limit_kanan_kiri():
    # Meminta input beberapa fungsi dari pengguna, dipisahkan dengan koma
    fungsi_str = input("Masukkan fungsi-fungsi dengan kondisi, dipisahkan dengan koma (contoh: (x-2)/(x+3) jika x<1, x**2 + 3*x jika x>=1): ")
    
    # Meminta input titik di mana limit akan dihitung
    titik_str = input("Masukkan titik untuk menghitung limit: ")
    
    # Mendefinisikan variabel
    x = sp.Symbol('x')
    
    # Memisahkan fungsi berdasarkan koma
    fungsi_kondisi_list = fungsi_str.split(',')
    
    # Daftar untuk menyimpan kondisi fungsi
    kondisi_pieces = []
    
    # Mengubah input string titik menjadi angka (float/int)
    titik = float(titik_str)
    
    # Loop untuk setiap fungsi dengan kondisi
    for fungsi_kondisi in fungsi_kondisi_list:
        # Memisahkan fungsi dan kondisinya
        if "jika" in fungsi_kondisi:
            fungsi_part, kondisi_part = fungsi_kondisi.split("jika")
            fungsi = sp.sympify(fungsi_part.strip())  # Mengubah fungsi menjadi simbolik
            kondisi = sp.sympify(kondisi_part.strip())  # Mengubah kondisi menjadi simbolik
            kondisi_pieces.append((fungsi, kondisi))  # Menambahkan fungsi dan kondisinya ke daftar
        else:
            # Jika tidak ada kondisi, anggap fungsi berlaku secara umum
            fungsi = sp.sympify(fungsi_kondisi.strip())
            kondisi_pieces.append((fungsi, True))  # Kondisi 'True' berarti berlaku umum
    
    # Menggunakan Piecewise untuk mendefinisikan fungsi bagian
    fungsi_piecewise = sp.Piecewise(*kondisi_pieces)
    
    # Menghitung limit kanan (x mendekati titik dari kanan)
    limit_kanan = sp.limit(fungsi_piecewise, x, titik, dir='+')
    
    # Menghitung limit kiri (x mendekati titik dari kiri)
    limit_kiri = sp.limit(fungsi_piecewise, x, titik, dir='-')
    
    # Menampilkan hasil limit kanan dan kiri
    print(f"\nFungsi dengan kondisi: {fungsi_piecewise}")
    print(f"Limit kanan dari f(x) ketika x mendekati {titik} adalah {limit_kanan}")
    print(f"Limit kiri dari f(x) ketika x mendekati {titik} adalah {limit_kiri}")

# Memanggil fungsi untuk pengguna
hitung_limit_kanan_kiri()
