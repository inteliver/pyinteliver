PyInteliver
===================
![alt text](https://res.inteliver.com/media/v1/amir/i_h_200,i_w_200,i_o_resize_keep/i_h_150,i_w_150,i_o_crop/000262302243490000000000000000000842.jpg "Inteliver Logo")

This is python repository for [Inteliver](https://www.inteliver.com) API.
You can **upload**, set **configs** and **retrieve** your data with this repository in python language. 

----------


Installation
-------------

This python package is available at **PyPI**.
simply run the following command to be able to use our python API.

`pip install pyinteliver`

You can also pull our repository and use the API **without any requirements** to install. 

`git pull https://github.com/inteliver/pyinteliver.git`

----------
#### <i class="icon-cog"></i> Inteliver Configs
After registering in  [Inteliver](https://www.inteliver.com) you will have a **cloud-name** and **token**. This pair will be used to authenticate you for uploading data or using intelligent service. 
To set this in your code simply:
```python
from InteliverConfig import InteliverConfig
config = InteliverConfig(cloudname=your-cloudname, token=your-token)
```
----------
#### <i class="icon-upload"></i> Upload

To upload your data first set your **config** object.
Then use the following lines:
```python
from Uploader import Uploader
uploader = Uploader(config)
file_key = uploader.upload('logo.jpg')
```
If uploaded successfully you will receive a **json** file with following format.
`{'success': True, 'message': 'Successfully uploaded.', 'resource_key': key}`

`resource_key` is a unique key which able you to receive your data later. 
Hey! I'm your first Markdown document in **StackEdit**[^stackedit]. Don't delete me, I'm very helpful! I can be recovered anyway in the **Utils** tab of the <i class="icon-cog"></i> **Settings** dialog.

----------

#### <i class="icon-upload"></i> Retrieve Data
Using InteliverRetrieve class you can **build the URL** of the data you need to get from Inteliver.
Some of our on-the-fly features for manipulating images are as follow:
> - Resize
> - Blur
> - Crop
> - Rotate 
> - Flip
> - Sharpen
>- Change image format
>- Grayscale
>- Pixalate
>- Face focus

You can find out more at [Inteliver Docs](https://docs.inteliver.com).
To retrieve your data first set your **config** object.

```python
from InteliverConfig import InteliverConfig
config = InteliverConfig(cloudname=your-cloudname)
```
> **Note:**
> - Note that for retrieving data you only need your **cloudname** to be set.

After setting your config object, build an InteliverRetrieve object.
```python
from InteliverConfig import InteliverConfig
from InteliverRetrieve import InteliverRetrieve
rt = InteliverRetrieve(config)
```
All the manuplation are sequentional. for example lets say you want to **select the main face** in picture **resize** it to 200 and 200 and keep the original ratio and to **crop** the image in a rounded shape and change the **format** to png and build the url. 
let say your resource image is this one:

![alt text](https://res.inteliver.com/media/v1/amir/000220973186370000000000000000000071.jpg "original image")

```python
    rt.select_face()
    rt.select('height', 200)
    rt.select('width', 200)
    rt.image_crop(round_crop=True)
    rt.image_change_format('PNG')
    url_to_get = rt.build_url(your_resource_key)
```
This will build a url like this:
**res.inteliver.com/media/v1/yourcloudname/i_c_face,i_h_200,i_w_200,i_o_resize_keep,i_o_rcrop,i_o_format_png/resourcekey.jpg**

The image you receive after manipulation is : 

![alt text](https://res.inteliver.com/media/v1/amir/i_c_face,i_h_200,i_w_200,i_o_resize_keep,i_o_rcrop,i_o_format_png/000220973186370000000000000000000071.jpg "Manipulated image")
