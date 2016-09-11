import requests

# get token
app_info = {"app_id": "203228","app_secret": "fbe54068c5eafd5262ff169a1682cca2"}
r = requests.post('http://127.0.0.1:5001/api/token', data=app_info)

token = "{'Authorization': 'Bearer 4698fe32-664c-4ba3-9ec7-8b505cd98a11'}"
session = "d8571c804999416e92e3007ccc494b25"

# create user
# data = {"token": token, "app_user_id": "TEST_testAccount111", "nickname": "abd"}
# r = requests.post('http://127.0.0.1:5000/api/user/create', data=data)

# update session
# data = {"token": token, "app_user_id": "TEST_testAccount111"}
# r = requests.post('http://127.0.0.1:5000/api/user/session', data=data)

# update user info
# data = {"token": token,
#         "app_user_id": "TEST_testAccount111", "nickname": "abc", "session": session}
# r = requests.post('http://127.0.0.1:5000/api/user/nickname', data=data)

#
# create group
# data = {"token": token, "session": session, "members": "TEST_testAccount222", "group_name": "test_groupName", "group_description": "test_groupDesc"}
# r = requests.post('http://127.0.0.1:5000/api/group/create', data=data)

# update group
# data = {"token": token, "session": session, "group_id": "80233c8073d511e69ce5fb907fee57ba", "group_name": "321", "group_description": "123"}
# r = requests.post('http://127.0.0.1:5000/api/group/update', data=data)

# get group info
# data = {"token": token, "session": session, "group_id": "80233c8073d511e69ce5fb907fee57ba", "detail": "1"}
# r = requests.post('http://127.0.0.1:5000/api/group/get', data=data)

# join group
# data = {"token": token, "session": session, "group_id": "80233c8073d511e69ce5fb907fee57ba", "members": "TEST_testAccount222"}
# r = requests.post('http://127.0.0.1:5000/api/group/join', data=data)

# remove member from group
# data = {"token": token, "session": session, "group_id": "80233c8073d511e69ce5fb907fee57ba", "members": "TEST_testAccount222"}
# r = requests.post('http://127.0.0.1:5000/api/group/remove', data=data)

# exit group
# data = {"token": token, "session": session, "group_id": "7b5ee230763c11e69c76a9e0fa8991a0"}
# r = requests.post('http://127.0.0.1:5000/api/group/exit', data=data)


print r.text