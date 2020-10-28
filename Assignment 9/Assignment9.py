import re

def sep_lines(filename):
    with open(filename, "r", encoding="utf-8") as f:
        with open(f"line_{filename}", "w", encoding="utf-8") as new:
            file = f.read()
            new.write(re.sub(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', "\n", file))

sep_lines("shorttext.txt")