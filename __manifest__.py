# -*- coding: utf-8 -*-
{
    'name': "CRM Dashboard",

    'summary': """
        Helps to provide a dashboard""",

    'description': """
        Description
    """,

    'author': "Minions 6",

    'version': '15.0.1.0.0',
    'depends': ['crm', 'project'],

    'data': [
        'views/dashboard_view.xml'],
    'assets': {
        'web.assets_backend': [
            'CRM_Dashboard/static/src/js/dashboard.js'
        ],
        'web.assets_qweb': [
            'CRM_Dashboard/static/src/xml/dashboard_views.xml'
        ]
    }
}
