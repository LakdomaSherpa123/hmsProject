from django.urls import path
from api.views import (DoctorList,DoctorDetails,PatientList,PatientDetails,AppointmentList,AppointmentDetails,
PatientDischargeList,PatientDischargeDetails)


urlpatterns = [
    path('api/doctor/', DoctorList.as_view(), name='doctor-list'),
    path('api/<int:id>/doctor/', DoctorDetails.as_view(), name='doctor-details'),

    path('api/patient/', PatientList.as_view(), name='patient-list'),
    path('api/<int:id>/patient/', PatientDetails.as_view(), name='patient-details'),

    path('api/appointment/', AppointmentList.as_view(), name='appointment-list'),
    path('api/<int:id>/appointment/', AppointmentDetails.as_view(), name='appointment-details'),

    path('api/patientdischarge/', PatientDischargeList.as_view(), name='patientdischarge-list'),
    path('api/<int:id>/patientdischarge/', PatientDischargeDetails.as_view(), name='patient-details')
]