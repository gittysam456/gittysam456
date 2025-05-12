"""WeCare insurance company wants to calculate premium of vehicles.
Vehicles are of two types – "Two Wheeler" and "Four Wheeler". Each vehicle is identified by vehicle id, type, cost and premium amount.
Premium amount is 2% of the vehicle cost for two-wheelers and 6% of the vehicle cost for four wheelers. Calculate the premium amount and display the vehicle details.

Identify the class name and attributes to represent vehicles.

calculate_premium()
vehicle_cost
TwoWheeler
vehicle_type
vehicle_id
Vehicle
premium_amount
FourWheeler
premium_percentage
calculate_vehicle_cost()
__init__()
display_vehicle_details()
Write a Python program to implement the class chosen with its attributes and methods.

Note:

Consider all instance variables to be private and methods to be public
Include getter and setter methods for all instance variables
Display appropriate error message, if the vehicle type is invalid
Perform case-sensitive string comparison
Represent few objects of the class, initialize instance variables using setter methods, invoke appropriate methods and test your program."""

class Vehicle:
    def __init__(self):
        self.__vehicle_id = None
        self.__vehicle_type = None
        self.__vehicle_cost = 0.0
        self.__premium_amount = 0.0

    # Getter and Setter for vehicle_id
    def set_vehicle_id(self, vehicle_id):
        self.__vehicle_id = vehicle_id

    def get_vehicle_id(self):
        return self.__vehicle_id

    # Getter and Setter for vehicle_type
    def set_vehicle_type(self, vehicle_type):
        if vehicle_type in ["Two Wheeler", "Four Wheeler"]:
            self.__vehicle_type = vehicle_type
        else:
            print("Error: Invalid vehicle type.")

    def get_vehicle_type(self):
        return self.__vehicle_type

    # Getter and Setter for vehicle_cost
    def set_vehicle_cost(self, vehicle_cost):
        self.__vehicle_cost = vehicle_cost

    def get_vehicle_cost(self):
        return self.__vehicle_cost

    # Getter for premium_amount
    def get_premium_amount(self):
        return self.__premium_amount

    # Method to calculate premium
    def calculate_premium(self):
        if self.__vehicle_type == "Two Wheeler":
            self.__premium_amount = self.__vehicle_cost * 0.02
        elif self.__vehicle_type == "Four Wheeler":
            self.__premium_amount = self.__vehicle_cost * 0.06
        else:
            print("Error: Cannot calculate premium for invalid vehicle type.")

    # Method to display vehicle details
    def display_vehicle_details(self):
        print(f"Vehicle ID: {self.__vehicle_id}")
        print(f"Vehicle Type: {self.__vehicle_type}")
        print(f"Vehicle Cost: {self.__vehicle_cost}")
        print(f"Premium Amount: {self.__premium_amount}")


# Example usage
vehicle1 = Vehicle()
vehicle1.set_vehicle_id("V001")
vehicle1.set_vehicle_type("Two Wheeler")
vehicle1.set_vehicle_cost(50000)
vehicle1.calculate_premium()
vehicle1.display_vehicle_details()

vehicle2 = Vehicle()
vehicle2.set_vehicle_id("V002")
vehicle2.set_vehicle_type("Four Wheeler")
vehicle2.set_vehicle_cost(800000)
vehicle2.calculate_premium()
vehicle2.display_vehicle_details()

vehicle3 = Vehicle()
vehicle3.set_vehicle_id("V003")
vehicle3.set_vehicle_type("Bike")  # Invalid type
vehicle3.set_vehicle_cost(30000)
vehicle3.calculate_premium()
vehicle3.display_vehicle_details()
