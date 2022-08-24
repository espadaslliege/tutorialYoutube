from odoo import api, fields, models


class Students(models.Model):
    _name = "students.school"
    _description = "Students"

    name = fields.Char(string="Name:", required="True")
    rg = fields.Integer(string="RG:", required="True")
    responsible = fields.Char(string="Responsible:", required="True", traking=True)
    serie = fields.Integer(string="Series:", required="True")
    city = fields.Char(string="City:", required="True")


class Course(models.Model):
    _name = "course.school"
    _description = "Courses"

    name = fields.Char(string="Course Name", required=True)
    description = fields.Text("Description", help="Add course description")


class Session(models.Model):
    _name = 'session.school'
    _description = "Semester sessions"

    name = fields.Char(string="Course Name", required=True)
    description = fields.Char("Description", help="Add session description")
    start_date = fields.Date(string="Start date")
    end_date = fields.Date(string="End date")
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('course.school', ondelete='cascade', string="Course", required=True)
    cidade = fields.Char(string="city")
    attendee_ids = fields.Many2many('students.school', string="Attendees", domain=[('city', '=', 'SP')])
    # seats = fields.Integer(string="Number of seats")
    # taken_seats = fields.Float('Taken seats', compute='_taken_seats')
    #
    # @api.depends('seats')
    # def _taken_seats(self):
    #     for r in self:
    #         if not r.seats:
    #             r.taken_seats = 0.0
    #         else:
    #             r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats
