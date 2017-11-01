from Uploader import Uploader
from InteliverConfig import InteliverConfig
from InteliverRetrieve import InteliverRetrieve


def test_upload():
    token = ''
    cloudname = 'amir'

    config = InteliverConfig(cloudname=cloudname, token=token)
    up = Uploader(config)
    print up.upload('test_data/logo.jpg')


def test_retrieve():
    cloudname = 'amir'
    resource_key = '000220973186370000000000000000000071.jpg'
    config = InteliverConfig(cloudname=cloudname)
    rt = InteliverRetrieve(config)
    rt.select_face()
    rt.image_crop()

    rt.clear_steps()
    #i_c_face, i_h_200, i_w_200, i_o_crop, i_o_rcrop, i_o_format_png
    rt.select_face()
    rt.select('height', 200)
    rt.select('width', 150)
    rt.image_crop(round_crop=True)
    rt.image_change_format('PNG')
    # i_c_x_180,i_c_y_300,i_h_100,i_w_100,i_o_sharpen/i_c_face,i_o_sharpen
    rt.clear_steps()
    rt.select('center_x', 180)
    rt.select('center_y', 300)
    rt.select('height', 100)
    rt.select('width', 150)
    rt.image_sharpen()
    rt.select_face()
    rt.image_crop()

    print rt.build_url(resource_key)

#test_upload()
test_retrieve()