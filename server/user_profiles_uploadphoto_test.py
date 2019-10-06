# Function: user_profiles_uploadphoto()
# Parameters: (token, img_url, x_start, y_start, x_end, y_end)
# Output: {}
# Exception: ValueError when:
# - img_url is returns an HTTP status other than 200.
# - x_start, y_start, x_end, y_end are all within the dimensions of the image at the URL.
# Description: Given a URL of an image on the internet, crops the image within bounds (x_start, y_start) 
# and (x_end, y_end). Position (0,0) is the top left.
#

import pytest
import requests
from f_user_profiles_uploadphoto import user_profiles_uploadphoto
from f_auth_register import auth_register
from f_auth_logout import auth_logout
from PIL import Image
from io import BytesIO


def user_profiles_uploadphoto_test():
    validAuthRegisterDic = auth_register("richard123@gmail.com", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']

    # Bad picture
    response1 = requests.get('img_url1') 
    im1 = Image.open(BytesIO(response1.content))
    x_start1 = 0
    y_start1 = 0
    x_end, y_end1, _ = im1.shape
    # Good picture but dimensions not correct
    response2 = requests.get('img_url2')
    im2 = Image.open(BytesIO(response2.content))
    x_start2 = 0
    y_start2 = 0
    x_end2, y_end2, _ = im2.shape


    # Testing successful run 
    assert user_profiles_uploadphoto(token, img_url, x_start, y_start, x_end, y_end) == {}

    with pytest.raises(ValueError):
        # img_url returns an HTTP status other than 200
        user_profiles_uploadphoto(token, response1.status_code, x_start1, y_start1, x_end1, y_end1)
        # x_start, y_start, x_end, y_end are all within the dimensions of the image at the URL
        user_profiles_uploadphoto(token, response2.status_code, x_start2, y_start2, x_end2, y_end2)
