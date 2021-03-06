from django.test import Client
from django.urls import reverse
from rest_framework.status import HTTP_302_FOUND, HTTP_403_FORBIDDEN, HTTP_200_OK

from auth.tests.factories import UserFactory
from organizations.tests.factories import OrganizationFactory


def setup():
    user = UserFactory.create()
    organization = OrganizationFactory.create()

    return user, organization, Client()


def login(client, user):
    user.set_password('test')
    user.save()
    return client.login(username=user.email, password='test')


def user_permissions_test_manage(view, client, user, organization, args):
    # Not logged in should redirect to the login page
    response = client.get(reverse(view, args=args), follow=True)
    assert response.redirect_chain[0][0] == '{0}?next={1}'.format(
        reverse('users:login'),
        reverse(view, args=args)
    )
    assert response.redirect_chain[0][1] == HTTP_302_FOUND

    assert login(client, user)

    response = client.get(reverse(view, args=args))
    assert response.status_code == HTTP_403_FORBIDDEN

    # Test correct permissions
    organization.add_manage(user)
    response = client.get(reverse(view, args=args))
    assert response.status_code == HTTP_200_OK
    organization.delete_manage(user)

    # Super user does what they want
    user.is_superuser = True
    user.save()
    response = client.get(reverse(view, args=args))
    assert response.status_code == HTTP_200_OK
    user.is_superuser = False
    user.save()

    # Test that other permissions do not work
    organization.add_create(user)
    organization.add_invite(user)
    response = client.get(reverse(view, args=args))
    assert response.status_code == HTTP_403_FORBIDDEN
    organization.delete_create(user)
    organization.delete_invite(user)



def user_permissions_test_create(view, client, user, organization, args):
    # Not logged in should redirect to the login page
    response = client.get(reverse(view, args=args), follow=True)
    assert response.redirect_chain[0][0] == '{0}?next={1}'.format(
        reverse('users:login'),
        reverse(view, args=args)
    )
    assert response.redirect_chain[0][1] == HTTP_302_FOUND

    assert login(client, user)

    response = client.get(reverse(view, args=args))
    assert response.status_code == HTTP_403_FORBIDDEN

    # Test correct permissions
    organization.add_manage(user)
    response = client.get(reverse(view, args=args))
    assert response.status_code == HTTP_200_OK
    organization.delete_manage(user)

    # Super user does what they want
    user.is_superuser = True
    user.save()
    response = client.get(reverse(view, args=args))
    assert response.status_code == HTTP_200_OK
    user.is_superuser = False
    user.save()

    organization.add_create(user)
    response = client.get(reverse(view, args=args))
    assert response.status_code == HTTP_200_OK
    organization.delete_create(user)

    organization.add_invite(user)
    response = client.get(reverse(view, args=args))
    assert response.status_code == HTTP_200_OK
    organization.delete_invite(user)


def user_permissions_test_invite(view, client, user, organization, args):
    # Not logged in should redirect to the login page
    response = client.get(reverse(view, args=args), follow=True)
    assert response.redirect_chain[0][0] == '{0}?next={1}'.format(
        reverse('users:login'),
        reverse(view, args=args)
    )
    assert response.redirect_chain[0][1] == HTTP_302_FOUND

    assert login(client, user)

    response = client.get(reverse(view, args=args))
    assert response.status_code == HTTP_403_FORBIDDEN

    # Test correct permissions
    organization.add_manage(user)
    response = client.get(reverse(view, args=args))
    assert response.status_code == HTTP_200_OK
    organization.delete_manage(user)

    # Super user does what they want
    user.is_superuser = True
    user.save()
    response = client.get(reverse(view, args=args))
    assert response.status_code == HTTP_200_OK
    user.is_superuser = False
    user.save()

    organization.add_create(user)
    response = client.get(reverse(view, args=args))
    assert response.status_code == HTTP_403_FORBIDDEN
    organization.delete_create(user)

    organization.add_invite(user)
    response = client.get(reverse(view, args=args))
    assert response.status_code == HTTP_200_OK
    organization.delete_invite(user)
