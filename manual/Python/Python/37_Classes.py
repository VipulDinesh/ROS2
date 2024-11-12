# import math

# class Number:
    # def __init__(self, x, y): #dunder method which is automatically called
#         self.x = x
#         self.y = y
#     def distance(self, p):
#         dis = (math.sqrt((self.x - p.x)**2 + (self.y-p.y)**2))
#         print(dis)


# point1 = Number (2, 3)
# point2 = Number (4,5)

# point1.distance(point2)

import math

class Number:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, p):
        dis = (math.sqrt((self.x - p.x)**2 + (self.y-p.y)**2))
        return(dis)


point1 = Number (2, 3)
point2 = Number (4,5)
# point3 = Number (6, 7)

distance1=point1.distance(point2)
# distance2=point1.distance(point3)

print(distance1)
# print(distance2)
