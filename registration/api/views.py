
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import generics
from  registration.models import ProfileModel
from .serializers import ProfileModelSerializer
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

import jwt




class ProfileModelListAPIView(generics.ListAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username','first_name','last_name','bio']

    


class ProfileDetailAPIView(generics.RetrieveAPIView):
    queryset=ProfileModel.objects.all()
    serializer_class=ProfileModelSerializer
    lookup_field='username'

    permission_classes = [IsAuthenticated]
    

    def retrieve(self, request, *args, **kwargs):
        username=self.kwargs.get('username')
        profile=ProfileModel.objects.get(username=username)
        key='super-secret'
        payload={"id":str(request.user.id),}
        token= jwt.encode(payload, key)
        print(token)
        decoded = jwt.decode(token, options={"verify_signature": False}) # works in PyJWT >= v2.0
        print (decoded['id'])
        if request.user.id==profile.id:
            print("YYES!")
        return super().retrieve(request, *args, **kwargs)




class RegistrationAPIView(generics.CreateAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileModelSerializer
    lookup_field='username'
    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data["username"]=str(request.data['first_name']+request.data['last_name'])
        if request.data['password1']!=request.data['password2']:
            raise serializers.ValidationError('passwords must be the same!')
        request.data['password']=request.data['password1']
        request.data._mutable = False
        return super().create(request, *args, **kwargs)
        


class DeleteProfileAPIView(generics.DestroyAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileModelSerializer
    permission_classes = [IsAuthenticated]
    lookup_field='username'


    def delete(self, request, *args, **kwargs):
        username=self.kwargs.get('username')
        profile=ProfileModel.objects.get(username=username)

        key='super-secret'
        payload={"id":str(request.user.id),}
        token= jwt.encode(payload, key)
        
        decoded = jwt.decode(token, options={"verify_signature": False}) # works in PyJWT >= v2.0
        
        if str(decoded['id']) == str(profile.id):
            return super().delete(request, *args, **kwargs)

        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)




class UpdateProfileModelView(generics.RetrieveUpdateAPIView):
    serializer_class=ProfileModelSerializer
    queryset=ProfileModel.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field='username'


    def update(self, request, *args, **kwargs):
        username=self.kwargs.get('username')
        profile=ProfileModel.objects.get(username=username)

        key='super-secret'
        payload={"id":str(request.user.id),}
        token= jwt.encode(payload, key)
        
        decoded = jwt.decode(token, options={"verify_signature": False}) # works in PyJWT >= v2.0
        
        if str(decoded['id']) == str(profile.id):

            updated_data=request.data      
            updated_profile=ProfileModel.objects.filter(username=username).update(
                                                        first_name=updated_data['first_name'],
                                                        last_name=updated_data['last_name'],
                                                        email=updated_data['email'],
                                                        bio=updated_data['bio'],
                                                        school_number=str(updated_data['school_number']),
                                                        phone=updated_data['phone'],
                                                        departmand=updated_data['departmand'],
                                                        grade=updated_data['grade'],
                                                        fee=bool(updated_data['fee']),
                                                        register_date=updated_data['register_date'],
            
            )
            return Response(status=status.HTTP_200_OK)     
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
               

          