from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from squandered.account.models import Profile

UserModel = get_user_model()


class ProfileTests(TestCase):
    VALID_USER_CREDENTIALS = {
        'username': 'testuser',
        'email': 'test@test.com',
        'password': '12345qwe',
    }
    VALID_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'Testov',
    }

    @staticmethod
    def __create_user(**credentials):
        return UserModel.objects.create_user(**credentials)

    def __create_valid_user_and_profile(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )
        return user, profile

    def test_when_opening_non_existing_profile__expect_404(self):
        response = self.client.get(
            reverse('profile details', kwargs={'pk': 1})
        )
        self.assertEqual(404, response.status_code)

    def test_expect_correct_template(self):
        _, profile = self.__create_valid_user_and_profile()
        self.client.get(
            reverse('profile details', kwargs={'pk': 1})
        )
        self.assertTemplateUsed('account/profile_details.html')
