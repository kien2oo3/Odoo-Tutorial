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

    @api.model_create_multi
    def create(self, vals):
        print("Create method called!")
        print(self)
        print(vals)
        students = super().create(vals)
        print(students)
        for student in students:
            student.display_name =  f'{student.student_id} - {student.name}'
        return students

    def write(self, vals):
        print("Write method called!")
        print(self)
        print(vals)
        rs = super().write(vals)
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
                [('student_id', '=', record.student_id), ('id' , '!=', record.id)]
            )
            if exist_student:
                raise ValidationError("Mã sinh viên đã tồn tại, vui lòng nhập mã sinh viên khác")

    def custom_method(self):
        print(self)
        print("Clicked!")
        print(self.env['student.student'])
        print(self.env['student.student'].create({'student_id':'STU006','name':'Trần Dự'}))