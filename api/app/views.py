from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer
from rest_framework.generics import get_object_or_404

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'name'  # Set the default lookup field to 'name'

    def get_object(self):
        lookup_value = self.kwargs.get(self.lookup_field)
        queryset = self.filter_queryset(self.get_queryset())

        # Allow both 'id' and 'name' lookups
        if lookup_value.isdigit():  # Check if the lookup value is numeric (ID)
            return get_object_or_404(queryset, id=lookup_value)
        else:  # Assume 'name' lookup
            return get_object_or_404(queryset, name=lookup_value)
