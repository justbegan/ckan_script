from database.sql import get_query


def get_report_by_id(id: str):
    query = """
        SELECT
            pkg.name AS id,
            pkg.title AS title,
            pkg.author AS org,
            pe_responsible_person.value AS person,
            pe_report_access_level.value AS access,
            pe_report_type.value AS form,
            pe_report_data_format.value AS format,
            pe_report_category.value AS theme,
            pe_report_refresh_period.value AS period,
            pe_report_adresat.value AS org_get_report,
            pe_org_put_report.value AS org_put_report
        FROM
            public."package" AS pkg
        LEFT JOIN
            public."group" AS grp ON pkg.owner_org = grp.id
        LEFT JOIN
            public."package_extra" AS pe_responsible_person ON pkg.id = pe_responsible_person.package_id AND
            pe_responsible_person.key = 'responsible_person'
        LEFT JOIN
            public."package_extra" AS pe_report_access_level ON pkg.id = pe_report_access_level.package_id AND
            pe_report_access_level.key = 'report_access_level'
        LEFT JOIN
            public."package_extra" AS pe_report_type ON pkg.id = pe_report_type.package_id AND
            pe_report_type.key = 'report_type'
        LEFT JOIN
            public."package_extra" AS pe_report_data_format ON pkg.id = pe_report_data_format.package_id AND
            pe_report_data_format.key = 'report_data_format'
        LEFT JOIN
            public."package_extra" AS pe_report_category ON pkg.id = pe_report_category.package_id AND
            pe_report_category.key = 'report_category'
        LEFT JOIN
            public."package_extra" AS pe_report_refresh_period ON pkg.id = pe_report_refresh_period.package_id AND
            pe_report_refresh_period.key = 'report_refresh_period'
        LEFT JOIN
            public."package_extra" AS pe_report_adresat ON pkg.id = pe_report_adresat.package_id AND
            pe_report_adresat.key = 'report_adresat'
        LEFT JOIN
            public."package_extra" AS pe_org_put_report ON pkg.id = pe_org_put_report.package_id AND
            pe_org_put_report.key = 'org_put_report'
        WHERE pkg.name = %s
    """
    return get_query(id, query)


def get_geo_by_id(id: str):
    query = """
        SELECT
            pkg.name AS id,
            pkg.title AS title,
            pkg.author AS data_owner,

            pkg.notes AS description,
            pkg.url AS link_view,

            pe_dim_data_format.value AS format,
            pe_dim_representation_method.value AS visual,
            pe_dim_data_create_date.value AS date_create,
            pe_dim_land_state_date.value AS date_condition,
            pe_dim_carthographic_projection.value AS projection,
            pe_dim_coordinate_system.value AS coord_system,

            pe_dim_data_type.value AS type,
            pe_dim_gis.value AS gis,
            pe_dim_accuracy.value AS scale,
            pe_dim_land_state_status.value AS status,
            pe_dim_refresh_period.value AS period

        FROM
            public."package" AS pkg
        LEFT JOIN
            public."package_extra" AS pe_report_access_level ON pkg.id = pe_report_access_level.package_id AND
            pe_report_access_level.key = 'report_access_level'
        LEFT JOIN
            public."package_extra" AS pe_dim_data_format ON pkg.id = pe_dim_data_format.package_id AND
            pe_dim_data_format.key = 'dim_data_format'
        LEFT JOIN
            public."package_extra" AS pe_dim_representation_method ON
            pkg.id = pe_dim_representation_method.package_id AND
            pe_dim_representation_method.key = 'dim_representation_method'
        LEFT JOIN
            public."package_extra" AS pe_dim_data_create_date ON pkg.id = pe_dim_data_create_date.package_id AND
            pe_dim_data_create_date.key = 'dim_data_create_date'
        LEFT JOIN
            public."package_extra" AS pe_dim_land_state_date ON pkg.id = pe_dim_land_state_date.package_id AND
            pe_dim_land_state_date.key = 'dim_land_state_date'
        LEFT JOIN
            public."package_extra" AS pe_dim_carthographic_projection ON
            pkg.id = pe_dim_carthographic_projection.package_id AND
            pe_dim_carthographic_projection.key = 'dim_carthographic_projection'
        LEFT JOIN
            public."package_extra" AS pe_dim_coordinate_system ON pkg.id = pe_dim_coordinate_system.package_id AND
            pe_dim_coordinate_system.key = 'dim_coordinate_system'

        LEFT JOIN
            public."package_extra" AS pe_dim_data_type ON pkg.id = pe_dim_data_type.package_id AND
            pe_dim_data_type.key = 'dim_data_type'
        LEFT JOIN
            public."package_extra" AS pe_dim_gis ON pkg.id = pe_dim_gis.package_id AND
            pe_dim_gis.key = 'dim_gis'
        LEFT JOIN
            public."package_extra" AS pe_dim_accuracy ON pkg.id = pe_dim_accuracy.package_id AND
            pe_dim_accuracy.key = 'dim_accuracy'
        LEFT JOIN
            public."package_extra" AS pe_dim_land_state_status ON pkg.id = pe_dim_land_state_status.package_id AND
            pe_dim_land_state_status.key = 'dim_land_state_status'
        LEFT JOIN
            public."package_extra" AS pe_dim_refresh_period ON pkg.id = pe_dim_refresh_period.package_id AND
            pe_dim_refresh_period.key = 'dim_refresh_period'

        WHERE pkg.name = %s
    """
    return get_query(id, query)
