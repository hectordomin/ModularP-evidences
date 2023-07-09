import requests
from bs4 import BeautifulSoup

class Subject:
    def __init__(self) -> None:
        self.nrc = None
        self.schedule = {"L":None, "M":None, "I":None, "J":None, "V":None, "S":None}
        self.professor = None

    def __init__(self, value):
        self.nrc = value['nrc']
        self.schedule = {"L":None, "M":None, "I":None, "J":None, "V":None, "S":None}
        self.confSchedule(value['days'], value['schedule'])
        self.professor = value['professor']

    def confSchedule(self, days, schedule):
        if len(days) == len(schedule):
            index = 0
            for day in days:
                self.schedule[day] = schedule[index]
                index += 1
        elif len(schedule) == 1:
            for day in days:
                self.schedule[day] = schedule[0]
        else:
            print("ERROR")

    def getSize(self):
        size = 0
        for i in self.schedule:
            if self.schedule.get(i) != None:
                size += 1
        return size 
    
    def printSchedule(self):
        for i in self.schedule:
            if self.schedule.get(i) != None:
                print(str(i) + " de " + str(self.schedule.get(i)[0]) + " - " + str(self.schedule.get(i)[1]))

class Dataset:
    URL = "http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta"
    def __init__(self) -> None:
        self.form = {
            "ciclop": "202310",
            "cup": "D",
            "majrp": "INCO",
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
        response = requests.post(self.URL, data=self.form)
        soup = BeautifulSoup(response.text, features='html.parser')
        # Encontrar la tabla en el HTML
        tabla = soup.find('table')
        query = []
        professor = None ; nrc = None ; days = None; schedule = None
        # Recorrer las filas de la tabla
        for fila in tabla.find_all('tr'):
            # Recorrer las columnas de cada fila
            #NRC
            if fila.select('td') and fila.select('td')[0].text.strip() != "01":
                #print("NRC: " + str(fila.select('td')[0].text.strip()))
                nrc = fila.select('td')[0].text.strip()
            for columna in fila.find_all('td'):
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
                    aux = Subject({"nrc" : nrc, "professor": professor, "days":days, "schedule":schedule})
                    query.append(aux)
                    professor = None ; nrc = None ; days = None; schedule = None
        return query

    def checkday(self, values, days):
        for i in values:
            if i != ".":
                days.append(i)

    def schedule(self, values, schedule):
        schedule.append(values)