import base64
from functools import reduce

"""八卦编码器（？"""

num2gua = {1: "乾", 11: "泰", 34: "大壮", 26: "大畜", 14: "大有", 5: "需", 43: "夬", 9: "小畜",
           12: "否", 2: "坤", 16: "豫", 23: "剥", 35: "晋", 8: "比", 45: "萃", 20: "观",
           25: "无妄", 24: "复", 51: "震", 27: "颐", 21: "噬嗑", 3: "屯", 17: "随", 42: "益",
           33: "遁", 15: "谦", 62: "小过", 52: "艮", 56: "旅", 39: "蹇", 31: "咸", 53: "渐",
           13: "同人", 36: "明夷", 55: "丰", 22: "贲", 30: "离", 63: "既济", 49: "革", 37: "家人",
           6: "讼", 7: "师", 40: "解", 4: "蒙", 64: "未济", 29: "坎", 47: "困", 59: "涣",
           10: "履", 19: "临", 54: "归妹", 41: "损", 38: "睽", 60: "节", 58: "兑", 61: "中孚",
           44: "姤", 46: "升", 32: "恒", 18: "蛊", 50: "鼎", 48: "井", 28: "大过", 57: "巽", }
num2hex = {}
for i in range(16):
    num2hex[i] = chr(i + 48) if i < 10 else chr(i + 87)
gua2num = {ele[1]: ele[0] for ele in num2gua.items()}
hex2num = {ele[1]: ele[0] for ele in num2hex.items()}


def num2dec(n, k):
    s = ""
    while n > 0:
        s = str(n % 2) + s
        n = n // 2
    if len(s) < k:
        s = "0" * (k - len(s)) + s
    return s


def dec2num(s):
    ans = 0
    for i in range(len(s)):
        ans = ans * 2 + int(s[i])
    return ans


def encoder(s):
    bs = str(base64.b64encode(s.encode("utf-8")), "utf-8")
    # print(bs)
    dec = [ord(c) for c in bs]
    # print(dec)
    dec = [num2dec(ele, 7) for ele in dec]
    # print(dec)
    dec_str = reduce(lambda a, b: a + b, dec)
    # print(dec_str)
    # 补零
    if len(dec_str) % 6 != 0:
        dec_str += "0" * (6 - len(dec_str) % 6)
    # print(dec_str)
    # print(len(dec_str))
    result = reduce(lambda a, b: a + b, [num2gua[dec2num(dec_str[i * 6:i * 6 + 6])]
                                         for i in range(len(dec_str) // 6)])
    # print(result)
    return result


def decoder(s):
    words = list(filter(lambda s: len(s) > 1, num2gua.values()))
    # print(words)
    first = [e[0] for e in words]
    first = list(set(list(first)))  # 去重
    # print(first)
    for ele in first:
        if list(num2gua.values()).__contains__(ele):
            print("fuck")
    guas = []
    w = ""
    for c in s:
        if first.__contains__(c) and w == "":
            w = c
        else:
            w += c
            guas.append(w)
            w = ""
    # print(guas)
    dec = [num2dec(gua2num[e], 6) for e in guas]
    dec_str = reduce(lambda a, b: a + b, dec)
    if len(dec_str) % 7 > 0:
        dec_str = dec_str[:-(len(dec_str) % 7)]
    ori = [chr(dec2num(dec_str[i * 7:i * 7 + 7])) for i in range(len(dec_str) // 7)]
    ori = reduce(lambda a, b: a + b, ori)
    # print(ori)
    result = str(base64.b64decode(ori), "utf-8")
    # print(result)
    return result


s = "鸽了"

enc = encoder(s)
print(enc)
print(decoder(enc))
