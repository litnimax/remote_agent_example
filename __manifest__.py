# -*- encoding: utf-8 -*-
{
    'name': 'Odoo remote agent example',
    'version': '1.0',
    'author': 'Odooist',
    'maintainer': 'Odooist',
    'support': 'odooist@gmail.com',
    'category': 'Hidden',
    'summary': 'Example of custom remote agent',
    'description': "",
    'external_dependencies': {
        'python': ['tinyrpc'],
    },
    'depends': ['remote_agent'],
    'data': [
        'views/room.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
