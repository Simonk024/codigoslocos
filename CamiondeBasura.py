import folium
import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('garbage_truck_routes.db')
cursor = conn.cursor()

# Crear un mapa
m = folium.Map(location=[40.7128, -74.0060], zoom_start=12)

# Función para obtener la ruta del camión
def get_route(route_name):
    cursor.execute("SELECT latitude, longitude, timestamp FROM routes WHERE route_name = ?", (route_name,))
    route_points = cursor.fetchall()
    return route_points

# Función para dibujar la ruta en el mapa
def draw_route(route_points):
    route_layer = folium.FeatureGroup(name='Garbage Truck Route')
    for point in route_points:
        lat, lon, timestamp = point
        folium.Marker(location=[lat, lon], popup=timestamp).add_to(route_layer)
    route_layer.add_to(m)

# Obtener la ruta del camión
route_name = 'Route 1'  # Cambiar por el nombre de la ruta deseada
route_points = get_route(route_name)

# Dibujar la ruta en el mapa
draw_route(route_points)

# Mostrar el mapa
m

#Requisitos previos

Instalar folium y sqlite3 utilizando pip: pip install folium sqlite3
Tener una base de datos SQLite con una tabla routes que contenga las siguientes columnas:
id: identificador único de la ruta
route_name: nombre de la ruta
latitude: latitud de cada punto de la ruta
longitude: longitud de cada punto de la ruta
timestamp: timestamp de cada punto de la ruta

#Explicación

Primero, conectamos a la base de datos SQLite utilizando sqlite3.
Creamos un mapa utilizando folium y establecemos la ubicación inicial y el nivel de zoom.
Definimos una función get_route que obtiene los puntos de la ruta del camión de la base de datos según el nombre de la ruta.
Definimos una función draw_route que dibuja la ruta en el mapa utilizando folium.Marker para agregar marcadores en cada punto de la ruta.
Obtenemos la ruta del camión utilizando get_route y la dibujamos en el mapa utilizando draw_route.
Finalmente, mostramos el mapa utilizando m.
Notas

Asegúrate de reemplazar garbage_truck_routes.db con el nombre de tu base de datos SQLite.
Asegúrate de que la tabla routes tenga las columnas mencionadas anteriormente.
Puedes personalizar la apariencia del mapa y los marcadores según tus necesidades.
Esta es solo una implementación básica y puede requerir ajustes y mejoras según tus necesidades específicas.