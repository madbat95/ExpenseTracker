# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from expensetracker.models import Account
# from expensetracker.serializers import AccountSerializer
# from rest_framework import generics
# Create your views here.


# # @csrf_exempt
# # def user_list(request):
# #     """this should list all users or allow to create a new user"""

# #     if request.method == 'GET':
# #         users = User.objects.all()
# #         serializer = UserSerializer(users, many=True)
# #         return JsonResponse(serializer.data, safe=False)

# #     elif request.method == 'POST':
# #         data = JSONParser().parse(request)
# #         serializer = UserSerializer(data=data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return JsonResponse(serializer.data, status=201)
# #         return JsonResponse(serializer.errors, status=400)


# # @csrf_exempt
# # def user_detail(request, pk):
# #     """retieve update or delete a user"""

# #     try:
# #         user = User.objects.get(pk=pk)
# #     except User.DoesNotExist:
# #         return HttpResponse(status=404)

# #     if request.method =='GET':
# #         serializer = UserSerializer(user)
# #         return JsonResponse(serializer.data)

# #     elif request.method == 'PUT':
# #         data = JSONParser().parse(request)
# #         serializer = UserSerializer(user, data=data)
        
# #         if serializer.is_valid():
# #             serializer.save()
# #             return JsonResponse(serializer.data)
# #         return JsonResponse(serializer.errors, status=400)

# #     elif request.method == 'DELETE':
# #         user.delete()
# #         return HttpResponse(status = 204)

# class account_list(generics.ListCreateAPIView):
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer

# class account_detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer


#     from django.contrib.auth.models import AbstractUser