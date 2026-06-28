"""Script to build programmatic_flashcards.py in parts."""
import os

path = r'D:\Prevcom\prevcom_app\programmatic_flashcards.py'

# Delete if exists
if os.path.exists(path):
    os.remove(path)

print("File removed, ready to build")
