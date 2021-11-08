from notifypy import Notify

notificacion = Notify()
notificacion.tittle = "Titulo"
notificacion.message = "mensaje"

notificacion.send(block=False)



