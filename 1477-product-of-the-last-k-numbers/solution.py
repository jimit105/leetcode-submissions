# Approach: Prefix Product

# Time: 
# add(): O(1)
# getProduct(): O(1). For n operations: O(n)

# Space: O(n)

class ProductOfNumbers:

    def __init__(self):
        self.prefix_product = [1]
        self.size = 0
        
    def add(self, num: int) -> None:
        if num == 0:
            # If num is 0, reset the cumulative product
            self.prefix_product = [1]
            self.size = 0
        else:
            self.prefix_product.append(self.prefix_product[-1] * num)
            self.size += 1        

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0

        return self.prefix_product[self.size] // self.prefix_product[self.size - k]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
