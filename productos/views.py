from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Producto
from .serializers import ProductoSerializer


class ProductoListCreateView(APIView):

    def get(self, request):
        productos = Producto.objects.filter(
            activo=True
        ).order_by('id')

        serializer = ProductoSerializer(
            productos,
            many=True
        )

        return Response(serializer.data)


    def post(self, request):
        serializer = ProductoSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ProductoDetailView(APIView):

    def get(self, request, pk):
        producto = get_object_or_404(
            Producto,
            pk=pk
        )

        serializer = ProductoSerializer(producto)

        return Response(serializer.data)


    def put(self, request, pk):
        producto = get_object_or_404(
            Producto,
            pk=pk
        )

        serializer = ProductoSerializer(
            producto,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    def delete(self, request, pk):
        producto = get_object_or_404(
            Producto,
            pk=pk
        )

        producto.activo = False
        producto.save()

        return Response(
            {
                'mensaje': 'Producto eliminado correctamente.'
            },
            status=status.HTTP_200_OK
        )