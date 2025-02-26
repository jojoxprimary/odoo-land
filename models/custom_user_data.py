from odoo import fields, models

class CustomUserData(models.Model):
    _name = 'custom.user.data'
    _description = 'Custom User Data'

    name = fields.Char('Name')
    email = fields.Char('Email')  
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], 'Gender')
    company = fields.Char('Company Name')
