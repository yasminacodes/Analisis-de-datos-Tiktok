import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar el driver de Selenium (asegúrate de tener el driver correspondiente instalado y en el PATH)
driver = webdriver.Chrome()

# URL de la página a la que deseas hacer scraping
url = 'https://www.tiktok.com/@yasminacodes'

try:
    # Abrir la página en el navegador controlado por Selenium
    driver.get(url)

    # Esperar a que el título se cargue (aumentamos el tiempo de espera a 20 segundos)
    titulo_principal_elemento = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main-content-others_homepage"]/div/div[1]/div[1]/div[2]/h1'))
    )
    
    # Imprimir el título principal utilizando repr() para manejar caracteres problemáticos
    print("Título Principal:", repr(titulo_principal_elemento.text).encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))

    # Obtener el número de seguidores, seguidos y me gusta
    seguidores_elemento = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main-content-others_homepage"]/div/div[1]/h3/div[2]/strong'))
    )
    seguidos_elemento = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main-content-others_homepage"]/div/div[1]/h3/div[1]/strong'))
    )
    me_gusta_elemento = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main-content-others_homepage"]/div/div[1]/h3/div[3]/strong'))
    )

    # Imprimir el número de seguidores, seguidos y me gusta
    print("Seguidos:", seguidos_elemento.text)
    print("Seguidores:", seguidores_elemento.text)
    print("Me gusta:", me_gusta_elemento.text)
    
    # Hacer clic en el botón (aumentamos el tiempo de espera a 10 segundos)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="loginContainer"]/div/div/div[3]/div/div[2]/div/div/div'))
    ).click()
    
    # Esperar a que el título se cargue (aumentamos el tiempo de espera a 20 segundos)
    titulo_elemento = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main-content-others_homepage"]/div/div[1]/h2'))
    )
    
    # Imprimir el título utilizando repr() para manejar caracteres problemáticos
    print("Título:", repr(titulo_elemento.text).encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))

    # Obtener los elementos con los XPath proporcionados
    for i in range(1, 16):  # Cambia el rango según el número de elementos que desees obtener
        xpath_text = '//*[@id="main-content-others_homepage"]/div/div[2]/div[3]/div/div[{}]/div[2]/div/a/div/span[1]'.format(i)
        xpath_url = '//*[@id="main-content-others_homepage"]/div/div[2]/div[3]/div/div[{}]/div[2]/div/a'.format(i)
        
        # Esperar a que el texto y la URL del elemento estén presentes
        elemento_texto = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, xpath_text))
        )
        elemento_url = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, xpath_url))
        )
        
        # Obtener el texto y la URL del elemento
        texto = elemento_texto.text
        url = elemento_url.get_attribute('href')
        print(url)

finally:
    # Cerrar el navegador controlado por Selenium
    driver.quit()
