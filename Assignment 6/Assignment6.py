def numbered_lines(filename):
    """
    Creates a new text file with numbered lines from an existing text file

    Args:
        filename (str): Name of the original text file
    """
    i = 1
    with open(filename, "r", encoding="utf-8") as file:
        with open(f"numbered_{filename}", "w", encoding="utf-8") as new: # Opening a new file with the format numbered_OriginalFileName.txt
            for line in file.readlines(): # Reads the lines from the original file one by one
                new.write(str(i) + " " + line) # Writes the number associated with the line starting from 1
                i += 1

numbered_lines("No. 6.txt")