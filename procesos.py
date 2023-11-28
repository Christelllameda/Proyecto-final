import pandas as pd
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from geopy.geocoders import Nominatim
#driver configuration
opciones=Options()
opciones.add_experimental_option('excludeSwitches', ['enable-automation'])
opciones.add_experimental_option('useAutomationExtension', False)
opciones.headless=False    # si True, no aperece la ventana (headless=no visible)
opciones.add_argument('--start-maximized')         # comienza maximizado
#opciones.add_argument('user-data-dir=selenium')    # mantiene las cookies
#opciones.add_extension('driver_folder/adblock.crx')       # adblocker
opciones.add_argument('--incognito')

def obtener_datos_obra(url):
    
    driver = webdriver.Chrome(options = opciones) # inicia el driver
    
    driver.get(url)  # abre ventana
    
    # Encuentra los elementos relevantes en la página
    elementos = driver.find_elements(By.CSS_SELECTOR, 
                                     "#main-content > div > div > div.et_pb_section.et_pb_section_0_tb_body.et_section_regular")
    
    # Extrae y procesa los datos de la obra
    valencia = [elemento.text.split("\n") for elemento in elementos]
    obra = [item.split(": ", 1)[1] if ": " in item else item for item in valencia[0]]
    
    columnas = [item.split(":")[0] if ":" in item else item for item in valencia[0]]
    
    return obra



def obtener_latitudes(direcciones):
    geolocator = Nominatim(user_agent="vzla")
    latitudes = []

    for direccion in direcciones:
        location = geolocator.geocode(direccion)
        if location:
            latitudes.append(location.latitude)
        else:
            latitudes.append(None)  # Otra opción es usar None para direcciones no encontradas

    return latitudes



def obtener_longitudes(direcciones):
    geolocator = Nominatim(user_agent="obras_vlza")
    longitudes = []

    for direccion in direcciones:
        location = geolocator.geocode(direccion)
        if location:
            longitudes.append(location.longitude)
        else:
            longitudes.append(None)  # Otra opción es usar None para direcciones no encontradas

    return longitudes


def extract_numeric_value(text):
    try:
        numeric_value = re.search(r'\d+\.*\d*', text)
        return float(numeric_value.group()) if numeric_value else None
    except Exception as e:
        print(f"Error al extraer el valor numérico: {e}")
        return None
