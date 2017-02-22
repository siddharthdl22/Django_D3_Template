from django.conf.urls import url
from studentwebsite import views
from studentwebsite import templates
from django.conf import settings
from django.conf.urls.static import static

app_name = 'studentwebsite'
urlpatterns = [
    url(r'^getstudentlist/$', views.get_student_list, name = "get_student_list"),
    url(r'^$', views.show_student_page, name = "show_student_page"),
]
