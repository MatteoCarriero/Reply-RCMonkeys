file_path = "input/00-trailer.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

# Extracting values from the first line
values = lines[0].split()
wtemp = ""
for c in values[0]:
    if c.isnumeric():
        wtemp += c
W = int(wtemp)
H = int(values[1])
GN = int(values[2])
SM = int(values[3])
TL = int(values[4])

print(f"W: {W}")
print(f"H: {H}")
print(f"GN: {GN}")
print(f"SM: {SM}")
print(f"TL: {TL}")