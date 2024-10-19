# Imports
import subprocess
import os


# Function to update rclone
def update():
    # rclone can update itself since v1.55
    print('Looking for updates...')

    command = ['rclone', 'selfupdate']

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

    # Configure rclone flags
    if (sync == 'y' or cryptcheck == 'y'):
        print('Choose optional flags (y/n):')

        # --log-level
        while (True):
            debug = input('- Debug? ').strip().lower()

            if (debug == 'y' or debug == 'n'):
                break
            else:
                print('Please answer with (y/n).')

        # --dry-run
        while (True):
            dryrun = input('- Dry run? ').strip().lower()

            if (dryrun == 'y' or dryrun == 'n'):
                break
            else:
                print('Please answer with (y/n).')

        print('')

    # Execute sync
    if (sync == 'y'):
        command = ['rclone', 'sync', 'data:', 'OneDrive:',  # Command
                   '--config', './rclone.conf',             # Flags
                   '--create-empty-src-dirs',
                   '--no-update-dir-modtime',
                   '--modify-window', '1s',
                   '--filter-from', './filters.md',
                   '--log-file', './rclone.log',
                   '--stats', '0']

        if (debug == 'y'):
            command += ['--log-level', 'DEBUG']
        else:
            command += ['--log-level', 'INFO']

        if (dryrun == 'y'):
            command += ['--dry-run']

        print('Sync started...')
        subprocess.run(command)
        print('Sync finished!\n')

    # Execute cryptcheck
    if (cryptcheck == 'y'):
        command = ['rclone', 'cryptcheck', 'data:', 'OneDrive:',
                   '--config', './rclone.conf',
                   '--filter-from', './filters.md',
                   '--log-file', './rclone.log',
                   '--stats', '0']

        if (debug == 'y'):
            command += ['--log-level', 'DEBUG']
        else:
            command += ['--log-level', 'INFO']

        if (dryrun == 'y'):
            command += ['--dry-run']

        print('Cryptcheck started...')
        subprocess.run(command)
        print('Cryptcheck finished!\n')

    # Reminder to check logs
    print('Check the logs to see if there were any errors.\n')


# Execute the functions when script is called directly
if (__name__ == '__main__'):
    # Opening message
    print('Python script to back up data to OneDrive via rclone.\n')

    # Update rclone only on startup
    update()

    # Back up data
    while (True):
        backup()

        # Ask to run the script again
        while (True):
            restart = input('Run the script again (y/n)? ').strip().lower()

            if (restart == 'y' or restart == 'n'):
                break
            else:
                print('Please answer with (y/n).')

        if (restart == 'y'):
            print('')
            continue
        if (restart == 'n'):
            break
