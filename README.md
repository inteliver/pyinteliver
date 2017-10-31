PyInteliver
===================
![alt text](https://res.inteliver.com/media/v1/amir/i_h_200,i_w_200,i_o_resize_keep/i_h_150,i_w_150,i_o_crop/000262302243490000000000000000000842.jpg "Logo Title Text 1")

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
