import math

def trigonometri (sudut_derajat):
    sudut_radians = math.radians(sudut_derajat)

    sin = math.sin(sudut_radians)
    cos = math.cos(sudut_radians)
    tan = math.tan(sudut_radians)

    cot = None if tan == 0 else 1/tan
    sec = None if cos == 0 else 1/cos
    csc = None if sin == 0 else 1/sin

    return {
        "sudut (derajat)": sudut_derajat,
        "sin": sin,
        "cos": cos,
        "tan": tan,
        "cot": cot,
        "sec": sec,
        "csc": csc
    }

def penyesualian_sudut_dengan_kuadran (sudut, kuadran):
    if kuadran == 1:
        return sudut
    elif kuadran == 2:
        return 180 - sudut
    elif kuadran == 3:
        return 180 + sudut
    elif kuadran == 4:
        return 360 - sudut
    else:
        return None

def main():
    try:
        sudut = float(input("Masukkan sudut (dalam derajat): "))
        kuadran = int(input("Masukkan kuadran (1-4): "))

        if kuadran not in [1, 2, 3, 4]:
            print("Kuadran hanya bisa 1-4.")
            return

        penyesuaian_sudut = penyesualian_sudut_dengan_kuadran (sudut, kuadran)

        if penyesuaian_sudut is None:
            print("Sudut tidak valid.")
            return

        result = trigonometri (penyesuaian_sudut)

        print(f"Sudut asli: {sudut} derajat")
        print(f"Sudut setelah disesuaikan di kuadran {kuadran}: {penyesuaian_sudut} derajat")
        print(f"sin: {result['sin']}")
        print(f"cos: {result['cos']}")
        print(f"tan: {result['tan']}")
        print(f"cot: {result['cot']}")
        print(f"sec: {result['sec']}")
        print(f"csc: {result['csc']}")

    except:
        print("Input tidak valid, pastikan Anda memasukkan angka.")

main()
