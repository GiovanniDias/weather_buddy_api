import pytest
# from app.api import get_weather, get_city_weather


@pytest.mark.parametrize('max_number', [None,0,1,10])
def test_get_weather_cached_list_success(client, max_number):
    url = '/weather'
    if max_number:
        url += f'?max={max_number}'
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_get_weather_cached_list_not_found(client):
    url = '/weather'
    response = client.get(url)
    assert response.status_code == 404


@pytest.mark.parametrize('city_name', ['São Paulo'])
def test_get_weather_by_city_success(client, city_name):
    url = f'/weather/{city_name}'
    response = client.get(url)
    assert response.status_code == 200
    assert response.json.get('name') == city_name


@pytest.mark.parametrize('city_name', ['-'])
def test_get_weather_by_city_not_found(client, city_name):
    url = f'/weather/{city_name}'
    response = client.get(url)
    assert response.status_code == 404