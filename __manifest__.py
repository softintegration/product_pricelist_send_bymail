# -*- coding: utf-8 -*- 


{
    'name': 'Send Pricelist by email',
    'author': 'Soft-integration',
    'application': False,
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'description': False,
    'images': [],
    'version': '1.0.1.2',
    'category': 'Product',
    'demo': [],
    'depends': ['product_pricelist_report','product_pricelist_chatter'],
    'data': [
        'data/mail_templates_data.xml',
        'views/product_pricelist_views.xml'
    ],
    'license': 'LGPL-3',
}
