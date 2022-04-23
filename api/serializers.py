from pyexpat import model
from rest_framework import serializers
from hospital.models import Doctor, Patient, Appointment, PatientDischargeDetails

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"


class PatientDischargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDischargeDetails
        fields = "__all__"