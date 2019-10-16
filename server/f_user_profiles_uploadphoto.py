# Function name: user_profiles_uploadphoto()
# Parameters: (token, img_url, x_start, y_start, x_end, y_end)
# Return type: {}
# Exception: ValueError when:
# - img_url is returns an HTTP status other than 200.
# - x_start, y_start, x_end, y_end are all within the dimensions of the image at the URL.
# Description: Given a URL of an image on the internet, crops the image within bounds 
# (x_start, y_start) and (x_end, y_end). Position (0,0) is the top left.
#

def user_profiles_uploadphoto(token, img_url, x_start, y_start, x_end, y_end):
    
    user_profile_uploadphoto_dict = {}
    
    return user_profile_uploadphoto_dict