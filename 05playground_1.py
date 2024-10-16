cisla_in = input().split()
cisla = []

for i in cisla_in:
    cisla.append(float(i))

avg_cisla = sum(cisla) / len(cisla)


if (len(cisla) % 2) == 1:                         # nefunguje ti pocitanie medianu
    median_cisla = cisla[(len(cisla)) // 2]
else:
    med1 = cisla[(len(cisla) // 2) - 1]
    med2 = cisla[(len(cisla) // 2)]
    median_cisla = (med1 + med2) / 2

print(f"Min: {min(cisla):>9.2f}")
print(f"Max: {max(cisla):>9.2f}")
print(f"Mean:{avg_cisla:>9.2f}")
print(f"Median:{median_cisla:>7.2f}")



# Vzorové vstupy pro kopírování:
# 150 13 7 10 11
# 1 2 3 4 8 9