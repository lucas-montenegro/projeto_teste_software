from django.test import SimpleTestCase
from django.urls import reverse, resolve
from hospital.views import HomeView, ServiceListView, ServiceDetailView, DoctorListView, DoctorDetailView, FaqListView, GalleryListView, ContactView

class TestUrls(SimpleTestCase):

    def test_index_url(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func.view_class, HomeView)

    def test_services_url(self):
        url = reverse('services')
        self.assertEquals(resolve(url).func.view_class, ServiceListView)

    def test_service_details_url(self):
        url = reverse('service_details', args=['1']) # any integer number in args
        self.assertEquals(resolve(url).func.view_class, ServiceDetailView)

    def test_doctors_url(self):
        url = reverse('doctors')
        self.assertEquals(resolve(url).func.view_class, DoctorListView)

    def test_doctor_details_url(self):
        url = reverse('doctor_details', args=['2012']) # any integer number in args
        self.assertEquals(resolve(url).func.view_class, DoctorDetailView)

    def test_faqs_url(self):
        url = reverse('faqs')
        self.assertEquals(resolve(url).func.view_class, FaqListView)

    def test_gallery_url(self):
        url = reverse('gallery')
        self.assertEquals(resolve(url).func.view_class, GalleryListView)

    def test_contact_url(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func.view_class, ContactView)