def all_variants(text):
    n = len(text)
    for i in range(1, 2**n):
        subset = [text[j] for j in range(n) if (i & (1 << j))]
        yield ''.join(subset)


a = all_variants("abc")
for i in a:
    print(i)
