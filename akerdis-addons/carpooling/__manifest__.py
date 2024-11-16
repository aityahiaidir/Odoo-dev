# -*- coding: utf-8 -*-
{
    'name':'Carpoolin Application',
    'version':'1.0',
    'author' : 'AIT YAHIA',
    'description': """ Module to hel you toorganize the traject with your employees.
    Make your life easize
    """,
    'website':'www.akerdis.com',
    'license' :'LGPL-3',
    'category':'Customizations',
    'depends' : ['base','sale','contacts'],
    'data':[
      
        'security/ir.model.access.csv',
        'security/groups.xml',
        'views/carpooling_views.xml',
        'views/res_partner_views.xml',
        'wizards/carpooling_wizard_views.xml',
        'views/carpooling_menus.xml',
        'data/ir_cron.xml',
        'reports/car_report.xml',
        'reports/zpl_report.xml',

        ]

}