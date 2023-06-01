#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 11:46:00 2023

@author: jjf3
"""

import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
import fitz

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        label.config(text="Selected File: " + file_path)
        display_pdf(file_path)

    else:
        label.config(text="No file selected.")
        
def display_pdf(file_path):
    pdf_text.delete(1.0, tk.END)  # Clear the text widget
    try:
        doc = fitz.open(file_path)
        num_pages = doc.page_count
        for page_num in range(num_pages):
           page = doc.load_page(page_num)
           text = page.get_text("text")
           pdf_text.insert(tk.END, text)
           pdf_text.insert(tk.END, "\n\n")
        doc.close()
    except:
       pdf_text.insert(tk.END, "Error: Failed to read PDF file.")


# Create the main window
window = tk.Tk()

# Set an empty string as the window title
window.title("jjf3's PDF VIewer")

# Create a label for the instructions
instructions_text = "Please select a PDF file to import."
instructions_label = tk.Label(window, text=instructions_text)
instructions_label.pack()

# Create a label to display the selected file path
label = tk.Label(window, text="No file selected.")
label.pack()

# Create a browse button
browse_button = tk.Button(window, text="Browse", command=browse_file)
browse_button.pack()

# Create a scrolled text widget to display the PDF content
pdf_text = scrolledtext.ScrolledText(window, wrap=tk.WORD)
pdf_text.pack()

# Start the Tkinter event loop
window.mainloop()