# -*- coding: utf-8 -*-
{
    'name': "ALLOcloud",

    'summary': """ALLOcloud summary""",

    'description': """
        ALLOcloud description
    """,

    'author': "ALLOcloud",
    'website': "https://www.allocloud.com",
    'images': ['static/description/banner.jpg'],

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo.xml',
    # ],
}