from bson import ObjectId
from flask import jsonify

from app.model import Class
from app.controller import classes_collection
from app.services import verify_request_data, get_data_by_id, get_items_data, update_time_data


def get_available_classes():
    
    classes_list = get_items_data(classes_collection.find({}))
    return jsonify(classes_list), 200


def get_class_profile(data):

    wrong_request_data = verify_request_data(data, classes_collection, 'GET')
    if wrong_request_data:
        return wrong_request_data, 400
    
    class_id = data.get('id')
    class_profile = classes_collection.find_one({'_id': ObjectId(class_id)})
    class_profile = get_data_by_id(class_id, classes_collection)

    return jsonify(class_profile), 200


def insert_new_class(data):

    is_wrong_data = Class.verify_new_class_data(data, classes_collection.find({}))  

    if is_wrong_data: 
        return is_wrong_data, 400

    new_class = Class(**data)
    classes_collection.insert_one(new_class.__dict__)

    return 'Nova turma registrada com sucesso!', 200


def update_class(data):

    wrong_data_request = verify_request_data(data, classes_collection, 'PATCH')
    if wrong_data_request: 
        return wrong_data_request, 400

    class_id = data.get('id')

    for key in data.keys():

        if key != 'id':
            new_values = {"$set": {key: data[key]} }
            classes_collection.update_one({'_id' : ObjectId(class_id)}, new_values)
    
    classes_collection.update_one({'_id' : ObjectId(class_id)}, update_time_data())

    return 'Turma atualizada com sucesso', 200


def delete_class(data):

    wrong_data = verify_request_data(data, classes_collection)
    if wrong_data:
        return wrong_data, 400
 
    class_id = {"_id": ObjectId(data.get("id"))}
    classes_collection.delete_one(class_id)

    return 'Turma removida com sucesso', 200