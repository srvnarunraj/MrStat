from django.urls import path
from . import views

urlpatterns = [
    path('',views.Startup),
    path('histoGraph',views.histogram),
    path('scatterPlot',views.scatterPlot),
    path('barGraph',views.barGraph),
    path('lineGraph',views.lineGraph),
    path('GraphView',views.GraphView),
]
