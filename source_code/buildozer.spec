[app]

title = Test App
package.name = source_code
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,certifi,chardet,comtypes,docutils,idna,Kivy,kivy-deps.angle,kivy-deps.glew,kivy-deps.sdl2,
Kivy-Garden,Pygments,pypiwin32,pyttsx3,pywin32,requests,urllib3

orientation = portrait
fullscreen = 0
android.arch = armeabi-v7a

# iOS specific
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.7.0

[buildozer]
log_level = 2
