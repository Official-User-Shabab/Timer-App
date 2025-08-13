# Ming's Timer

Ming's Timer is a desktop timer application allowing users to set a custom countdown timer and provides an audio alert when the time is up. Coded on Linux.

## Features

  * **Customisable Timer**: Set a timer for hours, minutes, and seconds using dropdown menus.
  * **Start/Restart, Stop, and Resume Controls**: Easily manage the timer's state with dedicated buttons.
  * **Always-on-Top Window**: The timer window stays visible on top of other applications, so you can always keep an eye on it.
  * **Alarm Sound**: A sound alert plays when the timer reaches zero.
  * **Simple and Clean UI**: A minimalist interface with a black and red colour scheme for easy readability (and coolness).

## How to Run

### Prerequisites

You'll need to install the following libraries:

```bash
pip install pygame
```

### Running the Script

1.  Download the `timer.py` file and a sound file named `alarm.wav` to the same directory.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved the files.
4.  Run the script using the following command:

<!-- end list -->

```bash
python timer.py
```

The timer application window will appear.

## How to Build an Executable

To create a standalone executable file (e.g., `.exe` for Windows), you can use `PyInstaller`. This is useful if you want to run the application without installing Python or the required libraries.

### Steps

1.  Install `PyInstaller`:

    ```bash
    pip install pyinstaller
    ```

2.  Navigate to the directory containing `timer.py` and `alarm.wav`.

3.  Run the following command in your terminal:

    ```bash
    pyinstaller --noconsole --onefile --add-data "alarm.wav;." timer.py
    ```

      * `--noconsole`: Prevents a command-line window from appearing.
      * `--onefile`: Packages the application into a single executable file.
      * `--add-data "alarm.wav;.":` Includes the `alarm.wav` file in the executable. The format `source;destination` is for Windows. If you are on macOS or Linux, use `--add-data "alarm.wav:."` instead.

4.  After the command finishes, you will find the executable file in the `dist` folder.
