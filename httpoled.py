import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import pdb

from io import BytesIO
from klein import run, route
from PIL import Image

# 128x64 display with hardware SPI
screen = Adafruit_SSD1306.SSD1306_128_64(rst=24, dc=23, spi=SPI.SpiDev(0, 0, max_speed_hz=8000000))
screen.begin()

screen.clear()
screen.display()

def corsify(request):
  request.setHeader('Access-Control-Allow-Origin', '*')
  request.setHeader('Access-Control-Allow-Methods', 'POST')

@route('/', methods=['POST'])
def upload(request):
  corsify(request)

  image_post = request.args.get('image')

  # Support both `curl --data-binary "@image.png" localhost:8080`,
  # or JS FormData with "image" field as blob data
  image = Image.open(BytesIO(image_post[0])) if image_post else Image.open(request.content)

  # pdb.set_trace()

  screen.image(image.resize((screen.width, screen.height), Image.ANTIALIAS).convert('1', dither=Image.NONE))
  screen.display()

  return 'done - look over there!'

@route('/', methods=['OPTIONS'])
def preflight(request):
  corsify(request)

run("0.0.0.0", 8080)
