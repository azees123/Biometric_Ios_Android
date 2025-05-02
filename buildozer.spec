[app]
title = FingerprintAuth
package.name = fingerprintauth
package.domain = org.example
source.dir = .
source.main = main.py
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
orientation = portrait
#icon.filename = %(source.dir)s/icon.png
target = ios
ios.min_version = 12.0
ios.archs = arm64
fullscreen = 1
include_launcher_icon = True
requirements = python3,kivy==2.2.1,pillow
use_private_storage = 1
