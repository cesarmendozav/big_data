import pandas as pd
import matplotlib.pyplot as plt

# Definición de la ruta del archivo de chat de WhatsApp
RUTA_ARCHIVO = 'WhatsApp Chat with Cabildo.txt'

def leer_chat(archivo):
    """
    Lee y procesa un archivo de chat de WhatsApp para extraer fecha, hora, autor y mensaje.

    Parámetros:
    archivo (str): Ruta al archivo de chat de WhatsApp.

    Devuelve:
    pandas.DataFrame: Un DataFrame con las columnas 'Fecha_Hora', 'Autor' y 'Mensaje'.
    """
    datos = []  # Lista para almacenar los datos procesados
    with open(archivo, "r", encoding="utf-8") as file:
        for linea in file:
            try:
                fecha_hora, resto = linea.strip().split(' - ', 1)
                autor, mensaje = resto.split(': ', 1)
            except ValueError:
                # Maneja líneas que no se ajustan al formato esperado, como mensajes del sistema
                continue
            datos.append([fecha_hora, autor, mensaje])

    df = pd.DataFrame(datos, columns=['Fecha_Hora', 'Autor', 'Mensaje'])
    # Convertir 'Fecha_Hora' a datetime para facilitar el análisis temporal
    df['Fecha_Hora'] = pd.to_datetime(df['Fecha_Hora'], errors='coerce', format='%d/%m/%Y, %H:%M')

    return df

# Procesar el archivo de chat
df_chat = leer_chat(RUTA_ARCHIVO)

# Análisis básico: contar los mensajes por usuario
conteo_mensajes = df_chat['Autor'].value_counts()

# Mostrar el conteo de mensajes por autor
print(conteo_mensajes)

# Visualización: Gráfico de barras del número de mensajes por autor
conteo_mensajes.plot(kind='bar')
plt.xlabel('Autor')
plt.ylabel('Número de Mensajes')
plt.title('Mensajes por Autor en el Chat de WhatsApp')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()  # Ajusta automáticamente los parámetros de la figura para que encaje todo
plt.show()
