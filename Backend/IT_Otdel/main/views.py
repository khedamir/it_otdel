from django.shortcuts import render
from .models import Aplications, Cabinets, Frame
from rest_framework import generics
from .serializers import AplicationsSerializer#, CabinetsSerializer, FrameSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class AplicationsAPIView(APIView):
    def get(self, request):
        aplications = Aplications.objects.all()
        serializer_class = AplicationsSerializer(aplications, many = True)
        return Response({'aplications' : serializer_class.data}) 
    
    def post(self, request):
        serializer = AplicationsSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        # serializer.save()

        return Response({'post': serializer.data})

# class CabinetsAPIViev(APIView):
#     def get(self, request):
#         cabinets = Cabinets.objects.all()
#         serializer_class = CabinetsSerializer(cabinets, many = True)
#         return Response({'cabinets' : serializer_class.data})
        
#         def post(self, request):
#             serializer = CabinetsSerializer(data=request.data)
#             serializer.is_valid(raise_exception = True)
#             serializer.save()

#         return Response({'post': serializer.data})

# class FrameAPIViev(generics.ListAPIView):
#     def get(self, request):
#         frame = Frame.objects.all()
#         serializer_class = FrameSerializer(frame, many= True)
#         return Response({'frame' : serializer_class.data})