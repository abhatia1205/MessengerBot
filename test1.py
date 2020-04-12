import test_utils as tu
import src.python.main.core as core
from flask import Flask, request

app = Flask(__name__)

def run():
    db = tu.connectToTestDB()
    ref = core.get_reference(db, "robotics")
    return ref

if __name__ == "__main__":
    app.run(host='1.0.0.0', port=7280)
