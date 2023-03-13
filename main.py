import tkinter
import customtkinter
from tkinter import ttk
from pytube import YouTube






def download():
    try:
        youtubeLink = link.get()
        youtubeObject = YouTube(youtubeLink, on_progress_callback=on_progress)
        video = youtubeObject.streams.get_highest_resolution()
        title = youtubeObject.title
        progress_bar.start()
        video.download()
        progress_bar.stop()
    except Exception as e:
        message.configure(text=f"Error :{e}", bg_color="red" )
        return None
        
    message.configure(text=f"{title} Download Completed", bg_color="green")
    

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress = round((bytes_downloaded / total_size) * 100, 2)
    progress_percentage.configure(text=str(progress) + "%")
    progress_percentage.update()
    print(progress)
    progress_bar.set(progress)

# System settings

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")



# App frame

app =  customtkinter.CTk()
app.geometry("500x500")
app.title("YouTube Downloader")


# Adding UI elements
title = customtkinter.CTkLabel(app, text="Insert YouTube link below")
title.pack(padx=10, pady=10)



# Link input 
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Progress percentage
progress_percentage = customtkinter.CTkLabel(app, text="0%")
progress_percentage.pack(padx=10, pady=10)


# Message 
message = customtkinter.CTkLabel(app, text="")
message.pack()

# Download button
download = customtkinter.CTkButton(app, text="Download", command=download)
download.pack(padx=10, pady=10)

# Progress bar


progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)
# Run app

app.mainloop()