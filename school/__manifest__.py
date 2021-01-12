# -*- coding: utf-8 -*-
{
    'name': "School",

    'summary': "School Management Software",

    'description': """
        Long description of module's purpose
    """,

    'author': "Honey",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base', 'mail', 'board', 'website', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        #'views/views.xml',
        'wizards/wizard_view.xml',
        'views/templates.xml',
        'views/views.xml',
        'views/dashboard.xml',
        'views/form.xml',
        'reports/report.xml',
        'reports/student_card.xml',
    ],
        # only loaded in demonstration mode
    'demo': [],
    'qweb':[],
    'installable':True,
    'application':True,
}
