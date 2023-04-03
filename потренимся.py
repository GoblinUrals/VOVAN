
string = """Python is cool
            Python is easy
            Python is mighty
            """
list = []
for line in string.split("\n"):
    if not line.strip():
        continue
    list.append(line.lstrip())
print(list)
# ['Python is cool', 'Python is easy', 'Python is mighty']
