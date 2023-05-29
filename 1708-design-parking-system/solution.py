# Approach 4: Single Array

# Time: O(n)
# Space: O(1)

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):

        # Save count of empty slots
        self.empty = [big, medium, small]
        

    def addCar(self, carType: int) -> bool:
        if self.empty[carType - 1] > 0:
            self.empty[carType - 1] -= 1
            return True

        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
