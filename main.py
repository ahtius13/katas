

def string_calculator(s):
    resultado = 0
    if s == "":
        resultado = 0
    else:
        partes = s.split(',') # "1,2" => ['1','2']
        for num in partes:
            resultado= resultado + int(num)

    return resultado





if __name__ == "__main__":

    s = input ("introduzca una cadena de nº ")

    print(string_calculator(s))