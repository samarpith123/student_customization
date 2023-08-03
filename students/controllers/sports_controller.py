from odoo import http
from odoo.http import request


class StudentRegistration(http.Controller):
    @http.route(['/register'], type='http', auth="public",website=True)
    def website_menu(self):
        # request.env['hostel.student'].sudo().create()
        
        return request.render("students.register_form")
    
    @http.route(['/register_submit'], type='http', auth="public", website=True)
    def website_menu_student(self, **post):
        request.env['students.player'].create(post)
        return request.render('students.registration_success_template')
       