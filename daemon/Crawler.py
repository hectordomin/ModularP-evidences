import requests
import psycopg2
from bs4 import BeautifulSoup
from .Subject import Subject

class Crawler:
    URL = "http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta"
    def __init__(self, ciclo, carrera) -> None:
        self.form = {
            "ciclop": ciclo,
            "cup": "D",
            "majrp": carrera,
            "crsep": None,
            "materiap": None,
            "horaip": None,
            "horafp": None,
            "edifp": None,
            "aulap": None,
            "ordenp": "0",
            "mostrarp": "100",
            "dispp":"D"
        }

    def query(self, cve):
        self.form["crsep"] = cve
        response = requests.post(self.URL, data=self.form)
        # Realizar una solicitud POST para enviar los datos del formulario
        topic = None
        response = requests.post(self.URL, data=self.form)
        soup = BeautifulSoup(response.text, features='html.parser')
        # Encontrar la tabla en el HTML
        tabla = soup.find('table')
        #print(tabla)
        query = [None]
        professor = None ; nrc = None ; days = None; schedule = None
        # Recorrer las filas de la tabla
        for fila in tabla.find_all('tr'):
            # Recorrer las columnas de cada fila
            #print(fila)
            #NRC
            if fila.select('td') and fila.select('td')[0].text.strip() != "01":
                #print("NRC: " + str(fila.select('td')[0].text.strip()))
                nrc = fila.select('td')[0].text.strip()
                if topic == None:
                    topic = fila.select('td')[2].text.strip()
            for columna in fila.find_all('td'):
                #print(columna)
                #PROFESOR
                if columna.select('.tdprofesor'):
                    #print(columna.select('.tdprofesor')[1].text.strip())
                    professor = (columna.select('.tdprofesor')[1].text.strip())
                if columna.find('table', class_ = 'td1'):
                    item = columna.find_all('td')
                    STD_ELEMENTS = 6
                    #DIAS Y HORAS
                    schedule = []
                    days = []
                    for i in range(len(item) // STD_ELEMENTS):
                        #print("Dias: " + str(item[i*STD_ELEMENTS+2].text.strip()))
                        #print("Horario: " + str(item[i*STD_ELEMENTS+1].text.strip()))
                        self.checkday(str(item[i*STD_ELEMENTS+2].text.strip()).split(), days)
                        self.schedule(str(item[i*STD_ELEMENTS+1].text.strip()).split("-"), schedule)
                if professor != None and nrc != None and days != None and schedule != None:
                    aux = Subject({"nrc" : nrc, "professor": professor, "days":days, "schedule":schedule, "topic": topic})
                    query.append(aux)
                    professor = None ; nrc = None ; days = None; schedule = None
        db_params = {
                    "dbname": "CPdb",
                    "user": "postgres",
                    "password": "devusr",
                    "host": "164.92.95.57",
                    "port": "5455"  
                }
        connection = psycopg2.connect(**db_params)
        #print("Conexión exitosa a la DB")
        cursor = connection.cursor()
        for i in query:
            if i is not None:
                i.consultar(cursor)
        cursor.close()
        connection.close()
        return query, topic

    

    def checkday(self, values, days):
        for i in values:
            if i != ".":
                days.append(i)

    def schedule(self, values, schedule):
        schedule.append(values)

"""def printResult(arr, name):
    print(name)
    for i in arr:
        if i != None:
            print(i.nrc)
            print(i.professor)
            i.printSchedule()
            print(i.promedio)
        else:
            print("None")

test = Crawler("202310", "INCO")
result, name = test.query("I5888")
printResult(result, name)"""
