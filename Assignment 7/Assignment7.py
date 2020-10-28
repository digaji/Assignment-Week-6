def avg_length(filename):
    """
    Returns average word length of text from a file

    Args:
        filename (str): Name of the original text file

    Returns:
        [int]: Average word length
    """
    y = []
    count = 0
    with open(filename, "r", encoding="utf-8") as file:
        for word in file:
            y += word.split() # Adds each word into one list
        for i in y:
            count += len(i) # Counts the length of each word
        return count / len(y) # Divides the length of each word by the number of words


print(avg_length("Adventures of Huckleberry Finn.txt"))