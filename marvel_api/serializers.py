from rest_framework import serializers 
from .models import Marvel 

class MarvelSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Marvel # tell django which model to use
        fields = ('id', 'name', 'age',) # tell django which fields to include