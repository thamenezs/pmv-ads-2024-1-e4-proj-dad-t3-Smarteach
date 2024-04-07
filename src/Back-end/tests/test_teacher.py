from random import randrange, choice

from tests import available_school_subjects, get_fake_data_profile

fake_profile = {'type': 'teacher'}

def test_get_all_teachers(client):

    response = client.get('/teacher')
    assert response.status_code == 200


def test_register_new_teacher(client):

    random_subject = choice(available_school_subjects)
    random_email = f"fulano_{randrange(1, 1000000000)}@mail.com"
    fake_profile.update({'email': random_email})
    
    response = client.post('/teacher', json={
        "nome":"Fulano de Tal",
	    "email": random_email,
	    "disciplina": random_subject,
	    "turmas": [101],
	    "turno": "vespertino"
    })

    assert response.status_code == 201


def test_update_teacher_register(client):

    user = get_fake_data_profile(client, fake_profile)
    
    response = client.patch('/teacher', json={
    "id": user.get("_id"),
    "nome": "Fulano de Tal Silva",
    "turno": "Noturno",
    "disciplina": choice(available_school_subjects)
    })

    assert response.status_code == 200


def test_update_teacher_without_send_id(client):
    
    response = client.patch('/teacher', json={
    "email": "folano@mail.com",
    "turno": "Noturno",
    "disciplina": choice(available_school_subjects)
    })

    assert response.status_code == 400


def test_delete_teacher_user(client):

    user = get_fake_data_profile(client, fake_profile)
    fake_profile.update({"id": user.get("_id")})

    response = client.delete('/teacher', json={
        "id": fake_profile.get("id")
    })

    assert response.status_code == 200


def test_delete_unregistered_teacher(client):
        
    response = client.delete('/teacher', json={
        "id": fake_profile.get("id")
    })

    assert response.status_code == 400
