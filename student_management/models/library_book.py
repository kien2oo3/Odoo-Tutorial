from odoo import models, fields, api


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    book_id = fields.Char(string='Book Id')
    book_name = fields.Char(string='Book name', required=True)
    publish_year = fields.Char(string='Publish year')
    book_author = fields.Char(string='Book author')

    student_id = fields.Many2one('student.student', string='Student')
    student_count = fields.Integer(string='Student count', compute='_compute_student_count', store=True)

    # Ghi đè hàm create
    @api.model_create_multi
    def create(self, vals_list):
        rs = super().create(vals_list)
        for record in rs:
            numberId = str(100000 + record.id)[1:]
            record.book_id = f'TV{numberId}'
        return rs

    # Hàm lấy số lượng sinh viên mượn sách
    @api.depends('student_id')
    def _compute_student_count(self):
        for record in self:
            record.student_count = 1 if record.student_id else 0

    # Check mã sách trùng khi thêm mới
    _sql_constraints = [('unique_book_id', 'unique(book_id)', 'Mã sách đã tồn tại, hãy nhập một mã sách khác')]


