import csv
from datetime import timedelta

from DataHandler import create_dictionaries
from Package import Package

# Truck object constructor
class Truck:
    def __init__(self, packages, capacity, speed, miles_driven, current_address, current_time, left_hub):
        self.packages = packages
        self.capacity = capacity
        self.speed = speed
        self.miles_driven = miles_driven
        self.current_address = current_address
        self.current_time = current_time
        self.hub_address = "4001 South 700 East"
        self.left_hub = left_hub

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.packages, self.capacity, self.speed, self.miles_driven,
                                           self.current_address, self.current_time, self.left_hub)

    # Returns a list package objects with the ID and address only for ease of referencing
    # O(n^2) time O(n) space
    def get_package_addresses(self):
        # create an empty list to store all packages
        all_packages = []

        # create an empty list to store package addresses for packages that need to be delivered
        package_addresses = []

        # open the Packages.csv file
        with open('Packages.csv') as package_list:
            # read the csv file using csv.reader
            package_data = csv.reader(package_list, delimiter=',')

            # loop through the packages in the csv file
            for package in package_data:
                # extract the package ID and address from the csv file
                mID = int(package[0])
                mAddress = package[1]

                # create a Package object using the package ID and address
                package_obj = Package(mID, mAddress)

                # append the Package object to the all_packages list
                all_packages.append(package_obj)

        # loop through the package IDs in the truck's packages list
        for package_ID in self.packages:
            # loop through the Package objects in the all_packages list
            for package in all_packages:
                # if the package ID matches the ID of the Package object
                if package.ID == package_ID:
                    # append the package address to the package_addresses list
                    package_addresses.append(package.address)
                    # break out of the inner loop to save time
                    break

        # return the list of package addresses
        return package_addresses

    # Returns a list of all package objects
    # O(n^2) time O(n) space
    def get_all_packages(self):
        # create an empty list to store all packages
        all_packages = []

        # create an empty list to store the packages with the corresponding package IDs
        all_package_objects = []

        # open the Packages.csv file
        with open('Packages.csv') as package_list:
            # read the csv file using csv.reader
            package_data = csv.reader(package_list, delimiter=',')
            # loop through the packages in the csv file
            for package in package_data:
                # extract the package info
                mID = int(package[0])
                mAddress = package[1]
                mCity = package[2]
                mState = package[3]
                mZip = package[4]
                mDelivery_Deadline = package[5]
                mMass = package[6]
                mStatus = "At Hub"

                # package object
                package = Package(mID, mAddress, mCity, mState, mZip, mDelivery_Deadline, mMass, mStatus)

                # append the Package object to the all_packages list
                all_packages.append(package)

                for package_ID in self.packages:
                    # loop through the Package objects in the all_packages list
                    for package in all_packages:
                        # if the package ID matches the ID of the Package object
                        if package.ID == package_ID:
                            # append the package address to the package_addresses list
                            all_package_objects.append(package)
                            # break out of the inner loop to save time
                            break

        # return the list of package objects
        return all_package_objects

    # calculates the distance between two addresses given the dictionary of distances between pairs of addresses
    # O(1) space & time
    def calculate_distance(self, start, end, address_distances, current_address):
        # Check if start address is the same as the current address of the truck
        if start == current_address:
            # If the distance between the current address and the end address has been queried before, use it
            if (current_address, end) in address_distances:
                return address_distances[(current_address, end)]
            # If the distance has not been queried before, check if the opposite direction distance is in the dictionary
            elif (end, current_address) in address_distances:
                return address_distances[(end, current_address)]
        # Check if end address is the same as the current address of the truck
        elif end == current_address:
            # If the distance between the start address and the current address has been queried before, use it
            if (start, current_address) in address_distances:
                return address_distances[(start, current_address)]
            # If the distance has not been queried before, check if the opposite direction distance is in the dictionary
            elif (current_address, start) in address_distances:
                return address_distances[(current_address, start)]
        # If neither start nor end is the current address of the truck, find the distance between start and end
        else:
            # Check if the distance between the start and end address has been queried before, use it
            if (start, end) in address_distances:
                return address_distances[(start, end)]
            # If the distance has not been queried before, check if the opposite direction distance is in the dictionary
            elif (end, start) in address_distances:
                return address_distances[(end, start)]

    # Uses a variation of the Nearest Neighbor algorithm to deliver packages
    # O(n^2) time O(n) space
    def deliver_packages(truck, hashMap):

        # Get the addresses of all the packages on the truck
        package_addresses = truck.get_package_addresses()

        # Get all package objects
        all_packages = truck.get_all_packages()

        # Create a dictionary of distances between addresses
        address_distances = create_dictionaries()

        # Create a set of unvisited addresses (initially all package addresses)
        unvisited_addresses = set(package_addresses)

        # Start at the truck's current address
        current_address = truck.current_address

        # Set the status of all packages on the truck as En Route
        for package in all_packages:
            if package.ID in truck.packages:
                package.status = "In Route"
                hashMap.insert(package.ID, package)

        # Loop until all addresses have been visited
        while unvisited_addresses:
            # Find the shortest distance to an unvisited address
            shortest_distance = float('inf')
            best_address = None
            for address in unvisited_addresses:
                distance = truck.calculate_distance(current_address, address, address_distances, truck.current_address)
                if float(distance) < float(shortest_distance):
                    shortest_distance = distance
                    best_address = address

            # Update the truck's mileage and current time based on the distance traveled
            truck.miles_driven += float(shortest_distance)
            time_traveled = float(shortest_distance) / 18.0
            truck.current_time += timedelta(hours=time_traveled)


            # Get the package ID for the current address
            for package in all_packages:
                if package.address == best_address:
                    package_id = package.ID
                    # Update package delivery time
                    if package_id in truck.packages:
                        hashMap.insert(package_id, Package(package.ID, package.address, package.city, package.state,
                                                           package.zip, package.delivery_deadline, package.mass,
                                                           package.status, truck.current_time.strftime('%H:%M:%S')))

            # Update the current address to the best address found
            current_address = best_address

            # Remove the best address from the unvisited set
            unvisited_addresses.remove(current_address)

            # Check if it's time to update package with ID 9
            if truck.current_time.strftime('%H:%M') == '10:20' and 9 in truck.packages:

                # Update the package address in the hash map
                package = hashMap.lookup(9)
                package.address = "410 S State St"
                hashMap.insert(9, package)
                # print(
                    # f"Package with ID 9 address updated to '410 S State St' at {truck.current_time.strftime('%H:%M:%S')}")

            # Print the current status of the truck
            # print(
                # f"Current time is {truck.current_time.strftime('%H:%M:%S')}, {round(truck.miles_driven, 2)} miles driven. Visited {current_address}")

        # Return to the hub once all packages are delivered
        distance = truck.calculate_distance(current_address, truck.hub_address, address_distances,
                                            truck.current_address)
        truck.miles_driven += float(distance)
        time_traveled = float(distance) / 18.0
        truck.current_time += timedelta(hours=time_traveled)
        current_address = truck.hub_address

        # print(f"Visited {current_address}, all packages have been delivered")

        return truck