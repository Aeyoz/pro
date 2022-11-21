import sys

values = sys.argv[1:]
values = [int(v) for v in values]
media = sum(values) / len(values)
print(f"{media:0.2f}")