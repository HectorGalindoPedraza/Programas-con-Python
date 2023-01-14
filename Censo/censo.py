import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def imprimir(jefeHogar, familiares, cantFamiliares):
    clear()
    print(f"""
        =======JEFE DEL HOGAR=======
        NOMBRE: {jefeHogar['nombre']}
        APELLIDO: {jefeHogar['apellido']}
        TIPO DOCUMENTO:{jefeHogar['tipoDocumento']}
        DOCUMENTO: {jefeHogar['documentoID']}
        FECHA NACIMIENTO: {jefeHogar['fechaNacimiento']}
        DEPARTAMENTO: {jefeHogar['departamentoNacimiento']}
        CIUDAD: {jefeHogar['ciudadNacimiento']}
        DIRECCION: {jefeHogar['direccionResidencia']}
        CANT. FAMILIARES: {cantFamiliares},
     """)
    for i in range(len(familiares)):
        print(f""" 
            =======FAMILIAR {i}=======
            NOMBRE: {familiares[i]['nombre']}
            APELLIDO: {familiares[i]['apellido']}
            TIPO DOCUMENTO: {familiares[i]['tipoDocumento']}
            DOCUMENTO: {familiares[i]['documentoID']}
            FECHA NACIMIENTO: {familiares[i]['fechaNacimiento']}
            PARENTESCO: {familiares[i]['parentesco']}
        """) 



def tipoDocu():
    i=1
    while i!=0:
        tipoDoc = input('Tipo de documento de identidad (CC, CE, TI, PC): ')
        if tipoDoc == 'CC':
            i=0
            return 'CC'
        elif tipoDoc == 'CE':
            i=0
            return 'CE'
        elif tipoDoc == 'TI':
            i=0
            return 'TI'
        elif tipoDoc == 'PC':
            i=0
            return 'PC'
        else:
            print('Ingrese un tipo de documento valido')


def dataFamilia(cantFamiliares):
    familiares=[]
    for i in range(cantFamiliares):
        if cantFamiliares != 1:
            print(f'======= INGRESE LOS DATOS DEL FAMILIAR {i} =======')
        else:
            print(f'======= INGRESE LOS DATOS DEL FAMILIAR =======')

        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        tipoDocument = tipoDocu()
        documentoID = input('Número de documento de identidad: ')
        dateNacimiento = input('Fecha de nacimiento: ')
        parentesco = input('Parentesco: ')
        familiar={
            'nombre': nombre,
            'apellido': apellido,
            'tipoDocumento': tipoDocument,
            'documentoID': documentoID,
            'fechaNacimiento': dateNacimiento,
            'parentesco': parentesco,
        }
        familiares.append(familiar)
    return familiares

def dataJefe():
    print("\n======INGRESE LOS DATOS DEL JEFE DE HOGAR=======")
    nombre = input('\nNombre: ')
    apellido = input('Apellido: ')
    tipoDocument= tipoDocu()
    documentoID = input('Número de documento de identidad: ')
    dateNacimiento = input('Fecha de nacimiento: ')
    departamentoNacimiento = input('Departamento de nacimiento: ')
    ciudadNacimiento = input('Ciudad de nacimiento: ')
    direccionResidencia = input('Dirección de residencia: ')
    jefe = {
        'nombre': nombre,
        'apellido': apellido,
        'tipoDocumento': tipoDocument,
        'documentoID': documentoID,
        'fechaNacimiento': dateNacimiento,
        'departamentoNacimiento': departamentoNacimiento,
        'ciudadNacimiento': ciudadNacimiento,
        'direccionResidencia': direccionResidencia,
    }
    return jefe

def main():
    jefeHogar = dataJefe()
    cantFamiliares = int(input('Cantidad de familiares a registrar: '))
    familiares = dataFamilia(cantFamiliares)
    imprimir(jefeHogar, familiares, cantFamiliares)


if __name__ == "__main__":
    main()