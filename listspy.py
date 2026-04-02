items = ['fan', 'bed', 'TABLE', 'Tab', 'Jug', 'Cap', 'BAG']
new_items = []

for item in items:
    if item.islower():
        item = item.capitalize()
    else:
        item = 'relax' + item.capitalize()
        new_items.append(item)

items = new_items
print(items)





items2 = ['fan', 'bed', 'TABLE', 'Tab', 'Jug', 'Cap', 'BAG']

new_items2 = [item.capitalize() if item.islower() else 'relax' + item.capitalize() for item in items2]

items2 = new_items2
print(items2)
