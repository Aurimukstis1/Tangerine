# TANGERINE
The simple pygame-based loading screen applet.

This is highly modifiable.
- Changeable screen and height in pixels;
- Changeable rotational speed and size coefficients;
- Changeable colors; *<-- not implemented yet*

The loading bar code is also a variable, so it is possible to link that to some loading percentage.

### To install:
```
git clone https://github.com/Aurimukstis1/Tangerine.git
cd Tangerine
pip install .
```
**If on Linux and it recommends to use pacman instead:**
```
git clone https://github.com/Aurimukstis1/Tangerine.git
cd Tangerine
pip install . --break-system-packages
```

*What was originally a screw-up in learning python rendering, has been turned into an interesting looking icon.*

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

