
##from typing_extensions import Required
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import  Establecimiento

# se importa información del archivo configuracion
##from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///bases_isntituciones.db')
Session = sessionmaker(bind=engine)
session = Session()
# se lee el csv
with open("data/Listado-Instituciones-Educativas.csv","r", encoding="utf-8") as archivo:
    lector_csv = csv.reader(archivo, delimiter='|')
    datos_pro = list(lector_csv)
    leer = []
    for d in datos_pro:
        # analziar si tiene datos repetidos
        if ([d[0],  d[6],
             d[8], d[1],
            d[9], d[10],
            d[11], d[12], d[13],
                d[14], d[15]]) not in leer:
            # solo se eligen lso valores unicos eliminando los duplicados 
            leer.append([d[0], d[1],
                          d[8], d[9], d[10],
                          d[11], d[12], d[13],
                          d[14], d[15]])
            # Agregar los datos
            agregar = Establecimiento(amie=d[0], 
                nombreInstitu=d[1],
                sostenimiento=d[9], tipoEdu=d[10],
                modalidad=d[11], jornada=d[12], 
                acceso=d[13],
                num_estudiantes=d[14], 
                num_docentes=d[15],
                codigo_distrito=d[8],
                codigoParroquia=d[6])
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