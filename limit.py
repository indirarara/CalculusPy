import sympy as sp

def find_limit(func_str, var_str, point):
    """
    Mencari limit kanan dan limit kiri dari suatu fungsi pada titik tertentu.

    Parameters:
    func_str : str
        Fungsi yang ingin dicari limitnya (dalam bentuk string).
    var_str : str
        Variabel independen dalam fungsi (misal: 'x').
    point : float or int
        Titik di mana limit ingin dihitung.

    Returns:
    tuple : (limit kanan, limit kiri)
        Hasil limit kanan dan limit kiri dari fungsi pada titik yang diberikan.
    """
    # Definisikan variabel dan fungsi dari input pengguna
    var = sp.symbols(var_str)
    func = sp.sympify(func_str)  # Konversi string fungsi menjadi ekspresi sympy

    # Cari limit kanan (dir='+') dan limit kiri (dir='-')
    limit_right = sp.limit(func, var, point, dir='+')
    limit_left = sp.limit(func, var, point, dir='-')

    return limit_right, limit_left

# Contoh penggunaan
if __name__ == "__main__":
    # Input dari pengguna
    func_str = input("Masukkan fungsi (misal: 1/x atau x**2): ")
    var_str = input("Masukkan variabel (misal: x): ")
    point = float(input("Masukkan titik di mana limit ingin dihitung (misal: 0): "))

    # Mencari limit kanan dan kiri
    limit_kanan, limit_kiri = find_limit(func_str, var_str, point)

    # Menampilkan hasil
    print(f"Limit kanan dari {func_str} saat {var_str} mendekati {point}: {limit_kanan}")
    print(f"Limit kiri dari {func_str} saat {var_str} mendekati {point}: {limit_kiri}")
