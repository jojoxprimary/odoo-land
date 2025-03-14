from odoo import fields, models

class SubPropertyListData(models.Model):
    _name = 'subproperty.list.data'
    _description = 'Sub Property List Data'

    property_name = fields.Many2one(
        'property.list.data', 
        string = 'Property Name',
        required=True
    ) # from property list
    name = fields.Char('Sub Property Name', required=True)
    # subproperty_code = fields.Char('Sub Property Code')
    # development_type = fields.Many2one(
    #     'land.master.data.line',
    #     string='Development Type',
    #     domain="[('master_id.name', '=', 'Development Type')]"
    # ) # from development type master 

    #available_area = fields.Float('Available Area')
    #subproperty_land_area = fields.Float('Sub Property Area')
    
