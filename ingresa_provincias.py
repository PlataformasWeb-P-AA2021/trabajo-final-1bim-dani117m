from typing import Text
##from typing_extensions import Required
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Provincia

# se importa información del archivo configuracion
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///bases_isntituciones.db')

Session = sessionmaker(bind=engine)
session = Session()

#  se leee csv
with open("data/Listado-Instituciones-Educativas.csv","r", encoding="utf-8") as archivo:
    lector_csv = csv.reader(archivo, delimiter='|')
    datos_pro = list(lector_csv)
    leer = []    
for d in datos_pro:
    # analziar si tiene datos repetidos
    if [d[2], d[3]] not in leer:
        # solo se eligen los valores unicos eliminando los duplicados 
        leer.append([d[2],d[3]])
        # Agregar los datos
        agregar = Provincia(codigo_provincia=d[2],nombre_provincia=d[3])
        session.add(agregar)

# agregar
session.commit()

# se confirma las transacciones
# 0|Código AMIE
# 1|Nombre de la Institución Educativa
# 2|Código División Política Administrativa Provincia
# 3|Provincia
# 4|Código División Política Administrativa  Cantón
# 5|Cantón
# 6|Código División Política Administrativa  Parroquia
# 7|Parroquia
# 8|Código de Distrito
# 9|Sostenimiento
# 10|Tipo de Educación
# 11|Modalidad|Jornada
# 12|Acceso (terrestre/ aéreo/fluvial)
# 13|Número de estudiantes
# 14|Número de docentes
