#actor演员的意思
import tkinter
import time
import config

class Actor(object):
    """所有移动着的基本类"""
    def __init__(self, root, canvas, position, x, y, tags, w, h, play):
        '''
        :param root:
        :param canvas:
        :param position:
        :param x:
        :param y:
        :param tags:
        :param w:
        :param h:
        :param play:是否播放死亡动画
        '''
    #获取左上角的值
    def get_anchor_nw_position(self):
        pass

    # 获取右上角的值
    def get_anchor_ne_position(self):
        pass

    # 获取左下角的坐标值
    def get_anchor_sw_position(self):
        pass

    # 获取右下角的坐标值
    def get_anchor_se_position(self):
        pass

    # 获取中心坐标值
    def get_anchor_center_position(self):
        pass

    # 设置画布上图片
    def set_canvas_image(self, cimg):
        pass

    # 获取画布上图片
    def get_canvas_image(self):
        pass

    # 删除画布上图片
    def del_canvas_image(self):
        pass

    # 指定对象的移动
    def base_move(self, tags, x, y):
        self.canvas.move(tags, x, y)
        self.update_positions(x, y)

    # 更新坐标值
    def update_postion(self):
        pass

    # 设置生命值
