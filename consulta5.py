from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_  

from genera_tablas import Provincia,  Canton, Parroquia, Establecimiento

# sql lite generador
engine = create_engine('sqlite:///bases_isntituciones.db')
Session = sessionmaker(bind=engine)
session = Session()

# * Los establecimientos ordenados por nombre de parroquia que tengan más de 20 profesores y la cadena "Permanente" en tipo de educación.
		
consulta_1 = session.query(Establecimiento).join(Parroquia).order_by(Parroquia.nombre_parroquia).\
    filter(Establecimiento.num_docentes > 20, Establecimiento.tipoEdu.like("%Permanente%")).all()

for d in consulta_1:
    print(d)
    print(d.parroquia)
    print(d.parroquia.canton)
    print(d.parroquia.canton.provincia)
    print("\n")
#* Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D02.

consulta_2 = session.query(Establecimiento).order_by(Establecimiento.sostenimiento).\
    filter(Establecimiento.codigo_distrito == '11D02').all()

for d in consulta_2:
    print(d)
    print(d.parroquia)
    print(d.parroquia.canton)
    print(d.parroquia.canton.provincia)
    print("\n")