from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import RedirectView, TemplateView

from oscar.apps.catalogue.models import Product


class HomeView(TemplateView):
    """
    This is the home page and will typically live at /
    """
    template_name = 'promotions/home.html'
    
    def get(self, request, *arg, **kwargs):
      products = Product.objects.all()
      return render(request, self.template_name, {"products": products})


class RecordClickView(RedirectView):
    """
    Simple RedirectView that helps recording clicks made on promotions
    """
    permanent = False
    model = None

    def get_redirect_url(self, **kwargs):
        try:
            prom = self.model.objects.get(pk=kwargs['pk'])
        except self.model.DoesNotExist:
            return reverse('promotions:home')

        if prom.promotion.has_link:
            prom.record_click()
            return prom.link_url
        return reverse('promotions:home')
