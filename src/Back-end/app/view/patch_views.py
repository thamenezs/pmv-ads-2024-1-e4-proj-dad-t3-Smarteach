from flask import request

from app.controller.teacher_controller import update_teacher_profile
from app.controller.student_controller import update_student_profile
from app.controller.class_controller import update_class


def patch_routes(app):
    @app.patch('/teacher')
    def change_teacher_data_profile():
        data = request.get_json()
        return update_teacher_profile(data)
    
    @app.patch('/student')
    def change_student_data_profile():
        data = request.get_json()
        return update_student_profile(data)

    @app.patch('/class')
    def change_class_data():
        data = request.get_json()
        return update_class(data)
