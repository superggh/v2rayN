# -*- coding:utf-8 -*-
import pystray
from PIL import Image
from pystray import MenuItem

def on_exit():
    icon.stop()
menu = (MenuItem('菜单1', lambda: print("点击了菜单1")),     MenuItem(text='退出', action=on_exit))
image = Image.open("icon.png")
icon = pystray.Icon("name", image, "跨鲸浏览器", menu)
icon.run()