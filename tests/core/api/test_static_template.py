import pytest
from django.test import RequestFactory
from django.urls import reverse

from core.views import index


@pytest.mark.django_db
class TestStaticTemplate:
    def test_index_view(self):
        factory = RequestFactory()
        request = factory.get(reverse('index'))
        response = index(request)
        assert response.status_code == 200
