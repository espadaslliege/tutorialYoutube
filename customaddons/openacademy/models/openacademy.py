from odoo import models, fields

class Course(models.Model):
    _name = 'openacademy.couse'
    _description = 'Courses'

    name = fields.Char(string='Course Name', required=True)
    description = fields.Text('Description', help='Add course description')
