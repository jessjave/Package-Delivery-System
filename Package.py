import csv

# package constructor
class Package:
    def __init__(self, ID, address, city=None, state=None, zip=None, delivery_deadline=None, mass=None, status=None, delivery_time=None):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery_deadline = delivery_deadline
        self.mass = mass
        self.status = status
        self.delivery_time = delivery_time

    def __str__(self):  # overwrite otherwise it will print an object reference not an object
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (
        self.ID, self.address, self.city, self.state, self.zip, self.delivery_deadline, self.mass, self.status,
        self.delivery_time)

    # loads all package object data to the hash table
    # O(n) time and space
    @staticmethod
    def loadPackageDataToHash(fileName, hashMap):
        with open(fileName) as package_list:
            package_data = csv.reader(package_list, delimiter=',')
            for package in package_data:
                mID = int(package[0])
                mAddress = package[1]
                mCity = package[2]
                mState = package[3]
                mZip = package[4]
                mDelivery_Deadline = package[5]
                mMass = package[6]
                mStatus = "At Hub"
                mDelivery_Time = package[7]

                # package object
                package = Package(mID, mAddress, mCity, mState, mZip, mDelivery_Deadline, mMass, mStatus, mDelivery_Time)

                hashMap.insert(mID, package)

    # loads package addresses and IDs to a list for use in other functions
    # O(n) time and space
    def loadPackageDataToList(fileName):
        all_packages = []
        with open(fileName) as package_list:
            package_data = csv.reader(package_list, delimiter=',')
            for package in package_data:
                mID = int(package[0])
                mAddress = package[1]

                # package object
                package = Package(mID, mAddress)

                all_packages.append(Package(mID, mAddress))
                return all_packages

