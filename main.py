# Jessica Javeed 010063704
from datetime import datetime

from DataHandler import create_dictionaries
from HashMap import HashMap
from Package import Package
from Truck import Truck

# import package data from csv file and store in hash map and list
package_hash = HashMap()
Package.loadPackageDataToHash('Packages.csv', package_hash)
all_packages = Package.loadPackageDataToList('Packages.csv')
# create dictionary of address distances using distances file
address_distances = create_dictionaries()

# assign packages to each truck
truck_1_packages = [14, 15, 16, 19, 13, 25, 32, 20, 17, 6, 31, 40, 28, 1, 2, 34]
truck_2_packages = [18, 36, 3, 38, 30, 10, 39, 35, 27, 12, 23, 11, 24, 22, 26, 29]
truck_3_packages = [9, 8, 21, 5, 37, 33, 4, 7]

# create Truck objects with package assignments and starting location/time
truck_1 = Truck(truck_1_packages, 16, 18, 0.0, "4001 South 700 East", datetime.strptime("9:05", "%H:%M"), datetime.strptime("9:05", "%H:%M"))
truck_2 = Truck(truck_2_packages, 16, 18, 0.0, "4001 South 700 East", datetime.strptime("8:00", "%H:%M"), datetime.strptime("8:00", "%H:%M"))
truck_3 = Truck(truck_3_packages, 16, 18, 0.0, "4001 South 700 East", datetime.strptime("10:02", "%H:%M"), datetime.strptime("10:02", "%H:%M"))

# get addresses of packages assigned to truck 1
package_addresses = truck_1.get_package_addresses()

# Print the addresses
# for key, value in address_distances.items():
        # print(key, value)

# deliver packages using each truck's assigned packages and update package status in hash table
Truck.deliver_packages(truck_1, package_hash)
Truck.deliver_packages(truck_2, package_hash)
Truck.deliver_packages(truck_3, package_hash)

# calculate total miles driven by all trucks
total_miles = truck_1.miles_driven + truck_2.miles_driven + truck_3.miles_driven

# print total miles driven
print("***************************************************")
print("Welcome to the WGUPS package tracking program.")
print("The total miles for the current route is: " + str(round(total_miles)) + " miles")
print("***************************************************\n")

print("\tTruck 1: " + str(round(truck_1.miles_driven)) + " miles")
print("\tTruck 2: " + str(round(truck_2.miles_driven)) + " miles")
print("\tTruck 3: " + str(round(truck_3.miles_driven)) + " miles")

print("\nTo exit, please type 'exit'\n")

# prompt user to enter a time to view package statuses
while True:
    try:
        # get user input for time to view package statuse
        time_str = input("To view packages statuses, please enter a time in the format HH:MM:SS: ")

        # if user inputs exit, close the program
        if time_str == "exit":
            exit()

        # convert user input time string to datetime object
        time_format = '%H:%M:%S'
        user_time = datetime.strptime(time_str, time_format)
        # set created to keep track of which package IDs have been printed.
        printed_package_ids = set()
        # iterates over all package IDs to retrieve objects from hash table
        for package_id in range(1, 41):
            package = package_hash.lookup(package_id)
            # convert delivery time string to datetime object
            delivery_time = datetime.strptime(package.delivery_time, time_format)
            # sets package status to At Hub if truck has not left yet
            if package_id in truck_1_packages and user_time.time() < datetime.strptime("09:05:00", time_format).time():
                package.status = "At Hub"
            if package_id in truck_2_packages and user_time.time() < datetime.strptime("08:00:00", time_format).time():
                package.status = "At Hub"
            if package_id in truck_3_packages and user_time.time() < datetime.strptime("10:02:00", time_format).time():
                package.status = "At Hub"
            # Ensures correct address before it is changed at 10:20 in lines 194-199 in Truck.py
            if package_id == 9 and user_time.time() < datetime.strptime("10:20:00", time_format).time():
                package.address = "300 State St"
            # sets Delivered status if user's input time is after Delivery time
            if delivery_time <= user_time:
                package.status = "Delivered"
                package_hash.insert(package_id, package)
            if package_id in printed_package_ids:
                # skip printing if package has already been printed
                continue
                # add package ID to printed set and print package
            printed_package_ids.add(package_id)
            print(
                "Package ID: {}, Address: {}, City: {}, State: {}, Zip: {}, Delivery Deadline: {}, Mass: {}, Status: {}{}".format(
                    package.ID, package.address, package.city, package.state, package.zip,
                    package.delivery_deadline, package.mass, package.status,
                    "" if package.status == "In Route" or package.status == "At Hub" else " at {}".format(
                        package.delivery_time)
                ))
    except ValueError:
        # Accounts for improper data input
        print("Invalid time format. Please enter a time in HH:MM:SS format.")
