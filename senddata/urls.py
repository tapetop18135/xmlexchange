
from django.urls import path, include
from . import views
urlpatterns = [
    path('/getXML/', views.index, name='index'),
    path('/getCal/<int:x>/<int:y>', views.cal, name='cal'),
]
