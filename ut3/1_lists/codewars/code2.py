num = 24
to_bin = []
while num >= 1:
    to_bin.append(num % 2)
    num //= 2
to_bin = [str(b) for b in to_bin[::-1]]
to_bin = ''.join(to_bin)
print(to_bin)