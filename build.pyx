import marshal

with open("bruh.dat","rb") as fh:
    data = marshal.open(fh)

print(data)

