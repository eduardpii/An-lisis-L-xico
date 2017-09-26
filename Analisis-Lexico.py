import re

class Pila:#Clase pila
    def __init__(self):
        self.items=[]

    def apilar(self, x):
        self.items.append(x)

    def desapilar(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def es_vacia(self):
        return self.items == []

class Nodo():#clase arbol
    def __init__(self, val, izq=None, der=None):
        self.valor = val
        self.izq = izq
        self.der = der

#Esta función convierte la lista,en una pila.
def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":#evalua los operadores
            nodo_der = pila.desapilar()#Desapila debido a la posfija
            nodo_izq = pila.desapilar()#Desapila debido a la posfija
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))#apila arbol
        elif lista[0] in variables:
            valor = variables[lista[0]]
            pila.apilar(Nodo(valor[0]))
        elif lista[0] in "=":
            variable = pila.desapilar().valor
            variables[variable] = [evaluar(pila.desapilar())]
            print (variable+"="+str(variables[variable][0]))
        else:
            pila.apilar(Nodo(lista[0]))#apila nodos
        return convertir(lista[1:],pila)#recursividad

#Esta función resuelve el árbol
def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)

def evaluar_patrones(expresion):
    error = 0
    #patron = re.compile('([0-9]+)([+|-|*|/|=]+)([a-z]+)')
    patronNum = re.compile('^[-+]?[0-9]+$')
    patronVar = re.compile('^[a-z][a-zA-Z_$0-9]*$')
    patronOpe = re.compile('[+|-|*|/|=]')
    for i in expresion:
        if(patronNum.match(i)):
            #print("Num "+ i)
            tokens["Valor"]= [i]
        elif(patronVar.match(i)):
            #print("Var "+ i)
            tokens["Variable"]= [i]
        elif(patronOpe.match(i)):
            #print("Ope "+ i)
            tokens["Operador"]= [i]
        else:
            tokens["Erroneos"]= [i]
            error += 1
    return error

if __name__ == "__main__":
    variables = {}
    tokens = {}
    variable = ""
    n = "s"
    pila = Pila()
    while (n == "s"):
        expresion = input("Ingrese una expresión en POSFIJA: ").split(" ")
        error = evaluar_patrones(expresion)
        if(error == 0):
            for token in tokens:
                print (token, ":", tokens[token])
            convertir(expresion, pila)
        else:
            for token in tokens:
                print (token, ":", tokens[token])
            print("El numero de errores es: "+ str(error))
        n = input("Desea ingresar otras expresion? s/n ")