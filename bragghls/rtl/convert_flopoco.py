import flopoco_converter


def convert_float_to_flopoco_binary_str(f, width_exp=4, width_frac=4):
    s = flopoco_converter.fp2bin(width_exp, width_frac, str(f))
    assert len(s) == width_exp + width_frac + 2 + 1
    return s


def convert_flopoco_binary_str_to_float(s, width_exp=4, width_frac=4):
    assert len(s) == width_exp + width_frac + 2 + 1
    return float(flopoco_converter.bin2fp(width_exp, width_frac, s))


if __name__ == "__main__":
    for i in range(100):
        print("#", i, f"b{convert_float_to_flopoco_binary_str(i)}")

# 0 b00000000000
# 1 b01001110000
# 2 b01010000000
# 3 b01010001000
# 4 b01010010000
# 5 b01010010100
# 6 b01010011000
# 7 b01010011100
# 8 b01010100000
# 9 b01010100010
# 10 b01010100100
# 11 b01010100110
# 12 b01010101000
# 13 b01010101010
# 14 b01010101100
# 15 b01010101110
# 16 b01010110000
# 17 b01010110001
# 18 b01010110010
# 19 b01010110011
# 20 b01010110100
# 21 b01010110101
# 22 b01010110110
# 23 b01010110111
# 24 b01010111000
# 25 b01010111001
# 26 b01010111010
# 27 b01010111011
# 28 b01010111100
# 29 b01010111101
# 30 b01010111110
# 31 b01010111111
# 32 b01011000000
# 33 b01011000000
# 34 b01011000001
# 35 b01011000010
# 36 b01011000010
# 37 b01011000010
# 38 b01011000011
# 39 b01011000100
# 40 b01011000100
# 41 b01011000100
# 42 b01011000101
# 43 b01011000110
# 44 b01011000110
# 45 b01011000110
# 46 b01011000111
# 47 b01011001000
# 48 b01011001000
# 49 b01011001000
# 50 b01011001001
# 51 b01011001010
# 52 b01011001010
# 53 b01011001010
# 54 b01011001011
# 55 b01011001100
# 56 b01011001100
# 57 b01011001100
# 58 b01011001101
# 59 b01011001110
# 60 b01011001110
# 61 b01011001110
# 62 b01011001111
# 63 b01011010000
# 64 b01011010000
# 65 b01011010000
# 66 b01011010000
# 67 b01011010001
# 68 b01011010001
# 69 b01011010001
# 70 b01011010010
# 71 b01011010010
# 72 b01011010010
# 73 b01011010010
# 74 b01011010010
# 75 b01011010011
# 76 b01011010011
# 77 b01011010011
# 78 b01011010100
# 79 b01011010100
# 80 b01011010100
# 81 b01011010100
# 82 b01011010100
# 83 b01011010101
# 84 b01011010101
# 85 b01011010101
# 86 b01011010110
# 87 b01011010110
# 88 b01011010110
# 89 b01011010110
# 90 b01011010110
# 91 b01011010111
# 92 b01011010111
# 93 b01011010111
# 94 b01011011000
# 95 b01011011000
# 96 b01011011000
# 97 b01011011000
# 98 b01011011000
# 99 b01011011001