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
