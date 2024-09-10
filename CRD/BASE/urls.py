from django.urls import path,include
from .views import prod,prodId,delId,updateId,get_PRODUCTION_id,get_producer,get_artists,get_supervisors

from .views import gettasks2
from .views import get_task2_ids_by_production
from .views import delTaskId,gettask2Id
from .views import updateTask2,updatetask2Version
from .views import createUser
from .views import start
from .views import createProd
from .views import call_listei,call_listes
from .views import updateTaskName
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
from .views import launch_scene
from .views import pathAdd
from .views import vpath
from .views import image_production
from .views import updateSup
from .views import updateArtist
from .views import updateDueDate
from .views import updateStatus

urlpatterns = [
    path('updateTaskName/<str:id>',updateTaskName),
    path('updatesup/<str:id>',updateSup),
    path('updateartist/<str:id>',updateArtist),
    path('updateduedate/<str:id>',updateDueDate),
    path('updatestatus/<str:id>',updateStatus),
    path('image/<str:idprod>/',image_production),
    path('vpath/<str:id>/',vpath),
    path('changepath/<str:id>/',pathAdd),
    path('productions',prod),
    path('tasks2',gettasks2),
    path('task2/<str:task_id>',gettask2Id),
    
    path('producer/', get_producer),
    
    
    path('artists/', get_artists),
    
    path('supervisors/', get_supervisors),

    path('production/<str:prod_id>/', prodId),
    
    path('delete/<str:prod_id>/', delId),
    path('deleteTask/<str:prod_id>/', delTaskId),
    
    #met à jour les informations d'une production à partir de son ID
    path('update/<str:prod_id>/', updateId),
    path('updatetask2/<str:task2_id>/', updateTask2),
    path('updatetask2version/<str:id>/', updatetask2Version),
    
    #joute une production
    path('change',createProd),
    
    
     #joute une task
    path('newtask2',createTask),
    
    
    path('get_prod_id/<int:task_id>/', get_PRODUCTION_id, name='get_production_id'),
    
    
   
    #obtient les tâches liées à une production à partir de son ID
    path('get_task2_ids_by_production/<int:production_id>/', get_task2_ids_by_production, name='get_task2_ids_by_production'),

    #creation user
    path('createuser', createUser, name='createuser'),
    
  
    #files management
    path('api/auth/token/', CustomTokenObtainPairView3.as_view(), name='token_obtain_pair'),
    
    path('call_listei/<str:nameprod>/<str:nametask>/<str:nametasktype>',call_listei,name="call_listei"),
    path('call_listes/<str:nameprod>/<str:nametask>/<str:nametasktype>',call_listes,name="call_listes"),
    path('launch_scene/',launch_scene, name='lancer_scene'),

    

    
    
    
    
]






