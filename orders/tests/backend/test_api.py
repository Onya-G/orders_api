import pytest as pytest

from backend.models import User, Category, Shop, ProductInfo, Product, ProductParameter, OrderItem, Order, Contact


@pytest.mark.django_db
def test_create_contact(client, authorized_user):
    contact_data = {'user': authorized_user.id, 'city': 'Msk', 'street': 'longstreet', 'phone': '23987492183'}
    response = client.post('/api/v1/user/contact/', contact_data)

    assert response.status_code == 201
    assert response.json()['street'] == contact_data['street']


@pytest.mark.django_db
def test_get_contact(client, authorized_user, contact_factory):
    contact = contact_factory(authorized_user)
    response = client.get(f'/api/v1/user/contact/{authorized_user.id}/')

    assert response.status_code == 200
    assert response.json()['street'] == contact.street


@pytest.mark.django_db
def test_create_user(client):
    count = User.objects.count()
    user_data = {'first_name': 'tname', 'last_name': 'tlname', 'email': 'testmail@mail.ru',
                 'password': 'WDBTR345hqwjksd!@', 'company': 'tcom', 'position': 'tpos'}
    response = client.post('/api/v1/user/register', user_data)

    assert User.objects.count() == count + 1
    assert response.status_code == 200


@pytest.mark.django_db
def test_partner_update(client, authorized_shop):
    shop_data = {'user': authorized_shop.id,
                 'url': 'https://raw.githubusercontent.com/netology-code/pd-diplom/master/data/shop1.yaml'}
    response = client.post('/api/v1/partner/update', shop_data)

    assert response.status_code == 200
