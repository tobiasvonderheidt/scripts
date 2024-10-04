# Imports
import subprocess
import os


# Function to update rclone
def update():
    # rclone can update itself since v1.55
    print('Looking for updates...')

    command = ['./rclone', 'selfupdate']

    subprocess.run(command) # No try-except when calling rclone:
                            # Prints out success/error message by itself, exit code 0 doesn't distinguish update or no update

    # Delete old executable after update (Windows only)
    if (os.name == 'nt'):
        try:
            os.remove('./rclone.old.exe')
            print('Old executable was removed after the update.\n')
        except FileNotFoundError:
            print('There was no old executable to remove.\n')


# Function to back up data to OneDrive
def backup():
    # Configure rclone commands
    print('Choose commands to execute (y/n):')

    # sync
    while (True):
        sync = input('- Sync? ').strip().lower()

        if (sync == 'y' or sync == 'n'):
            break
        else:
            print('Please answer with (y/n).')

    # cryptcheck
    while (True):
        cryptcheck = input('- Cryptcheck? ').strip().lower()

        if (cryptcheck == 'y' or cryptcheck == 'n'):
            break
        else:
            print('Please answer with (y/n).')

    print('')   # Empty line to format output

    # Execute sync
    if (sync == 'y'):
        command = ['./rclone', 'sync', 'data:', 'OneDrive:',    # Command
                   '--config', './rclone.conf',                 # Flags
                   '--create-empty-src-dirs',
                   '--no-update-dir-modtime',
                   '--modify-window', '1s',
                   '--filter-from', './filters.md',
                   '--log-file', './rclone.log',
                   '--verbose']

        print('Sync started...')
        subprocess.run(command)
        print('Sync finished!\n')

    # Execute cryptcheck
    if (cryptcheck == 'y'):
        command = ['./rclone', 'cryptcheck', 'data:', 'OneDrive:',
                   '--config', './rclone.conf',
                   '--filter-from', './filters.md',
                   '--log-file', './rclone.log',
                   '--verbose']

        print('Cryptcheck started...')
        subprocess.run(command)
        print('Cryptcheck finished!\n')

    # Reminder to check logs
    print('Check the logs to see if there were any errors.\n')


# Execute the functions when script is called directly
if (__name__ == '__main__'):
    # Opening message
    print('Python script to back up data to OneDrive via rclone.\n')

    # Update rclone
    update()

    # Back up data
    backup()

    # Don't close window immediately when script finishes
    input('Press enter to exit!')
