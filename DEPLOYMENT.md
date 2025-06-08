# Guía de Despliegue en Netlify con CI/CD

Este documento describe el proceso de despliegue continuo implementado para este proyecto, utilizando GitHub Actions y Netlify.

## Configuración de Netlify

### Archivos de configuración

El archivo `netlify.toml` en la raíz del proyecto configura cómo Netlify debe construir y publicar el sitio:

```toml
[build]
  publish = "docs"
  command = ""

[[redirects]]
  from = "/scraping"
  to = "/scraping.html"
  status = 200
```

Esta configuración:
- Establece el directorio `docs` como la carpeta que contiene los archivos a publicar
- Configura una redirección para mejorar la URL del scraping

### Pasos para configurar en Netlify

1. Crear una cuenta en [Netlify](https://www.netlify.com/)
2. Conectar el repositorio de GitHub con Netlify
3. Configurar las siguientes variables de entorno en Netlify:
   - No se requieren variables de entorno adicionales para este proyecto
4. Iniciar manualmente el primer despliegue desde la interfaz de Netlify

## Flujo de trabajo de CI/CD con GitHub Actions

El archivo `.github/workflows/netlify.yml` define el flujo de trabajo de integración y despliegue continuo:

```yaml
name: Deploy to Netlify

on:
  push:
    branches:
      - main
      - master
  pull_request:
    branches:
      - main
      - master

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '16'
      
      - name: Install Netlify CLI
        run: npm install -g netlify-cli
      
      - name: Deploy to Netlify
        env:
          NETLIFY_AUTH_TOKEN: ${{ secrets.NETLIFY_AUTH_TOKEN }}
          NETLIFY_SITE_ID: ${{ secrets.NETLIFY_SITE_ID }}
        run: netlify deploy --dir=docs --prod
```

Este flujo de trabajo:
1. Se activa automáticamente cuando se realiza un push a las ramas principales
2. Configura el entorno necesario (Node.js)
3. Instala la CLI de Netlify
4. Despliega automáticamente los cambios en Netlify

## Configuración de Secretos en GitHub

Para que el flujo de trabajo funcione correctamente, es necesario configurar dos secretos en el repositorio de GitHub:

1. `NETLIFY_AUTH_TOKEN`: Token de autenticación para acceder a Netlify
   - Se puede generar en Netlify: User Settings > Applications > Personal access tokens
2. `NETLIFY_SITE_ID`: ID del sitio en Netlify
   - Se encuentra en la configuración del sitio en Netlify: Site settings > General > Site details > API ID

## Verificación del Despliegue

Cuando el flujo de trabajo se ejecuta correctamente:

1. Se puede ver el estado del despliegue en la pestaña "Actions" del repositorio de GitHub
2. Netlify proporciona una URL única para el sitio (ej. `nombre-sitio-123abc.netlify.app`)
3. También se puede configurar un dominio personalizado en la configuración de Netlify

## Beneficios de este Enfoque

- **Integración Continua**: Cada cambio en el código desencadena verificaciones automáticas
- **Despliegue Continuo**: Los cambios aprobados se publican automáticamente
- **Transparencia**: Todo el proceso es visible y registrado en GitHub
- **Consistencia**: El entorno de producción se actualiza de manera predecible y sistemática
