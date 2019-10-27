from f_auth_register import auth_register
from f_auth_login import auth_login
from f_auth_logout import auth_logout
from f_auth_passwordreset_request import auth_passwordreset_request
from f_auth_passwordreset_reset import auth_passwordreset_reset
from f_channel_addowner import channel_addowner
from f_channel_details import channel_details
from f_channel_invite import channel_invite
from f_channel_join import channel_join
from f_channel_leave import channel_leave
from f_channel_messages import channel_messages
from f_channel_removeowner import channel_removeowner
from f_channels_create import channels_create
from f_channels_list import channels_list
from f_channels_listall import channels_listall
from f_message_edit import message_edit
from f_message_pin import message_pin
from f_message_react import message_react
from f_message_remove import message_remove
from f_message_send import message_send
from f_message_sendlater import message_sendlater
from f_message_unpin import message_unpin
from f_message_unreact import message_unreact
from f_search import search
from f_user_profile import user_profile
from f_user_profile_setemail import user_profile_setemail
from f_user_profile_sethandle import user_profile_sethandle
from f_user_profile_setname import user_profile_setname
from f_admin_user_permission_change import admin_user_permission_change


from flask import Flask, request
import json
from json_clean import jsonClean

APP = Flask(__name__)

APP.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='snackathon123@gmail.com',
    MAIL_PASSWORD="Where'smyHSP"
)

@APP.route('/auth/register', methods=["POST"])
def wrap_auth_register():
    auth_register(request.form.get('email'), request.form.get('password'), request.form.get('name_first'), request.form.get('name_last'))
    jsonClean()
    return json.dumps({})

@APP.route('/auth/login', methods=['POST'])
def wrap_auth_login():
    auth_login(request.form.get('email'), request.form.get('password'))
    jsonClean()
    return json.dumps({})

@APP.route('/auth/logout', methods=['POST'])
def wrap_auth_logout():
    auth_logout(request.form.get('token'))
    jsonClean()
    return json.dumps({})

@APP.route('/auth/passwordreset/request', methods=['POST'])
def wrap_auth_passwordreset_request():
    auth_passwordreset_request(request.form.get('email'))
    jsonClean()
    return json.dumps({})

@APP.route('/auth/passwordreset/reset', methods=['POST'])
def wrap_auth_passwordreset_reset():
    auth_passwordreset_reset(request.form.get('reset_code'), request.form.get('new_password'))
    jsonClean()
    return json.dumps({})

@APP.route('/channel/addowner', methods=['POST'])
def wrap_channel_addowner():
    channel_addowner(request.form.get('token'), request.form.get('channel_id'), request.form.get('u_id'))
    jsonClean()
    return json.dumps({})

@APP.route('/channel/details', methods=['GET'])
def wrap_channel_details():
    channel_details(request.args.get('token'), request.args.get('channel_id'))
    jsonClean()
    return json.dumps({})

@APP.route('/channel/invite', methods=['POST'])
def wrap_channel_invite():
    channel_invite(request.form.get('token'), request.form.get('channel_id'), request.form.get('u_id'))
    jsonClean()
    return json.dumps({})
    
@APP.route('/channel/join', methods=['POST'])
def wrap_channel_join():
    channel_join(request.form.get('token'), request.form.get('channel_id'))
    jsonClean()
    return json.dumps({})
    
@APP.route('/channel/leave', methods=['POST'])
def wrap_channel_leave():
    channel_leave(request.form.get('token'), request.form.get('channel_id'))
    jsonClean()
    return json.dumps({})

@APP.route('/channel/messages', methods=['GET'])
def wrap_channel_messages():
    channel_messages(request.args.get('token'), request.args.get('channel_id'), request.args.get('start'))
    jsonClean()
    return json.dumps({})

@APP.route('/channel/removeowner', methods=['POST'])
def wrap_channel_removeowner():
    channel_removeowner(request.form.get('token'), request.form.get('channel_id'), request.form.get('u_id')) 
    jsonClean()
    return json.dumps({})

@APP.route('/channel/create', methods=['POST'])
def wrap_channels_create():
    channels_create(request.form.get('token'), request.form.get('name'), request.form.get('is_public'))
    jsonClean()
    return json.dumps({})

@APP.route('/channel/list', methods=['GET'])
def wrap_channels_list():
    channels_list(request.args.get('token'))
    jsonClean()
    return json.dumps({})

@APP.route('/channel/listall', methods=['GET'])
def wrap_channels_listall():
    channels_listall(request.args.get('token'))
    jsonClean()
    return json.dumps({})
    
@APP.route('/message/edit', methods=['PUT'])
def wrap_message_edit():
    message_edit(request.form.get('token'), request.form.get('message_id'), request.form.get('message'))
    jsonClean()
    return json.dumps({})
    
@APP.route('/message/pin', methods=['POST'])
def wrap_message_pin():
    message_pin(request.form.get('token'), request.form.get('message_id'))
    jsonClean()
    return json.dumps({})
    
@APP.route('/message/react', methods=['POST'])
def wrap_message_react():
    message_react(request.form.get('token'), request.form.get('message_id'), request.form.get('react_id'))
    jsonClean()
    return json.dumps({})
 
@APP.route('/message/remove', methods=['DELETE'])
def wrap_message_remove():
    message_remove(request.form.get('token'), request.form.get('message_id'))
    jsonClean()
    return json.dumps({})

@APP.route('/message/send', methods=['POST'])
def wrap_message_send():
    message_send(request.form.get('token'), request.form.get('channel_id'), request.form.get('message'))
    jsonClean()
    return json.dumps({})
    
@APP.route('/message/sendlater', methods=['POST'])
def wrap_message_sendlater():
    message_sendlater(request.form.get('token'),request.form.get('channel_id'), request.form.get('message'), request.form.get('time_sent'))
    jsonClean()
    return json.dumps({})

@APP.route('/message/unpin', methods=['POST'])
def wrap_message_unpin():
    message_unpin(request.form.get('token'), request.form.get('message_id'))
    jsonClean()
    return json.dumps({})
    
@APP.route('/message/unreact', methods=['POST'])
def wrap_message_unreact():
    message_unreact(request.form.get('token'), request.form.get('message_id'), request.form.get('react_id'))
    jsonClean()
    return json.dumps({})

@APP.route('/search', methods=['GET'])
def wrap_search():
    search(request.args.get('token'), request.args.get('query_str'))
    jsonClean()
    return json.dumps({})

@APP.route('/user/profile', methods=['GET'])
def wrap_user_profile():
    user_profile(request.args.get('token'), request.args.get('u_id'))
    jsonClean()
    return json.dumps({})

@APP.route('/user/profile/setemail', methods=['PUT'])
def wrap_user_profile_setemail():
    user_profile_setemail(request.form.get('token'), request.form.get('email'))
    jsonClean()
    return json.dumps({})

@APP.route('/user/profile/sethandle', methods=['PUT'])
def wrap_user_profile_sethandle():
    user_profile_sethandle(request.form.get('token'),request.form.get('handle_str'))
    jsonClean()
    return json.dumps({})

@APP.route('/user/profile/setname', methods=['PUT'])
def wrap_user_profile_setname():
    user_profile_setname(request.form.get('token'), request.form.get('name_first'), request.form.get('name_last'))
    jsonClean()
    return json.dumps({})

@APP.route('/admin/userpermission/change', methods=['POST'])
def wrap_admin_userpermission_change():
    admin_user_permission_change(request.form.get('token'), request.form.get('u_id'), request.form.get('permission_id'))
    jsonClean()
    return json.dumps({})

@APP.route('/names', methods=['GET'])
def getnames():
    return sendSuccess(data)
        
if __name__=='__main__':
    APP.run(port=7878)