# Trabajo Final Primer Bimestre

## Uso de SqlAlchemy

Dada la información de la carpeta ***data***. Realizar las siguientes tareas:

* Analizar el contenido

* Identificar las posibles entidades que se puedan generar

* Las entidades deben satisfacer lo siguiente:
	* Un establecimiento tiene características propias.
	* Un establecimiento pertenece a una parroquia.
	* Una parroquia pertence a un cantón.
	* Un cantón pertence a un provincia.

* Generar un proceso de generación de entidades a través de SqlAlchemy. Usar Sqlite
	* genera_tablas.py

* Ingresar la información en cada entidad creada.
	* ingresa_provincias.py
	* ingresa_cantones.py
	* ingresa_parroquias.py
	* ingresa_establecimientos.py

* Generar las siguientes consultas:
	* consulta1.py
		* Todos los establecimientos de la provincia de Loja.
		* Todos los establecimientos del cantón de Loja.
	* consulta2.py
    	* Las parroquias que tienen establecimientos únicamente en la jornada Nocturna
		* Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459
	* consulta3.py
		* Los cantones que tiene establecimientos con 0 número de profesores
		* Los establecimientos que pertenecen a la parroquia Catacocha con estudiantes mayores o iguales a 21
	* consulta4.py
		* Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores. 
		* Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores.
	* consulta5.py
		* Los establecimientos ordenados por nombre de parroquia que tengan más de 20 profesores y la cadena "Permanente" en tipo de educación.
		* Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D02.

Guía de uso del proyecto final:

Para iniciar con la creación del proyecto debemos ejecutar primero:
Genera_tablas.py el cual generada un sqllite con las tablas vacías.
A continuación, se ejecuta ingreso del ingreso de datos que seguiría el siguiente orden:
1.Ingresa_provincias ---> 2.Ingresa_cantones ---> 3.Ingresa_parroquias ---> 4.Ingresa_establecimiento

Una vez se realiza este proceso la base de datos está completamente funcional y lista para que se realicen consultas.
En caso de la ejecución de las consultas, las misma tiene un orden por ello se puede ejecutar cualquiera de ellas en cualquier momento.

