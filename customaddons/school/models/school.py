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
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True, traking=True)


class Session(models.Model):
    _name = "session.school"
    _description = "Semester sessions"

    name = fields.Char(string="Course Name", required=True)
    description = fields.Char("Description", help="Add session description")
    start_date = fields.Date(string="Start date", default=fields.date.today())
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    end_date = fields.Date(
        string="End Date", store=True, compute="_get_end_date", inverse="_set_end_date"
    )
    instructor_id = fields.Many2one("res.partner", string="Instructor")
    course_id = fields.Many2one(
        "course.school", ondelete="cascade", string="Course", required=True
    )
    cidade = fields.Char(string="city")
    attendee_ids = fields.Many2many("students.school", string="Attendees")
    seats = fields.Integer(string="Number of seats")
    taken_seats = fields.Float("Taken seats", compute="_taken_seats")
    active = fields.Boolean(string="Active", default=True)
    attendees_count = fields.Integer(
        string="Attendees count", compute="_get_attendees_count", store=True
    )

    @api.depends("attendee_ids")
    def _get_attendees_count(self) ->None:
        for r in self:
            r.attendees_count = len(r.attendee_ids)

    @api.depends("start_date", "duration")
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue

                # Add duration to start_date, but: Monday + 5 days = Saturday, so
                # subtract one second to get on Friday instead
                duration = timedelta(days=r.duration, seconds=-1)
                r.end_date = r.start_date + duration

    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                continue
            r.duration = (r.end_date - r.start_date).days + 1

    @api.depends("seats")
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats

    @api.onchange("seats", "attendee_ids")
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                "warning": {
                    "title": "Incorrect 'seats' value",
                    "message": "The number of available seats may not be negative",
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                "warning": {
                    "title": "To many attendees",
                    "message": "Increase seats or remove excess attendees",
                },
            }
