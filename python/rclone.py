# Imports
import subprocess


# Function to back up data to OneDrive
def main():
    # Opening message
    print('Python script to back up data to OneDrive via rclone.\n')

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

    # Don't close window immediately when script finishes
    input('Press enter to exit!')


# Execute main when script is called directly
if (__name__ == '__main__'):
    main()
