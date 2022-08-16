import io
import sys

# globe variables
kanji_table = []
pin_yin_s = sys.argv


def look_up(pinyin, table):
    result = []
    for t in table:
        if pinyin == t[0]:
            result.append(t)
    return result


def print_kana(kana):
    for k in kana:
        print(k[1], " -- ", k[2])
    print("\n")


if len(pin_yin_s) == 1:
    print("please type PinYin to look up Kanji/Kana")
    exit(1)

with open('kanji.txt', 'r', encoding='utf-16') as f:
    lines = f.readlines()
    for line in lines:
        token = line.strip('\n').split('\t')
        kanji_table.append(token)
f.close()

# kana = look_up("ai", kanji_table)
# print(kana)
for py in pin_yin_s:
    r = look_up(py, kanji_table)
    if len(r) > 0:
        print(r[0][0] + ":")
        print_kana(r)
