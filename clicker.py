import time
import pyautogui as gui

# We don't need to check if image is None here,
# since it'll get caught in the except block
def click(image):
  left, top, window, height = image
  gui.moveTo(left, top)
  gui.click()

retries = 0
while retries < 5:
  try:
    download_button = gui.locateOnScreen("assets/download-button.png", confidence=0.5)
    endorsement_reminder = gui.locateOnScreen("assets/endorsement-reminder.png", confidence=0.5)

    click(download_button)
    click(endorsement_reminder)
    retries = 0 # Reset retries after success
  except:
    # To simplify things, we don't care about not being able
    # to find images. We'll just retry after a second
    time.sleep(1)
    continue