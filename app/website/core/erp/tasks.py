from celery import shared_task
#from planrcomm.celery import app

@shared_task(queue='request_queue')
def horario(ciclo_escolar, id_carrera, materias, horas):
    pass
    #print(f'working with {id_carrera} and {ciclo_escolar}')
    #return ciclo_escolar, id_carrera