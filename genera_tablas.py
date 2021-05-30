from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.expression import column, true

# se importa información del archivo configuracion
##from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

engine = create_engine('sqlite:///bases_isntituciones.db')

Base = declarative_base()



##
class Provincia(Base):
    __tablename__ = 'provincia'
    codigo_provincia = Column(String(10), primary_key=True)
    nombre_provincia = Column(String(50))
    # Relaciones
    canton = relationship("Canton", back_populates="provincia")
    def __repr__(self):
        return "Provincia: codigo_provincia=%s nombre_provincia=%s" % (
                          self.codigo_provincia, 
                          self.nombre_provincia)

###
class Canton(Base):
    __tablename__ = 'canton'
    codigo_canton = Column(String(10), primary_key=True)
    nombre_canton = Column(String(100))
    # se agrega la columna club_id como ForeignKey
    codigo_provincia = Column(Integer, ForeignKey('provincia.codigo_provincia'))
    # relaciones 
    provincia = relationship("Provincia", back_populates="canton")
    parroquia = relationship("Parroquia", back_populates="canton")
    def __repr__(self):
        return "Canton: codigo_canton: %s codigo_provincia: %s nombre_canton: %s " % (
                self.codigo_canton,
                self.codigo_provincia,
                self.nombre_canton)
class Parroquia(Base):
    __tablename__ = 'parroquia'
    codigoParroquia = Column(String(10), primary_key=True)
    nombre_parroquia = Column(String(100))
    
    # se agrega la columna id como ForeignKey
    codigoC = Column(String, ForeignKey('canton.codigo_canton'))
    # relaciones entre las clasese 
    canton = relationship("Canton", back_populates="parroquia")
    establecimiento = relationship("Establecimiento", back_populates="parroquia")
    def __repr__(self):
        return "Parroquia: codigoParroquia: %s nombre_parroquia: %s codigoC: %s" % (
                self.codigoParroquia,
                self.codigoC,
                self.nombre_parroquia)

###
class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    amie = Column(String(100), primary_key= True)
    nombreInstitu = Column(String(100))
    sostenimiento = Column(String(20))
    tipoEdu = Column(String(50))
    modalidad = Column(String(25))
    jornada = Column(String(25))
    acceso = Column(String(25))
    num_estudiantes = Column(Integer)
    num_docentes = Column(Integer)
    codigo_distrito = Column(String(100))
    # Mapea la relación entre las clases
    codigoParroquia = Column(String(10), ForeignKey('parroquia.codigoParroquia'))
    # llave foránea
    parroquia = relationship("Parroquia", back_populates="establecimiento")
    def __repr__(self):
        return "Establecimiento: amie=%s nombreInstitu=%s sostenimiento=%s tipoEdu=%s\
            modalidad=%s jornada=%s acceso=%s num_estudiantes=%d num_docentes=%d codigo_distrito=%s codigoParroquia=%s" % (
                          self.amie, 
                          self.nombreInstitu, 
                          self.sostenimiento,
                          self.tipoEdu, 
                          self.modalidad, 
                          self.jornada,
                          self.acceso, 
                          self.num_estudiantes, 
                          self.num_docentes,
                          self.codigo_distrito,
                          self.codigoParroquia)







Base.metadata.create_all(engine)