import requests
import configuration
import data


def create_user(body_user):
    return requests.post(configuration.URL_SERVISE + configuration.NEW_USER,
                          json = body_user,
                         headers= data.headers)
def create_board(uid):
    return requests.post(configuration.URL_SERVISE + configuration.NEW_BOARD,
                         json = {"userId" : uid} + data.body_board,
                         headers= data.headers)
