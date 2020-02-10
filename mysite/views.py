from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from mysite import forms
def home_view(request):
    template_name = 'home.html'
    content = {}
    return render(request, template_name, content)


def credits_view(request):
    template_name = 'credits.html'
    content = {}
    return render(request, template_name, content)


def about_view(request):
    template_name = 'about.html'
    content = {}
    return render(request, template_name, content)


class CreatePlaceView(View):
    template_name = template_name = 'register.html'
    def get(self, request, *args, **kwargs):
        form = forms.PlaceForm
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = forms.PlaceForm(request.POST)
        if form.is_valid():
            form.save()
        context = {"form": form}
        return render(request, self.template_name, context)
