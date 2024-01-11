import corefilegeneros as cfg
import corefileactores as cfa
import corefileformatos as cff
header="""
*******************************************
* SISTEMA GESTOR DE PELICULAS BLOCKBUSTER *
*******************************************
"""
print(header)

menugp=print('1.administrador de generos\n2.Administrador de actores\n3.Administrador de formatos\n4.Gestor de informes\n5.Gestor peliculas\n6.salir')
opcion=int(input("Selecciona una de estas opciones:\n:)"))
if opcion==1:
    title="""
    *****************************************
    *          GESTOR DE GENEROS            *
    *****************************************
    """
    print(title)
    menugg=print('1.crear genero\n2.Listar genero\n3.ir a menu principal')
    rta=int(input("cual es su seleccion: \n:) "))
    if rta==1:
        genero={}
        G01={
            'id':'',
            'nombre':''
        }
        G01['id']=input("Ingrese id de la pelicula:\n:)")
        G01['nombre']=input("Ingrese nombre de la pelicula:\n:)")
        genero.update(G01)
        cfg.crear(genero)
        
        quiere=input("Desea agregar otro genero si (s) o no(n): \n:) ").lower
        if quiere=="s":genero={}
        G01={
            'id':'',
            'nombre':''
        }
        G01['id']=input("Ingrese id de la pelicula:\n:)")
        G01['nombre']=input("Ingrese nombre de la pelicula:\n:)")
        genero.update(G01)
        cfg.addData(genero)

        
    elif rta==2:
        print()
elif opcion==2:
    titi="""
    *****************************************
    *          GESTOR DE ACTORES            *
    *****************************************
    """
    print(titi)
    menua=(print('1.crear actor\n2.Listar actor\n3.ir a menu principal'))
    rta2=int(input("cual es su seleccion: \n:) "))
    if rta2==1:
        A01={}
        actor={
            'id':'',
            'nombre':''
        }
        
        actor['id']=input("Ingrese id del actor o actriz:\n:)")
        actor['nombre']=input("Ingrese nombre del actor o actriz:\n:)")
        A01.update(actor)
        cfa.crear(A01)      
    elif rta2==2:
        pass
elif opcion==3:
    g="""
    *****************************************
    *          GESTOR DE FORMATOS           *
    *****************************************
    """
    print(g)
    menuf=(print('1.crear formato\n2.Listar formato\n3.ir a menu principal'))
    rta3=int(input("cual es su seleccion: \n:) "))
    if rta3==1:
        F01={}
        formato={
            'id':'',
            'nombre':''
        }
        
        formato['id']=input("Ingrese id del formato:\n:)")
        formato['nombre']=input("Ingrese nombre del formato dvd o blueray:\n:)")
        F01.update(formato)
        cff.crear(F01)      
    elif rta3==2:
        pass
elif opcion==4:
    tito="""
    *****************************************
    *         GESTOR DE PELICULAS           *
    *****************************************
    """
    print(tito)
    menup=(print('1.agragar pelicula \n2.editar pelicula\n3.eliminar pelicula\n4.eliminar actor\n5.buscar pelicula\6.listar todas las peliculas\n7.ir al menu principal'))
elif opcion==5:
    tita="""
    *****************************************
    *          GESTOR DE INFORMES           *
    *****************************************
    """
    print(tita)
    menui=(print('1.listar por genero\n2.Listar por actor\n3.sinopsis\n4.ir al menu principal'))
elif opcion==6:
    pass
else:
    print("Opcion invalida... Reinicia el programa")