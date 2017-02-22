from django.shortcuts import render
from studentwebsite import services
from django.http import JsonResponse


def get_student_list(request):
    get_list = services.student_list()
    return JsonResponse(get_list, safe = False)

def show_student_page(request):
    return render(request, 'studentwebsite/index.html')
