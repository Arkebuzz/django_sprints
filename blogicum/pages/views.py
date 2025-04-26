from django.shortcuts import render


def about(request):
    template_name = 'pages/about.html'
    return render(request, template_name)


def rules(request):
    template_name = 'pages/rules.html'
    return render(request, template_name)


def page404(request, exception):
    template_name = 'base.html'
    return render(request, template_name, status=404)
