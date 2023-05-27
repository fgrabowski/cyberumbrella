import board
import neopixel
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.color import JADE, BLUE, PINK

stripe_length = 34

pixels = neopixel.NeoPixel(board.GP28, stripe_length, brightness=0.5, auto_write=False)

blink = Blink(pixels, speed=0.5, color=JADE)
comet = Comet(pixels, speed=0.01, color=BLUE, tail_length=10, bounce=True)
chase = Chase(pixels, speed=0.2, size=8, spacing=3, color=PINK)
 

animation0 = AnimationSequence(comet, advance_interval=3, auto_clear=True)
animation1 = AnimationSequence(blink, advance_interval=3, auto_clear=True)
animation2 = AnimationSequence(chase, advance_interval=3, auto_clear=True)
while True:
    animation0.animate()
    animation1.animate()
    animation2.animate()
