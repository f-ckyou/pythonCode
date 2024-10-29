def is_unique_chars(string):
    unique_chars = set()
    for char in string:
        if char in unique_chars:
            return "NO"
        unique_chars.add(char)
    return "YES"

T = int(input())

results = []

for _ in range(T):
    string = input()
    results.append(is_unique_chars(string))

print("\n".join(results))
