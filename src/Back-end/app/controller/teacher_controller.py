from flask import jsonify
from bson import ObjectId

from app.model import Teacher, Class
from app.controller import teacher_collection, classes_collection
from app.controller.class_controller import update_class_profile
from app.services import verify_request_data, get_items_data, get_data_by_id, get_user_by_email, verify_user_email, update_time_data, verify_update_sent_data_request


def get_available_teachers():

    teacher_list = get_items_data(teacher_collection.find({}))

    return jsonify(teacher_list), 200


def get_teacher_profile(user_id):

    wrong_request_data = verify_request_data({'id': user_id}, teacher_collection, 'GET')
    if wrong_request_data:
        return wrong_request_data, 400
    
    teacher_profile = get_data_by_id(user_id, teacher_collection)

    return jsonify(teacher_profile), 200


def insert_new_teacher(data: dict):

    is_wrong_data = Teacher.verify_new_teacher_data(data)  

    if is_wrong_data: 
        return is_wrong_data, 400

    teacher_email = data.get('email')
    is_same_email = verify_user_email(teacher_email, teacher_collection.find({}))

    if is_same_email: 
        return is_same_email, 409
    
    inexistent_class_numbers = []

    for class_number in data.get("classes"):
        is_existent_class = Class.verify_if_exist_class_data(class_number, classes_collection.find({}))

        if not is_existent_class:
           inexistent_class_numbers.append(class_number)

    if inexistent_class_numbers:
        return "Turma(s) inexistente(s):{}".format(inexistent_class_numbers), 400

    new_teacher = Teacher(**data)
    teacher_collection.insert_one(new_teacher.__dict__)
    teacher_data = get_user_by_email(teacher_email, teacher_collection)

    for class_number in data.get("classes"):
        selected_class = classes_collection.find_one({'number': int(class_number)})
        class_id = selected_class.get('_id')
        class_teachers = selected_class.get('teachers')

        if teacher_data not in class_teachers:
            class_teachers.append(teacher_data)
            update_class_profile({'id': class_id, 'teachers': class_teachers})

    return 'Novo Professor registrado com sucesso!', 201
    

def update_teacher_profile(data):

    wrong_data_request = verify_request_data(data, teacher_collection, 'PATCH')
    if wrong_data_request: 
        return wrong_data_request, 400

    user_id = data.get('id')
    available_teacher_keys = ['name', 'email', 'password', 'classes', 'subject', 'period', 'id']

    wrong_properties = verify_update_sent_data_request(data, available_teacher_keys)
    if wrong_properties:
        return wrong_properties, 400

    for key in data.keys():

        if key != 'id':
            new_values = {"$set": {key: data[key]} }
            teacher_collection.update_one({'_id' : ObjectId(user_id)}, new_values)
    
    teacher_collection.update_one({'_id' : ObjectId(user_id)}, update_time_data())

    return 'Perfil de Professor atualizado com sucesso!', 200


def delete_teacher_profile(data):
    
    wrong_data_request = verify_request_data(data, teacher_collection)
    if wrong_data_request: 
        return wrong_data_request, 400
    
    user_id = data.get('id')
    teacher_data = get_data_by_id(user_id, teacher_collection)
    teacher_collection.delete_one({"_id": ObjectId(user_id)})

    for class_number in teacher_data.get("classes"):
        selected_class = classes_collection.find_one({'number': class_number})
        class_id = selected_class.get('_id')
        class_teachers = selected_class.get('teachers')

        filtered_class_teachers = [teacher for teacher in class_teachers if teacher['_id'] != user_id]
        update_class_profile({'id': class_id, 'teachers': filtered_class_teachers})

    return 'Perfil de Professor deletado com sucesso!', 200 
