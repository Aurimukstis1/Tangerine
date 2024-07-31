# TANGERINE
The simple pygame-based loading screen applet.

This is supposed to be fully modifiable.
- Changeable screen and height in pixels;
- Changeable rotational speed and size coefficients;
- Changeable colors;

The loading bar code is also highly changeable, allowing for dynamic linking between another app for loading percentage.

*What was originally a screw-up in learning python rendering, has been turned into an interesting looking icon.*

# WORK-IN-PROGRESS TRANSITION

### Example code
```
import tangerine
import time

def main():

  # now optionally you can change some values:
  # custom_screen_width :        default = 360,
  # custom_screen_height :       default = 480,
  # rotation_speed_coefficient : default = 0.2,
  # cube_size :                  default = 100.0,
  # cube_size_coefficient :      default = 1.0

  tangerine.start_loading_applet()

  time.sleep(1)

  tangerine.stop_loading_applet()

if __name__ == "__main__":
  main()
```

