# pydungen

PyDungen es una pequeña utilidad en Python para generar mapas de mazmorras aleatorios. Para ello usa un conjunto de imágenes llamados geomorfos. La aplicación incluye un conjunto de estas imágenes listas para su uso en la carpeta BLUE (CC-By-SA 4.0), aunque se pueden usar otras imágenes como las creadas por el gran Dyson Logos.

Para poder usar este programa es necesario tener instalada alguna versión de Python 3. También es necesario tener instalada la librería PIL (Python Image Libray), que puede instalarse con el siguiente comando:

pip3 install pillow

# Ejecutar el programa

PyDungen requiere dos parámetros: la carpeta con los geomorfos que queremos usar y el nombre que queremos para la imagen resultado. Un ejemplo sería:

python3 pydungen.py BLUE mapagen

Cuyo resultado consistirá en una imagen final llamada mapagen.png y otras cuatro imagenes que son los cuadrantes que dan lugar a dicha imagen final.

Para agilizar la ejecución, y a modo de ejemplo, se incluye un script para Windows y Linux/MacOS que básicamente ejecuta el comando anterior (pydungen.sh y pydungen.bat)



