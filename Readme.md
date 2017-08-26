# HTTPImage

A Raspberry Pi program which displays images on an OLED display when POSTed to it via HTTP.

## Requirements

- A Raspberry Pi
- Python & pip
- An SSD1306-based, 128x64 OLED
- cURL and/or a modern browser
- Sketch (optional)

## Setting up

You'll need access to both `/dev/gpiomem` and `/dev/spidev0.{0,1}`.

First, you need to [enable SPI](https://www.raspberrypi.org/documentation/hardware/raspberrypi/spi/README.md#overview) in your Raspberry Pi's boot configuration.

Then, use `sudo usermod -aG spi,gpio $(whoami)` to give your user direct access. Then log out and back in.

Finally, clone this repo to your Pi, and run `pip install -r requirements.txt`

## Running

To run the server, from your Pi, run `python httpoled.py`! The server will be running on port 8080.

## Sending Images

Images can be sent either as the request body, or as the `image` parameter.

To send an image from the command line, you can use cURL:

```shell
curl -v --data-binary "@/path/to/image.png" http://<your-raspberry-pi>:8080/
```

### Sketch Mirror integration

A script is included which integrates httpoled with Sketch Mirror.

Start Sketch Mirror with a 128x64 artboard. Replace `<your-raspberry-pi>` with your Raspberry Pi's address, and paste the script into your developer console.

The script will then transmit updates to the Pi directly!
