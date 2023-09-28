# Fungsi penjumlahan
def add(x, y):
    return x + y

# Fungsi pengurangan
def minus(x, y):
    return x - y

# Fungsi perkalian
def mult(x, y):
    return x * y

# Fungsi pembagian
def div(x, y):
    if y != 0:
        return x / y
    else:
        return "Pembagian oleh nol tidak valid."

# Contoh penggunaan fungsi-fungsi aritmatika
result_add = add(3, 5)
result_minus = minus(10, 4)
result_mult = mult(6, 7)
result_div = div(8, 2)

print("Hasil penjumlahan:", result_add)
print("Hasil pengurangan:", result_minus)
print("Hasil perkalian:", result_mult)
print("Hasil pembagian:", result_div)


def tree(node):
    if isinstance(node, (int, float)):
        return node
    elif isinstance(node, tuple) and len(node) == 3:
        operator, left_operand, right_operand = node
        if operator == '+':
            return tree(left_operand) + tree(right_operand)
        elif operator == '-':
            return tree(left_operand) - tree(right_operand)
        elif operator == '*':
            return tree(left_operand) * tree(right_operand)
        elif operator == '/':
            return tree(left_operand) / tree(right_operand)
    else:
        raise ValueError("Pohon ekspresi tidak valid")

# Contoh pohon ekspresi: (2+3) * (5-1)
expression_tree = ('*', ('+', 2, 3), ('-', 5, 1))

result = tree(expression_tree)

print("Hasil evaluasi pohon ekspresi:", result)

# ============================= AFTER ============================

def tree(node):
    if isinstance(node, (int, float)):
        return node
    elif isinstance(node, tuple) and len(node) == 3:
        left_operand, operator, right_operand = node
        if operator == '+':
            return tree(left_operand) + tree(right_operand)
        elif operator == '-':
            return tree(left_operand) - tree(right_operand)
        elif operator == '*':
            return tree(left_operand) * tree(right_operand)
        elif operator == '/':
            return tree(left_operand) / tree(right_operand)
    else:
        raise ValueError("Pohon ekspresi tidak valid")

# Contoh pohon ekspresi: (2+3) * (5-1)
expression_tree = ((2, '+', 3), '*', (5, '-', 1))

result = tree(expression_tree)

print("Hasil evaluasi pohon ekspresi (after):", result)
