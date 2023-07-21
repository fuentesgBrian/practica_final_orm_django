from django.test import TestCase
from django.urls import reverse 
from .models import Laboratorio

# Create your tests here.
class LaboratorioTest(TestCase):
    databases = '__all__'
    @classmethod

    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(nombre='Laboratorio15', ciudad='Los Angeles', pais='Chile')

    def test_model_content(self):
        self.assertEqual(self.laboratorio.nombre, 'Laboratorio15')
        self.assertEqual(self.laboratorio.ciudad, 'Los Angeles')
        self.assertEqual(self.laboratorio.pais, 'Chile')

    def test_url_exists_at_correct_location(self):
        response = self.client.get('/mostrar/')
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse('mostrar_lab'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laboratorio/mostrar.html')
        self.assertContains(response, 'Información de Laboratorios')