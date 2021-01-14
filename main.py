
def main():
    right = False #boolea per comprovar les condicions

    print("************************************************")
    print("*********Aplicació d'anàlisi estadístic*********")
    print("************************************************")

    historia = int(input("Introdueix l'història clínica: ")) #Es demana integer per teclat de la variable historia

    years = 0
    months = 0 #declarem variables per mostrar l'edat amb anys i mesos
    edat = 0
    edat = int(input("Introdueix l'edat de debut del pacient(en mesos): ")) #Es demana integer per teclat de la variable edat
    years = int(edat) // 12 #Es realitza divisió entera
    months = int(edat) % 12 #Ens dona el mòdul

    dx = str(input("Introdueix el seu diagnòstic (DX): ")) #Es demana string per teclat de la variable dx


    nt = int(input("Té els nivells de NT alterats? (1=Si 0=No): ")) #Es demana integer per teclat de la variable nt
    convulsions = int(input("Té convulsions generalitzades? (1=Si 0=No): ")) #Es demana integer per teclat de la variable convulsions
    ntfinal = nt #Es declara per fer la condició i ens doni Si o No
    convulsionsfinal = convulsions #Es declara per fer la condició i ens doni Si o No

    if(nt == 1): #Condició per comprar el valor introduit i en el cas que sigui el número indicat guardarlo a la variable amb el valor de Si o No
        ntfinal = "Si"
    elif (nt == 0):
        ntfinal = "No"
    else:
        print("Error en dades")

    if(convulsions == 1): #Condició per comprar el valor introduit i en el cas que sigui el número indicat guardarlo a la variable amb el valor de Si o No
        convulsionsfinal = "Si"
    elif(convulsions == 0):
        convulsionsfinal = "No"
    else:
        print("Error en dades")

    this_set = "|HC     |  Edat          |  DX                       |  Alteració NT   |  Conv. Generals  |" #conjunt per solament poder afegir o eleminar elements
    print(this_set)

    print("{}\t".format(historia), "{}".format(int(years)), "anys i", "{}".format(int(months)), "mesos", "{}\t".format(dx), "{}\t\t\t\t".format(ntfinal), "{}\t\t\t".format(convulsionsfinal))
    #retornar els valors tabulats
if __name__ == '__main__':
    main()


