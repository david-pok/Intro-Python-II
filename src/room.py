# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
# class Store:
#     def __init__(self, store_type, depts=[]):
#         """Constructor"""
#         self.store_type = store_type
#         self.depts = depts
# ​
#     def add_dept(self, dept):
#         """Adds a department to this store."""
#         self.depts.append(dept)
    
#     def max_dept_num(self):
#         return len(self.depts) - 1
# ​
#     def get_dept(self, num):
#         return self.depts[num]
# ​
#     def __str__(self):  # for human consumption
#         s = f"Store (type: {self.store_type})\n"
# ​
#         for d in self.depts:
#             s += f"    {d}\n"
# ​
#         return s
# ​
#     def __repr__(self):  # for programmer consumption
#         #return f'Store("{self.store_type}")'
#         return f'Store({repr(self.store_type)},{repr(self.depts)})'
# ​
# class Dept:
#     def __init__(self, name, inventory=[]):
#         self.name = name
#         self.inventory = inventory
# ​
#     def __str__(self):  # for human consumption
#         return f"Dept {self.name}"
# ​
#     def __repr__(self):  # for programmer consumption
#         #return f'Store("{self.store_type}")'
#         return f'Dept({repr(self.name)},{repr(self.inventory)})'
# ​
# class Item:
#     pass