# List Comprehensions
# squares = [x**2 for x in range(5)]
# print(squares)

# Generator Expressions
# gen = (x**2 for x in range(5))
# print(gen) 
# <generator object <genexpr> at 0x...> 

# Converting generator to list to display its contents 
# print(list(gen)) 


# Dictionary Comprehensions
# squares = {x: x**2 for x in range(5)}
# print(squares)



# class Person:
#     def __init__(self, name, age):
#         self.__name = name  # Private attribute
#         self.__age = age    # Private attribute

#     def get_name(self):
#         return self.__name  # Getter method to access private attribute

#     def set_name(self, name):
#         self.__name = name  # Setter method to modify private attribute

#     def get_age(self):
#         return self.__age  # Getter method to access private attribute

#     def set_age(self, age):
#         if age > 0:         # Validation before modifying private attribute
#             self.__age = age
#         else:
#             print("Age must be positive!")

# # Using the Person class
# person = Person("Alice", 25)

# # Accessing data via methods
# print(person.get_name())  # Output: Alice
# print(person.get_age())   # Output: 25

# # Modifying data via methods
# person.set_age(30)
# print(person.get_age())   # Output: 30

# # Attempting invalid modification
# person.set_age(-5)        # Output: Age must be positive!



# def tower_of_hanoi(n, source, target, auxiliary):
#     """
#     Solves the Tower of Hanoi problem for `n` disks.

#     Parameters:
#     n (int): Number of disks.
#     source (str): The name of the source rod.
#     target (str): The name of the target rod.
#     auxiliary (str): The name of the auxiliary rod.
#     """
#     if n == 1:
#         print(f"Move disk 1 from {source} to {target}")
#         return

#     # Move n-1 disks from source to auxiliary using target as auxiliary
#     tower_of_hanoi(n - 1, source, auxiliary, target)

#     # Move the nth disk from source to target
#     print(f"Move disk {n} from {source} to {target}")

#     # Move the n-1 disks from auxiliary to target using source as auxiliary
#     tower_of_hanoi(n - 1, auxiliary, target, source)

# # Example usage
# n = 3  # Number of disks
# tower_of_hanoi(n, 'A', 'C', 'B')




# from collections import defaultdict, deque

# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)

#     def add_edge(self, u, v):
#         """Add an edge to the graph."""
#         self.graph[u].append(v)

#     def dfs(self, start):
#         """Perform Depth-First Search starting from a given node."""
#         visited = set()
#         result = []

#         def dfs_recursive(node):
#             visited.add(node)
#             result.append(node)
#             for neighbor in self.graph[node]:
#                 if neighbor not in visited:
#                     dfs_recursive(neighbor)

#         dfs_recursive(start)
#         return result

#     def bfs(self, start):
#         """Perform Breadth-First Search starting from a given node."""
#         visited = set()
#         queue = deque([start])
#         result = []

#         while queue:
#             node = queue.popleft()
#             if node not in visited:
#                 visited.add(node)
#                 result.append(node)
#                 for neighbor in self.graph[node]:
#                     if neighbor not in visited:
#                         queue.append(neighbor)

#         return result

# # Example usage:
# if __name__ == "__main__":
#     g = Graph()
#     g.add_edge(0, 1)
#     g.add_edge(0, 2)
#     g.add_edge(1, 2)
#     g.add_edge(2, 0)
#     g.add_edge(2, 3)
#     g.add_edge(3, 3)

#     start_node = 2

#     print("DFS starting from node", start_node, ":", g.dfs(start_node))
#     print("BFS starting from node", start_node, ":", g.bfs(start_node))

# def apply_function(func, value):
#     return func(value)

# def square(x):
#     return x * x

# print(apply_function(square, 5))


# from functools import reduce
# numbers = [1, 2, 3, 4]
# result = reduce(lambda x, y: x + y, numbers)
# print(result)  # Output: 10


# def outer_function(x):
#     def inner_function(y):
#         return x + y
#     return inner_function

# closure = outer_function(5)
# print(closure(3))  # Output: 8


def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper
#Example:

def greet():
    print("Hello!")

result = decorator(greet)
result()
