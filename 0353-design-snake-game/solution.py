from collections import deque

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = deque([(0, 0)])
        self.snake_set = {(0, 0): 1}
        self.width = width
        self.height = height
        self.food = food
        self.food_index = 0
        self.movement = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}
        

    def move(self, direction: str) -> int:
        new_head = (self.snake[0][0] + self.movement[direction][0],
                    self.snake[0][1] + self.movement[direction][1])

        # Boundary conditions
        crosses_boundary1 = new_head[0] < 0 or new_head[0] >= self.height
        crosses_boundary2 = new_head[1] < 0 or new_head[1] >= self.width

        # If snake bites itself
        bites_itself = new_head in self.snake_set and new_head != self.snake[-1]

        # If any of the terminal conditions are satisfied, then exit
        if crosses_boundary1 or crosses_boundary2 or bites_itself:
            return -1

        next_food_item = self.food[self.food_index] if self.food_index < len(self.food) else None

        if self.food_index < len(self.food) and \
            next_food_item[0] == new_head[0] and \
            next_food_item[1] == new_head[1]:
            # Eat Food
            self.food_index += 1
        
        else:
            # Not eating food; delete tail
            tail = self.snake.pop()
            del self.snake_set[tail]

        # Add new head
        self.snake.appendleft(new_head)
        self.snake_set[new_head] = 1

        return len(self.snake) - 1




# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
