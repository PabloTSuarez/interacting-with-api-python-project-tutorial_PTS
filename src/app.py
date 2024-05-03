#Defino librerias, variables de conexion y establezco la conexion
import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# load the .env file variables
load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,client_secret=client_secret,redirect_uri='https://localhost'))


#Defino el string del artista a consultar + almaceno en variables la respuesta
id_artista = '64tNsm6TnZe2zpcMVMOoHL'
respuesta = sp.artist_top_tracks(id_artista)
tracks = respuesta['tracks']


#Defino el dataframe y lo muestro
df_tracks = pd.DataFrame.from_records(tracks)
df_tracks


#Reordeno el DF y lo muestro
df_tracks.sort_values(['popularity'],inplace=True)
df_tracks

#Muestro los primeros 3 despues de reordenarlos
df_tracks.head(3)


#Finalmente grafico, muestro y saco conclusiones
import matplotlib.pyplot as plt

plt.scatter(x=df_tracks['popularity'],y=df_tracks['duration_ms'])
plt.show

#Terminado el ejercicio