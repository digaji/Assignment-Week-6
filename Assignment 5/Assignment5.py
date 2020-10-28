def hapax(filename):
    """
    Returns a list with all the words that occurs only once from a text file

    Args:
        filename (str): Name of the text file

    Returns:
        (list): Words that occur only once
    """
    with open(filename, "r", encoding = "utf-8") as file: # Opens the text file and then closes it after finishing the function
        hapaxes = []
        y = []
        for word in file:
            x = word.lower().split() # List with words splitted and lowercased. Still in the format of multiple lists
            for i in x:
                    if i.isalpha(): # Checks if word is an alphabetic string
                        y.append(i) # Appends to empty list that combines all the words from the multiple lists
        for i in y:
            if y.count(i) == 1: # Checks if word appears once or not
                hapaxes.append(i) # Appends to list of hapaxes
        return hapaxes

print(hapax("Adventures of Huckleberry Finn.txt"))