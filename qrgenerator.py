import os
import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode

def generate_qr():
	data = text_entry.get().strip()
	filename = filename_entry.get().strip()
