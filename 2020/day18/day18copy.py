import sys
import re

def get_lines_from_file():
    with open(sys.argv[1]) as inf:
        return inf.readlines()


lines = [line.rstrip() for line in get_lines_from_file()]


def calc(expr):
    x, op, y = expr.split(" ")

    if op == "+":
        return int(x) + int(y)
    elif op == "*":
        return int(x) * int(y)
    
    print("hitt ska vi inte")
    assert(False)

def find_inner_most_expr(expr):
    first_idx = -1
    for idx in range(len(expr)):
        if expr[idx] == "(":
            first_idx = idx
        elif expr[idx] == ")":
            return expr[first_idx: idx + 1]

    return None


p1 = False

def evaluate_expression(expr):
    print("Eval", expr)
    if expr.isnumeric():
        return int(expr)
    # look for paranth
    inner = find_inner_most_expr(expr)
    
    if inner:
        assert inner[0] == "("
        assert inner[-1] == ")"
        inner_res = evaluate_expression(inner[1: -1])

        assert inner_res
        new_expr = expr.replace(inner, str(inner_res))
        return evaluate_expression(new_expr)

    if p1:
        find_op = re.findall(r'\d+ . \d+', expr)
        # if len(find_op):
        for leftmost_expr in find_op:
            #leftmost_expr = find_op[0]
            res = calc(leftmost_expr)
            assert(res > 0)
            rest_expr = expr[len(leftmost_expr):]
            if rest_expr == "":
                return calc(leftmost_expr)
            new_expr = expr.replace(leftmost_expr, str(res), 1)
            
            return evaluate_expression(new_expr)
    else:
        find_add = re.findall(r'\d+ \+ \d+', expr)
        for add_expr in find_add:
            res = calc(add_expr)
            assert(res > 0)

            #rest_left = expr[:len(add_expr)]
            rest_right = expr[len(add_expr):]

            #new_expr = str(res) + rest_right
            #print(new_expr)
            #return
            new_expr = expr.replace(add_expr, str(res), 1)
            
            return evaluate_expression(new_expr)

        find_mul = re.findall(r'\d+ \* \d+', expr)
        for mult_expr in find_mul:
            res = calc(mult_expr)
            assert(res > 0)

            #rest_left = expr[:len(mult_expr)]
            rest_right = expr[len(mult_expr):]

            #new_expr = str(res) + rest_right
            new_expr = expr.replace(mult_expr, str(res), 1)
            
            return evaluate_expression(new_expr)

    assert(False)


ans = 0
for line in lines: 
    #print(lines)
    res = evaluate_expression(line)
    assert res > 0
    ans += res
    print("Answer: ", ans)

