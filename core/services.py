import random
import string

from django.utils import timezone


class UserService:
    """Service class for user"""
    @classmethod
    def check_token(cls, user_verify_token, token_for_check):
        """Method for check user verify token"""
        if user_verify_token:
            diff_days = timezone.now() - user_verify_token.created_at

            return (user_verify_token.token == token_for_check and
                    diff_days.seconds <= 24 * 60 * 60)

    @classmethod
    def create_random_password(cls):
        """Method for create random initial password"""
        return ''.join(
            random.choice(string.ascii_uppercase + string.digits)
            for _ in range(10)
        )
