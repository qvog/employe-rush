from django.db import models
from .storage import Storage

class EmployerStorage(Storage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)




