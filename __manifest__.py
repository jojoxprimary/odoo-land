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
        'views/land_master_data.xml',  
        'views/menu.xml',
        'data/land_master_xmldata.xml',
        'data/philippines_state_data.xml',
        'data/city_data.xml'

        # 'data/remove_land_master_record.xml',
    ],
    'installable': True,    
}