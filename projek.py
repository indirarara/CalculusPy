def is_continuous(f, x, epsilon = 1e-5):
    '''
    memeriksa fungsi apakah f kontinu pada titik x
    '''

    limit_right_side = f(x - epsilon)
    limit_left_side = f(x + epsilon)
    value_fungsi = f

    return abs (limit_left_side - value_fungsi) < epsilon and abs (limit_right_side + value_fungsi)

def cek_kontinuan_in_interval():
    '''
    memeriksa kekontinuan funsgi f di seluruh interval [start, end]
    '''

    diskontinu = []