from base import TemplateView


class HomepageView(TemplateView):
    template_name = "homepage.html"

homepage_view = HomepageView.as_view()
