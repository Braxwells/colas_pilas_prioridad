def esta_balanceada(cadena):
  pila = []
  for caracter in cadena:
    if caracter == "(":
      pila.append(caracter)
    elif caracter == ")":
      if len(pila) == 0:
        return False
      else:
        pila.pop()

  return len(pila) == 0


print(esta_balanceada("()"))  # True
print(esta_balanceada("()()"))  # True
print(esta_balanceada("(()())"))  # True
print(esta_balanceada("((())"))  # False
print(esta_balanceada("())"))  # False
print(esta_balanceada("((("))  # False
print(esta_balanceada("{[()]}"))  # True
print(esta_balanceada("{[(]}"))  # False