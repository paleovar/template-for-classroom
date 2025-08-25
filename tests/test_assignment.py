# tests/test_assignment.py
import subprocess

def test_output():
    result = subprocess.run(["python", "check.py"], capture_output=True, text=True)
    output = result.stdout.strip()
    assert output == "Hello, world!"   # expected output
