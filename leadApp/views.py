from django.shortcuts import render
from leadApp.serializers import LeadSerializer
from leadApp.models import Lead
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView,ListAPIView
from rest_framework import authentication,permissions
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
# Create your views here.


class LeadCreateListView(CreateAPIView,ListAPIView):
    serializer_class=LeadSerializer
    queryset=Lead.objects.all()
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    filter_backends=[
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    search_fields=['name','email','status','source']
    ordering_fields=['name','added_date']

class LeadRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=LeadSerializer
    queryset=Lead.objects.all()


# class LeadCounts(APIView):
#     authentication_classes=[authentication.BasicAuthentication]
#     permission_classes=[permissions.IsAuthenticated]
#     def get(self,request,*args,**kwargs):
#         new_leads=Lead.objects.filter(status="New")
#         contacted=Lead.objects.filter(status="Contacted")
#         Converted=Lead.objects.filter(status="Converted")
#         Lost=Lead.objects.filter(status="Lost")

#         res={
#             "new_leads":new_leads,
#             "contacted leads":contacted,
#             "Converted_lead":Converted,
#             "lost_leads":Lost
#         }
#         return Response(res)
    
