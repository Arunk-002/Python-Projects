from plyer import notification

# this is a basic notification script that displays a message whith an icon
notification.notify(
    title="did you know?",
    message="The Sulabh International Museum Of Toilets in New Delhi features the historic evolution of toilets from "
            "2500 BC to today.",

    app_icon="D:\\Finished Projects\\Python projects\\Python_projects\\assets\\icon.ico",
    # should specify the path directly in windows

    timeout=7
    # exits the program after 7 seconds
)
# note:the maximum words should not exceed 256 including the path as well

