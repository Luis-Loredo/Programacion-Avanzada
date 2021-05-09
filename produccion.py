import csv, re, os

from datetime import datetime
import pathlib
import datetime
from os import remove

ruta =str(pathlib.Path().absolute())+'/produccion2.csv'
archivo_csv =ruta

class Lote:
    
    def __init__(self, clave='', nombre='', caducidad='', unidades=''):
        self.clave = clave
        self.nombre = nombre
        self.caducidad = caducidad
        self.unidades = unidades
        
        # Metodos Accesores
    def getClave(self):
        while True:
            clave = str(input("Ingresa la clave del lote en formato AAA-000 o X para salir:"))
            if clave == 'X':
                return clave
            elif bool(re.match("^[A-Z]{3}-\d{3}$", clave)):
                return clave
            print('Error ingrese de nuevo')    
            
            
    def getNombre(self):
        while True:
            nombre = str(input("Ingresa el nombre del producto (De 5 a 30 caracteres alfanumericos): "))
            if bool(re.match("^[A-Z-a-z]{5,40}$", nombre)):
                return nombre
                
            print("El nombre del producto es: ")
        
    def getCaducidad(self):
        while True:
            try:
                caducidad = input("Fecha de caducidad (aaaa-mm-dd): ")
                if (caducidad ==""):
                    print("La fecha de caducidad no se puede omitir.")
                else:
                    if (re.match(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", caducidad)):
                        print("La caducidad es de: ")
                        anio=int(caducidad[0:4])
                        mes=int(caducidad[5:7])
                        dia=int(caducidad[-2:])
                        caducidad = datetime.date(anio, mes, dia)
                        return caducidad
                    else:
                        print("El dato no está en formato aaaa-mm-dd.")
            except ValueError:
                print("La fecha no es una fecha válida.")
                
    def getUnidades(self):
        while True:
            unidades = int(input("Cuantas cantidad de unidades producidas (valor ente 100 y 1000): "))
            if unidades >= 100 and unidades <= 1000 :
                return self.unidades
            else:
                print('Cantidad no validad, intente de nuevo')

def llenar_lista(lista):
    if os.path.exists(archivo_csv):
        try:
            with open(archivo_csv, 'r', newline='', encoding='utf-8') as archivo:
                contador = 0
                lector = csv.reader(archivo, delimiter='|')
                for linea in lector:
                    if contador > 1:
                        lista.append(Lote(linea[0], linea[1], linea[2], linea[3]))
                    contador += 1
        except Exception as e:
            print(f'Ha ocurrido un error al llenar la lista: {e}')

def agregar_registros(lista):
    try:

        remove(archivo_csv)

        with open(archivo_csv, 'a', newline='', encoding='utf-8') as archivo:  
            archivo.write('Clave|Nombre|Caducidad|Unidades\n')          
            for e in lista:
                archivo.write(f'{e.clave}|{e.nombre}|{e.caducidad}|{e.unidades}\n')
        
            
    except Exception as e:
        print(f'Ocurrió un problema: {e}')



def crear_archivo(registro):
    try:
        with open(archivo_csv, 'w', newline='', encoding='utf-8') as archivo:
            archivo.write('Clave|Nombre|Caducidad|Unidades\n')
            for e in registro:
                archivo.writes(f'{e.clave}|{e.nombre}|{e.caducidad}|{e.unidades}\n')
    except Exception as e:
        print(f'Ocurrió un problema: {e}')

def actualizar_csv(lista):
    if os.path.exists(archivo_csv):
        agregar_registros(lista)
    else:
        crear_archivo(lista)

def mostrar_listado(lista):
    print('########################### Lista de produccion ############################################')
    if len(lista) >0:
        for elemento in lista:
            
            print(f'{elemento.clave}\t{elemento.nombre}\t{elemento.caducidad}\t{elemento.unidades}')
    else:
        
        print('La lista esta vacia')  

def buscar_clave(clave):    
    if len(clave) > 0:
        for i in range(len(produccion)):
            if produccion[i].clave == clave:
                return i
        return -1



produccion = []
llenar_lista(produccion)

l = Lote('ABC-123','queso','2021-08-21','150')
produccion.append(l)
while True:
 
    clave = l.getClave()
    print(clave)
    esta = buscar_clave(clave)
   
    if clave == 'X':
        break
    elif esta >= 0:
        print('Clave ya registrada')  
            
    else:
        nombre = l.getNombre()
        caducidad = l.getCaducidad()
        unidad = l.getUnidades()
        clasproduccion= Lote(clave,nombre,caducidad,unidad)
        produccion.append(clasproduccion)  



mostrar_listado(produccion)        
actualizar_csv(produccion)


print('Saliendo....')

 