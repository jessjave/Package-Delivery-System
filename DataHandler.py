import csv


# creates dictionary with 2 addresses as keys and a distance as a value
# O(n^2) time and space
def create_dictionaries():
    # Initialize empty lists for addresses and distances
    addresses_1 = []
    addresses_2 = []
    distances = []

    # Loop through the first file and add the addresses to the first list
    with open('Addresses.csv') as file1:
        reader = csv.reader(file1)
        for row in reader:
            addresses_1.append(row[0])

    # Loop through the second file and add the addresses to the second list
    with open('Addresses.csv') as file2:
        reader = csv.reader(file2)
        for row in reader:
            addresses_2.append(row[0])

    # Loop through the third file and add the distances to the distances list
    with open('Distances.csv', newline='') as file3:
        reader = csv.reader(file3, delimiter=',')
        for row in reader:
            distances.append(row)

    # Create a dictionary with every combination of addresses as keys and distances as values
    address_distances = {}
    for i, address_1 in enumerate(addresses_1):
        for j, address_2 in enumerate(addresses_2):
            distance = distances[i][j]
            key = (address_1, address_2)
            if distance != "":
                address_distances[key] = distance

    return address_distances

    # Print the resulting dictionary
    # for key, value in address_distances.items():
        # print(key, value)


# look up address
# O(n) time and O(1) space
def address_lookup(address):
    # Read the addresses from the CSV file and find the index of the given address
    with open('Addresses.csv') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if row[0].lower() == address.lower():
                return i

    # If the address is not found, return none
    return None


