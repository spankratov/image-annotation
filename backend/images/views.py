from images.models import Image
from images.serializers import (ImageCreateSerializer, ImageRetrieveSerializer,
                                ImageUpdateSerializer, ImageURLSerializer)
from rest_framework import generics, parsers


class ImageCreateAPIView(generics.CreateAPIView):
    serializer_class = ImageCreateSerializer
    parser_classes = [parsers.MultiPartParser]


class ImageRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageUpdateSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ImageRetrieveSerializer
        else:
            return ImageUpdateSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        query_params = self.request.query_params
        context['annotation_format'] = query_params.get('format', 'internal')
        return context


class ImageURLAPIView(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageURLSerializer
