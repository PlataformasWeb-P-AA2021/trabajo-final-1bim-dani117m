from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_  

from genera_tablas import Provincia,  Canton, Parroquia, Establecimiento

# sql lite generador
engine = create_engine('sqlite:///bases_isntituciones.db')
Session = sessionmaker(bind=engine)
session = Session()

#* Las parroquias que tienen establecimientos únicamente en la jornada Nocturna
consulta_1 = session.query(Establecimiento).filter(
    Establecimiento.jornada == 'Nocturna').all()

for d in consulta_1:
    print(d)
    print(d.parroquia)
    print(d.parroquia.canton)
    print(d.parroquia.canton.provincia)
    print("\n")
#* Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459

consulta_2 = session.query(Establecimiento).filter(or_(Establecimiento.num_estudiantes == 448,\
    Establecimiento.num_estudiantes == 450, Establecimiento.num_estudiantes == 451, \
    Establecimiento.num_estudiantes == 454, Establecimiento.num_estudiantes == 558, \
    Establecimiento.num_estudiantes == 459, )).all()

for d in consulta_2:
    print(d)
    print(d.parroquia)
    print(d.parroquia.canton)
    print(d.parroquia.canton.provincia)
    print("\n")