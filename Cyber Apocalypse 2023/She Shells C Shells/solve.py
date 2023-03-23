t = '2c 4a b7 99 a3 e5 70 78 93 6e 97 d9 47 6d 38 bd ff bb 85 99 6f e1 4a ab 74 c3 7b a8 b2 9f d7 ec eb cd 63 b2 39 23 e1 84 92 96 09 c6 99 f2 58 fa cb 6f 6f 5e 1f be 2b  13 8e a5 a9 99 93 ab 8f 70 1c c0 c4 3e a6 fe 93 35 90 c3 c9 10 e9'
m1 = '6e 3f c3 b9 d7 8d 15 58 e5 0f fb ac 22 4d 57 db df cf ed fc 1c 84 6a d8 1c a6 17 c4 c1 bf a0 85 87 a1 43 d4 58 4f 8d a8 b2 f2 7c a3 b9 86 37 da bf 07 0a 7e 73 df 5c 60 ae ca cf b9 e0 de ff 00 70 b9 e4 5f c8 9a b3 51 f5 ae a8 7e 8d'
m2 = '64 1e f5 e2 c0 97 44 1b f8 5f f9 be 18 5d 48 8e 91 e4 f6 f1 5c 8d 26 9e 2b a1 02 f7 c6 f7 e4 b3 98 fe 57 ed 4a 4b d1 f6 a1 eb'

t_bytes = bytes.fromhex(t)
m2_bytes = bytes.fromhex(m2)
m1_bytes = bytes.fromhex(m1)

result1 = bytes(a ^ b for (a, b) in zip(t_bytes, m1_bytes))
result2 = bytes(a ^ b for (a, b) in zip(t_bytes, m2_bytes))

print(f"Password: {result1.decode('utf-8')}")
print(f"Flag: {result2.decode('utf-8')}")