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
import TANGERINE
import time

def main():
  TANGERINE.start_loading_applet()

  time.sleep(1)

  TANGERINE.stop_loading_applet()

if __name__ == "__main__":
  main()
```

