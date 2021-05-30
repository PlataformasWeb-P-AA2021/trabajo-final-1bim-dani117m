
##from typing_extensions import Required
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Canton

# se importa información del archivo configuracion
# datos
# para el ejemplo se usa la base de datos
# sqlite
##engine = create_engine(cadena_base_datos)
engine = create_engine('sqlite:///bases_isntituciones.db')
Session = sessionmaker(bind=engine)
session = Session()

# se leee csv
with open("data/Listado-Instituciones-Educativas.csv", "r", encoding="utf-8") as csv_file:
    lector_canton = csv.reader(csv_file, delimiter='|')
    leer = list(lector_canton)
    lista = []
    for d in leer:
        # analziar si tiene datos repetidos
        if [d[4],d[5], d[2]] not in lista:
            # solo se eligen lso valores unicos eliminando los duplicados 
            lista.append([d[4],d[5], d[2]])
            # Agregar los datos
            agregar = Canton(codigo_canton=d[4],  codigo_provincia=d[2], nombre_canton=d[5])
            session.add(agregar)

# se confirma las transacciones
session.commit()

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