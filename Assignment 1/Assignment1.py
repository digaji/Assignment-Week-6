inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

# Add a key to inventory called 'pocket'
# Set value of 'pocket' to be a list with strings 'seashell', 'strange berry', and 'lint'
# .sort() items in the list stored under 'backpack' key
# .remove('dagger') from the list under 'backpack' key
# Add 50 to 'gold' key

inventory['pocket'] = []
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50