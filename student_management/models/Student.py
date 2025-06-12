from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'

    student_id = fields.Char(string='Student Id', required=True)
    name = fields.Char(string='Name', required=True)
    display_name = fields.Char(string='Display name')
    birth_date = fields.Date(string='Birth date')
    email = fields.Char(string='Email')
    phone_number = fields.Char(string='Phone number')
    # Many2one
    class_id = fields.Many2one('school.class', string='Class')
    # Many2many
    course_ids = fields.Many2many('school.course', string='Courses')
    # One2many
    partner_ids = fields.One2many('res.partner', 'student_id', string='Student partners')
    # On2Many
    book_ids = fields.One2many('library.book', 'student_id', string='Library books')

    @api.model_create_multi
    def create(self, vals):
        print("Create method called!")
        print(self)
        print(vals)
        students = super(Student, self).create(vals)
        print(students)
        for student in students:
            student.display_name = f'{student.student_id} - {student.name}'
        return students

    def write(self, vals):
        print("Write method called!")
        print(self)
        print(vals)
        rs = super(Student, self).write(vals)
        print(rs)
        if 'student_id' in vals or 'name' in vals:
            for student in self:
                studentId = vals.get('student_id', student.student_id)
                studentName = vals.get('name', student.name)
                student.display_name = f'{studentId} - {studentName}'
        return rs

    @api.constrains('student_id')
    def _check_unique_student_id(self):
        print("Call check unique student_id method")
        for record in self:
            exist_student = self.env['student.student'].search(
                [('student_id', '=', record.student_id), ('id', '!=', record.id)]
            )
            if exist_student:
                raise ValidationError("Mã sinh viên đã tồn tại, vui lòng nhập mã sinh viên khác")

    def custom_method(self):
        print(self)
        print("Clicked!")
        print(self.env['student.student'])
        print(self.env['student.student'].create({'student_id': 'STU006', 'name': 'Trần Dự'}))

    def action_show_student_partners(self):
        # Lấy ra tất cả partner id gắn với sv
        partner_ids = self.partner_ids.ids
        return {
            'name': 'Partners',               # Tiêu đề của sổ
            'type': 'ir.actions.act_window',          # Loại hành động
            'res_model': 'res.partner',               # Model sẽ hiển thị
            'view_mode': 'tree,form',                 # Chế độ xem
            'domain': [('id', 'in', partner_ids)],    # Lọc theo id liên hệ
            'target': 'current'                       # Mở trong cửa sổ hiện tại
        }


class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'Class of Student'

    name = fields.Char(string='Class name', required=True)
    code = fields.Char(string='Class code')

    # One2many
    student_ids = fields.One2many('student.student', 'class_id', string='Students')


class SchoolCourse(models.Model):
    _name = 'school.course'
    _description = 'Course'

    name = fields.Char(string='Course name')
    code = fields.Char(string='Course code')

    # Many2many
    student_ids = fields.Many2many('student.student', string='Students')
