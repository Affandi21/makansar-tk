from django.test import TestCase
from account.models import User
from main.models import Makanan
from .models import Review

class ReviewModelTest(TestCase):
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

        self.makanan = Makanan.objects.create(
            category="Main Course",
            food_name="Test Food",
            location="Test Location",
            shop_name="Test Shop",
            price=10000.00,
            rating_default=4.0,
            new_rating=4.0,
            food_desc="Delicious test food.",
            jumlah_review=0
        )

    def test_review_creation(self):
        review = Review.objects.create(
            buyer=self.user,
            food_item=self.makanan,
            rating=5,
            comment="Bagus sekali"
        )

        # Test instance creation
        self.assertIsInstance(review, Review)
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comment, "Bagus sekali")
        self.assertEqual(review.buyer, self.user)
        self.assertEqual(review.food_item, self.makanan)

    def test_review_rating_range(self):
        review = Review.objects.create(
            buyer=self.user,
            food_item=self.makanan,
            rating=4,
            comment="Good rating test"
        )
        self.assertTrue(1 <= review.rating <= 5)
        
    def test_review_buyer_relationship(self):
        review = Review.objects.create(
            buyer=self.user,
            food_item=self.makanan,
            rating=4,
            comment="Testing buyer relationship"
        )
        self.assertEqual(review.buyer.nama, "Test User")
        self.assertTrue(review.buyer.buyer)
        self.assertFalse(review.buyer.seller)

    def test_review_food_item_relationship(self):
        review = Review.objects.create(
            buyer=self.user,
            food_item=self.makanan,
            rating=4,
            comment="Testing food relationship"
        )
        self.assertEqual(review.food_item.food_name, "Test Food")
        self.assertEqual(review.food_item.shop_name, "Test Shop")
        self.assertEqual(review.food_item.category, "Main Course")