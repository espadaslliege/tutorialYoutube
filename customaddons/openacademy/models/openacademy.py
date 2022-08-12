from odoo import models, fields

class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Courses'

    name = fields.Char(string='Course Name', required=True)
    description = fields.Text('description', help='Add course description')

class Session(models.Model):
    _name = 'openacademy'
    _description = "Open Academy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
