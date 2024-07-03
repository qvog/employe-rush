from .storage import Storage
#from .models import DefaultStorage

def storage(request):
    return {'storage': Storage(request)}
