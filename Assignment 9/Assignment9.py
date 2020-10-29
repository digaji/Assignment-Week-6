from re import sub

def sep_lines(filename):
    with open(filename, "r", encoding="utf-8") as f:
        with open(f"line_{filename}", "w", encoding="utf-8") as new:
            file = f.read()
            # Writes over the new text file with the old text, but replacing whitespace that meets the conditions with regex
            new.write(sub(r"(?<=[^A-Z].[.?]) +(?=[A-Z\"])", "\n", file))

sep_lines("shorttext.txt")