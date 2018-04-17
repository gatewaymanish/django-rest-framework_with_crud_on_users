from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import User
from rest_framework import generics
from .serializers import UserSerializer




# ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


#
# def home(request):
#     query = request.GET.get("q")
#     if query:
#         result = User.objects.all().filter(
#             Q(username__icontains=query) |
#             Q(first_name__icontains=query) |
#             Q(last_name__icontains=query)
#         )
#         searchResult = {'result': result}
#         return render(request, 'searchresult.html', searchResult)
#     else:
#         queryset = User.objects.all()
#         context = {'usr':queryset}
#         return render(request, 'index.html', context)
#
#



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('users:user-list', request=request, format=format),
    })




class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all().filter(username=self.request.user)