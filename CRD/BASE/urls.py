from django.urls import path,include
from .views import prod,addProd,prodId,delId,updateId,get_PRODUCTION_id,get_producer,get_artists,get_supervisors,newTask2

from .views import gettasks2
from .views import get_task2_ids_by_production
from .views import delTaskId,gettask2Id
from .views import updateTask2,updatetask2Version
from .views import createUser
from .views import start
from .views import createProd
from .views import call_listei,call_listes
from django.contrib.auth.views import LoginView,LogoutView
# from rest_framework_simplejwt.views import TokenObtainPairView


# from rest_framework_simplejwt.views import TokenObtainPairView

# class TokenObtainPairView(TokenObtainPairView):
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         return response


from .views import CustomTokenObtainPairView3
from .views import CustomTokenObtainPairView2

from .views import createdir
from .views import createTask
urlpatterns = [
    path('dir/',createdir),
    # path('pr/',createProd),
    # path('tk/',createTask),
    # path('index',start,name='index'),
    path('productions',prod),
    path('tasks2',gettasks2),
    path('task2/<str:task_id>',gettask2Id),
    
    #liste les chargés de production disponible (
    #appelée pour créer une production : le formulaire pour en créer une doit permettre d'afficher
    # et sélectionner un ou plusieurs)  )
    path('producer/', get_producer),
    
    
    path('artists/', get_artists),
    
    path('supervisors/', get_supervisors),

    #affiche une production en particulier à partir de son ID
    path('production/<str:prod_id>/', prodId),
    
    #supprime une production à partir de son ID
    path('delete/<str:prod_id>/', delId),
    path('deleteTask/<str:prod_id>/', delTaskId),
    
    #met à jour les informations d'une production à partir de son ID
    path('update/<str:prod_id>/', updateId),
    path('updatetask2/<str:task2_id>/', updateTask2),
    path('updatetask2version/<str:id>/', updatetask2Version),
    
    #joute une productions
    # path('change',addProd),
    path('change',createProd),
    
    
    #creation tache
    # path('newtask2',newTask2),
    path('newtask2',createTask),
    # path('newtask2',newTask2),
    
    
    path('get_prod_id/<int:task_id>/', get_PRODUCTION_id, name='get_production_id'),
    
    
   
    #obtient les tâches liées à une production à partir de son ID
    path('get_task2_ids_by_production/<int:production_id>/', get_task2_ids_by_production, name='get_task2_ids_by_production'),

    ##auth
    path('createuser', createUser, name='createuser'),
    
    # path('login/', login, name='login'),
    
    path('api/auth/token/', CustomTokenObtainPairView3.as_view(), name='token_obtain_pair'),
    
    path('call_listei/<str:nameprod>/<str:nametask>/<str:nametasktype>',call_listei,name="call_listei"),
    path('call_listes/<str:nameprod>/<str:nametask>/<str:nametasktype>',call_listes,name="call_listes"),

    

    
    
    
    
]






