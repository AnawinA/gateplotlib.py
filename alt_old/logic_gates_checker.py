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
    
    def compare(self, a, b):
        return self.result[a] == self.result[b]
    
    # use inside/outside class
    def md_table(self):
        self.table = tabulate(self.result, headers="keys", tablefmt='pipe', numalign='center')
        return self.table
    
    # External use
    def write_md(self, path_file: str):
        with open(path_file, 'w') as f:
            self.ctable = self.md_table()
            f.write(f"## {self.name}\n\n")
            f.write(self.ctable)
            f.write('\n\n')
    
    
    

gic_1 = LogicGates(3, "Test")

print(gic_1)
print(gic_1.dict())
print(gic_1["A"])
print(gic_1.compare("A", "B"))

