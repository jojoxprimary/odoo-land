from odoo import fields, models

class PropertyListData(models.Model):
    _name = 'property.list.data'
    _description = 'Property List Data'

    name = fields.Char('Name')
    area = fields.Char('Area')
    remarks = fields.Char('Remarks')
    