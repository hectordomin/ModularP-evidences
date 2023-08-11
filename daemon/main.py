import copy
import numpy as np
from Dataset import Dataset
from Scheduler import Scheduler

class Individuo:
    def __init__(self, alelos, longitud_gen, cromosoma):
        self._alelos = alelos
        self._longitud_gen = longitud_gen
        self._cromosoma = cromosoma
        self._fitness = 0

class AG:
    def __init__(self, cantidad_individuos, alelos, tamano_gen, generaciones, p, problema):
        self._cantidad_individuos = cantidad_individuos
        self._alelos = alelos
        self._tamano_gen = tamano_gen
        self._generaciones = generaciones
        self._p = p
        self._problema = problema
        self._individuos = np.array([])

    def run(self):
        self.crearIndividuos()
        self._mejor_historico = self._individuos[0]
        generacion = 1
        while generacion <= self._generaciones:
            self.evaluaIndividuos()
            hijos = np.array([])
            while len(hijos) < len(self._individuos):
                padre1 = self.ruleta()
                padre2 = self.ruleta()
                while padre1 == padre2:
                    padre2 = self.ruleta()
                h1, h2 = self.cruza(self._individuos[padre1], self._individuos[padre2])
                hijos = np.append(hijos, [h1])
                hijos = np.append(hijos, [h2])
            self.mutacion(hijos)
            self._individuos = np.copy(hijos)
            self._individuos[np.random.randint(len(self._individuos))] = copy.deepcopy(self._mejor_historico)
            generacion += 1

        print('Respuesta binaria:     '+ str(self._mejor_historico._cromosoma))
        print("Fitness: " + str(self._mejor_historico._fitness))
        print("Horario")
        index = 0
        for i in self._mejor_historico._cromosoma:
            if i != 0:
                print("NRC : " + self._problema._valores[index][i-1].nrc)
                print("Profesor: " + self._problema._valores[index][i-1].professor)
                self._problema._valores[index][i-1].printSchedule()
            index += 1

    def crearCromosoma(self): #COMPLETA
        cromosoma = []
        for alelo in self._problema._valores:
            size = len(alelo)
            cromosoma.append(np.random.randint(size+1)) #PONEMOS UN MAS UNO, PARA CONSIDERAR A LA POSICION 0 COMO NADA
        return cromosoma

    def crearIndividuos(self): #COMPLETA
        for _ in range(self._cantidad_individuos):
            cromosoma = self.crearCromosoma()
            individuo = Individuo(self._alelos, self._tamano_gen, cromosoma)
            self._individuos = np.append(self._individuos, [individuo])

    def evaluaIndividuos(self): #COMPLETA
        for i in self._individuos:
            i._fitness = self._problema.f(i._cromosoma)
            if i._fitness > self._mejor_historico._fitness and self._problema.aptitude(i._cromosoma):
                self._mejor_historico = copy.deepcopy(i)

    def ruleta(self):
        f_sum = np.sum([i._fitness for i in self._individuos])
        if f_sum < 0:
            f_sum *= -1
        if f_sum == 0:
            return np.random.randint(len(self._individuos))
        else:
            r = np.random.randint(f_sum + 1)
            k = 0
            F = self._individuos[k]._fitness
            if F < 0:
                F *= -1
            while F < r and k < len(self._individuos):
                k += 1
                if self._individuos[k]._fitness < 0:
                    F += self._individuos[k]._fitness * -1
                else:
                    F += self._individuos[k]._fitness
            return k

    def cruza(self, i1, i2):
        h1 = copy.deepcopy(i1)
        h2 = copy.deepcopy(i2)

        s = self._alelos - 1
        punto_cruza = np.random.randint(s) + 1
        h1._cromosoma[punto_cruza:], h2._cromosoma[punto_cruza:] = h2._cromosoma[punto_cruza:], h1._cromosoma[punto_cruza:]
        return h1, h2

    def mutacion(self, hijos):
        for h in hijos:
            for bit in range(len(h._cromosoma)):
                if np.random.rand() < self._p:
                    size = len(self._problema._valores[bit])
                    h._cromosoma[bit] = np.random.randint(size)
        
def main():
    A = Dataset()
    s1 = A.query("I7040") ; s2 = A.query("I7038")
    s3 = A.query("I7031") ; s4 = A.query("I5888")
    s5 = A.query("I5890") ; s6 = A.query("I7041")
    subjects = [s1, s2, s3, s4, s5, s6]
    target =  {'I':[15,21], 'V':[15, 21], 'S':[7, 15]}
    problema = Scheduler(subjects, target)
    alelos = len(subjects)
    individuos = 100
    tamano_gen = 1 #cada celda representa a una materia
    generaciones = 1000
    factor_mutacion = 0.01
    ag = AG(individuos, alelos, tamano_gen, generaciones, factor_mutacion, problema)
    ag.run()
main()
