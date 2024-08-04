from flask import Flask
import pyautogui

app = Flask(__name__)

@app.route("/<x>/<y>")
def tap(x, y):
    print(x,y)
    pyautogui.moveRel(int(x),int(y), duration=0)
    return ""



dimensions = pyautogui.size()
print(dimensions)


app.run(host="0.0.0.0", port="40")
