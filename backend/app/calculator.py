import re
from sympy import sympify, SympifyError, sqrt

def calcular_expressao(expressao: str) -> str:
    try:
        expr = expressao.replace('x', '*').replace('X', '*')
        expr = expr.replace('÷', '/')
        expr = expr.replace('%', '*0.01')

        # Regex para colocar parênteses após sqrt se não tiver
        # Exemplo: sqrt9 -> sqrt(9)
        expr = re.sub(r'sqrt(\d+(\.\d+)?|\([^()]*\))', lambda m: f"sqrt({m.group(1).strip('()')})", expr)

        expr_sem_espaco = expr.replace(' ', '')

        if not re.fullmatch(r'[0-9+\-*/().sqrt]+', expr_sem_espaco):
            return "Erro: caracteres inválidos"

        sympy_expr = sympify(expr, evaluate=True, locals={"sqrt": sqrt})

    except SympifyError:
        return "Erro: expressão inválida"
    except Exception:
        return "Erro: expressão inválida"

    if sympy_expr.is_rational:
        if sympy_expr.q == 1:
            return str(sympy_expr.p)
        else:
            val_float = float(sympy_expr.evalf())
            return f"{val_float:.2f}".rstrip('0').rstrip('.')
    else:
        val_float = float(sympy_expr.evalf())
        return f"{val_float:.2f}".rstrip('0').rstrip('.')
