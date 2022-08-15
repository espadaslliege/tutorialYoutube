from odoo import models, fields, api


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Courses'

    name = fields.Char(string='Course Name', required=True)
    description = fields.Text('description', help='Add course description')
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)
    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')

    def _taken_sets(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats


class Session(models.Model):
    _name = 'openacademy.session'
    _description = "Open Academy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.date.today())
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one('res.partner', string="Instructor", domain=[('country_id', '=', 'Belgium')])
    country_id = fields.Many2one('res.country', related='instructor_id.country_id')
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    taken_seats = fields.Float('Taken seats', compute='_taken_seats')
    active = fields.Boolean(string='Active', default=True)

    @api.depends('seats')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of available seats may not be negative",
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "To many attendees",
                    'message': "Increase seats or remove excess attendees",
                },
            }
