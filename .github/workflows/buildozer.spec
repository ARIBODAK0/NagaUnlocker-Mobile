[app]
title = NagaUnlocker
package.name = nagaunlocker
package.domain = org.naga
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,bin,mbn,elf
version = 1.0
requirements = python3,kivy,pyusb,pyserial,pycryptodome,requests
orientation = portrait
permissions = INTERNET,USB_PERMISSION,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 29
android.arch_build = arm64-v8a
android.allow_backup = True
