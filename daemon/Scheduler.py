import psycopg2

def ranges_overlap(start1, end1, start2, end2):
    return not (end1 <= start2 or end2 <= start1)

class Scheduler:
    def __init__(self, valores, desired_schedule):
        self._valores = valores
        self.desired = desired_schedule
    
    def prettySchedule(self, values):
        start = values[0]
        start = int(start[0]+start[1])
        end = values[1]
        if end[2] == '5' and end[3] == '5':
            end = int(end[0]+end[1]) + 1
        else:
            end = int(end[0]+end[1])
        return [start, end]
    
    def suitable(self, day, lapse, selected):
        for element in selected:
            slot = element.split(',')
            d = slot[0] ; time = slot[1].split('-')
            start = int(time[0]) ; end = int(time[1])
            if ranges_overlap(start, end, lapse[0], lapse[1]) and day == d:
                return False
        s = day+","+str(lapse[0])+"-"+str(lapse[1])
        return not s in str(selected)
    
    def isValid(self, cromosoma): #FUNCION FITNESS ADAPTADA
        index = 0
        selected = []
        for alelo in cromosoma:
            if alelo != 0: #SI ES 0, QUIERE DECIR QUE YA NO SE LLEVARA ESA MATERIA
                subject = self._valores[index][alelo-1]
                if self.posible(subject, selected) == False:
                    return False
            index += 1
        return True
    
    def posible(self, subject, selected):
        if subject != None:
            schedule = subject.schedule
            for day in schedule.keys():
                if schedule[day] != None:
                    horario = self.prettySchedule(schedule[day])
                    if self.suitable(day, horario, selected):
                        selected.append(day+","+str(horario[0])+"-"+str(horario[1]))
                    else:
                        return False
        return True
    
    def aptitude(self, subject, selected, aptitud):
        aux = 0
        if subject != None:
            schedule = subject.schedule
            for day in schedule.keys():
                if schedule[day] != None:
                    horario = self.prettySchedule(schedule[day])
                    if self.desired.get(day) != None:
                        desired = self.desired[day]
                        if horario[0]>= desired[0] and horario[1]<=desired[1]:
                            aux += 10
                        else:
                            aux -= 10
                    else:
                        return False  
                    if self.suitable(day, horario, selected):                       
                        selected.append(day+","+str(horario[0])+"-"+str(horario[1]))
                    else:
                        return False
            aptitud[0] += aux
        return True

    def f(self, cromosoma): #FUNCION FITNESS ADAPTADA
        index = 0
        selected = [] #ARREGLO PARA GUARDAR MATERIAS QUE YA FUERON SELECCIONADAS
        aptitud = [0]
        aux = 0
        
        
        for alelo in cromosoma:
            if alelo != 0: #SI ES 0, QUIERE DECIR QUE YA NO SE LLEVARA ESA MATERIA
                subject = self._valores[index][alelo]
                
                if self.aptitude(subject, selected, aptitud) == False:
                    return 0
                """
                    *** AQUI DEBE AGREGARSE LA CONSULTA A LA CALIFICACION DEL PROFESOR ***
                """
                if subject.promedio is not None:
                    aux += subject.promedio

            index += 1
        
        return aptitud[0] + aux


"""
def test(day, lapse, selected):
    for element in selected:
        slot = element.split(',')
        d = slot[0] ; time = slot[1].split('-')
        start = int(time[0]) ; end = int(time[1])
        if ranges_overlap(start, end, lapse[0], lapse[1]) and day == d:
            return False
    s = day+","+str(lapse[0])+"-"+str(lapse[1])
    return not s in str(selected)

sel = ["S,7-11","I,13-15","V,13-15","L,11-13","I,11-13"]

if test("I", [15,17], sel):
    print("Viable")
else:
    print("Not viable")
"""