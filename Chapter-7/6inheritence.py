class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def get_fare(self):
        return self.seating_capacity * 100
    

    class Bus(Vehicle):

        def __init__(self, seating_capacity):
            super().__init__(seating_capacity)

        def get_fare(self):
            Vehicle_fare = super().get_fare()
            maintence_fare = Vehicle_fare * 0.1
            tota_fare = Vehicle_fare + maintence_fare
            return tota_fare
        
Vehicle1 = Vehicle(50)
print("Vehicle fare:", Vehicle1.get_fare() )

bus1 = Bus(50)
print("Bus Fare: ", bus1.get_fare())