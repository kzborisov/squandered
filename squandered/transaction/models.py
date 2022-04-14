from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import localtime

from squandered.account.models import Profile, CustomUser

UserModel = get_user_model()


class ExpenseCategory(models.Model):
    NAME_MAX_LENGTH = 256
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Expense Categories'
        ordering = ('-created_at',)


class IncomeCategory(models.Model):
    NAME_MAX_LENGTH = 256
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Income Categories'
        ordering = ('-created_at',)


class Expense(models.Model):
    NAME_MAX_LENGTH = 1024
    AMOUNT_DECIMAL_PLACES = 2
    AMOUNT_MAX_DIGITS = 14

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(),  # Char only validator
    )
    amount = models.DecimalField(
        max_digits=AMOUNT_MAX_DIGITS,
        decimal_places=AMOUNT_DECIMAL_PLACES,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    date = models.DateField(
        default=localtime,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    category = models.ForeignKey(
        ExpenseCategory,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.category} {self.date} {self.amount}'

    class Meta:
        ordering = ('-date',)


class Income(models.Model):
    NAME_MAX_LENGTH = 1024
    AMOUNT_DECIMAL_PLACES = 2
    AMOUNT_MAX_DIGITS = 14

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )
    amount = models.DecimalField(
        max_digits=AMOUNT_MAX_DIGITS,
        decimal_places=AMOUNT_DECIMAL_PLACES,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    date = models.DateField(
        default=localtime,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    category = models.ForeignKey(
        IncomeCategory,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.category} {self.date} {self.amount}'

    class Meta:
        ordering = ('-date',)
