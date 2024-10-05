# Scripts
This repository contains some scripts I wrote to automate daily tasks. I hope they are useful to you as well :)

## rclone.py
This Python script creates backups of your data to Microsoft OneDrive using [rclone](https://rclone.org). It checks for updates on every start, interactively asks if you want to execute rclone's `sync` or `cryptcheck` commands (with some reasonable CLI flags set) and logs everything.

### Why use this over Microsoft's native OneDrive client?
- Both Python and rclone are platform-independent
- rclone's `union` remote allows multiple accounts to be pooled together to bypass OneDrive's per-user quotas
- rclone's `crypt` remote allows your backups to be end-to-end encrypted
- rclone's `cryptcheck` command allows you to verify the integrity of your data
- rclone's logs are actually useful

### What to look out for?
- Relative paths `./rclone.conf` and `./filters.md` are used for portability, so these files are expected to exist in the same directory as this script
    - `rclone.conf` is expected to contain a source remote called `data:` (an `alias` for a local path) and a target remote called `OneDrive:`
    - Encrypting `rclone.conf` is possible, but the password has to be entered again for every command as rclone currently doesn't support reading it from stdin during runtime
- For automatic deletion of `rclone.old.exe` after an update to work on Windows, `rclone.exe` needs to be in the same directory as this script (but can be anywhere otherwise)
