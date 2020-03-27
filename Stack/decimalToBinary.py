from stack import Stack


def convert_int_to_bin(dec_num):
    s = Stack()
    dec_num = int(dec_num)
    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num