from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from .models import Makanan, User, Favorite

class UserAndMakananTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            buyer=True,
            seller=False,
            nama='Test User',
            no_telp='08123456789',
            tanggal_lahir='1990-01-01'
        )

        self.makanan = Makanan.objects.create(
            category="Test Category",
            food_name="Test Food",
            location="Test Location",
            shop_name="Test Shop",
            price=10000,
            rating_default=4.5,
            food_desc="Delicious Test Food",
            image=None
        )


    def test_main_url_is_exist(self):
        """Test that the main URL returns a 200 status code."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_nonexistent_page(self):
        """Test that a nonexistent page returns a 404 status code."""
        response = self.client.get('/nonexistent/')
        self.assertEqual(response.status_code, 404)

    def test_main_using_main_template(self):
        """Test that the main URL uses the correct template."""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'main.html')  # Update this to your actual main template

    def test_favorite_creation(self):
        favorite = Favorite.objects.create(user=self.user, product=self.makanan)
        self.assertEqual(favorite.user, self.user)
        self.assertEqual(favorite.product, self.makanan)
        self.assertFalse(favorite.is_top_three)
        self.assertFalse(favorite.is_favorite)

    def test_favorite_str_method(self):
        """Test the __str__ method of Favorite."""
        favorite = Favorite.objects.create(user=self.user, product=self.makanan)
        self.assertEqual(str(favorite), f"{self.user.username} - {self.makanan.food_name}")