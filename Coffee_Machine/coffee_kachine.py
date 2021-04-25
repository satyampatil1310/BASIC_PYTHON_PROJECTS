from prettytable import PrettyTable
table = PrettyTable()
table.field_names=["Pokemon Name","Type"]
table.add_row(['pikachu', 'electric'])
table.add_row(["aquirtle", "water"])
table.add_row(["charmander", "fire"])
print(table)