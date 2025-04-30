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

# (list) List of service to declare
services =

# (str) Icon of the application
icon.filename = %(source.dir)s/icon.png

# (str) Supported platforms
# Change this to just `ios` for iOS support
target = ios

# (str) Minimum iOS version supported
ios.min_version = 12.0

# (str) iOS status bar style
ios.statusbarstyle = UIStatusBarStyleLightContent

# (bool) Hide the status bar
fullscreen = 1

# (str) Supported architectures for iOS: "arm64"
ios.archs = arm64

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (bool) Whether or not to include a launcher icon
include_launcher_icon = True

# (list) Permissions
# No Android-specific permissions needed
android.permissions =

# (list) Dependencies required by your app
requirements = python3,kivy,pillow

# (str) Custom source folders for requirements
# (e.g. custom source for `pygame`)
# requirements.source =

# (list) Garden requirements
# garden_requirements =

# (str) Custom Java namespace (Not used for iOS)
# android.add_jars =

# (bool) Use --private data storage (needed for iOS sandbox rules)
use_private_storage = 1

# (str) Presplash screen of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) The format used to package the app for iOS
# Available options: app, xcode
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

# (str) Custom plist for iOS
#ios.custom_plist = %(source.dir)s/custom.plist

# (str) The Apple Team ID
ios.codesign.teamid = YOUR_TEAM_ID_HERE

# (str) The provisioning profile name (must match your Apple Developer account)
ios.codesign.provisioning_profile = YOUR_PROFILE_NAME_HERE

# (str) The development certificate identity
ios.codesign.development = iPhone Developer

# (str) The app store certificate identity
# ios.codesign.release = iPhone Distribution

# (str) iOS deployment target version
ios.deployment_target = 12.0

# (bool) Automatically create Xcode project (recommended)
ios.create_xcode_project = True

# (bool) Sign the app when building
ios.codesign = True

# (list) Environment variables for iOS
ios.env =

[buildozer]

# (str) Buildozer log level (0 = error only, 1 = normal, 2 = verbose, 3 = debug)
log_level = 2

# (bool) Whether to clean before building
clean = False

# (str) Where to store the .buildozer dir
build_dir = .buildozer

# (str) Path to Xcode project (auto-handled if `ios.create_xcode_project` = True)
ios.xcode_project_path =

# ------------------------------------------------------------------------------
# Optional iOS extras (leave as is if unsure)
# ------------------------------------------------------------------------------
ios.no_opengl_headers = False
