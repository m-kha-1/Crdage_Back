from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from rest_framework.response import Response
from rest_framework.decorators import api_view
from requests.exceptions import RequestException

import requests
import subprocess


from django.http import HttpResponse

def hello_view(request):
    return HttpResponse("Hello")



import os
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from requests.exceptions import RequestException

@api_view(['GET'])
def liste_fichiers(request, np, tt,nt):
    def versions_list_images(url, depth=0, max_depth=3):
        try:
            response = requests.get(url)
            response.raise_for_status()
            
            if response.status_code == 200:
                content = response.text
                soup = BeautifulSoup(content, "html.parser")
                paths = soup.find_all("a")
                PATHS = []

                for p in paths:
                    path = urljoin(url, p.get("href"))
                    PATHS.append(path)

                if depth < max_depth:
                    for path in PATHS[:]:  # Utilisation de [:] pour éviter les modifications en cours d'itération
                        sub_paths = versions_list_images(path, depth + 1, max_depth)
                        PATHS.extend(sub_paths)

                return PATHS

        except RequestException as e:
            return []

    try:
        url = f'http://localhost:8080/{np}/{tt}/{nt}/PUBLISH/'
        PATHS = versions_list_images(url)
        
        # Filtrer les chemins pour ne conserver que ceux se terminant par '.png'
        PATHS = [path for path in PATHS if path.endswith('.png')]
        
        return Response(PATHS)
    

    except RequestException as e:
        return Response({'message': 'Erreur de connexion au serveur distant'}, status=500)
    
# @api_view(['GET'])
# def liste_fichiers(request, np):
#      try:
#         url = f'http://localhost:8080/{np}/'
#         path_img=  '.png'
#      except RequestException as e:
#          return Response ({'message': 'Erreur de connexion au serveur'},status=500)
        


@api_view(['GET'])
def image_production(request, np):
    try:
        # Construire l'URL de base
        url_base = f'http://localhost:8080/{np}/'

        # Faire une requête GET pour obtenir le contenu de la page
        response = requests.get(url_base)
        response.raise_for_status()

        # Analyser le contenu HTML de la page
        soup = BeautifulSoup(response.text, "html.parser")
        # print(soup)

        # Trouver tous les liens dans la page
        links = soup.find_all("a")

        # Initialiser une liste pour stocker les chemins des images
        image_paths = []

        # Parcourir tous les liens trouvés
        for link in links:
            href = link.get("href")
            # Vérifier si le lien pointe vers une image.jpg
            if href and href.endswith('.jpg') or href and href.endswith('.png'):
                # Construire le chemin complet de l'image
                full_path = urljoin(url_base, href)
                # Ajouter le chemin de l'image à la liste
                image_paths.append(full_path)

        # Renvoyer les chemins des images en utilisant Response
        return Response(image_paths, status=200)

    except requests.RequestException as e:
        # Gérer les exceptions de requête
        return Response({'message': 'Erreur de connexion au serveur distant'}, status=500)
    
    
    
    
    
    
    
    
    
# @api_view(['GET'])
# def liste_scenes(request, np, tt,nt):
#     def versions_list_images(url, depth=0, max_depth=3):
#         try:
#             response = requests.get(url)
#             response.raise_for_status()
            
#             if response.status_code == 200:
#                 content = response.text
#                 soup = BeautifulSoup(content, "html.parser")
#                 paths = soup.find_all("a")
#                 PATHS = []

#                 for p in paths:
#                     path = urljoin(url, p.get("href"))
#                     PATHS.append(path)

#                 if depth < max_depth:
#                     for path in PATHS[:]:  # Utilisation de [:] pour éviter les modifications en cours d'itération
#                         sub_paths = versions_list_images(path, depth + 1, max_depth)
#                         PATHS.extend(sub_paths)

#                 return PATHS

#         except RequestException as e:
#             return []

#     try:
#         url = f'http://localhost:8080/{np}/{tt}/{nt}/PUBLISH/'
#         PATHS = versions_list_images(url)
        
#         # Filtrer les chemins pour ne conserver que ceux se terminant par '.png'
#         PATHS = [path for path in PATHS if path.endswith('.blend')]
        
#         return Response(PATHS)

#     except RequestException as e:
#         return Response({'message': 'Erreur de connexion au serveur distant'}, status=500)
    
    
    
    
    import os
from django.http import JsonResponse
from rest_framework.decorators import api_view

from django.http import FileResponse




###white noise####
from urllib.parse import quote

@api_view(['GET'])
def liste_images(request, organization, np, tt, nt):
    try:
        stockage = Stockage.objects.get(name=organization)
        media_root = stockage.media_root
        filepath = os.path.join(media_root, np, tt, nt, 'PUBLISH')

        # Récupérer tous les fichiers dans le dossier spécifié
        filenames = [f.name for f in os.scandir(filepath) if f.is_file()]

        # Retourner la liste des noms de fichiers
        return JsonResponse(filenames, safe=False)
    except Stockage.DoesNotExist:
        return JsonResponse({"error": f"No storage found for organization {organization}"}, status=404)















@api_view(['GET'])
def liste_images(request,organization, np, tt, nt):
   
    stockage=Stockage.objects.get(name=organization)
    print ("stockage:",stockage.media_root)
    base_dir = os.path.join(stockage.media_root, np, tt, nt, 'PUBLISH')
    # base_url = request.build_absolute_uri('/serve_file/')
    
    try :
        if not os.path.exists(base_dir):
            return JsonResponse({'message': str(base_dir)+'Directory does not exist'},status=404)
        
        all_files = [os.path.join(root, file)
                    for root, dirs, files in os.walk(base_dir)
                    for file in files
                    if file.endswith('.png')]
        
        # image_urls = [f"{base_url}{organization}/{np}/{tt}/{nt}/{file}"
        #               for file in all_files]
        
        

        
        # return Response(all_files, status=200)
        return Response(all_files, status=200)
        
        
        

    except Exception as e:
        return JsonResponse({'message':str(e)},status=500)




from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import os

# @api_view(['GET'])
# def liste_images(request, organization, np, tt, nt):
#     stockage = Stockage.objects.get(name=organization)
#     base_dir = os.path.join(stockage.media_root, np, tt, nt, 'PUBLISH')

#     # Construire l'URL de base pour les fichiers
#     base_url = request.build_absolute_uri('/serve_file/')

#     try:
#         if not os.path.exists(base_dir):
#             return JsonResponse({'message': f'{base_dir} Directory does not exist'}, status=404)

#         # Créer les chemins relatifs
#         all_files = [os.path.relpath(os.path.join(root, file), base_dir)
#                      for root, dirs, files in os.walk(base_dir)
#                      for file in files
#                      if file.endswith('.png')]

#         # Créer les URLs complètes pour les images avec correction des barres obliques
#         image_urls = [f"{base_url}{organization}/{np}/{tt}/{nt}/{file.replace(os.sep, '/')}"
#                       for file in all_files]

#         return Response(image_urls, status=200)
#     except Exception as e:
#         return JsonResponse({'message': str(e)}, status=500)

    
    
        






## sans http server
@api_view(['GET'])
def liste_scenes2(request,organization, np, tt, nt):
    
    # organization="dev"
    stockage=Stockage.objects.get(name=organization)
    

    base_dir = os.path.join(stockage.media_root, np, tt, nt, 'PUBLISH')
    print("chemin:",base_dir)
    try:
        # Vérifier si le répertoire existe
        if not os.path.exists(base_dir):
            return JsonResponse({'message': 'Directory does not exist'}, status=404)

        # Lister tous les fichiers .blend dans le répertoire
        
        # numbers = [1, 2, 3, 4, 5]
        # doubled_numbers = [number * 2 for number in numbers]
        
        
        all_files = [os.path.join(root, file)
                     for root, dirs, files in os.walk(base_dir)
                     for file in files
                     if file.endswith('.blend')]

        return JsonResponse(all_files, safe=False)

    except Exception as e:
        return JsonResponse({'message': str(e)}, status=500)
    
    
    
    
   



@api_view(['POST'])
def lancer_scene(request):
    # Extraire le chemin du fichier .blend des données POST
    blend_file_path = request.data.get('blend_file_path')

    # Vérifier si le chemin du fichier est fourni et valide
    if not blend_file_path or not os.path.exists(blend_file_path):
        return JsonResponse({'message': 'Invalid or non-existent file path'}, status=400)

    # Chemin vers l'exécutable Blender
    blender_path = r"C:\Program Files\Blender Foundation\Blender 4.2\blender.exe"
    
    try:
        # Lancer Blender avec le fichier .blend
        subprocess.Popen([blender_path, blend_file_path])
        return JsonResponse({'message': 'Scene launched successfully'}, status=200)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=500)
    
from .serializers import StockageSerializer
from .models import Stockage
# @api_view(['GET'])
# def get_stockage(request,name):
#     stockage=Stockage.get(name=name)
#     serialiser=StockageSerializer(stockage)
    
#     return JsonResponse(serialiser.data)
    
    
    
from rest_framework import status
@api_view(['GET'])
def get_stockage(request,name_name):
    try:
        # Utiliser `.get()` sur le manager du modèle
        stockage = Stockage.objects.get(name=name_name)
        # Sérialiser l'instance de modèle
        serializer = StockageSerializer(stockage)
        # Retourner la réponse JSON
        return Response(serializer.data)
    except Stockage.DoesNotExist:
        # Gérer le cas où l'instance n'existe pas
        return Response({'message': 'Stockage not found'}, status=status.HTTP_404_NOT_FOUND)
    
    
    
    
# Importer les modules nécessaires
import os
from django.http import HttpResponse, Http404
from django.views import View

@api_view(['GET'])
def get_image_url(request):
    # Chemin du fichier
    file_path = r'C:\CORD\ProductionC3\lighting\LIGHTING\PUBLISH\images\V01\PA1_light_v01.png'
    
    # Vérifier si le fichier existe
    if not os.path.exists(file_path):
        return Response({"error": "File does not exist"}, status=status.HTTP_404_NOT_FOUND)

    # Convertir le chemin local en URL
    relative_path = file_path.replace(r'C:\CORD', '').replace('\\', '/')
    image_url = f"http://{request.get_host()}/media{relative_path}"
    
    return Response({"image_url": image_url}, status=status.HTTP_200_OK)






