from django.conf import settings
from django.views.generic import TemplateView as BaseTemplateView, \
    DetailView as BaseDetailView, FormView as BaseFormView


class ConfigMixin(object):
    config = None
    
    def get_config(self):
        if self.config is None:
            self.config = {
                'production': settings.PRODUCTION,
                'base_url': settings.PROJECT_URL,
            }
        return self.config
    
    def get_config_data(self):
        return {
            'config': self.get_config(),
        }


class TemplateView(ConfigMixin, BaseTemplateView):
    def get_context_data(self, *args, **kwargs):
        context = super(TemplateView, self).get_context_data(*args, **kwargs)
        context.update(self.get_config_data())
        return context


class DetailView(ConfigMixin, BaseDetailView):
    def get_context_data(self, *args, **kwargs):
        context = super(DetailView, self).get_context_data(*args, **kwargs)
        context.update(self.get_config_data())
        return context


class FormView(ConfigMixin, BaseFormView):
    def get_context_data(self, *args, **kwargs):
        context = super(FormView, self).get_context_data(*args, **kwargs)
        context.update(self.get_config_data())
        return context

