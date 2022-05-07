import PySimpleGUI as sg
import subprocess


start = [[sg.Button("Cancel"), sg.Button("Start")]]

# Input Ouput Sections

io = [
    [
        sg.Text("python_inference.py location", size=(20, 1)),
        sg.Input(size=(25, 1), key="-SCRIPT-"),
        sg.FileBrowse(),
    ],
    [
        sg.Text("Folder or Video Path", size=(20, 1)),
        sg.Input(size=(25, 1), key="-INPUT-"),
        sg.FolderBrowse(),
    ],
    [  # Output Path
        sg.Text("Output Path", size=(20, 1)),
        sg.Input(size=(25, 1), key="-OUTPUT-"),
        sg.FolderBrowse(),
    ],
]

model = [
    [  # Model Choosing
        sg.Text("Choose model name", size=(20, 1)),
        sg.Listbox(
            values=[
                "realesrgan-x4plus",
                "realesrnet-x4plus",
                "realesrgan-x4plus-anime",
                "realesr-animevideov3",
            ],
            default_values="realesrgan-x4plus",
            select_mode="LISTBOX_SELECT_MODE_SINGLE",
            size=(25, 5),
            key="-MODEL-",
        ),
    ],
]

general_settings = [
    [  # Tail Size
        sg.Text("Suffix for the output file", size=(20, 1)),
        sg.Input(size=(10, 1), key="-SUFFIX-"),
    ],
    [  # Tail Size
        sg.Text("Choose the tail-size", size=(20, 1)),
        sg.Input(size=(10, 1), key="-TAIL-"),
    ],
    [
        # Outscale Factor
        sg.Text("Choose the scale factor", size=(20, 1)),
        sg.Input(
            size=(10, 15),
            default_text="4.0",
            key="-SCALE-",
        ),
    ],
]


gpu = [
    [sg.Text("Choose the GPU", size=(20, 1))],
    [
        sg.Combo(
            [
                "GPU:0",
                "GPU:1",
                "GPU:2",
                "GPU:3",
            ],
            default_value="GPU:0",
            size=(10, 1),
            key="-GPU-",
        ),
    ],
]


layout = [
    [sg.Column(io, justification="left")],
    [sg.Column(model, justification="left")],
    [
        sg.Column(general_settings, justification="left"),
        sg.Column(gpu, justification="right"),
    ],
    # [sg.Column(gpu, justification="left")],
    [sg.Column(start, justification="right")],
]


# Create the window
window = sg.Window("Cobanov Upscaler", layout)  # Part 3 - Window Defintion

# Display and interact with the Window
event, values = window.read()  # Part 4 - Event loop or Window.read call

# command = f'python {values["-SCRIPT-"]} -i {values["-INPUT-"]} -o {values["-OUTPUT-"]} -n {values["-MODEL-"][0]} -s {values["-SCALE-"]} -t {values["-TAIL-"]} -g {values["-GPU-"]} --suffix {values["-SUFFIX-"]}'
# print(command)

subprocess.run(
    [
        "python",
        values["-SCRIPT-"],
        "-i",
        values["-INPUT-"],
        "-o",
        values["-OUTPUT-"],
        "-n",
        values["-MODEL-"][0],
        "-s",
        values["-SCALE-"],
        "-t",
        values["-TAIL-"],
        "-g",
        values["-GPU-"],
        "--suffix",
        values["-SUFFIX-"],
    ]
)
window.close()
