from flask import request

from app.controller import get_available_teachers, get_available_admins, get_available_classes, get_available_students
from app.controller.teacher_controller import get_teacher_profile
from app.controller.class_controller import get_class_profile


def get_routes(app):

    @app.get('/teacher')
    def show_teachers():
        return get_available_teachers()
    
    @app.get('/teacher/profile')
    def show_teacher_profile():
        data = request.get_json()
        return get_teacher_profile(data)
    
    @app.get('/class')
    def show_classes():
        return get_available_classes()
    
    @app.get('/class/profile')
    def show_class_profile():
        data = request.get_json()
        return get_class_profile(data)
    
    @app.get('/student')
    def show_students():
        return get_available_students()
    
    @app.get('/admin')
    def show_admins():
        return get_available_admins()
