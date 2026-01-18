[app]
# (str) Title of your application
title = NagaUnlocker Mobile

# (str) Package name
package.name = nagaunlocker

# (str) Package domain (needed for android packaging)
package.domain = org.naga

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,bin,mbn,elf,txt,sh

# (list) Application requirements
# Ditambahkan pyusb, pyserial, dan pycryptodome untuk mesin mtk/edl
requirements = python3,kivy==2.3.0,pyusb,pyserial,pycryptodome,requests,tqdm,certifi

# (str) Custom source folders for requirements
# (list) Garden requirements
# (str) Presplash of the application
# (str) Icon of the application
# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# -----------------------------------------------------------------------------
# Android specific
# -----------------------------------------------------------------------------

# (list) Permissions
# Ditambahkan MANAGE_EXTERNAL_STORAGE untuk Android 11+
permissions = INTERNET,USB_PERMISSION,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE,FOREGROUND_SERVICE

# (int) Target Android API, should be as high as possible.
android.api = 34

# (int) Minimum API your APK will support. (API 29 = Android 10)
android.minapi = 29

# (str) Android SDK directory (if empty, it will be automatically downloaded)
# (str) Android NDK directory (if empty, it will be automatically downloaded)
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded)
android.ndk_path = 

# (list) The Android architectures to build for (Poco F1 uses arm64-v8a)
android.archs = arm64-v8a

# (bool) Allow the app to be placed on external storage
android.allow_backup = True

# (list) add tag-value pairs in a XML file (f.e. for USB OTG)
android.manifest.xml_intent_filters = usb_filters.xml

# (bool) Accept SDK license agreements
android.accept_sdk_license = True

# -----------------------------------------------------------------------------
# Buildozer specific
# -----------------------------------------------------------------------------

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifacts
bin_dir = ./bin
