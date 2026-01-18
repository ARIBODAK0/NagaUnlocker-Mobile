[app]
# (str) Title of your application
title = NagaUnlocker

# (str) Package name
package.name = nagaunlocker

# (str) Package domain (needed for android packaging)
package.domain = org.naga

# (str) Source code where the main.py lives
source.dir = .

# (str) Application versioning (INI YANG TADI ERROR KARENA HILANG)
version = 1.0

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,bin,mbn,elf,txt,xml,sh

# (list) Application requirements
requirements = python3,kivy==2.3.0,pyusb,pyserial,pycryptodome,requests,tqdm

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# -----------------------------------------------------------------------------
# Android specific
# -----------------------------------------------------------------------------

# (list) Permissions
permissions = INTERNET,USB_PERMISSION,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 34
android.minapi = 29
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a
android.allow_backup = True

# (list) XML Intent filters for USB OTG
android.manifest.xml_intent_filters = usb_filters.xml

[buildozer]
log_level = 2
warn_on_root = 1
bin_dir = ./bin
