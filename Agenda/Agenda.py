import os
from datetime import datetime

class Agenda:

    lista_personas = []
    lista_empresas = []

    #abre el archivo y si no exsiste, lo crea
    with open('Data.txt', 'a') as archivo:
      pass          

    def __init__(self):
        self.lista_personas = []
        self.lista_empresas = []
  
    def menu(self):
        os.system('cls')
        print('-------------------------')
        print('-      A G E N D A      -')
        print('-------------------------')
        print('--Seleccione una opcion--')
        print()
        print('1. Agregar un contacto ')
        print('2. Borrar un contacto ')
        print('3. Mostrar un contacto ')
        print('4. Mostrar los contactos persona ')
        print('5. Salir ')
        print('-------------------------')
        seleccion = int(input())
        
        if seleccion   == 1:
            Contacto.agregar_contacto(self)
            Agenda.menu(self)
        
        elif seleccion == 2:
            # capturamos la excepcion y continuamos el flujo del programa
            # con el siguiente ingreso de opciones.
            try:
                Contacto.borrar_contacto(self)
            except ValueError:
                Contacto.borrar_contacto(self)
                
            Agenda.menu(self)
            
        if seleccion   == 3:
            Agenda.mostrar_contacto(self)
            Agenda.menu(self)
    
        elif seleccion == 4:
            Persona.mosrar_lista_personas(self)
            Agenda.menu(self)

        elif seleccion == 5:
            print('Saliendo...')
            print('::Gracias por utilizar la agenda::')
            
        else:
            print('Opcion invalida')
            Agenda.menu(self)
            input()

            
    def mostrar_contacto(self):
        print('::::MOSTRAR  CONTACTO::::')
        print('-------------------------')
        print('--Seleccione una opcion--')
        print('\n1: Mostrar una persona')
        print('2: Mostrar una empresa')
        print('-------------------------')
        seleccion = int(input())
        aux = False
    
        if seleccion == 1:
            print(':::::MOSTRAR PERSONA:::::')
            print('-------------------------')
            print('\n1. Buscar por Apellido')
            print('2. Buscar por DNI')
            seleccion2 = int(input())

            if seleccion2 == 1:
                print('Ingrese el apellido del contacto')
                apellido = input()
                ok = True
            
                with open('Data.txt', 'r') as file:
                    lineas = file.readlines()

                    for i in range(len(lineas)):
                        contacto_mostrar = lineas[i]
                        separador = ', '
                        separado = contacto_mostrar.split(separador)
                        if 'Persona' in separado[0]:
                            if ok:
                                print('\n:::::::::PERSONA:::::::::')
                                print('-------------------------')          
                                ok = False
                            if apellido in separado[1]:
                                print(':::CONTACTO ENCONTRADO:::\n')
                                for i in separado:
                                    print(i)
                                print(Persona.dia_nacimiento(separado[5]))
                                aux = True
                                input()    
                                
            elif seleccion2 == 2:
                print('Ingrese el DNI del contacto')
                dni = input()
                ok = True
            
                with open('Data.txt', 'r') as file:
                    lineas = file.readlines()

                for i in range(len(lineas)):
                    contacto_mostrar = lineas[i]
                    separador = ', '
                    separado = contacto_mostrar.split(separador)
                    if 'Persona' in separado[0]:
                        if ok:
                            print('\n:::::::::PERSONA:::::::::')
                            print('-------------------------')          
                            ok = False
                        if dni in separado[3]:
                            print(':::CONTACTO ENCONTRADO:::\n')
                            for i in separado:
                                print(i)
                            aux = True
                            input()

        elif seleccion == 2:
            print(':::::MOSTRAR EMPRESA:::::')
            print('-------------------------')
            print('\n1. Buscar por nombre')
            print('2. Buscar por CUIT')
            seleccion3 = int(input())

            if seleccion3 == 1:
                print('Ingrese el nombre de la empresa')
                nombre = input()
                ok = True
            
                with open('Data.txt', 'r') as file:
                    lineas = file.readlines()

                for i in range(len(lineas)):
                    contacto_mostrar = lineas[i]
                    separador = ', '
                    separado = contacto_mostrar.split(separador)
                    if 'Empresa' in separado[0]:
                        if ok:
                            print('\n:::::::::EMPRESA:::::::::')
                            print('-------------------------\n')          
                            ok = False
                        if nombre in separado[1]:
                            print(':::CONTACTO ENCONTRADO:::\n')
                            for i in separado:
                                print(i)
                            print(Empresa.cuando_nacio(separado[4]))
                            aux = True
                            
                            input() 

            elif seleccion3 == 2:
                print('Ingrese el CUIT de la empresa')
                cuit = input()
                ok = True
            
                with open('Data.txt', 'r') as file:
                    lineas = file.readlines()

                for i in range(len(lineas)):
                    contacto_mostrar = lineas[i]
                    separador = ', '
                    separado = contacto_mostrar.split(separador)
                    if 'Empresa' in separado[0]:
                        if ok:
                            print('\n:::::::::EMPRESA:::::::::')
                            print('-------------------------\n')          
                            ok = False
                        if cuit in separado[2]:
                            print(':::CONTACTO ENCONTRADO:::\n')
                            for i in separado:
                                print(i)
                            print(Empresa.cuando_nacio(separado[4]))
                            aux = True
                            
                            input() 
          
        else:
            print('Opcion invalida')
            input()
            Agenda.mostrar_contacto(self)
        
        if not aux:
            print('No hay contactos para mostrar en la agenda')
            input()
            Agenda.menu(self)


class Contacto:
    def __init__(self, tipo_contacto, nombre, direccion, fecha):
        self.tipo_contacto = tipo_contacto
        self.nombre = nombre
        self.direccion = direccion
        self.fecha = fecha

#coloque los metodos 'agregar' y 'borrar' en la clase Contacto, porque asi lo decia el
#enunciado, pero a mi me parecio mas logico y conveniente que esos metodos sean propios de 
#la clase Agenda, por el hecho de que un contacto no debiera poder crearse a si mismo, seria 
#mas logico que lo cree, borre y modifique, la clase Agenda.
#aun asi, repete la consigna

    def agregar_contacto(self):
        print()
        print('-   AGREGAR  CONTACTO   -')
        print('-------------------------')
        print('--Seleccione una opcion--\n')
        print('1. Agregar una PERSONA')
        print('2. Agregar una EMPRESA')
        print('-------------------------')
        seleccion = int(input())

        if seleccion == 1:
            apellido = input('Ingrese el apellido\n')
            nombre = input('Ingrese el nombre\n')
            dni = input('Ingrese el DNI\n')
            direccion = input('Ingrese la direccion\n')
            fecha_nacimiento = input('Ingrese la fecha de nacimiento (aaaa/mm/dd\n')
            person = 'Persona'
            contacto_persona = [person, apellido, nombre, dni, direccion, fecha_nacimiento]
            Agenda.lista_personas.append(contacto_persona)

            with open('Data.txt', 'a') as archivo:
                archivo.write('Tipo de contacto: ' + person + ', ')
                archivo.write('Apellido: ' + apellido + ', ')
                archivo.write('Nombre: ' + nombre + ', ')
                archivo.write('DNI: ' + dni + ', ')
                archivo.write('Direccion: ' + direccion + ', ')
                archivo.write('Fecha de nacimiento: ' + fecha_nacimiento + '\n')
                print('-----------------------------')
                print('Persona agregada exitosamente')
                print('-----------------------------')
                input()

        elif seleccion == 2:
            company = 'Empresa'
            nombre = input('Ingrese el nombre\n')
            cuit = input('Ingrese el CUIL\n')
            direccion = input('Ingrese la direccion\n')
            fecha_fundacion = input('Ingrese la fecha de fundacion (aaaa/mm/dd)\n')
            contacto_empresa = [company, nombre, cuit, direccion, fecha_fundacion]
            Agenda.lista_personas.append(contacto_empresa)

            with open('Data.txt', 'a') as archivo:
                archivo.write('Tipo de contacto: ' + company + ', ')
                archivo.write('Nombre: ' + nombre + ', ')
                archivo.write('CUIT: ' + cuit + ', ')
                archivo.write('Direccion: ' + direccion + ', ')
                archivo.write('Fecha de fundacion: ' + fecha_fundacion + '\n')
                print('-----------------------------')
                print('Empresa agregada exitosamente')
                print('-----------------------------')
                input()
            
        else:
            print('Opcion invalida')
            input()
            Contacto.agregar_contacto(self)

    def borrar_contacto(self):
        print(':::::BORRAR CONTACTO:::::')
        print('-------------------------')
        print('--Seleccione una opcion--\n')
        print('1. Borrar una persona')
        print('2. Borrar una empresa')
        print('-------------------------')
        seleccion = int(input())
        aux = False
        # validamos la respuesta
        if seleccion < 1 or seleccion > 2:
            raise ValueError('El numero no puede ser menor a 1 ni mayor a 2')
        
        elif seleccion == 1:
            print(':::::BORRAR CONTACTO:::::')
            print('-------------------------\n')
            print('Ingrese el apellido de la persona')
            print('-------------------------')
            apellido = input()
            ok = True
        
            file = open('Data.txt', 'r')
            lineas = file.readlines()
            file.close()

            for i in range(len(lineas)):
                contacto_mostrar = lineas[i]
                separador = ', '
                separado = contacto_mostrar.split(separador)

                if 'Persona' in separado[0]:
                    if ok:
                        print('\n:::::::::PERSONA:::::::::')
                        print('-------------------------')          
                        ok = False

                    if apellido in separado[1]:
                        for i in separado:
                            print(i)
                        print('\n-------------------------')          
                        print('Desea eliminar el contacto? (si/no)')
                        print('-------------------------\n')          
                        eliminar = input()
                        
                        if eliminar == 'no':
                            print('Contacto no eliminado')
                            print('-------------------------')          
                            input()
                            Agenda.menu(self)

                        file2 = open('Data.txt', 'w')
                        for line in lineas:
                            separado1 = line.split(separador)
                            if separado != separado1:
                                file2.write(line)
                            else:
                                print('Contacto eliminado...')
                                aux = True
                        file2.close()
                        input()
                        Agenda.menu(self)

        elif seleccion == 2:
            print(':::::BORRAR CONTACTO:::::')
            print('-------------------------\n')
            print('Ingrese el nombre de la empresa')
            print('-------------------------')
            apellido = input()
            ok = True
        
            file = open('Data.txt', 'r')
            lineas = file.readlines()
            file.close()

            for i in range(len(lineas)):
                contacto_mostrar = lineas[i]
                separador = ', '
                separado = contacto_mostrar.split(separador)

                if 'Empresa' in separado[0]:
                    if ok:
                        print('\n:::::::::EMPRESA::::::::')
                        print('-------------------------')          
                        ok = False

                    if apellido in separado[1]:
                        for i in separado:
                            print(i)
                        print('\n-------------------------')          
                        print('Desea eliminar el contacto? (si/no)')
                        print('-------------------------\n')          
                        eliminar = input()
                        
                        if eliminar == 'no':
                            print('Contacto no eliminado')
                            print('-------------------------')          
                            input()
                            Agenda.menu(self)

                        file2 = open('Data.txt', 'w')
                        for line in lineas:
                            separado1 = line.split(separador)
                            if separado != separado1:
                                file2.write(line)
                            else:
                                print('Contacto eliminado...')
                                aux = True
                        file2.close()
                        input()
                        Agenda.menu(self)
          

        if not aux:
            print('No hay contactos para borrar en la agenda')
            input()
            Agenda.menu(self)

class Persona(Contacto):

    def __init__(self, tipo_contacto, apellido, nombre, dni, direccion, fecha):
        super().__init__(self, tipo_contacto, nombre, direccion, fecha)
        self.apellido = apellido
        self.dni = dni

    def dia_nacimiento(fecha):
        dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
        separacion1 = str(fecha)
        separacion2= separacion1.split(': ')
        lista_fecha = separacion2[1].split('/')
        anio = int(lista_fecha[0])
        mes = int(lista_fecha[1])
        dia = lista_fecha[2]
        dia_sep = int(dia[:-1])
        d = datetime(anio, mes, dia_sep, 1, 1, 3)
        print('El contacto nacio un dia', dias[d.weekday()])

    def mosrar_lista_personas(self):
        ok = True
        with open('Data.txt', 'r') as file:
            lineas = file.readlines()

            for i in range(len(lineas)):
                contacto_mostrar = lineas[i]
                separador = ', '
                separado = contacto_mostrar.split(separador)
                if 'Persona' in separado[0]:
                    if ok:
                        print('::MOSTRAR LISTA CONTACTO::')
                        print('-------------------------\n')
                        ok = False
                    Agenda.lista_personas.append(contacto_mostrar[i])
                    # mostramos la lista
                    print(contacto_mostrar, end='')
        input()

class Empresa(Contacto):

    empresa = True
    
    def __init__(self, tipo_contacto, nombre, cuit, direccion, fecha):
        super().__init__(self, tipo_contacto, nombre, fecha)
        self.cuit = cuit
        self.direccion = direccion

    def cuando_nacio(fecha):
        separacion1 = str(fecha)
        separacion2= separacion1.split(': ')
        fundacion = separacion2[1].split('/')
        return f'La fundacion de la empresa fue el dia {fundacion[2]}, del mes {fundacion[1]}, del anio {fundacion[0]}'

# COMIENZA EL PROGRAMA
a = Agenda()
a.menu()
