import psycopg2
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
        self.promedio = None
        self.topic = value["topic"]

    def consultar(self, cursor):
        knowledge, punctuality, difficult, dedication, number_elements = 0, 0, 0, 0, 1
        name = self.professor
                
        name = name.replace(",", "")
        # query = """SELECT (g_knowledge + g_punctuality + g_difficult + g_dedication) / 4 \
        #             FROM "Professor" \
        #             where name = %s;"""
        
        # cursor.execute(query, (name,))
        # row = cursor.fetchone()
        # if row is not None:
        #     row = row[0]
        query = '''
                SELECT
                    p.g_knowledge + COALESCE(e.total_knowledge, 0) AS total_knowledge,
                    p.g_punctuality + COALESCE(e.total_punctuality, 0) AS total_punctuality,
                    p.g_difficult + COALESCE(e.total_difficult, 0) AS total_difficult,
                    p.g_dedication + COALESCE(e.total_dedication, 0) AS total_dedication,
                    COALESCE(e.total_evaluations, 0) AS total_evaluations
                FROM
                    "Professor" p
                LEFT JOIN (
                    SELECT
                        SUM(knowledge) AS total_knowledge,
                        SUM(punctuality) AS total_punctuality,
                        SUM(difficult) AS total_difficult,
                        SUM(dedication) AS total_dedication,
                        COUNT(*) AS total_evaluations
                    FROM
                        "Evaluation"
                    WHERE
                        professor_id = (
                            SELECT professor_id FROM "Professor" WHERE name = %s
                        )
                ) e ON true
                WHERE
                    p.name = %s;
            '''        
        cursor.execute(query, (name, name,))
        row = cursor.fetchone()
        average = 0
        if row is not None:
            knowledge, punctuality, difficult, dedication = row[0], row[1], row[2], row[3]
            number_elements += row[4]
            average = ((knowledge / number_elements)
                   + (punctuality / number_elements)
                   + (difficult / number_elements)
                   + (dedication /number_elements)) / 4
        return average

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
        horas = {}
        for i in self.schedule:
            if self.schedule.get(i) != None:
                #print(str(i) + " de " + str(self.schedule.get(i)[0]) + " - " + str(self.schedule.get(i)[1]))
                horas[str(i)] = [str(self.schedule.get(i)[0]), str(self.schedule.get(i)[1])]
        return horas