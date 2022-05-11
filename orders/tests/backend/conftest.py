from rest_framework.test import APIClient
import pytest as pytest
from model_bakery import baker

from backend.models import User, Category, Shop, ProductInfo, Product, ProductParameter, OrderItem, Order, Contact


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def authorized_user(client):
    user = User.objects.create_user(email='lshdv@klnn.ru', password='kj#GFB76j9BRE#112', is_active=True)
    client.force_authenticate(user=user)
    return user


@pytest.fixture
def authorized_shop(client):
    shop = User.objects.create_user(email='lshdv@klnn.ru', password='kj#GFB76j9BRE#112', is_active=True, type='shop')
    client.force_authenticate(user=shop)
    return shop


@pytest.fixture
def contact_factory():
    def factory(user, *args, **kwargs):
        contact = baker.make(Contact, user=user, *args, **kwargs)
        return contact

    return factory
