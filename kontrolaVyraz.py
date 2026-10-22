Python

from fastapi import FastAPI
from pydantic import BaseModel
from sympy import sympify, simplify, diff, Symbol

app = FastAPI()

# Definujeme symbol 'x' pre SymPy
x = Symbol('x')

# Definícia dátovej štruktúry (Pydantic model)
class IntegralCheckRequest(BaseModel):
    typ: str = "integral"  # Ak typ nepríde, automaticky bude "integral"
    student_input: str
    correct_answer: str

@app.post("/verify")
def verify(data: IntegralCheckRequest):
    # Dáta sú už skontrolované a bezpečne dostupné cez bodku:
    typ = data.typ
    s = sympify(data.student_input)
    c = sympify(data.correct_answer)

    if typ == "integral":
        # Overenie neurčitého integrálu deriváciou
        return {"ok": simplify(diff(s - c, x)) == 0}

    elif typ == "expression":
        # Overenie bežného algebraického výrazu
        return {"ok": simplify(s - c) == 0}