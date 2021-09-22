from appointment.models import Appointment
from hospital.models import Doctor, Expertize
from django.test import TestCase, Client
from django.urls import reverse
from appointment.models import Appointment
import datetime
import tempfile

class TestViews(TestCase):
    def setUp(self):
        self.expertize1 = Expertize.objects.create(
            name = 'testing'
        )

        self.expertize1.save()

        self.doctor1 = Doctor.objects.create(
            name = 'Lucas',
            speciality = 'Otorrinolaringologista',
            picture = tempfile.NamedTemporaryFile(suffix=".jpg").name,
            details = 'Trabalha com partes especificas do corpo',
            experience = 'Tem experiencia em mais de 30 hospitais e 3 paises',
            twitter = '@lucasthedoctor',
            facebook = 'lucasthedoctor',
            instagram = 'lucasthedoctor'
        )

        self.doctor1.save()
        self.doctor1.expertize.add(self.expertize1)

        self.client = Client()
        self.appointment_url = reverse('appointment')


    def test_appointment_view_get(self):
        response = self.client.get(self.appointment_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'appointment/index.html')
        self.assertQuerysetEqual(response.context['doctors'], map(repr, Doctor.objects.all()))

    def test_Appointment_view_post_successful(self):
        response = self.client.post(self.appointment_url, {
            'name': 'Jonathan',
            'phone': '82999913265',
            'email': 'jonatan@gmail.com',
            'doctor': self.doctor1.id,
            'date': datetime.date(2001, 11, 20),
            'time':  'morning',
            'note': 'Qualquer anotacao'
        })
        appointment =  Appointment.objects.get(name='Jonathan')

        self.assertEquals(response.status_code, 302)
        self.assertEquals(appointment.phone, '82999913265')

    def test_appointment_view_post_no_doctor(self):
        response = self.client.post(self.appointment_url, {
            'name': 'Jonathan',
            'phone': '82999913265',
            'email': 'jonatan@gmail.com',
            'doctor': 90,
            'date': datetime.date(2001, 11, 20),
            'time':  'morning',
            'note': 'Qualquer anotacao'
        })

        self.assertEquals(response.status_code, 404)

    def test_appointment_view_post_missing_data(self):
        response = self.client.post(self.appointment_url, {
            'name': 'Jonathan',
            'email': 'jonatan@gmail.com',
            'doctor': self.doctor1.id,
            'date': datetime.date(2001, 11, 20),
            'time':  'morning',
            'note': 'Qualquer anotacao'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Appointment.objects.filter(id=1).first(), None)