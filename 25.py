input = open("input_25").read()

snafuToDecMap = {"2":2,"1":1,"0":0,"-":-1,"=":-2}
def snafuToDec(snafu):
    nums = [snafuToDecMap[c] for c in snafu][::-1]
    val = 0
    for i, num in enumerate(nums):
        val += 5**i * num
    return val

decToSnafuMap = ["0", "1", "2", "=", "-"]
def decToSnafu(dec):
    s = ""
    v = dec
    while True:
        m = v % 5
        s = decToSnafuMap[m] + s
        v = v // 5
        if m >= 3: v += 1
        if v <= 0 : break
    return s


print(decToSnafu(sum([snafuToDec(n) for n in input.strip().split("\n")])))
