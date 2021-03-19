import device
import hospital
import utils

device.takeScreenshot()
hospitalPositionX, hospitalPositionY = hospital.getPosition()

## heal amount of troops
troopsCount = 1

## delay for healing in seconds
waitForNextSession = 60

## fixed delay between tapping in seconds
waitForTap = 1.0

#randomizer for pixels
randomPixel = 0

while True:
 # tap on hospital
 device.tap(hospitalPositionX, hospitalPositionY);
 utils.randomWaitForTap(.5);

 # tap on quick select
 device.swipe(623,1359);
 utils.randomWaitForTap(.5);

 # tap on number of troops first row
 device.tap(361,889);
 utils.randomWaitForTap();

 # input number of troops to heal
 device.text(troopsCount);
 utils.randomWaitForTap(.5);

 # tap on ok
 device.tap(1539,850);
 utils.randomWaitForTap(.5);

 # tap on heal
 device.tap(828,1339);
 utils.randomWaitForTap(.5);

 # ask for help
 device.tap(hospitalPositionX, hospitalPositionY);
 utils.randomWaitForTap(15);