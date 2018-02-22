import pandas as pd
# INSTRUCCION
# Es necesario instalar el paquete folium desde Anaconda Navigator
import folium

# INSTRUCCION
# Debeis descargaros un fichero csv con un conjunto de registros (records) de una especie
# desde la pagina del OBIS: http://www.iobis.org y leerla en un DataFrame de pandas
# que se llame specie con pd.read_csv
specie = pd.read_csv (trichechus_manatus.csv, sep=',')

# Lectura de latitud y longitud de las observaciones
lon, lat = specie['decimalLongitude'], specie['decimalLatitude']

# MODIFICABLE
# Lectura de datos adicionales (se deben convertir a cadena para visualizarlos)
dates = specie['eventDate'].astype('str')

# MODIFICABLE
# Opciones de visualizacion de la especie
# Debeis ajustar las coordenadas y el zoom del mapa a la localizacion de la especie
# Muchas mas en: http://python-visualization.github.io/folium/docs-v0.5.0/modules.html
m = folium.Map(location=[50, 10], zoom_start=4, tiles='Stamen Watercolor')

# Creacion del conjunto de puntos
feature_group = folium.FeatureGroup('Ocurrences')

# MODIFICABLE
for lon, lat, date in zip(lon, lat, dates):
    feature_group.add_child(folium.Marker(location=[lat, lon], popup=date))

# Se incorporan los puntos al mapa
m.add_child(feature_group)

# Se guarda el mapa como una pagina web
m.save('index.html')
