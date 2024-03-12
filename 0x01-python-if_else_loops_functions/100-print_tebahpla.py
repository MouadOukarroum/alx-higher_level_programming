#!/usr/bin/python3
tebahpla = []
for i in reversed(range(97, 123)):
    if i % 2 == 0:
        tebahpla.append(chr(i))
    else:
        tebahpla.append(chr(i - 32))
print("{}".format("".join(tebahpla)), end="")
