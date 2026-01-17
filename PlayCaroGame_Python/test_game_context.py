#!/usr/bin/env python3
"""
Test avatar loading in actual game context
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from shared.utils import get_asset_path
from shared.user import User
from PIL import Image, ImageTk
import tkinter as tk

def test_game_context():
    """Test avatar loading in game context"""
    print("Testing avatar loading in game context...")

    # Create root window
    root = tk.Tk()
    root.withdraw()  # Hide window

    # Simulate Client.user
    user = User(username="testuser", avatar="2")
    print(f"User avatar: '{user.get_avatar()}'")

    # Create avatar label like in game
    avatar_label = tk.Label(root, bg="white")
    avatar_images = []

    # Load avatar like in game
    try:
        avatar_id = user.get_avatar()
        print(f"Loading avatar_id: '{avatar_id}'")
        avatar_path = get_asset_path('avatar', f'{avatar_id}.jpg')
        print(f"Avatar path: {avatar_path}")

        if avatar_path and os.path.exists(avatar_path):
            print("File exists, loading image...")
            img = Image.open(avatar_path)
            img = img.resize((60, 60), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            # Keep reference BEFORE config
            avatar_images.append(photo)
            avatar_label.config(image=photo)
            print("Avatar loaded successfully")

            # Check if image is set
            has_image = avatar_label.cget('image') != ''
            print(f"Label has image: {has_image}")

            # Check label text (should be empty if image is set)
            label_text = avatar_label.cget('text')
            print(f"Label text: '{label_text}'")

        else:
            print(f"Avatar file not found: {avatar_path}")
            avatar_label.config(text="👤", font=("Arial", 24))

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

    root.destroy()

if __name__ == "__main__":
    test_game_context()