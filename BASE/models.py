from django.db import models
from django.contrib.auth.models import User


import os

#Entité infographiste 


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    type=models.CharField(default=False)
    organization=models.CharField(max_length=100,null=True,blank=True)


    
class CgArtist3(models.Model):
    
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     types=[
        ('LIGHT','lighting'),
        ('COMP','compositing'),
        ('ANIM','animation'),
        ('MODEL','modelling'),
        ('SURFACE','surfacing'),
        ('FX','fx'),
        ('RIG','rigging')
                             ]
     name=models.CharField(max_length=50,unique=True)
    #  email=models.EmailField(unique=False)
     role=models.CharField(max_length=50,choices=types)
     USERNAME_FIELD = 'name'
    
     def __str__(self):
        return self.name


#Entité chargé de production
class Producer(models.Model):
    name=models.CharField(max_length=50,unique=True)
    email=models.EmailField(unique=True)
    USERNAME_FIELD = 'name'
  
    
    def __str__(self):
        return self.name
    
class Producer2(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    name=models.CharField(max_length=50,unique=True)
    # email=models.EmailField(unique=False)
    USERNAME_FIELD = 'name'
  
    
    def __str__(self):
        return self.name



    
class Supervisor2(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,unique=True)
    # email=models.EmailField(unique=False)
    USERNAME_FIELD = 'name'
  
    
    def __str__(self):
        return self.name

 
 #Entité Production
class PRODUCTION(models.Model):
    name=models.CharField(max_length=50)
    client=models.CharField(max_length=50, default='client-default')
    producers=models.ManyToManyField(Producer2,related_name="prods")  #related_name permettra de récupérer les productions suivies par un Producer
    USERNAME_FIELD = 'name'                                                                 #producer_instance=Producer.objects.get(pk=number)
                                                                     #productions_suivies=producer_instance.prods.all()
   
    def __str__(self):
        return self.name
    
    
    
    
    
   
 #Entité Task  
    
class Task2(models.Model):
    types=[
        ('lighting','lighting'),
        ('compositing','compositing'),
        ('animation','animation'),
        ('modelling','modelling'),
        ('surfacing','surfacing'),
        ('fx','fx'),
        ('rigging','rigging')
    ]
    name=models.CharField(max_length=50)
    type=models.CharField(max_length=50,choices=types)
    dateCreated=models.DateField(auto_now_add=True)
    dateDue=models.DateField(auto_now_add=False, null=True, blank=True)
    comments_cgArtist=models.JSONField(default=list, null=True, blank=True)
    comments_supervisor2=models.JSONField(default=list, null=True, blank=True)
    comments_producer=models.JSONField(default=list, null=True, blank=True)
    versions=models.IntegerField(default=1)
    completed=models.BooleanField(default=False)
                                #4 clés étrangères : une tâche est associée à l'ID d'un producer(chargé de prod), l'ID  d'un Superviseur, l'ID d'Un cgArtist(infographiste)
                                #et l'ID d'une PRODUCTION 
                                # Si une PRODUCTION est détruite toutes les tâches associées seront aussi détruites (en cascade) alors que si un Producer , Supervisor et CgArtist
                                #le champ de la Task associée sera laissé vide (Set Null)
                            
    # producerID=models.ForeignKey(Producer, on_delete=models.SET_NULL,blank=True,null=True,related_name="producerTasks")
    # supervisorID=models.ForeignKey(Supervisor, on_delete=models.SET_NULL,blank=True,null=True,related_name="supervisorTasks")
    # cgArtistId=models.ForeignKey(CgArtist, on_delete=models.SET_NULL,blank=True,null=True,related_name="cgArtistTasks")
    # PRODUCTIONId=models.ForeignKey(PRODUCTION, on_delete=models.CASCADE,null=True,related_name="PRODUCTIONTasks")
    
    producerID = models.ForeignKey(Producer2, on_delete=models.SET_NULL, blank=True, null=True, related_name="producer_tasks2")
    supervisor2ID = models.ForeignKey(Supervisor2, on_delete=models.SET_NULL, blank=True, null=True, related_name="supervisor2_tasks2")
    cgArtist3Id = models.ForeignKey(CgArtist3, on_delete=models.SET_NULL, blank=True, null=True, related_name="cg_artist3_tasks2")
    PRODUCTIONId = models.ForeignKey(PRODUCTION, on_delete=models.CASCADE, null=True, related_name="production_tasks2")
    

    def __str__(self):
        return self.name
       
    
    

    

    
    
    
    
    

    
    