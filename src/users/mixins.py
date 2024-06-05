from django.core.exceptions import PermissionDenied
from django.contrib.auth.views import redirect_to_login

class EmployerRequiredMixin:
    """
    Mixin to check if the user is an employer.
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not request.user.type == 'EMPLOYER':
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self):
        return redirect_to_login(self.request.get_full_path())
    
class WorkerRequiredMixin:
    """
    Mixin to check if the user is an worker.
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not request.user.type == 'WORKER':
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self):
        return redirect_to_login(self.request.get_full_path())