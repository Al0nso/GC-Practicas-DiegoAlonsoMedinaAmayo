"""Universidad Nacional Autónoma de México
Autora: Ruíz Almanza Nancy Selene 
Biología, 8vo semestre
Autor: Medina Amayo D. Alonso 
Ciencias de la Computación, 8vo semestre
Lenguaje: Python
Versión del Lenguaje: Python 3
Versión del programa: v1.0
Fecha: 08/ABR/2022
El comando para correr el programa:
python3 p2_MedinaAmayoDiegoAlonso
"""


"""Método para recibir la secuencia del usuario y validarla
Pide una cadena en minusculas y/o mayusculas, en caso de algo más se vuelve a pedir """
def recibeSecuencia():
    secuencia = input('¿Qué secuencia desea procesar?\n')
    if(secuencia.isalpha()):
        secuencia = secuencia.upper()
        for i in secuencia:
            if(not(((i == 'A') or (i == 'C')) or ((i == 'T') or (i == 'G')))):
                print(
                    'ERROR: La secuencia dada no es una secuencia aceptada, contiene caracteres que no represetan genes')
                return
        if(len(secuencia) % 3 != 0):
            print(
                'ERROR: La secuencia dada no es una secuencia aceptada, último codón incompleto')
            return
        return secuencia
    else:
        print('ERROR: La secuencia dada no es una secuencia aceptada, contiene caracteres no alfabéticos')


"""Función que recibe una secuencia de DNA y devuelve la cadena complemento"""
def obtenerComplementaria(secuencia):
    cadenaComplementaria = ''
    for i in secuencia:
        if(i == 'A'):
            cadenaComplementaria += 'T'
        if(i == 'C'):
            cadenaComplementaria += 'G'
        if(i == 'G'):
            cadenaComplementaria += 'C'
        if(i == 'T'):
            cadenaComplementaria += 'A'
    return cadenaComplementaria

"""Función que recibe una cadena de DNA y devuelve la cadena de RNAm correspondiente"""
def obtenerRNAm(secuencia):
    cadenaRNA = ''
    for i in secuencia:
        if(i == 'T'):
            cadenaRNA += 'U'
        else:
            cadenaRNA += i
    return cadenaRNA

"""Función que recibe una secuencia de RNAm y verifica si tiene el codón de inicio
Devuelve True de ser asi, False en otro caso"""
def verificaCodon(secuenciaRNA):
    if(secuenciaRNA[:3] == 'AUG'):
        return True
    else:
        print('ERROR:', secuenciaRNA[:3] ,'no es codón de inicio')
        return False

"""Método para traducir de codones a genes con el diccionario dado
Recibe una secuencia de RNA y devuelve una cadena"""
def generaAminoacidos(secuenciaRNA):
    codones_traduccion = {"GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",  # Alanina
                      # Cisteina
                      "UGU": "C", "UGC": "C",
                      # Acido aspartico
                      "GAU": "D", "GAC": "D",
                      # Acido glutamico
                      "GAA": "E", "GAG": "E",
                      # Fenilalanina
                      "UUU": "F", "UUC": "F",
                      # Glicina
                      "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
                      # Histidina
                      "CAU": "H", "CAC": "H",
                      # Isoleucina
                      "AUA": "I", "AUU": "I", "AUC": "I",
                      # Lisina
                      "AAA": "K", "AAG": "K",
                      # Leucina
                      "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
                      # Metionina
                      "AUG": "M",
                      # Aspargina
                      "AAU": "N", "AAC": "N",
                      # Prolina
                      "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                      # Glutamina
                      "CAA": "Q", "CAG": "Q",
                      # Arginina
                      "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
                      # Serina
                      "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
                      # Treonina
                      "ACU": "U", "ACC": "U", "ACA": "U", "ACG": "U",
                      # Valina
                      "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
                      # Triptofano
                      "UGG": "W",
                      # Tirosina
                      "UAU": "Y", "UAC": "Y",
                      # Stop
                      "UAA": "_", "UAG": "_", "UGA": "_"}
    cadenaAminoacidos = ''
    for i in range(0, len(secuenciaRNA), 3):
        codon = ''
        codon += secuenciaRNA[i]
        codon += secuenciaRNA[i+1]
        codon += secuenciaRNA[i+2]
        codonTraducido = codones_traduccion.get(codon)
        cadenaAminoacidos += '-' if( codonTraducido == None ) else codonTraducido
    return cadenaAminoacidos


secuencia = recibeSecuencia()
#Ejemplo de gen aceptado tacaaagagcagagtttttggcaacggtga
if secuencia != None:
    cadenaComplementaria = obtenerComplementaria(secuencia)
    print('Cadena Complementaria: ', cadenaComplementaria)
    rnam = obtenerRNAm(cadenaComplementaria)
    print('RNAm correspondiente: ', rnam)
    if(verificaCodon(rnam)):
        cadenaAminoacidos = generaAminoacidos(rnam)
        print('Genes traducidos:', cadenaAminoacidos)
