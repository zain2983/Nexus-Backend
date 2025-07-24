from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def signup(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not username or not email or not password:
        return Response({'error': 'Username, email, and password are required.'}, status=400)
    
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=400)
    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email already exists'}, status=400)
    
    user = User.objects.create_user(username=username, password=password, email=email)
    return Response({'message': 'User created'}, status=201)

@api_view(['POST'])
def login(request):
    print("BACKEND - LOGIN API CALLED ")
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not email or not password:
        return Response({'error': 'Email and password are required.'}, status=400)
    
    try:
        user_obj = User.objects.get(email=email)
        user = authenticate(username=user_obj.username, password=password)
    except User.DoesNotExist:
        user = None
    
    if user is not None:
        print("BACKEND - LOGIN API CALLED - SUCCESS")
        return Response({'message': 'Login successful', 'username': user.username})
    else:
        print("BACKEND - LOGIN API CALLED - FAILURE")
        return Response({'error': 'Invalid credentials'}, status=400)
