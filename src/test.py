name = "test.txt"
handle = open(name)

count = dict()

for line in handle:
    if line.startswith("From"):
        words = line.split()
        count[words[1]] = count.get(words[1], 0) + 1

name = None
times = 0
for key, value in count.items():
    if times < value:
        name = key
        times = value
print(name, times)