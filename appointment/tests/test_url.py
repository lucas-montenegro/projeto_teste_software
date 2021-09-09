from django.test import SimpleTestCase
from django.urls import reverse, resolve
from appointment.views import AppointmentView

class TestUrls(SimpleTestCase):

    def test_appointment_url(self):
        url = reverse('appointment')
        self.assertEquals(resolve(url).func.view_class, AppointmentView)