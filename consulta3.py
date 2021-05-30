from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_  

from genera_tablas import Provincia,  Canton, Parroquia, Establecimiento

# sql lite generador
engine = create_engine('sqlite:///bases_isntituciones.db')
Session = sessionmaker(bind=engine)
session = Session()

# * Los cantones que tiene establecimientos con 0 número de profesores
		
consulta_1 = session.query(Establecimiento).filter(
    Establecimiento.num_docentes == 0).all()

for d in consulta_1:
    print(d)
    print(d.parroquia)
    print(d.parroquia.canton)
    print(d.parroquia.canton.provincia)
    print("\n")
# * Los establecimientos que pertenecen a la parroquia Catacocha con estudiantes mayores o iguales a 21

consulta_2 = session.query(Establecimiento).join(
    Parroquia).filter(Parroquia.nombre_parroquia == 'CATACOCHA', Establecimiento.num_estudiantes \
        >= 21).all()

for d in consulta_2:
    print(d)
    print(d.parroquia)
    print(d.parroquia.canton)
    print(d.parroquia.canton.provincia)
    print("\n")