from requests import get
from function_jwt import valida_token
from flask import Blueprint, request

users_git = Blueprint('users_git', __name__)


@users_git.before_request
def verify_token_middleware():
    token = request.headers['authorization'].split(' ')[1]
    return valida_token(token)


@users_git.route('/git/users', methods=['POST'])
def github():
    data = request.get_json()
    country = data['country']
    return get(f'https://api.github.com/search/users?q=location:"{country}"&page=1').json()