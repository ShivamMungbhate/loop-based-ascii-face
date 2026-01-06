WIDTH = 80

def center(s):
    return s.center(WIDTH)

# === TOP HEAD ===
head_layers = [20, 24, 28, 32, 36, 40, 44]
for w in head_layers:
    print(center("#" * w))

# === FOREHEAD ===
for _ in range(2):
    print(center("@" * 44))

# === EYES REGION ===
print(center("%%%   0     0   %%%"))
print(center("%%%   0     0   %%%"))

# === GLASSES / FRAME ===
for _ in range(2):
    print(center("===$$$$$$===   ===$$$$$$==="))

# === CHEEKS ===
for _ in range(2):
    print(center(" ( )   ^   ^   ^   ^   ^   ( ) "))

# === NOSE ===
print(center("        |||        "))
print(center("      ((|||))      "))

# === MOUTH ===
print(center("       .   ---   .       "))
print(center("       .   ___   .       "))

# === JAW ===
for _ in range(2):
    print(center("    ( )   ^^^   ( )    "))

# === CHIN ===
print(center("         &&&&&&&&&         "))
print(center("           &&&&&           "))

# === LOWER FADE ===
for w in [28, 26, 24]:
    print(center("*" * w))

# === NECK ===
print(center("            |||            "))
print(center("            |||            "))

# === SHOULDERS ===
print(center("=" * 44))
print(center("=" * 48))
print(center("=" * 52))