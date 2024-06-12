from .storage import Storage

def storage(request):
    return {'storage': Storage(request)}
