import datetime
import tempfile
from django.test import TestCase
from appointment.models import Appointment
from hospital.models import Doctor, Expertize



class TestModels(TestCase):
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
        
        self.appointment1 = Appointment.objects.create(
            name = 'Jonathan',
            phone = '82999913265',
            email = 'jonatan@gmail.com',
            doctor = self.doctor1,
            date = datetime.date(2001, 11, 20),
            time =  'morning',
            note = 'Qualquer anotacao'
        )

        self.appointment1.save()
    
    def test_appointment_str(self):
        self.assertEquals(self.appointment1.__str__(), 'Jonathan-Lucas')