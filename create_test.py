import data
import sender_stand_request

def test_pozitiv():
    uid = sender_stand_request.create_user(data.body_user).json()["userId"]
    get_status = sender_stand_request.create_board(uid)
    assert get_status.status_code == 201