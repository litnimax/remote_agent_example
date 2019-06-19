# -*- encoding: utf-8 -*-
{
    'name': 'Odoo remote agent example',
    'version': '12.0.1.0',
    'author': 'Odooist',
    'maintainer': 'Odooist',
    'support': 'odooist@gmail.com',
    'license': 'LGPL-3',
    'category': 'Tools',
    'summary': 'Example of custom remote agent',
    'description': "",
    'website': 'http://github.com/litnimax/remote_agent_example',
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
    'images': ['static/description/screenshot1.png'],
}
