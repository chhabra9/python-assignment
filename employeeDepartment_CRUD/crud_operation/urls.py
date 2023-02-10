from django.urls import path
from . import views
urlpatterns=[
    path('getEmployee',views.getEmployee,),
    path('insertEmployee',views.insertEmployee,),
    path('updateEmployee/<int:id>',views.updateEmployee,),
    path('deleteEmployee/<int:id>',views.deleteEmployee,),
    path('insertDepartment',views.insertDepartment,),
    path('getDepartment',views.getDepartment),
    path('updateDepartment/<int:id>',views.updateDepartment),
     path('deleteDepartment/<int:id>',views.deleteDepartment)
]