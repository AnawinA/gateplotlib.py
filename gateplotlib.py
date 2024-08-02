from itertools import product
from tabulate import tabulate

class LogicGates:
    
    #property outside can use
    result_header = []
    def __init__(self, length: int, name="unknown", order="A") -> None:
        self.length = length
        self.name = name
        self.possible_bool = list(product([0, 1], repeat=self.length))
        self.result = {chr(ord(order) + i): list(column) for i, column in enumerate(zip(*self.possible_bool))}
        self.result_header = list(self.result.keys())
    
    def __repr__(self) -> str:
        return f"## {self.name}\n" + self.md_table() + "\n"
    
    def __getitem__(self, key) -> list:
        return self.result[key]
    
    def dict(self) -> dict:
        return self.result
    
    # use inside/outside class
    def md_table(self) -> str:
        self.table = tabulate(self.result, headers="keys", tablefmt='pipe', numalign='center')
        return self.table
    
    def write_md(self, path_file: str) -> None:
        with open(path_file, 'w') as f:
            self.ctable = self.md_table()
            f.write(f"## {self.name}\n\n")
            f.write(self.ctable)
            f.write('\n\n')
    
    def __create_column_by_all(self, headers, logic_func: callable) -> None:
        new_column = []        
        self.result_selected = {k: v for k, v in self.result.items() if k in self.result_header}
        for i in zip(*self.result_selected.values()):
            ai = int(logic_func(i))
            new_column.append(ai)
        self.result.update({headers: new_column})
    
    def add_and(self, key1, key2) -> None:
        new_column = [int(a and b) for a, b in zip(self.result[key1], self.result[key2])]
        self.result.update({f"{key1}&{key2}": new_column})
    
    def add_or(self, key1, key2) -> None:
        new_column = [int(a or b) for a, b in zip(self.result[key1], self.result[key2])]
        self.result.update({f"{key1}|{key2}": new_column})
    
    def add_not(self, key) -> None:
        new_column = [int(not i) for i in self.result[key]]
        self.result.update({f"!{key}": new_column})

    def add_xor(self, key1, key2) -> None:
        new_column = [int(a ^ b) for a, b in zip(self.result[key1], self.result[key2])]
        self.result.update({f"{key1}^{key2}": new_column})
    
    def add_order(self):
        new_column = [i for i in range(2**self.length)]
        self.result.update({"[i]": new_column})
    
    def add_separate(self):
        new_column = ["/" for _ in range(2**self.length)]
        self.result.update({"/": new_column})

    def make(self, logic_str: str, label: str, is_print: bool = False) -> None:
        magic_str = logic_str
        is_print and print(magic_str)
        to_use_make = []
        for i, header in enumerate(self.result_header):
            magic_str = magic_str.replace(header, f'key_of[{i}]')
            to_use_make.append(self.result[header])
        magic_str = magic_str.replace('!', ' not ')
        magic_str = magic_str.replace('&', ' and ')
        magic_str = magic_str.replace('.', ' and ')
        magic_str = magic_str.replace('|', ' or ')
        magic_str = magic_str.replace('+', ' or ')
        # print(to_use_make)
        try:
            new_column = [int(eval(magic_str)) for key_of in zip(*to_use_make)]
            self.result.update({f"{label}": new_column})
        except Exception as e:
            print(f"there's an error while use .make() : {e}")
    
    def compare(self, a, b):
        return self.result[a] == self.result[b]
    
    def compare_recent(self):
        return self.result[-1] == self.result[-2]
    
    def add_all_and(self) -> None: # use function all() !!!
        self.__create_column_by_all("AND", all)
    
    def add_all_or(self) -> None: # use function all() !!!
        self.__create_column_by_all("OR", any)
    
    def add_all_nor(self) -> None:
        self.__create_column_by_all("NOR", lambda x: 0 if any(x) else 1)
    
    def add_all_nand(self) -> None:
        self.__create_column_by_all("NAND", lambda x: 0 if all(x) else 1)
    
    def clear_logic(self) -> None:
        self.result = {chr(65 + i): list(column) for i, column in enumerate(zip(*self.possible_bool))}
    
    def help(self) -> str:
        print("""\n=== LogicsGates by Anawin ===
-- for ITF fundamental

__init__(self, length: int, name="unknown") -> None
__repr__(self) -> str
__getitem__(self, key) -> list

dict(self) -> dict
md_table(self) -> str
write_md(self, path_file: str) -> None

add_and(self) -> None
add_or(self) -> None
add_nand(self) -> None
add_nor(self) -> None
    """)
    
