# Análisis de Computadores Portátiles en Mercado Libre Colombia

[![Netlify Status](https://api.netlify.com/api/v1/badges/YOUR-NETLIFY-APP-ID/deploy-status)](https://app.netlify.com/sites/YOUR-SITE-NAME/deploys)
[![CI Tests](https://github.com/codecsrayo/web-scraping-etl/actions/workflows/tests.yml/badge.svg)](https://github.com/codecsrayo/web-scraping-etl/actions/workflows/tests.yml)

## Descripción
Este proyecto implementa técnicas de web scraping para extraer información sobre computadores portátiles disponibles en Mercado Libre Colombia. El objetivo es analizar tendencias de precios, marcas populares, configuraciones comunes y otros patrones en el mercado de laptops en Colombia.

## Objetivos
- Extraer datos de computadores portátiles de Mercado Libre Colombia mediante web scraping
- Analizar tendencias de precios por marca, configuración y ubicación
- Visualizar los resultados mediante gráficos informativos
- Implementar un flujo de trabajo DevOps con GitHub Actions para CI/CD
- Desplegar los resultados automáticamente en Netlify

## Metodología de Scraping
El proyecto utiliza las siguientes tecnologías y técnicas:
- **Bibliotecas**: Requests, BeautifulSoup4, Pandas, Matplotlib, Seaborn
- **Técnicas**: Parseo HTML, expresiones regulares, análisis de datos, visualización
- **Buenas prácticas**: Delays aleatorios entre solicitudes, headers personalizados, manejo de errores

## Estructura del Proyecto
- `scraping.py`: Script principal con la lógica de web scraping y análisis
- `scraping.ipynb`: Notebook con el desarrollo interactivo y visualizaciones
- `requirements.txt`: Dependencias del proyecto
- `.github/workflows/`: Configuración de CI/CD con GitHub Actions
- `docs/`: Directorio de despliegue con archivos HTML para Netlify
- `netlify.toml`: Configuración para el despliegue en Netlify
- `DEPLOYMENT.md`: Documentación detallada del proceso de CI/CD y despliegue

## Instalación y Uso
```bash
# Clonar el repositorio
git clone https://github.com/codecsrayo/web-scraping-etl.git
cd web-scraping-etl.git

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el script de scraping
python scraping_module.py
```

## Resultados y Conclusiones
El análisis revela patrones interesantes en el mercado de laptops en Colombia:
- Distribución de precios por marca
- Relación entre especificaciones (RAM, almacenamiento, procesador) y precio
- Tendencias de ubicación geográfica de los vendedores

Para más detalles, consulta las visualizaciones generadas en el notebook.

## Flujo de Trabajo DevOps
Este proyecto implementa un pipeline de CI/CD utilizando GitHub Actions que:
1. Ejecuta pruebas automáticas cuando se realiza un push al repositorio
2. Verifica la sintaxis y estilo del código Python
3. Genera documentación automáticamente
4. Despliega los resultados del análisis automáticamente en Netlify

## Despliegue
Los resultados del análisis y la documentación están disponibles en línea:

- **URL del proyecto**: [https://your-site-name.netlify.app](https://your-site-name.netlify.app)
- **Estado del despliegue**: Ver el badge de Netlify al principio de este README

Consulta [DEPLOYMENT.md](./DEPLOYMENT.md) para obtener información detallada sobre el proceso de CI/CD y despliegue.

## Bibliografía
- Beautiful Soup Documentation. (2023). *Beautiful Soup Documentation*. https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- McKinney, W. (2022). *Python for Data Analysis*. O'Reilly Media.
- Mitchell, R. (2018). *Web Scraping with Python: Collecting More Data from the Modern Web*. O'Reilly Media.
