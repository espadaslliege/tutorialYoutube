from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    computer_generation = fields.Char(string='Computer Generation')
    warranty_start_date = fields.Date(string='Warranty start')
    warranty_end_date = fields.Date(string='Warranty End')