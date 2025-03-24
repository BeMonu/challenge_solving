# Remove duplicates from a list.

a = ['fork', 'soap', 'fork']
new_a = []
seen = set()

for i in a:
    if i not in seen:
        new_a.append(i)
        seen.add(i)

print(new_a)
