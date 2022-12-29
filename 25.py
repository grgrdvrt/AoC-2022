input = open("input_25").read()

snafuToDecMap = {"2":2,"1":1,"0":0,"-":-1,"=":-2}
def snafuToDec(snafu):
    nums = [snafuToDecMap[c] for c in snafu][::-1]
    return sum([5**i * num for i, num in enumerate(nums)])

decToSnafuMap = ["0", "1", "2", "=", "-"]
def decToSnafu(dec):
    s = ""
    v = dec
    while v > 0:
        m = v % 5
        s = decToSnafuMap[m] + s
        v = v // 5 + (m >= 3)
    return s


print(decToSnafu(sum([snafuToDec(n) for n in input.strip().split("\n")])))
