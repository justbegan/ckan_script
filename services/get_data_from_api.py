import requests
from services.transliterate import transliterate


def get(url: str) -> dict:
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        raise Exception(f"I can't get data via api: {e}")


def get_reports() -> list:
    """
    Получить нужные поля по report
    """
    url = 'http://10.18.100.33/form/export/data-report-catalog.json'
    data = get(url)
    result = []
    for i in data:
        obj = {
            "id": str(i["id"]) + transliterate(i['org_short']),
            "title": i.get("title"),
            "org": i.get("org"),
            "person": i.get("person"),
            "access": i.get("access"),
            "form": i.get("form"),
            "format": i.get("format"),
            "theme": i.get("theme"),
            "period": i.get("period"),
            "org_get_report": i.get("org_get_report"),
            "org_put_report": i.get("org_put_report")
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
            "title": i.get("title"),
            "data_owner": i.get("data_owner"),
            "format": i.get("format"),
            "visual": i.get("visual"),
            "date_create": i.get("date_create"),
            "date_condition": i.get("date_condition"),
            "projection": i.get("projection"),
            "coord_system": i.get("coord_system"),
            "type": i.get("type"),
            "gis": i.get("gis"),
            "scale": i.get("scale"),
            "status": i.get("status"),
            "period": i.get("period"),
            "description": i.get("description"),
            "link_view": i.get("link_view")
        }
        result.append(obj)
    return result
