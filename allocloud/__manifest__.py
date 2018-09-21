# -*- coding: utf-8 -*-
{
    'name': "ALLOcloud",

    'summary': "Integration of Odoo with the ALLOcloud VoIP telephony platform for advanced CTI functionalities",

    'description': """
        The ALLOcloud-Odoo integration allows to leverage your telephony directly from Odoo.
        
        Click-to-call, popup notification on incoming call are the basic CTI (Computer Telephony Integration) built-in features. 
        You can go further by using the Odoo and ALLOcloud APIs and build your own integrations (add calls to the contact activity log, attach call recordings to a specific contact, time call duration for invoicing etc.)
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