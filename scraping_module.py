#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Módulo de scraping para el análisis de laptops en Mercado Libre Colombia.
Este módulo contiene las funciones y variables principales para el scraping.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import time
import seaborn as sns
import re
from random import randint

# URL de búsqueda de laptops en mercadolibre.com.co
url_base = 'https://listado.mercadolibre.com.co'
busqueda = 'computadores-portatiles'  # Término más específico en español

# Headers para las solicitudes HTTP
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'es-CO,es;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Referer': 'https://www.mercadolibre.com.co/'
}

def get_laptop_data(max_pages=2):
    """
    Extrae datos de laptops de Mercado Libre Colombia.
    
    Args:
        max_pages (int): Número máximo de páginas a scrapear
        
    Returns:
        list: Lista de diccionarios con información de laptops
    """
    laptop_list = []
    
    for page in range(1, max_pages + 1):
        if page == 1:
            url = f'{url_base}/{busqueda}'
        else:
            url = f'{url_base}/{busqueda}_Desde_{(page-1)*48 + 1}'
            
        print(f"Obteniendo página {page}: {url}")
        
        try:
            # Añadir un retraso aleatorio para simular comportamiento humano
            time.sleep(randint(2, 5))
            
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            # Crear un objeto BeautifulSoup a partir de la respuesta
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Probar diferentes selectores
            laptops = soup.select('li.ui-search-layout__item')
            
            if not laptops:
                laptops = soup.select('div.ui-search-result')
            
            if not laptops:
                laptops = soup.select('div[class*="ui-search-result"]')
                
            if not laptops:
                laptops = soup.select('div.ui-search-result__wrapper')
                
            print(f"Se encontraron {len(laptops)} resultados en la página {page}")
            
            # Recorrer cada laptop encontrada
            for laptop in laptops:
                try:
                    # Extraer título
                    title_element = laptop.select_one('h3.poly-component__title-wrapper a.poly-component__title')
                    if not title_element:
                        title_element = laptop.select_one('h2.shops__item-title')
                    if not title_element:
                        title_element = laptop.select_one('h2[class*="ui-search"]')
                        
                    title = title_element.text.strip() if title_element else 'Sin título'
                    
                    # Extraer precio
                    price_element = laptop.select_one('span.andes-money-amount__fraction')
                    if not price_element:
                        price_element = laptop.select_one('span.price-tag-fraction')
                    if not price_element:
                        price_element = laptop.select_one('span[class*="price-tag-fraction"]')
                        
                    price_text = price_element.text.strip().replace(".", "") if price_element else '0'
                    price = float(price_text) if price_text.isdigit() else 0
                    
                    # Extraer ubicación
                    location_element = laptop.select_one('span.ui-search-item__location')
                    location = location_element.text.strip() if location_element else 'Sin ubicación'
                    
                    # Extraer marca
                    known_brands = ['HP', 'Dell', 'Lenovo', 'Asus', 'Acer', 'Apple', 'MSI', 'Samsung', 'Toshiba', 'Huawei']
                    brand = 'Otra'
                    for known_brand in known_brands:
                        if known_brand.lower() in title.lower():
                            brand = known_brand
                            break
                            
                    # Extraer RAM
                    ram_match = re.search(r'(\d+)\s*[Gg][Bb](\s*[Rr][Aa][Mm]|\s*[Mm][Ee][Mm]|\s*[Dd][Ee]\s*[Rr][Aa][Mm])?', title)
                    ram = ram_match.group(1) if ram_match else 'No especificado'
                    
                    # Extraer procesador
                    processor_patterns = [
                        r'Intel\s+Core\s+i\d+[^\s]*',
                        r'AMD\s+Ryzen\s+\d+[^\s]*',
                        r'Intel\s+Celeron[^\s]*',
                        r'AMD\s+A\d+[^\s]*',
                        r'Snapdragon[^\s]*'
                    ]
                    
                    processor = 'No especificado'
                    for pattern in processor_patterns:
                        processor_match = re.search(pattern, title, re.IGNORECASE)
                        if processor_match:
                            processor = processor_match.group(0)
                            break
                            
                    # Extraer almacenamiento
                    storage_match = re.search(r'\d+\s*[GT][B]\s*((SSD|HDD|(?:disco duro)|(?:estado sólido)))?', title, re.IGNORECASE)
                    storage = storage_match.group(0) if storage_match else 'No especificado'
                    
                    # Agregar la información de la laptop a la lista
                    laptop_list.append({
                        'title': title,
                        'price': price,
                        'location': location,
                        'brand': brand,
                        'ram': ram,
                        'processor': processor,
                        'storage': storage
                    })
                    
                    print(f"Laptop extraída: {title[:50]}... | Precio: {price} | Ubicación: {location}")
                    
                except Exception as e:
                    print(f"Error al procesar un elemento: {e}")
                    continue
                    
        except Exception as e:
            print(f"Error al obtener la página {page}: {e}")
            continue
            
    return laptop_list

def analyze_data(laptop_list):
    """
    Analiza los datos extraídos de laptops y genera visualizaciones.
    
    Args:
        laptop_list (list): Lista de diccionarios con información de laptops
        
    Returns:
        DataFrame: Pandas DataFrame con los datos analizados
    """
    # Crear DataFrame
    df = pd.DataFrame(laptop_list)
    
    # Limpiar y transformar datos
    df['ram_num'] = pd.to_numeric(df['ram'], errors='coerce')
    
    # Visualizaciones
    # 1. Histograma de precios
    plt.figure(figsize=(10, 6))
    plt.hist(df['price'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribución de Precios de Laptops')
    plt.xlabel('Precio (COP)')
    plt.ylabel('Frecuencia')
    plt.ticklabel_format(style='plain', axis='x')
    plt.tight_layout()
    plt.savefig('precio_distribucion.png')
    plt.close()
    
    # 2. Precio promedio por marca
    plt.figure(figsize=(12, 6))
    brand_avg = df.groupby('brand')['price'].mean().sort_values(ascending=False)
    sns.barplot(x=brand_avg.index, y=brand_avg.values)
    plt.title('Precio Promedio por Marca de Laptop')
    plt.xlabel('Marca')
    plt.ylabel('Precio Promedio (COP)')
    plt.xticks(rotation=45)
    plt.ticklabel_format(style='plain', axis='y')
    plt.tight_layout()
    plt.savefig('precio_por_marca.png')
    plt.close()
    
    # 3. Distribución por ubicación
    plt.figure(figsize=(12, 6))
    location_count = df['location'].value_counts()
    sns.barplot(x=location_count.index, y=location_count.values)
    plt.title('Distribución de Laptops por Ubicación')
    plt.xlabel('Ubicación')
    plt.ylabel('Cantidad de Laptops')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('distribucion_ubicacion.png')
    plt.close()
    
    return df

def main():
    """Función principal que ejecuta el scraping y el análisis"""
    print("Iniciando scraping de laptops en Mercado Libre Colombia...")
    laptop_data = get_laptop_data(max_pages=2)
    
    if laptop_data:
        print(f"Se encontraron {len(laptop_data)} laptops en total.")
        df = analyze_data(laptop_data)
        
        # Guardar datos en CSV
        df.to_csv('laptops_data.csv', index=False)
        print("Datos guardados en 'laptops_data.csv'")
        
        # Mostrar estadísticas básicas
        print("\nEstadísticas de precios:")
        print(df['price'].describe())
        
        print("\nDistribución por marcas:")
        print(df['brand'].value_counts())
    else:
        print("No se pudieron obtener datos. Verificar la conexión o los selectores HTML.")

if __name__ == "__main__":
    main()
