from database.peewee_models import Package, Package_extra, db
import logging


file_log = logging.FileHandler("logfile.log")
console_out = logging.StreamHandler()
logging.basicConfig(handlers=(file_log, console_out), level=logging.INFO)


class Update:
    def __init__(self, data: dict, geo: bool = False) -> None:
        self.data = data
        self.id = data.get('id')
        self.uid = Package.get(Package.name == self.id).id
        self.title = data.get('title')
        self.geo = geo
        if not geo:
            self.author = data.get('org')
        else:
            self.author = data.get('data_owner')

    def start(self):
        try:
            with db.atomic():
                self.update_package()
                self.update_package_extra()
        except Exception as e:
            logging.error(f"couldn't update record № {self.id}, {e}")
            db.rollback()

        db.close()

    def update_package(self) -> None:
        query = Package.update(title=self.title, author=self.author).where(Package.name == self.id)
        query.execute()

    def update_package_extra(self) -> None:
        query = Package.update(title=self.title, author=self.author).where(Package.name == self.id)
        query.execute()
        for obj in self.generator_pkg_extras_list():
            query = Package_extra.update(value=obj['value']).where(
                Package_extra.package_id == self.uid,
                Package_extra.key == obj['key']
            )
            query.execute()

    def generator_pkg_extras_list(self) -> list:
        data = self.data
        if not self.geo:
            pkg_extras_list = [
                {'key': 'responsible_person', 'value': data['person']},
                {'key': 'report_access_level', 'value': data['access']},
                {'key': 'report_type', "value": data['form']},
                {'key': 'report_data_format', 'value': data['format']},
                {'key': 'report_category', 'value': data['theme']},
                {'key': 'report_refresh_period', 'value': data['period']},
                {'key': 'report_adresat', 'value': data['org_get_report']},
                {'key': 'org_put_report', 'value': data['org_put_report']}
            ]
        else:
            pkg_extras_list = [
                {'key': 'dim_data_format', "value": data['format']},
                {'key': 'dim_representation_method', 'value': data['visual']},
                {'key': 'dim_data_create_date', 'value': data['date_create']},
                {'key': 'dim_land_state_date', 'value': data['date_condition']},
                {'key': 'dim_carthographic_projection', 'value': data['projection']},
                {'key': 'dim_coordinate_system', 'value': data['coord_system']}
            ]
        return pkg_extras_list
