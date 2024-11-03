
def list_operations():
    cartoons = ["Tom&Jerry", "Dragon Tales", "Scooby-Doo!"]
    cartoons.append("The Powerpuff Girls")
    print("List after addition:", cartoons)
    cartoons.insert(1, "Courage")
    print("List after insertion:", cartoons)
    sliced_list = cartoons[2:4]
    print("Sliced list:", sliced_list)
list_operations()

# OUTPUT:
# List after addition: ['Tom&Jerry', 'Dragon Tales', 'Scooby-Doo!', 'The Powerpuff Girls']
# List after insertion: ['Tom&Jerry', 'Courage', 'Dragon Tales', 'Scooby-Doo!', 'The Powerpuff Girls']
# Sliced list: ['Dragon Tales', 'Scooby-Doo!']
