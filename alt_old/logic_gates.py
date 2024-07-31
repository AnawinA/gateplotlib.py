from itertools import product
from tabulate import tabulate

possible_bool_2 = list(product([0, 1], repeat=2))
print(possible_bool_2)
result = {chr(65 + i): list(column) for i, column in enumerate(zip(*possible_bool_2))}
# a and b get bool in c





and_b, or_b, nand_b, nor_b, xor_b, xnor_b = [[] for _ in range(6)]


def logic(list_b, value):
    return list_b.append(int(value))

for a, b in zip(*result.values()):
    logic(and_b, a and b)
    logic(or_b, a or b)
    logic(nand_b, not (a and b))
    logic(nor_b, not (a or b))
    logic(xor_b, (a and not b) or (not a and b))
    logic(xnor_b, not ((a and b) or (not a and b)))

def new_result(dict_n):
    c_result = result.copy()
    c_result.update(dict_n)
    return c_result

# update and or
result_and_or = new_result({
    "AND": and_b,
    "OR": or_b,
})
# update nand or
result_nx = new_result({
    "NAND": nand_b,
    "NOR": nor_b,
})
# update xor xnor
result_xnor = new_result({
    "XOR": xor_b,
    "XNOR": xnor_b,
})


def md_table(result):
    table = tabulate(result, headers="keys", tablefmt='pipe', numalign='center')
    return table

with open('./bool.md', 'w') as f:
    f.write("# Truth table\n\n")
    def write_table(name, cresult):
        ctable = md_table(cresult)
        f.write(f"## {name}\n\n")
        f.write(ctable)
        f.write('\n\n')
        print(f"## {name}:")
        print(ctable)
        print()

    write_table("AND OR", result_and_or)
    write_table("NAND NOR XNOR", result_nx)
    write_table("XOR XNOR", result_xnor)


