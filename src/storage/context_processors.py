from .storage import Storage
from .models import EmployerStorage

def storage(request):
    return {'storage': Storage(request)}

def employer_storage(request):
    return {'employer_storage': EmployerStorage(request)}