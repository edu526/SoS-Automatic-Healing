from ppadb.client import Client as AdbClient
client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("emulator-5554")

def takeScreenshot():
    result = device.screencap()

    with open("images/screen.png", "wb") as fp:
        fp.write(result)

def tap(x, y):
    device.shell(f'input touchscreen tap {y} {x}')

def swipe(x, y):
    device.shell(f'input touchscreen swipe {y} {x} {y} {x} 250')

def text(text):
    device.shell(f'input text {text}')