

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import JsonResponse
from rest_framework import status
from django.db.models import F

from .models import*
from .serializers import *
from .models import Path

import os
import shutil

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

    
from BACKEND.settings import env as e

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import *
from .serializers import TaskSerializer2, ProducerSerializer, CgArtist2Serializer, Supervisor2Serializer, TaskSerializer2_noId

import requests

def start(request):
    return render(request, 'index.html')


# path_ngrok="https://f87f-93-2-82-77.ngrok-free.app/"
# path_ngrok="http://127.0.0.1:8080/"
# path_ngrok="https://34f3-93-2-82-77.ngrok-free.app/"

# @api_view(['GET'])
# def createdir(request):
#     req=requests.get(path_ngrok+"make_production_directories/")
#     message_local=req.json()
#     return Response({"message local": message_local})
    
# @api_view(['POST'])
# def createdir(request):
#     if request.method=="POST":
#         req=requests.post(f'{path_ngrok}make_production_directories/{request.data.get("a")}',json={"a":request.data.get('a')})
      
#         # message_local=req.json()
#         # return Response({"message local": message_local})
#         return Response({"message":f'{path_ngrok}make_production_directories/{request.data.get("a")}'})
    

@api_view(['POST'])
def createdir(request):
    if request.method == "POST":
        req = requests.post(f'{path_ngrok}make_production_directories/{request.data.get("a")}', json={"a": request.data.get('a')})

        # Vérification si la réponse est en JSON
        try:
            message_local = req.json()  # Tente de décoder le JSON
        except requests.JSONDecodeError:
            # Si ce n'est pas un JSON valide, renvoie la réponse brute
            message_local = req.text

        return Response({"message local": message_local})
    
@api_view(['GET'])
def vpath(request,id):
    path=Path.objects.get(id=id)
    seri=PathSerializer(path)
    return Response(seri.data["path"])

@api_view(['POST'])
def createProd(request):
    
    path_ngrok=Path.objects.get(id=1)
    
    
    serializer=ProdSerializer(data=request.data)
    
    
    if serializer.is_valid():
        serializer.save()
        
    pathProduction=serializer.validated_data.get("name")
    
    if request.method == "POST":
                req = requests.post(f'{path_ngrok}make_production_directories/{pathProduction}', json={"a": pathProduction})

                try:
                        message_local = req.json()  # Tente de décoder le JSON
                except requests.JSONDecodeError:
                        # Si ce n'est pas un JSON valide, renvoie la réponse brute
                        message_local = req.text
            
    
    return Response (serializer.data)


@api_view(['GET'])
def call_listes(request, nameprod, nametask, nametasktype):
    path_ngrok=Path.objects.get(id=1)
    
    req=requests.get(f'{path_ngrok}listes/{nameprod}/{nametask}/{nametasktype}')
    if req.status_code == 200:
        return Response (req.json(),status=200)
    else:
        return Response ({"error":"no scenes found"})
    
    
@api_view(['GET'])
def image_production(request, idprod):
        path_ngrok=Path.objects.get(id=1)
        mediaPath="http://localhost:8080/media/"
        try:
            production = PRODUCTION.objects.get(id=idprod)
            serializer=ProdSerializer(production)
            nameprod=serializer.data["name"]
            request=requests.get(f'{path_ngrok}vignette/{nameprod}')
            p=request.json()
            path_image=mediaPath+nameprod+"/presentation/"+p["vignette"]
            return JsonResponse({"vignette":path_image},status=200)
        except Exception as e:
            return JsonResponse({"err":str(e)},status=500)
  
     
        
        
        
        # req=requests.get(f'{path_ngrok}vignette/{np}')





def change_path(local_path):
    base_local_path = "C:\\cordage_service\\crdage_local\\media"
    base_url = "http://localhost:8080/media"
    # Remplacer la partie du chemin local par l'URL de base
    url_path = local_path.replace(base_local_path, base_url)
    # Remplacer les backslashes par des slashes pour l'URL
    url_path = url_path.replace('\\', '/')
    return url_path


@api_view(['GET'])
def call_listei(request, nameprod, nametask, nametasktype):
    
    path_ngrok=Path.objects.get(id=1)

    
    try:
    
        req=requests.get(f'{path_ngrok}listei/{nameprod}/{nametask}/{nametasktype}')
        if req.status_code == 200:
            
            images_paths=req.json()
            converted_paths=[change_path(path) for path in images_paths]
            
            
            
            return Response (converted_paths,status=200)
        else:
            return Response ({"error":"no images found"},status=req.status_code)
        
    
        
    except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=500)



@api_view(['POST'])
def launch_scene(request):
    
    path_ngrok=Path.objects.get(id=1)

    # Extraire le chemin du fichier .blend des données POST reçues
    blend_file_path = request.data.get('blend_file_path')

    if not blend_file_path:
        return Response({"error": "blend_file_path is required"}, status=400)

    try:
        # Envoyer la requête POST à l'API 'lancer_scene' avec le chemin du fichier
        response = requests.post(f'{path_ngrok}lancer_scene', json={"blend_file_path": blend_file_path})
        
        # Vérifier si la requête a réussi
        if response.status_code == 200:
            return Response({"ouverture scene": "success"}, status=200)
        else:
            # Gérer le cas où la requête à l'API échoue
            return Response({"ouverture scene": "failed", "details": response.text}, status=response.status_code)
    
    except requests.exceptions.RequestException as e:
        # Gérer les exceptions liées à la requête HTTP
        return Response({"error": str(e)}, status=500)




####new createtask
@api_view(['POST'])
def createTask(request):
    
    
    path_ngrok=Path.objects.get(id=1)

    serializer = TaskSerializer2(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
  
        idDeProd=serializer.data["PRODUCTIONId"]
        print("idDeProd=", idDeProd, "type:", type(idDeProd))  # Ajouter ce type de log pour déboguer
        
        # Récupérer objet PRODUCTION
        production = PRODUCTION.objects.get(id=idDeProd)
        print("production=", production, "type:", type(production))
        
        # Sérialiser objet PRODUCTION
        serializerP = ProdSerializer(production, many=False)
        nameOfProduction = serializerP.data["name"]
        
        nametask = serializer.validated_data.get("name")
        nametaskType = serializer.validated_data.get("type")
        nameCgArtist = serializer.validated_data.get("cgArtist3Id")
        
        if request.method == "POST":
            requests.post(
                f'{path_ngrok}make_task_directories/{nameOfProduction}/{nametask}/{nametaskType}/{nameCgArtist}', 
                json={"a": [nameOfProduction, nametask]}
            )
        
        return Response(serializer.data)
    
    return Response(serializer.errors, status=400)






@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def prod(request):
    productions=PRODUCTION.objects.all()
    serializer=ProdSerializer(productions,many=True)
    
    return Response (serializer.data)




@api_view(['GET'])
def gettasks2(request):
    tasks2=Task2.objects.all()
    serializer=TaskSerializer2_noId(tasks2,many=True)
    
    return Response (serializer.data)


@api_view(['GET'])
def gettask2Id(request,task_id):
    task2=Task2.objects.get(id=task_id)
    serializer=TaskSerializer2_noId(task2,many=False)
    
    return Response (serializer.data)



@api_view(['GET'])
def prodId(request,prod_id):
   production =PRODUCTION.objects.get(id=prod_id)
   serializer=ProdSerializer(production,many=False)
   
   return Response (serializer.data)

@api_view(['GET'])
def get_producer(request):
    producer=Producer2.objects.all()
    serializer=Producer2Serializer(producer,many=True)
    
    return Response (serializer.data)
        
@api_view(['GET'])
def get_artists(request):
    artists=CgArtist3.objects.all()
    serializer=CgArtist2Serializer(artists,many=True)
    
    return Response (serializer.data)


@api_view(['GET'])
def get_supervisors(request):
    supervisors=Supervisor2.objects.all()
    serializer=Supervisor2Serializer(supervisors,many=True)
    
    return Response (serializer.data)
        

@api_view(['PUT'])
def updateId(request,prod_id):
   production =PRODUCTION.objects.get(id=prod_id)
   serializer=ProdSerializer(production,data=request.data)
   if serializer.is_valid():
       serializer.save()
       return Response (serializer.data)
   
   return Response(serializer.errors, status=400)



@api_view(['PUT'])
def updateTask2(request,task2_id):
   task2 =Task2.objects.get(id=task2_id)
   serializer=TaskSerializer2_noId(task2,data=request.data)
   if serializer.is_valid():
       serializer.save()
       return Response (serializer.data)
   
   return Response(serializer.errors, status=400)



@api_view(['PUT'])
def updatetask2Version(request, id):
    try:
        mon_objet = Task2.objects.get(id=id)
        mon_objet.versions = F('versions') + 1
        mon_objet.save()
        return Response({"message": "La valeur de 'versions' a été incrémentée."})
    except Task2.DoesNotExist:
        return Response({"error": "L'objet n'existe pas."}, status=404)




@api_view(['DELETE'])
def delId(request,prod_id):
    
   production =PRODUCTION.objects.get(id=prod_id)
   
   production.delete() 
   return HttpResponse ("production deleted successfully")






@api_view(['DELETE'])
def delTaskId(request,prod_id):
    
   task2 =Task2.objects.get(id=prod_id)
   
   task2.delete() 
   
   return Response ({"message": "Task deleted successfully"}, status=status.HTTP_200_OK)





@api_view(['GET'])
def get_PRODUCTION_id(request, task_id):
    task = get_object_or_404(Task2, pk=task_id)
    production_id = task.PRODUCTIONId.id if task.PRODUCTIONId else None
    return Response({'production_id': production_id})






@api_view(['GET'])
def get_task2_ids_by_production(request, production_id):
    production = get_object_or_404(PRODUCTION, pk=production_id)
    
    tasks2 = production.production_tasks2.all()  # production_tasks2 est le related_name défini dans la classe Task2
    
    serializer = TaskSerializer2_noId(tasks2, many=True)
    
    return Response(serializer.data)






@api_view(['POST'])
def createUser(request):
           type=request.data.get("type")
           role=request.data.get("role")
           name=request.data.get("name")
           email=request.data.get("email")
           password=request.data.get("password")
           
           
           if type == "producer":
               user = User.objects.create_user(username=name, email=email, password=password)
               profile = UserProfile.objects.create(user=user, type=type)
               producer = Producer2.objects.create(user=user,name=name)
            
           if type == "supervisor":
               user = User.objects.create_user(username=name, email=email, password=password)
               profile = UserProfile.objects.create(user=user, type=type)
               supervisor = Supervisor2.objects.create(user=user,name=name)
               
            
           if type == "cgartist":
               user = User.objects.create_user(username=name, email=email,password=password)
               profile = UserProfile.objects.create(user=user, type=type)
               cgartist = CgArtist3.objects.create(user=user,name=name,role=role)
               
           
           
           return JsonResponse({'message': 'User created successfully'}, status=201)
       
       
#####authorization########

from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView2(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import AllowAny
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        data['user'] = self.user

        return data

class CustomTokenObtainPairView3(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response({"detail": "Invalid credentials"}, )
        
        user = serializer.validated_data.get('user', None)
        if user is None:
            return Response({"detail": "Unable to retrieve user"}, )

        token = serializer.validated_data['access']

        # Récupérer le type d'utilisateur
        try:
            profile = UserProfile.objects.get(user=user)
            user_type = profile.type
            user_organization=profile.organization
        except UserProfile.DoesNotExist:
            return Response({"detail": "User profile not found"},)

        user_serializer = UserSerializer(user)  #  sérialiser l'utilisateur
        user_data = user_serializer.data
        return Response({
            'access': token,
            'refresh': serializer.validated_data['refresh'],
            'user_type': user_type,  # Inclure  type d'utilisateur dans la réponse
            'user_organization': user_organization,  # Inclure  organization dans la réponse
            
            'user': user_data
        })



@api_view(['PUT'])
def pathAdd(request,id):
        oldpath=Path.objects.get(id=id)
        serializer=PathSerializer(oldpath,data=request.data)
        print(request.data["path"])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        
        
