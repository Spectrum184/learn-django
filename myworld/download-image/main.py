from instagrapi import Client
import pathlib

ACCOUNT_USERNAME = ''
ACCOUNT_PASSWORD = ''
LINK_INSTAGRAM = 'https://www.instagram.com/p/'
FOLDER_DOWNLOAD = str(pathlib.Path(__file__).parent.resolve()) + '/image'

print(FOLDER_DOWNLOAD)

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

user_id = cl.user_id_from_username("")
medias = medias = cl.user_medias(user_id, 20)
array_media_id = []

print('Start------>')

for m in medias:
    code = LINK_INSTAGRAM + m.code + '/'
    media_pk = cl.media_pk_from_url(code)
    media_info = cl.media_info(media_pk).dict()
    
    if media_info["media_type"] == 1:
        cl.photo_download(media_pk, folder=FOLDER_DOWNLOAD)
    elif media_info["media_type"] == 2:
        cl.video_download(media_pk, folder=FOLDER_DOWNLOAD)
    elif media_info["media_type"] == 8:
        cl.album_download(media_pk, folder=FOLDER_DOWNLOAD)
    
print('End------>')