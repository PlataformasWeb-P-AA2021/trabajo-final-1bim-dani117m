
##from typing_extensions import Required
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Parroquia

# se importa información del archivo configuracion

# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///bases_isntituciones.db')
Session = sessionmaker(bind=engine)
session = Session()

# se lee el csv

with open("data/Listado-Instituciones-Educativas.csv", "r", encoding="utf-8") as archivo:
    lector_par = csv.reader(archivo, delimiter='|')
    leer = list(lector_par)
    lista = []
    for d in leer:
       # analziar si tiene datos repetidos
        if [d[6],d[4],d[7]] not in lista:
            # solo se eligen los valores unicos eliminando los duplicados 
            lista.append([d[6],d[4], d[7]])
            # Agregar los datos
            agregar = Parroquia(codigoParroquia=d[6],
                                codigoC=d[4],nombre_parroquia=d[7])
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