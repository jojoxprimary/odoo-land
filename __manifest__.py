{
    'name': 'Custom Module',
    'author': 'Jojo',
    'category': 'Custom',
    'summary': 'Custom Odoo18 Module',
    'description': 'Custom Odoo Module for testing',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/custom_user_data.xml',
        'views/menu.xml',
    ],
    'installable': True,    
}