from hospital.models import Slider, Service, Item, Doctor, Expertize, Faq, Gallery
from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
import tempfile

class TestViews(TestCase):
    def setUp(self):
        self.slider1 = Slider.objects.create(
            caption = 'Venha para o melhor hospital',
            slogan = 'Aqui voce sera curado',
            image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        )
        
        self.slider1.save()

        self.service1 = Service.objects.create(
            title = 'Cirurgia',
            description = 'Fazemos cirurgia de qualquer tipo',
            thumbnail = tempfile.NamedTemporaryFile(suffix=".jpg").name,
            cover = tempfile.NamedTemporaryFile(suffix=".jpg").name,
            image1 = tempfile.NamedTemporaryFile(suffix=".jpg").name,
            image2 = tempfile.NamedTemporaryFile(suffix=".jpg").name
        )

        self.service1.save()

        self.item1 = Item.objects.create(
            title = 'Item de cirurgia'
        )

        self.item1.save()
        
        self.item2 = Item.objects.create(
            title = 'Item de plantao'
        )

        self.item2.save()

        self.item3 = Item.objects.create(
            title = 'Item de tirar sangue'
        )

        self.item3.save()

        # Adding items to a service
        self.service1.items.add(self.item1)
        self.service1.items.add(self.item2)
        self.service1.items.add(self.item3)

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

        self.expertize1 = Expertize.objects.create(
            name = 'testing'
        )

        self.expertize1.save()

        self.expertize2 = Expertize.objects.create(
            name = 'testing another expertize'
        )

        self.expertize2.save()

        # Adding expertizes to a doctor
        self.doctor1.expertize.add(self.expertize1)
        self.doctor1.expertize.add(self.expertize2)

        self.faq1 = Faq.objects.create(
            question = 'O servico e bom?',
            answer = 'Sim'
        )

        self.faq1.save()

        self.gallery1 = Gallery.objects.create(
            title = 'Medicos do hospital',
            image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        )

        self.gallery1.save()

        self.client = Client()

        self.home_url = reverse('index')
        self.service_list_url = reverse('services')
        self.service_detail_url = reverse('service_details', args=['1'])
        self.doctor_list_url = reverse('doctors')
        self.doctor_detail_url = reverse('doctor_details', args=['1'])
        self.faq_list_url = reverse('faqs')
        self.gallery_list_url = reverse('gallery')
        self.contact_url = reverse('contact')



    def test_home_list_view(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hospital/index.html')
        self.assertQuerysetEqual(response.context['services'], map(repr, Service.objects.all()))


    def test_home_get_context_data(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertQuerysetEqual(response.context['sliders'], map(repr, Slider.objects.all()))
        self.assertQuerysetEqual(response.context['experts'], map(repr, Doctor.objects.all()))  


    def test_service_list_view(self):
        response = self.client.get(self.service_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hospital/services.html')
        self.assertQuerysetEqual(response.context['services'], map(repr, Service.objects.all()))


    def test_service_detail_view(self):
        response = self.client.get(self.service_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hospital/service_details.html')


    def test_service_get_context_data(self):
        response = self.client.get(self.service_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hospital/service_details.html')
        self.assertEquals(response.context['services'].filter(id=1).first(), self.service1)            


    def test_doctor_list_view(self):
        response = self.client.get(self.doctor_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hospital/team.html')
        self.assertQuerysetEqual(response.context['object_list'], map(repr, Doctor.objects.all()))


    def test_doctor_detail_view(self):
        response = self.client.get(self.doctor_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hospital/team-details.html')

    
    def test_doctor_get_context_data(self):
        response = self.client.get(self.doctor_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hospital/team-details.html')
        self.assertEquals(response.context['doctors'].filter(id=1).first(), self.doctor1)            


    def test_faq_list_view(self):
        response = self.client.get(self.faq_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hospital/faqs.html')
        self.assertQuerysetEqual(response.context['object_list'], map(repr, Faq.objects.all()))


    def test_gallery_list_view(self):
        response = self.client.get(self.gallery_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hospital/gallery.html')
        self.assertQuerysetEqual(response.context['object_list'], map(repr, Gallery.objects.all()))

    
    def test_contact_view(self):
        response = self.client.get(self.contact_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hospital/contact.html')

    
    def test_contact_post_successful(self):
        response = self.client.post(self.contact_url, {
            'name': 'Lucas',
            'email': 'lucas@gmail.com',
            'phone': '82999913265',
            'subject': 'Falta de consulta',
            'message': 'Quero uma consulta logo'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, 'Falta de consulta'+'-'+'82999913265')

    def test_contact_post_missing_data(self):
        response = self.client.post(self.contact_url, {
            'name': 'Lucas',
            'phone': '82999913265',
            'subject': 'Falta de consulta',
            'message': 'Quero uma consulta logo'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(len(mail.outbox), 0)