import sys

text="""hb xtk biw ewkb oy bhrwk, hb xtk biw xoukb oy bhrwk, hb xtk biw tlw oy xhkqor, hb xtk biw tlw oy
yoophkiawkk, hb xtk biw wsofi oy ewphwy, hb xtk biw wsofi oy hafuwqvphbm, hb xtk biw kwtkoa oy
phlib, hb xtk biw kwtkoa oy qtucawkk, hb xtk biw ksuhal oy iosw, hb xtk biw xhabwu oy qwksthu, xw itq
wzwumbihal ewyouw vk, xw itq aobihal ewyouw vk, xw xwuw tpp lohal qhuwfb bo iwtzwa, xw xwuw
tpp lohal qhuwfb biw obiwu xtm  ha kioub, biw swuhoq xtk ko ytu phcw biw suwkwab swuhoq, bitb
korw oy hbk aohkhwkb tvbiouhbhwk hakhkbwq oa hbk ewhal uwfwhzwq, you looq ou you wzhp, ha biw
kvswuptbhzw qwluww oy forstuhkoa oapm.
"""


#it was the best of times, it was the worst of times, it was the age of wisdom, it was the age of
#foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of
#light, it was the season of darkness, it was the spring of hope, it was the winter of despair, we had
#everything before us, we had nothing before us, we were all going direct to heaven, we were
#all going direct the other way  in short, the period was so far like the present period, that
#some of its noisiest authorities insisted on its being received, for good or for evil, in the
#superlative degree of comparison only.'


text.lower()
#      abcdefghijklmnopqrstuvwxyz
key = "tefqwylih*cpraos*ukbvzx*m*"

for c in list(text):
    where=key.find(c)
    if where < 0:
        if c not in list(str("abcdefjhijklmnopqrstuvwxyz")):
            sys.stdout.write(c)
        else:
            sys.stdout.write(c)
    else:
        sys.stdout.write(chr(ord('a')+ where))

