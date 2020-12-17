# this function takes in a string and the no of character to shift.
def ceasar_cephar(s, n):
    a = ''
    for i in s.upper():
        if i.isalpha() is False:
            a += i
            continue
        if ord(i) + n <= 90:
            a += chr(ord(i) + n)
        else:
            a += chr(ord(i) + n - 90 + 65)
    return a.lower()


print(ceasar_cephar('hello world', 5))
