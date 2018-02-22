import pandas as pd

# INSTRUCCION
# Es necesario instalar el paquete folium desde Anaconda Navigator
import folium

# INSTRUCCION
# Debeis descargaros un fichero csv con un conjunto de registros (records) de una especie
# desde la pagina del OBIS: http://www.iobis.org y leerla en un DataFrame de pandas
# que se llame specie con pd.read_csv
manati = pd.read_csv ('trichechus_manatus.csv', sep=',')
coral_cervic = pd.read_csv('acropora_cervicornis.csv')
coral_palm = pd.read_csv('acropora_palmata.csv')


# elegir solo occurencias desde 2013 para reducir tamaño de df
manati_act = manati.query('year >= 2013')
cor_cervic_act = coral_cervic.query('year >= 2013')
cor_palm_act = coral_palm.query('year >= 2013')


# Lectura de latitud y longitud de las observaciones
lon_m, lat_m = manati_act['decimalLongitude'], manati_act['decimalLatitude']
lon_cc, lat_cc = cor_cervic_act['decimalLongitude'], cor_cervic_act['decimalLatitude']
lon_ca, lat_ca = cor_palm_act['decimalLongitude'], cor_palm_act['decimalLatitude']

# MODIFICABLE
# Lectura de datos adicionales (se deben convertir a cadena para visualizarlos)
dates_m = manati_act['eventDate'].astype('str')
dates_cc = cor_cervic_act['eventDate'].astype('str')
dates_ca = cor_cervic_act['eventDate'].astype('str')

# MODIFICABLE
# Opciones de visualizacion de la especie
# Debeis ajustar las coordenadas y el zoom del mapa a la localizacion de la especie
# Muchas mas en: http://python-visualization.github.io/folium/docs-v0.5.0/modules.html
m = folium.Map(location=None, zoom_start=10, tiles='Stamen Watercolor')

# Creacion del conjunto de puntos
feature_group_m = folium.FeatureGroup('Ocurrences')
feature_group_cc = folium.FeatureGroup('Ocurrences')
feature_group_ca = folium.FeatureGroup('Ocurrences')

# MODIFICABLE
for lon_m, lat_m, date_m in zip(lon_m, lat_m, dates_m):
    feature_group_m.add_child(folium.Marker(location=[lat_m, lon_m], popup=date_m, 
                            icon=folium.Icon(color='green')))
    
for lon_cc, lat_cc, date_cc in zip(lon_cc, lat_cc, dates_cc):
    feature_group_cc.add_child(folium.Marker(location=[lat_cc, lon_cc], popup=date_cc, 
                            icon=folium.Icon(color='red')))

for lon_ca, lat_ca, date_ca in zip(lon_ca, lat_ca, dates_ca):
    feature_group_ca.add_child(folium.Marker(location=[lat_ca, lon_ca], popup=date_ca, 
                            icon=folium.Icon(color='orange')))


# Se incorporan los puntos al mapa
m.add_child(feature_group_m)
m.add_child(feature_group_cc)
m.add_child(feature_group_ca)

# Se guarda el mapa como una pagina web
m.save('index.html')
