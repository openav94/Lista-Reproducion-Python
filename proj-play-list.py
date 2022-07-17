playlist = {}
playlist['canciones'] = []

#funcion Principal
def app():
    #agregar playlist
    agregar_playlist = True
    
    while agregar_playlist:
        nombre_playlist = input('Como quieres nombrar la PlayList?\r\n')
        
        if nombre_playlist:
            playlist['nombre playlist'] = nombre_playlist
            print("\r\n")
            
        #cerrar bucle ya tenemos nombre de la playlist
        agregar_playlist = False
                
        #Llamar la funcion agregar canciones
        agregar_canciones()
        
#funcion para agregar las canciones
def agregar_canciones():
    #bandera para agregar canciones
    agregar_cancion = True
    
    while agregar_cancion:
        #Preguntar al usuario las canciones que quiere agregar
        nombre_playlist = playlist['nombre playlist']
        pregunta = f'Agrega canciones para la playlist {nombre_playlist}: \r\n'
        pregunta += 'Escribe "X" para dejar de agregar canciones \r\n'
        
        cancion = input(pregunta)
        print("\r\n")
        
        if cancion == 'X':
            #dejaremos de agregar canciones
            agregar_cancion = False
            
            #Mostrar resumen de la playlist
            mostrando_resumen()            
            print('Finanlizando...\r\n')
            
        else:
            #seguir agregando canciones
            playlist['canciones'].append(cancion)            
            #print(playlist)
            
#Funcion para mostrar resumen de la lista de reproduccion
def mostrando_resumen():
    nombre_playlist = playlist['nombre playlist']
    print(f'Playlist: {nombre_playlist} \r\n')
    print('Canciones: \r\n') 
    for cancion in playlist['canciones']:
        print(cancion)
    print('\r\n')


#Funcion principal
app()        
    
    