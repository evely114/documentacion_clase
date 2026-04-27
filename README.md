🔍 Mini Data Explorer
Aplicación web interactiva construida con Streamlit para explorar y visualizar cualquier archivo CSV de forma rápida y sencilla.

✨ Características

📂 Carga de datos flexible — sube tu propio CSV o usa el dataset de ejemplo incluido
📏 Métricas instantáneas — filas, columnas y valores nulos a golpe de vista
👀 Vista previa — muestra las primeras 10 filas del dataset
📊 Estadísticas descriptivas — media, desviación estándar, cuartiles y más
📈 Gráficos interactivos — distribución de variables numéricas y frecuencia de variables categóricas


🚀 Instalación y uso
1. Clona el repositorio
bashgit clone https://github.com/tu-usuario/mini-data-explorer.git
cd mini-data-explorer
2. Instala las dependencias
bashpip install -r requirements.txt
3. Ejecuta la aplicación
bashstreamlit run app.py
La app se abrirá automáticamente en tu navegador en http://localhost:8501.

📦 Dependencias
PaqueteVersión mínimaDescripciónstreamlit1.28+Framework de la aplicación webpandas2.0+Carga y manipulación de datos
Instálalas todas de una vez:
bashpip install streamlit pandas

📁 Estructura del proyecto
mini-data-explorer/
├── app.py          # Código principal de la aplicación
├── datos.csv       # Dataset de ejemplo (usado si no se sube ningún archivo)
├── requirements.txt
└── README.md

🖥️ Cómo usar la aplicación
Cargar datos

CSV propio — usa el botón "Sube tu CSV" en la barra lateral izquierda
Dataset de ejemplo — si no subes nada, se carga datos.csv automáticamente

Explorar el dataset
Una vez cargados los datos, la app muestra tres secciones principales:

Métricas — número de filas, columnas y valores nulos totales
Vista previa — tabla con las primeras 10 filas
Estadísticas descriptivas — tabla con df.describe() para todas las columnas numéricas

Gráfico interactivo
Selecciona el tipo de visualización desde el selector:

Distribución de una variable numérica — elige una columna numérica y verás un gráfico de barras con sus valores
Frecuencia de una variable categórica — elige una columna de texto y verás un gráfico con el conteo de cada categoría


⚙️ Configuración
La página se configura con los siguientes parámetros de Streamlit:
pythonst.set_page_config(
    page_title='Mini Data Explorer',
    page_icon='🔍',
    layout='wide',
)
Para cambiar el dataset de ejemplo, reemplaza el archivo datos.csv en la raíz del proyecto manteniendo el mismo nombre.

🤝 Contribuir

Haz un fork del repositorio
Crea una rama para tu feature (git checkout -b feature/nueva-funcionalidad)
Haz commit de tus cambios (git commit -m 'Añade nueva funcionalidad')
Haz push a la rama (git push origin feature/nueva-funcionalidad)
Abre un Pull Request


📄 Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.