name = "test.txt"
handle = open(name)
result = dict()

for line in handle:
    if line.startswith("From"):
        words = line.split()
        try:
            time = words[5].split(":")
            hour = time[0]
            result[hour] = result.get(hour, 0) + 1
        except:
            continue

for hour, count in result.items():
    print(hour, count)

"""
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
    """