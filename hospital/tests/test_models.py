import datetime
import tempfile
from django.test import TestCase
from hospital.models import Slider, Service, Item, Doctor, Expertize, Faq, Gallery



class TestModels(TestCase):
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

    
    def test_slider_str(self):
        self.assertEquals(self.slider1.__str__(), 'Venha para o melhor ')

    def test_slider_meta_class(self):
        verbose_name_plural = self.slider1._meta.verbose_name_plural
        self.assertEquals(verbose_name_plural, 'Slider')

    def test_service_str(self):
        self.assertEquals(self.service1.__str__(), 'Cirurgia')

    def test_service_items(self):
        self.assertEquals(self.service1.items.count(), 3)


    def test_items_str(self):
        self.assertEquals(self.item1.__str__(), 'Item de cirurgia')
        self.assertEquals(self.item2.__str__(), 'Item de plantao')
        self.assertEquals(self.item3.__str__(), 'Item de tirar sangue')


    def test_doctor_str(self):
        self.assertEquals(self.doctor1.__str__(), 'Lucas')

    def test_doctor_expertizes(self):
        self.assertEquals(self.doctor1.expertize.count(), 2)

    def test_expertizes_str(self):
        self.assertEquals(self.expertize1.__str__(), 'testing')
        self.assertEquals(self.expertize2.__str__(), 'testing another expertize')
    
    def test_faq_str(self):
        self.assertEquals(self.faq1.__str__(), 'O servico e bom?')

    def test_gallery_str(self):
        self.assertEquals(self.gallery1.__str__(), 'Medicos do hospital')

    def test_gallery_meta_class(self):
        verbose_name_plural = self.gallery1._meta.verbose_name_plural
        self.assertEquals(verbose_name_plural, 'Galleries')

    