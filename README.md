# Mini Data Explorer

Mini Data Explorer es una aplicación web interactiva desarrollada con Streamlit, diseñada para explorar y visualizar archivos CSV de manera rápida y eficiente.

---

## ✨ Características principales

- **Carga de datos flexible**: Permite subir archivos CSV personalizados o utilizar el dataset de ejemplo incluido.
- **Métricas instantáneas**: Visualiza rápidamente el número de filas, columnas y valores nulos.
- **Vista previa de datos**: Muestra las primeras 10 filas del dataset cargado.
- **Estadísticas descriptivas**: Calcula métricas como media, desviación estándar, cuartiles, entre otras.
- **Gráficos interactivos**: Genera visualizaciones dinámicas para analizar distribuciones y frecuencias.

---

## 🚀 Guía de instalación y uso

### 1. Clonar el repositorio
Para comenzar, clona este repositorio en tu máquina local:
```bash
git clone https://github.com/evely114/documentacion_clase.git
cd documentacion_clase
```

### 2. Instalar dependencias
Asegúrate de tener Python instalado y ejecuta el siguiente comando para instalar las dependencias necesarias:
```bash
pip install -r requirements.txt
```

### 3. Ejecutar la aplicación
Inicia la aplicación con el siguiente comando:
```bash
streamlit run app.py
```
La aplicación se abrirá automáticamente en tu navegador en [http://localhost:8501](http://localhost:8501).

---

## 📦 Dependencias

| Paquete   | Versión mínima | Descripción                       |
|-----------|----------------|-----------------------------------|
| streamlit | 1.28+          | Framework para el desarrollo de aplicaciones web interactivas. |
| pandas    | 2.0+           | Biblioteca para la manipulación y análisis de datos.          |

Instala todas las dependencias con:
```bash
pip install streamlit pandas
```

---

## 📁 Estructura del proyecto

La estructura del proyecto es la siguiente:
```
documentacion_clase/
├── app.py          # Código principal de la aplicación
├── datos.csv       # Dataset de ejemplo (usado si no se sube ningún archivo)
├── requirements.txt
└── README.md
```

---

## 🖥️ Uso de la aplicación

### Carga de datos

- **Archivo CSV personalizado**: Utiliza el botón "Sube tu CSV" en la barra lateral izquierda para cargar tu propio archivo.
- **Dataset de ejemplo**: Si no se sube ningún archivo, se cargará automáticamente el archivo `datos.csv` incluido en el proyecto.

### Exploración del dataset

La aplicación proporciona las siguientes funcionalidades:

1. **Métricas generales**: Número total de filas, columnas y valores nulos.
2. **Vista previa**: Tabla con las primeras 10 filas del dataset.
3. **Estadísticas descriptivas**: Resumen estadístico de las columnas numéricas utilizando `df.describe()`.

### Visualizaciones interactivas
Selecciona el tipo de gráfico deseado desde el menú desplegable en la barra lateral para analizar los datos de manera visual.

---

## 🛠️ Contribuciones

Contribuciones son bienvenidas. Sigue estos pasos para colaborar:

1. Realiza un fork del repositorio.
2. Crea una nueva rama para tu funcionalidad o corrección de errores:
   ```bash
   git checkout -b mi-nueva-funcionalidad
   ```
3. Realiza tus cambios y crea un commit descriptivo:
   ```bash
   git commit -m "Agrega nueva funcionalidad"
   ```
4. Sube tus cambios a tu repositorio fork:
   ```bash
   git push origin mi-nueva-funcionalidad
   ```
5. Abre un Pull Request en GitHub y describe tus cambios.

---

## 📄 Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más información.

---

## 📞 Contacto

Si tienes preguntas o sugerencias, no dudes en ponerte en contacto con el propietario del repositorio a través de [GitHub](https://github.com/evely114).