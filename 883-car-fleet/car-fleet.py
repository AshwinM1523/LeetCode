class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        for i in range(len(cars)):
            time = (target - cars[i][0]) / cars[i][1]
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        
        return len(stack)