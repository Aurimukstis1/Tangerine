from .tangerine import tangerinemain
# The two main functions
def start_loading_applet(custom_screen_width:int=360,custom_screen_height:int=480,rotation_speed_coefficient:float=0.2,cube_size:float=100.0,cube_size_coefficient:float=1.0):
    tangerinemain.start(custom_screen_width,custom_screen_height,rotation_speed_coefficient,cube_size,cube_size_coefficient)

def stop_loading_applet():
    tangerinemain.stop()