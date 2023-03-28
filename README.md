## SCENARIO
The University Parcel Service (UPS) needs to determine an efficient route and delivery distribution for their Daily Local Deliveries (DLD) because packages are not currently being consistently delivered by their promised deadline. The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to deliver each day. Each package has specific criteria and delivery requirements. The goal is to have a route of under 140 miles. 

I utilized a version of the Nearest Neighbor Algorithm to solve a typical Traveling Salesman Problem with a time complexity of O(n^2) and space complexity of O(n)

## USAGE
When running the program you should see a Command Line Interface like this: 

``` 

***************************************************
Welcome to the WGUPS package tracking program.
The total miles for the current route is: 110 miles
***************************************************

	Truck 1: 42 miles
	Truck 2: 41 miles
	Truck 3: 27 miles

To exit, please type 'exit'

To view packages statuses, please enter a time in the format HH:MM:SS: 
 

```

Once a desired time is entered the user will be prompted with a series of options including

```

To view a single package status at the given time type 'single' otherwise type 'all' to display all package info: 

```

If a single package is selected it will show the status of the desired package at the given time.

```

To view packages statuses, please enter a time in the format HH:MM:SS: 10:00:00
To view a single package status at the given time type 'single' otherwise type 'all' to display all package info: single
Please enter the ID of the desired package: 5
Package ID: 5, Address: 410 S State St, City: Salt Lake City, State: UT, Zip: 84111, Delivery Deadline: EOD, Mass: 5, Status: At Hub

```

If all packages are selected, it will give the status of all the packages at the given time.

```

Package ID: 1, Address: 195 W Oakland Ave, City: Salt Lake City, State: UT, Zip: 84115, Delivery Deadline: 10:30 AM, Mass: 21, Status: Delivered at 09:58:40
Package ID: 2, Address: 2530 S 500 E, City: Salt Lake City, State: UT, Zip: 84106, Delivery Deadline: EOD, Mass: 44, Status: Delivered at 09:52:20
Package ID: 3, Address: 233 Canyon Rd, City: Salt Lake City, State: UT, Zip: 84103, Delivery Deadline: EOD, Mass: 2, Status: Delivered at 09:09:20
Package ID: 4, Address: 380 W 2880 S, City: Salt Lake City, State: UT, Zip: 84115, Delivery Deadline: EOD, Mass: 4, Status: At Hub
Package ID: 5, Address: 410 S State St, City: Salt Lake City, State: UT, Zip: 84111, Delivery Deadline: EOD, Mass: 5, Status: At Hub
Package ID: 6, Address: 3060 Lester St, City: West Valley City, State: UT, Zip: 84119, Delivery Deadline: 10:30 AM, Mass: 88, Status: In Route
Package ID: 7, Address: 1330 2100 S, City: Salt Lake City, State: UT, Zip: 84106, Delivery Deadline: EOD, Mass: 8, Status: At Hub
Package ID: 8, Address: 300 State St, City: Salt Lake City, State: UT, Zip: 84103, Delivery Deadline: EOD, Mass: 9, Status: At Hub
Package ID: 9, Address: 300 State St, City: Salt Lake City, State: UT, Zip: 84103, Delivery Deadline: EOD, Mass: 2, Status: At Hub
Package ID: 10, Address: 600 E 900 South, City: Salt Lake City, State: UT, Zip: 84105, Delivery Deadline: EOD, Mass: 1, Status: In Route

```
## ASSUMPTIONS
•   Each truck can carry a maximum of 16 packages, and the ID number of each package is unique.

•   The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.

•   There are no collisions.

•   Three trucks and two drivers are available for deliveries. Each driver stays with the same truck as long as that truck is in service.

•   Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed. 

•   The delivery and loading times are instantaneous, i.e., no time passes while at a delivery or when moving packages to a truck at the hub (that time is factored into the calculation of the average speed of the trucks).

•   There is up to one special note associated with a package.

•   The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m. UPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the correct address (410 S State St., Salt Lake City, UT 84111) until 10:20 a.m.

•   The distances provided in the UPS Distance Table are equal regardless of the direction traveled.

•   The day ends when all 40 packages have been delivered.
