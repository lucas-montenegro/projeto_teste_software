from django.test import TestCase, Client
from django.urls import reverse
from appointment.models import Appointment
from hospital.models import Doctor
import json


class TestViews(TestCase):
    '''def setUP(self):
        self.client = Client()
        self.appointment_url = reverse('appointment')
        self.doctor = Doctor.objects.create{
            name = 'lucas',
            speciality = 'heart',
            picture = models.ImageField(upload_to="doctors/")
            details = 'sou um medico'
            experience = 'tenho experiencia'
            expertize = models.ManyToManyField(to='Expertize', related_name='doctors')
            twitter = models.CharField(max_length=120, blank=True, null=True)
            facebook = models.CharField(max_length=120, blank=True, null=True)
            instagram = models.CharField(max_
        } 


    def test_Appointment_view_get(self):
        response = self.client.get(self.appointment_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'appointment/index.html')

    def test_Appointment_view_post(self):
       


        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.appointment1)'''
