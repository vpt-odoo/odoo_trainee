# -*- coding: utf-8 -*-
{
    'name': "Praposal Application",
    'sequence':'1',
    'summary': "Proposal Application",
    'description': "This app for the sent the proposal to customer for the products",
    'author': "Odoo India ,Roopam Rathod(rrt)",
    'website': "http://www.odoo.com",
    'category': 'Uncategorized',
    'version': '12.0.0.1',
    'depends': ['base','contacts','hr','sale','payment','portal','sales_team'],
    'data': [
        'data/sequence.xml',
        'views/proposal_css.xml',
        'views/portal_template.xml',
        'report/proposal_report.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}