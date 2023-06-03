from django.shortcuts import render


def certifications(request):
    return render(request, 'certifications.html')

