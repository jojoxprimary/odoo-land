{
    'name': 'Land Module',
    'author': 'Jojo',
    'category': 'Custom',
    'summary': 'Custom Land Module',
    'description': 'Custom Land Module for Odoo 18',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/property_list_data.xml',
        'views/menu.xml',
    ],
    'installable': True,    
}