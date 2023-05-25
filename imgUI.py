import tkinter as tk
from tkinter import filedialog
import moviepy.editor as mp
import os
import imageio
from threading import Thread

def capture_screenshots():
    # Get the input values from the UI
    video_path = video_path_entry.get()
    output_directory = output_directory_entry.get()
    interval = int(interval_entry.get())

    # Load the video file
    video = mp.VideoFileClip(video_path)

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Calculate the time interval in seconds
    time_interval = interval
    count = 1
    # Iterate over the video frames
    for t in range(0, int(video.duration), time_interval):
        # Get the frame at the specified time
        frame = video.get_frame(t)
        counter.config(text = "Images:"+str(count))
        count += 1
        # Generate the output file path
        output_file = os.path.join(output_directory, f"screenshot_{t}.jpg")

        # Save the screenshot using imageio
        imageio.imwrite(output_file, frame)

    print(f"Screenshots captured")

def browse_video_path():
    path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")])
    video_path_entry.delete(0, tk.END)
    video_path_entry.insert(tk.END, path)

def browse_output_directory():
    path = filedialog.askdirectory()
    output_directory_entry.delete(0, tk.END)
    output_directory_entry.insert(tk.END, path)

def start_main():
    t = Thread(target=capture_screenshots, daemon=True)
    t.start()

def callback(input):
    if input.isdigit():
        return True
                        
    elif input is "":
        return True

    else:
        return False
    
window = tk.Tk()
window.geometry("650x500")

small_icon = tk.PhotoImage(file="img100.png")
large_icon = tk.PhotoImage(file="IMG_64.png")
window.iconphoto(True, large_icon, small_icon)

window.title('VideoFrameSlicer')
# Create and place the labels and entry fields

left = tk.Frame(master=window, width=325, height=500, bg="#111418")
left.grid(row=0, column=0, sticky="nsew")
left.pack_propagate(False)

L1 = tk.Frame(master=left, width=325, height=350, bg="#111418")
L1.grid(row=0, column=0, sticky="nsew")
L1.pack_propagate(False)

L2 = tk.Frame(master=left, width=325, height=150, bg="#111418")
L2.grid(row=1, column=0, sticky="nsew")
L2.pack_propagate(False)

left.grid_rowconfigure(0, weight=2, minsize=50)
left.grid_rowconfigure(1, weight=1, minsize=50)
left.grid_columnconfigure(0, weight=1, minsize=50)

right = tk.Frame(master=window, width=325, height=625, bg="#191E24")
right.grid(row=0, column=1, sticky="nsew")
right.pack_propagate(False)

window.grid_rowconfigure(0, weight=1, minsize=50)
window.grid_columnconfigure(0, weight=1, minsize=50)
window.grid_columnconfigure(1, weight=1, minsize=50)

# -------- VIDEO PATH --------
video_path = tk.Frame(master=L1, bg="#111418")
video_path.grid(row=0, column=0, sticky="nsew")
video_path.pack_propagate(False)

video_path_label = tk.Label(master=video_path, text="Select Video", bg="#111418", fg="white", font=('Helvetica', 12))
video_path_label.grid(row=0, column=0, sticky="nsew")

video_input = tk.Frame(master=video_path, bg="#111418", height=8)
video_input.grid(row=1, column=0, sticky="ew", padx=50)
video_input.pack_propagate(False)

video_path_entry = tk.Entry(master=video_input, bg="#212830", bd=0, fg="white")
video_path_entry.grid(row=0, column=0, sticky="ew", ipady=5)

browse_video_button = tk.Button(master=video_input, text="Browse", relief="flat", bg="#0d8f53", command=browse_video_path)
browse_video_button.grid(row=0, column=1, sticky="ew")

video_path.grid_rowconfigure(0, weight=1, minsize=50)
video_path.grid_rowconfigure(1, weight=1, minsize=10)
video_path.grid_columnconfigure(0, weight=1, minsize=50)

video_input.grid_rowconfigure(0, weight=1, minsize=50)
video_input.grid_columnconfigure(0, weight=4, minsize=50)
video_input.grid_columnconfigure(1, weight=1, minsize=50)

# -------- OUTPUT DIRECTORY --------
output_directory = tk.Frame(master=L1, width=100, bg="#111418")
output_directory.grid(row=1, column=0, sticky="nsew")
output_directory.pack_propagate(False)

output_directory_label = tk.Label(master=output_directory, text="Output Directory:", bg="#111418", fg="white", font=('Helvetica', 12))
output_directory_label.grid(row=0, column=0)

output_input = tk.Frame(master=output_directory, width=400, bg="#111418")
output_input.grid(row=1, column=0, sticky="nsew", padx=50)
output_input.pack_propagate(False)

output_directory_entry = tk.Entry(master=output_input, bg="#212830", bd=0, fg="white")
output_directory_entry.grid(row=0, column=0, sticky="ew", ipady=5)

browse_output_directory_button = tk.Button(master=output_input, text="Browse", relief="flat", bg="#0d8f53", command=browse_output_directory)
browse_output_directory_button.grid(row=0, column=1, sticky="ew")

output_directory.grid_rowconfigure(0, weight=1, minsize=50)
output_directory.grid_rowconfigure(1, weight=1, minsize=50)
output_directory.grid_columnconfigure(0, weight=1, minsize=50)

output_input.grid_rowconfigure(0, weight=1, minsize=50)
output_input.grid_columnconfigure(0, weight=4, minsize=50)
output_input.grid_columnconfigure(1, weight=1, minsize=50)

# -------- INTERVAL --------
interval = tk.Frame(master=L1, width=100, bg="#111418")
interval.grid(row=2, column=0, sticky="nsew")
interval.pack_propagate(False)

interval_label = tk.Label(master=interval, text="Interval (seconds):", bg="#111418", fg="white", font=('Helvetica', 12))
interval_label.grid(row=0, column=0, sticky="nsew")

interval_input = tk.Frame(master=interval, width=400, bg="#111418")
interval_input.grid(row=1, column=0, sticky="ew", padx=50)
interval_input.pack_propagate(False)
reg=window.register(callback)
interval_entry = tk.Entry(master=interval_input, validate='all', validatecommand=(reg, '%P'))
interval_entry.grid(row=0, column=0, sticky="ew")

interval.grid_rowconfigure(0, weight=1, minsize=50)
interval.grid_rowconfigure(1, weight=1, minsize=50)
interval.grid_columnconfigure(0, weight=1, minsize=50)

interval_input.grid_rowconfigure(0, weight=1, minsize=50)
interval_input.grid_columnconfigure(0, weight=1, minsize=50)

# -------- ACTIVATION --------
activate = tk.Frame(master=L2, width=100, bg="#111418")
activate.pack(fill=tk.BOTH, expand=True)
activate.pack_propagate(False)
capture_button = tk.Button(master=activate, text="Capture Screenshots", command=start_main)
capture_button.pack()
counter = tk.Label(master=activate, text="Images:", bg="#111418", fg="#0d8f53", font=('Helvetica', 12))
counter.pack()
# Start the Tkinter event loop

L1.grid_rowconfigure(0, weight=1, minsize=50)
L1.grid_rowconfigure(1, weight=1, minsize=50)
L1.grid_rowconfigure(2, weight=1, minsize=50)
L1.grid_columnconfigure(0, weight=1, minsize=50)

L2.grid_rowconfigure(0, weight=1, minsize=50)
L2.grid_columnconfigure(0, weight=1, minsize=50)

window.mainloop()
