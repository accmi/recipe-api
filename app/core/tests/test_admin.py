from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from .test_models import EMAIL, PASSWORD

SUPERUSER_EMAIL = 'super@email.test'
SUPERUSER_PASSWORD = '87654321'


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email=SUPERUSER_EMAIL,
            password=SUPERUSER_PASSWORD
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email=EMAIL,
            password=PASSWORD
        )

    def test_users_listed(self):
        """Test that user are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that user edit page works"""
        # /admin/core/user/
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
