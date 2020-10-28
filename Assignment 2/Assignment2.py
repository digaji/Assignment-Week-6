prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}  # There was no information about stocks in the word doc, so I added assignment 3's one

for key in prices: # Iterates through all 4 keys in prices
    print(key, f"price: {prices.get(key)}", f"stock: {stock.get(key)}", sep="\n") # Prints all the info in 3 different lines. Utilized f-Strings for the formatting

total = 0
for key in prices:
    x = prices.get(key) * stock.get(key) # Multiplies value with stock and adds it to total
    print(x)
    total += x
print(total)