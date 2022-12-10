"""
SPECS
    iterate through a list of characters

    isolate thed action functionality into a function

    randmoly select action

"""

shopping_list = ['marsmallows', 'chocolate', 'crackers']
selected = [False, True, False]
selected_items = []

for index in range(len(shopping_list)):
    print ( f"{shopping_list[index]} {'has' if selected[index] else 'has not' } been selected.")

simple_dictionary = {
    "key": "value"
}

single_item = {
    "name": "milk",
    "selected": False,
    "junk_food": True
}

print ( single_item['name'] )

print ( f"{single_item['name']} {'has' if single_item['selected'] else 'has not' } been selected.")

#destructuring
name, selected, junk_food = single_item.values()

print ( f"{name} {'has' if selected else 'has not' } been selected.")

new_shopping_list = [
    {
        "name": "milk",
        "selected": False
    },
    {
        "name": "Chocolate",
        "selected": True
    },
    {
        "name": "crackers",
        "selected": False
    }
]

#iterate
for item in new_shopping_list:
    print(f"{item['name']")