from rest_framework import serializers
from .models import Task #Este es el modelo que queremos serializar

class TaskSerializer(serializers.ModelSerializer):#usas el nombre que vas a serializar
	class Meta:
		model = Task
		fields ='__all__'#Para mostrar todas las fields