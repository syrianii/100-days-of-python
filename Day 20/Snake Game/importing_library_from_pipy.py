from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon",["Pikatchu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "r"
print(table)
