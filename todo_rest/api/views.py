from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response #para tener la capacidad de usar el metodo GET de Rest
from .serializers import TaskSerializer #para importar el elemento que hemos serializado

from .models import Task
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	#Lista de cosas que podemos hacer con API
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	task = Task.objects.all()
	serializer = TaskSerializer(task, many=True)#paso el objeto al serializer
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)#pk = primary key lo que le queramos pasar
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])#este view solo permite el post method
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():#si es valido envia esa info a la base de datos
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')



