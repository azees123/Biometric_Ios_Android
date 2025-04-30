[app]

# (str) Title of your application
title = FingerprintAuth

# (str) Package name
package.name = fingerprintauth

# (str) Package domain (must be a valid domain name)
package.domain = org.example

# (str) Source code where main.py is located
source.dir = .

# (str) Application entry point
source.main = main.py

# (list) List of inclusions using pattern matching
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0

# (str) Supported orientation (portrait, landscape, all)
orientation = portrait

# (str) Icon of the application
icon.filename = %(source.dir)s/icon.png

# (str) Supported platforms (Only iOS)
# Set the target platform to `ios` to ensure it's iOS-only
target = ios

# (str) Minimum iOS version supported
ios.min_version = 12.0

# (bool) Hide the status bar on iOS
fullscreen = 1

# (str) Supported architectures for iOS (arm64 is required for iOS builds)
ios.archs = arm64

# (bool) Whether or not to include a launcher icon
include_launcher_icon = True

# (list) Dependencies required by your app
requirements = python3,kivy,pillow

# (str) Custom source folders for requirements
# If you have custom requirements, you can specify the source here

# (bool) Use --private data storage (needed for iOS sandbox rules)
use_private_storage = 1

# (str) Presplash screen of the application
# If you have a presplash screen, specify it here

# (str) The format used to package the app for iOS
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

# (bool) Automatically create Xcode project (recommended)
ios.create_xcode_project = True

# (str) The Apple Team ID
# You will need to configure this if you're using code-signing
# ios.codesign.teamid = YOUR_TEAM_ID_HERE

# (bool) Sign the app when building (this is only relevant for signed builds)
# ios.codesign = True

# (str) iOS deployment target version
ios.deployment_target = 12.0
