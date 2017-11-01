from InteliverConfig import InteliverConfig


class InteliverRetrieve:
    def __init__(self, config=None):
        self.config = None
        self.base_url = 'https://res.inteliver.com/media/v1'
        if isinstance(config, InteliverConfig):
            self.config = config
        self.commands = []
        self.url = ''
        self.selectors_dic = {
            'height': 'i_h_',
            'width': 'i_w_',
            'center_x': 'i_c_x_',
            'center_y': 'i_c_y_',
        }
        self.operators = {
            'crop': 'i_o_crop',
            'round_crop': 'i_o_rcrop',
            'resize': 'i_o_resize',
            'resize_keep': 'i_o_resize_keep',
            'format': 'i_o_format_',
            'blur': 'i_o_blur_',
            'rotate': 'i_o_rotate_',
            'flip': 'i_o_flip_',
            'sharpen': 'i_o_sharpen',
            'pixelate': 'i_o_pixelate_',
            'gray': 'i_o_gray',
            'text': ',i_o_text_'
        }
        self.formats = {
            'JPEG': 'jpg',
            'PNG': 'png'
        }
        self.flips = {
            'horizontal': 'h',
            'vertical': 'v',
            'both': 'b'
        }

    def select(self, selector, value):
        if selector in self.selectors_dic:
            self.commands.append('{}{}'.format(self.selectors_dic[selector], value))

    def select_face(self, specific_face=0):
        if specific_face:
            self.commands.append('{}_{}'.format('i_c_face', specific_face))
        else:
            self.commands.append('i_c_face')

    def image_crop(self, round_crop=False):
        if not round_crop:
            self.commands.append(self.operators['crop'])
        else:
            self.commands.append(self.operators['round_crop'])

    def image_resize(self, keep_ratio=True):
        if keep_ratio:
            self.commands.append(self.operators['resize_keep'])
        else:
            self.commands.append(self.operators['resize'])

    def image_change_format(self, required_format, value=None):
        if required_format in self.formats:
            if value:
                self.commands.append('{}{}_{}'
                                     .format(self.operators['format'],
                                             self.formats[required_format],
                                             value))
            else:
                self.commands.append('{}{}'
                                     .format(self.operators['format'],
                                             self.formats[required_format]))

    def image_blur(self, value=20):
        self.commands.append('{}{}'.format(self.operators['blur'], value))

    def image_rotate(self, rotate_degree, rotate_zoom=1):
        self.commands.append('{}{}_{}'.format(self.operators['rotate'], rotate_degree, rotate_zoom))

    def image_flip(self, horizontal=False, vertical=False):
        if horizontal and vertical:
            self.commands.append('{}{}'.format(self.selectors_dic['flip']), self.flips['both'])
        elif horizontal:
            self.commands.append('{}{}'.format(self.selectors_dic['flip']), self.flips['horizontal'])
        elif vertical:
            self.commands.append('{}{}'.format(self.selectors_dic['flip']), self.flips['vertical'])

    def image_sharpen(self):
        self.commands.append(self.operators['sharpen'])

    def image_pixelate(self, value=10):
        self.commands.append('{}{}'.format(self.operators['pixelate'], value))

    def image_gray_scale(self):
        self.commands.append(self.operators['gray'])

    def image_text_overlay(self):
        pass

    def build_url(self, resource_key):
        self.url = '{}/{}'.format(','.join(self.commands), resource_key)
        return '{}/{}/{}'.format(self.base_url, self.config.get_cloudname(), self.url)

    def clear_steps(self):
        self.url = ''
        self.commands = []

