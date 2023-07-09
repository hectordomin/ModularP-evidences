class Scheduler:
    def __init__(self, valores, desired_schedule):
        self._valores = valores
        self.desired = desired_schedule

    #VERIFICAR QUE ESTE DENTRO DEL HORARIO Y QUE NO SE EMPALMEN LOS HORARIOS
    def isValid(self, subject, selected):
        schedule = subject.schedule
        aux = 0
        for day in self.desired.keys():
            #VALIDACION DE QUE ESTA EN LOS DIAS SELECCIONADOS
            if schedule[day] != None:
                horario = self.prettySchedule(schedule[day])
                desired = self.desired[day]
                #VALIDAR QUE ESTA EN EL HORARIO
                if horario[0]>= desired[0] and horario[1]<=desired[1]:
                    #VALIDAR QUE NO SE ENCUENTRA REPETIDO
                    if not self.suitable(day, schedule[day], selected):
                        lapse = schedule[day]
                        selected.append(day+","+str(lapse[0])+"-"+str(lapse[1]))
                        aux += 1
        return aux == subject.getSize()
    
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
        s = day+","+str(lapse[0])+"-"+str(lapse[1])
        return s in selected
    
    def aptitude(self, cromosoma): #FUNCION FITNESS ADAPTADA
        index = 0
        selected = []
        for alelo in cromosoma:
            if alelo != 0: #SI ES 0, QUIERE DECIR QUE YA NO SE LLEVARA ESA MATERIA
                subject = self._valores[index][alelo-1]
                if not self.isValid(subject, selected):
                    return False
            index += 1
        return True

    def f(self, cromosoma): #FUNCION FITNESS ADAPTADA
        index = 0
        selected = []
        aptitud = 0
        for alelo in cromosoma:
            if alelo != 0: #SI ES 0, QUIERE DECIR QUE YA NO SE LLEVARA ESA MATERIA
                subject = self._valores[index][alelo-1]
                if self.isValid(subject, selected):
                    aptitud += 10
                else: 
                    return 0
            index += 1
        return aptitud