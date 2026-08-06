"""aeiou"""
name = input().lower()
a = name.count("a")
e = name.count("e")
i = name.count("i")
o = name.count("o")
u = name.count("u")
if a:
    print(f"a : {a}")

if e:
    print(f"e : {e}")

if i:
    print(f"i : {i}")

if o:
    print(f"o : {o}")

if u:
    print(f"u : {u}")
