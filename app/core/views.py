from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Advert
from .serializers import AdvertSerializer


class ListAdverts(ListAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer

class RetrieveAdvert(RetrieveAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer

    def retrieve(self, request, pk):
        advert = get_object_or_404(Advert, pk=pk)
        advert.views += 1
        advert.save()
        serializer = self.get_serializer(advert)
        return Response(serializer.data)
