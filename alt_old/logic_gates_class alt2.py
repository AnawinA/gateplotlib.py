from itertools import product
from tabulate import tabulate

class LogicGates:
    
    #property outside can use
    result_header = []
    
    def __init__(self, length: int, name="unknown"):
        self.length = length
        self.name = name
        self.possible_bool = list(product([0, 1], repeat=self.length))
        self.result = {chr(65 + i): list(column) for i, column in enumerate(zip(*self.possible_bool))}
        self.result_header = list(self.result.keys())
    
    def __repr__(self):
        return f"## {self.name}\n" + self.md_table() + "\n"
    
    def __getitem__(self, key):
        return self.result[key]
    
    def dict(self):
        return self.result
    
    # use inside/outside class
    def md_table(self):
        self.table = tabulate(self.result, headers="keys", tablefmt='pipe', numalign='center')
        return self.table
    
    def write_md(self, path_file: str):
        with open(path_file, 'w') as f:
            self.ctable = self.md_table()
            f.write(f"## {self.name}\n\n")
            f.write(self.ctable)
            f.write('\n\n')
    
    def __create_column_by_all(self, headers, logic_func: callable):
        self.new_column = []
        # use only A B C dict, AND, or, etc. do not calc
        # get only in self.result_header
        
        self.result_selected = {k: v for k, v in self.result.items() if k in self.result_header}
        for i in zip(*self.result_selected.values()):
            print(logic_func(i))
            ai = int(logic_func(i))
            self.new_column.append(ai)
        self.result.update({headers: self.new_column})
        
    def add_and(self): # use function all() !!!
        self.__create_column_by_all("AND", all)
    
    def add_or(self): # use function all() !!!
        self.__create_column_by_all("OR", any)
    
    def add_nor(self):
        self.__create_column_by_all("NOR", lambda x: 0 if any(x) else 1)
    
    def add_nand(self):
        self.__create_column_by_all("NAND", lambda x: 0 if all(x) else 1)
    
    def clear_logic(self):
        self.result = {chr(65 + i): list(column) for i, column in enumerate(zip(*self.possible_bool))}
    
    
    
    

gic_1 = LogicGates(3, "Test")

print(gic_1)
print(gic_1.dict())
print(gic_1["A"])
# gic_1.write_md("test.md")
gic_1.add_and()
gic_1.add_or()
gic_1.add_nor()
gic_1.add_nand()
gic_1.add_xor()
print(gic_1)
gic_1.clear_logic()
print(gic_1)
print(gic_1.result_header)


# use class from __str__


# gic_2 = LogicGates(3)
# print(gic_2)

# gic_4 = LogicGates(4)
# print(gic_4)


"""
What we get?
1. class 
__init__ = call when create object,
__repr__ = call when use or print object ex. print(gic_1)
__getitem__ = call when use [key] ex. print(gic_1["A"])
2. hiden class ex. __create_column_by_all
3. function use in function ex. add_and -> __create_column_by_all
4. callable input to function = logic_func (line 45)
5. tabulate use = tabulate(result, headers="keys", tablefmt='pipe', numalign='center') => 4 args = result, headers=, tablefmt=, numalign=
pipe tablefmt is same to markdown table

 
"""
