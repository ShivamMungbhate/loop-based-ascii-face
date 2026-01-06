WIDTH = 80

def center(s):
    return s.center(WIDTH)

# ===== TOP BACKGROUND =====
for _ in range(2):
    print(" " * WIDTH)

# ===== REALISTIC HAIR =====
hair_layers = [
    "@@##$$%%&&**",         # dense top
    "@@##$$%%&&**==",       # slightly wider
    "@@##$$%%&&**==--",     # with shine
    "@@##$$%%&&**==--..",   # fade
]

for layer in hair_layers:
    print(center(layer * 3))  # repeat for volume

# ===== FOREHEAD =====
for _ in range(2):
    print(center("@" * 30))

for _ in range(2):
    print(center("." * 32))

# ===== EYE REGION =====
print(center("." * 34))

# ===== EYES =====
print(center("...   -          -   ..."))
print(center("...   -          -   ..."))

# ===== GLASSES =====
print(center("==-=======-==    ==-=======-=="))
print(center("==-=======-==    ==-=======-=="))

# ===== EARS + UPPER CHEEKS =====
for _ in range(2):
    print(center(" ( )   .   .   .   .   .   .   ( ) "))

# ===== CHEEKS (ROUND FACE) =====
for _ in range(2):
    print(center("  ( )   .   .   .   .   .   .   ( )  "))

# ===== NOSE =====
print(center("        |||        "))
print(center("      ((|||))      "))

# ===== LOWER CHEEKS =====
for _ in range(2):
    print(center("  ( )   .   .   .   .   .   .   ( )  "))

# ===== MOUTH =====
print(center("       .    ___    .       "))
print(center("            -----            "))

# ===== JAW (ROUNDED) =====
for _ in range(2):
    print(center("    ( )      .      ( )    "))

# ===== CHIN =====
print(center("         .........         "))
print(center("           .......           "))

# ===== LOWER FACE FADE =====
for w in [26, 24, 22]:
    print(center("." * w))

# ===== NECK =====
print(center("            |||            "))
print(center("            |||            "))

# ===== SHOULDERS / JACKET =====
print(center("=" * 42))
print(center("=" * 46))
print(center("=" * 50))