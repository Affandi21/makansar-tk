from django.test import TestCase, Client
from django.utils import timezone
from .models import User

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/mogwartz/')
        self.assertEqual(response.status_code, 404)

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
            buyer=True,
            seller=False,
            nama="Test User",
            no_telp="08123456789",
            tanggal_lahir="1990-01-01"
        )

    def test_user_creation(self):
        # Memastikan pengguna dibuat dengan benar
        self.assertEqual(self.user.username, "testuser")
        self.assertTrue(self.user.buyer)
        self.assertFalse(self.user.seller)
        self.assertEqual(self.user.nama, "Test User")
        self.assertEqual(self.user.no_telp, "08123456789")
        self.assertEqual(str(self.user.tanggal_lahir), "1990-01-01")

    def test_user_str_method(self):
        # Menguji metode __str__ untuk output username
        self.assertEqual(str(self.user), "testuser")