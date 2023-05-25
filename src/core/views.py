from django.views.generic import TemplateView

class FrontPageView(TemplateView):
    template_name = 'core/frontpage.html'
