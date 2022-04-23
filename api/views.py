from django.shortcuts import render
from api.serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer, PatientDischargeSerializer
from rest_framework import mixins, generics
from hospital.models import Doctor, Patient, Appointment, PatientDischargeDetails
# Create your views here.

class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    lookup_field = 'id'


class PatientList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = 'id'

class AppointmentList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    lookup_field = 'id'

class PatientDischargeList(generics.ListCreateAPIView):
    queryset = PatientDischargeDetails.objects.all()
    serializer_class = PatientDischargeSerializer

class PatientDischargeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientDischargeDetails.objects.all()
    serializer_class = PatientDischargeSerializer
    lookup_field = 'id'