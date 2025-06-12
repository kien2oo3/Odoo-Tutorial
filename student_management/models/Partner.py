from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Partner(models.Model):
    _inherit = 'res.partner'

    # Trường đánh dấu là sinh viên
    is_student = fields.Boolean(string='Is student', default=False)

    # Mỗi liên hệ chỉ có 1 sv
    student_id = fields.Many2one('student.student', string='Partner')

    # @api.constrains('student_id')
    # def _check_unique_student(self):
    #     for record in self:
    #         if record.is_student:
    #             exist_partner = self.env['res.partner'].search([
    #                 ('student_id', '=', record.student_id.id), ('id', '!=', record.id)
    #             ])
    #             if exist_partner:
    #                 raise ValidationError('Sinh viên đã có trong liên hệ khác, bạn hãy chọn một sinh viên khác!')
