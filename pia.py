import re
class produccion:
desde  fecha  y hora importar  fecha y hora

import  fecha y hora
registro  = []

def  main ():
    menú ()


#Funcion para validad correo
def  valcorreo ( s ):
    mientras que es  cierto :
        correo  =  entrada ( s )
        si  re . coincidir ( '^ (\ w | \. | \ _ | \ -) ​​+ [@] (\ w | \ _ | \ - | \.) + [.] \ w {2,3} $' , correo ) :
            devolver  correo
        otra cosa :
            si  len ( correo ) ==  0 :
                menú ()
            imprimir ( correo )    
            imprimir ( 'Correo invalido' )    
     
#Funcion para validad nombre            
def  valnombre ( s ):
    mientras que es  cierto :
        nombre  =  entrada ( s )
        si  re . match ( '^ [AZ] {5,40} $' , nombre ):
            volver  nombre
        otra cosa :
            print ( 'Nombre incorrecto' )       

#funcion para validar la fecha 
def  valfecha ():
    mientras que es  cierto :
        prueba :
            _FechaNacimiento  =  input ( "Fecha de nacimiento (aaaa-mm-dd):" )
            si ( _FechaNacimiento == "" ):
                print ( "La fecha de nacimiento no se puede omitir." )
            otra cosa :
                if ( re . match ( r "^ [0-9] {4} - [0-9] {2} - [0-9] {2} $" , _FechaNacimiento )):
                    anio = int ( _FechaNacimiento [ 0 : 4 ])
                    mes = int ( _FechaNacimiento [ 5 : 7 ])
                    dia = int ( _FechaNacimiento [ - 2 :])
                    FechaNacimiento  =  fecha y hora . fecha y hora ( anio , mes , dia )
                    volver  FechaNacimiento
                    rotura
                otra cosa :
                    print ( "El dato no está en formato aaaa-mm-dd." )
        excepto  ValueError :
            print ( "La fecha no es una fecha válida." )     


# funcion para buscar los datos de un participante y mostrarlos 
def  buscar ():
        print ( '############# Buscar participantes #########################' )
        correo  =  valcorreo ( 'Ingresa el correo:' )
        indice  =  buscar_participante ( correo )
        si  índice  > =  0 :
            print ( f ' { registro [ indice ]. correo } \ t { registro [ indice ]. nombre } \ t { registro [ indice ]. nacimiento } \ t { registro [ indice ]. momento } ' )
            
        otra cosa :
             print ( 'Ese correo no está registrado en la lista' )
        menú ()

#funcion para buscar indice del participante         
def  buscar_participante ( correo ):    
    si  len ( correo ) >  0 :
        para  i  en  rango ( len ( registro )):
            si  registro [ i ]. correo  ==  correo :
                regreso  yo
        retorno  - 1
    menú ()            


# Función para registrador participante
def  registro_participante ():
    imprimir ( '#################### Registro participante ################################################################################################################################################################################################################################################################################# ####### ' )
    correo  =  valcorreo ( 'Ingresa el correo:' )
    indice  =  buscar_participante ( correo )
    si el  índice  <  0 :
        nombre  =  valnombre ( 'Ingresa el nombre:' )
        nacimiento  =  valfecha ()
        momento  =  fecha y hora . fecha y hora . ahora ()
        registro . añadir ( Participante ( correo , nombre , nacimiento , momento ))
        menú ()
    otra cosa :
        imprimir ( '####################################################################################################################################################################################################################################################################################################### ####################### ' )
        print ( 'correo ya registrado' )
        print ( f ' { registro [ indice ]. correo } \ t { registro [ indice ]. nombre } \ t { registro [ indice ]. nacimiento } \ t { registro [ indice ]. momento } ' )
        menú ()

#funcion para saber si la opcion que ingreso es valida 
def  opcion_correcta ( s ):
    
    mientras que es  cierto :
        opcion  =  input ( '¿Qué opcion desea ?:' )
        si  re . match ( '^ [X]? [x]? [1-8]? $' , opción ):
            return  int ( opcion )
        otra cosa :
            print ( 'Error !!!! Opcion no valida' )


#funcion para mostrar la lista de participantes registrados
def  mostrar_listado ( lista ):
    print ( '########################### Lista de participantes ##################################################################################################################################################################################################################################################################### ########################## ' )
    si  len ( lista ) > 0 :
        para  elemento  en  lista :
            
            print ( f ' { elemento . correo } \ t { elemento . nombre } \ t { elemento . nacimiento } \ t { elemento . momento } ' )
    otra cosa :
        
        print ( 'La lista esta vacia' )    
    menú ()  







#funcion para mostrar menu pedir la opcion e enviar a la funcion elegida
def  menu ():
    imprimir ( '################## Menú ############################################################################################################################################################################################################################################################################# ########## ' )
    print ( '[1] Cargar informacion de CSV' )
    print ( '[2] Registrar participantes' )
    print ( '[3] Buscar participantes' )
    print ( '[4] Modificar participantes' )
    print ( '[5] Eliminar participante' )
    print ( '[6] Ver lista de participantes' )
    print ( '[7] Actualizar información CSV' )
    print ( '[8] Serealizar información a JSON' )
    imprimir ( '[X] Salir' )
    opcion  =  opcion_correcta ( 'Que opcion desea:' )

    si  opcion  ==  1 :
        print ( 'Proximamente carga informacion' )
    elif  opcion  ==  2 :
        registro_participante ()
    elif  opcion  ==  3 :
        print ( 'Proximamente buscar' )
    elif  opcion  ==  4 :
        print ( 'Proximamente modificar' )
    elif  opcion  ==  5 :
        print ( 'Proximamente eliminar' )
     opcion  elif ==  6 :
        mostrar_listado ( registro )
        menú ()
    elif  opcion  ==  7 :
        print ( 'Proximamente actualizar' )
    elif  opcion  ==  8 :
        print ( 'Proximamente seralizar' )

principal ()
df.to_csv('ejemplo.csv')