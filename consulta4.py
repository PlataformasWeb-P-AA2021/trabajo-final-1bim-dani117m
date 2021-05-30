from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_  

from genera_tablas import Provincia,  Canton, Parroquia, Establecimiento

# sql lite generador
engine = create_engine('sqlite:///bases_isntituciones.db')
Session = sessionmaker(bind=engine)
session = Session()

# * Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores. 
		
		
consulta_1 = session.query(Establecimiento).order_by(Establecimiento.num_estudiantes).\
    filter(Establecimiento.num_docentes >= 100).all()

for d in consulta_1:
    print(d)
    print(d.parroquia)
    print(d.parroquia.canton)
    print(d.parroquia.canton.provincia)
    print("\n")
#* Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores.

consulta_2 = session.query(Establecimiento).order_by(Establecimiento.num_docentes).\
    filter(Establecimiento.num_estudiantes >= 100).all()

for d in consulta_2:
    print(d)
    print(d.parroquia)
    print(d.parroquia.canton)
    print(d.parroquia.canton.provincia)
    print("\n")