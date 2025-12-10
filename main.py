# 6 - Masala
kub = [i ** 3 for i in range(1, 6)]
print(kub)

# 7 - Masala
harf = ["dog", "cat", "mouse"]
bosh_harf = [s[0] for s in harf]
print(bosh_harf)

# 8 - Masala
musbat = [-5, 3, -1, 0, 7, -2]
musbat_son = [i for i in musbat if i > 0]
print(musbat_son)

# 9 - Masala
belgi = ["juft" if i % 2 == 0 else "toq" for i in range(1, 11)]
print(belgi)

# 10 - Masala
import math

sonlar = [4, 9, 16, 25]
kvadrat_ildizlar = [math.sqrt(i) for i in sonlar]

print(kvadrat_ildizlar)
