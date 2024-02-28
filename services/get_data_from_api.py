from requests import request
from services.transliterate import transliterate


def get(url: str) -> dict:
    try:
        response = request(
            method='GET',
            headers={
                "Content-Type": "application/json",
                "Accept": "*/*"
            },
            url=url
        )
        return response.json()
    except:
        raise Exception(f"I can't get data via api {url}")


def get_reports() -> list:
    """
    Получить нужные поля по report
    """
    url = 'http://10.18.100.33/form/export/data-report-catalog.json',
    data = get(url)
    result = []
    for i in data:
        obj = {
            "id": str(i["id"]) + transliterate(i['org_short']),
            "title": i.get("title", 'NaN'),
            "org": i.get("org", 'NaN'),
            "person": i.get("person", 'NaN'),
            "access": i.get("access", 'NaN'),
            "form": i.get("form", 'NaN'),
            "format": i.get("format", 'NaN'),
            "theme": i.get("theme", 'NaN'),
            "period": i.get("period", 'NaN'),
            "org_get_report": i.get("org_get_report", 'NaN'),
            "org_put_report": i.get("org_put_report", 'NaN')
        }
        result.append(obj)
    return result


def get_geo() -> list:
    """
    Получить нужные поля по geo
    """
    url = "http://10.18.100.33/form/export/data-geo.json"
    data = get(url)
    result = []
    for i in data:
        obj = {
            "id": str(i["id"]),
            "title": i.get("title", 'NaN'),
            "data_owner": i.get("data_owner", 'NaN'),
            "format": i.get("format", 'NaN'),
            "visual": i.get("visual", 'NaN'),
            "date_create": i.get("date_create", 'NaN'),
            "date_condition": i.get("date_condition", 'NaN'),
            "projection": i.get("projection", 'NaN'),
            "coord_system": i.get("coord_system", 'NaN'),
        }
        result.append(obj)
    return result
