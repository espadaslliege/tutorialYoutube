# -*- coding: utf-8 -*-
{
    'name': "school",

    'summary': """
        Module of a school""",

    'description': """
        Module of a school with:
        - Student registration
    """,

    'author': "Henrique Espadas",
    'website': "www.HenriqueParanhos.com.br",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/school.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
