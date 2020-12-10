[app]

title = Test App
package.name = source_code
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,certifi==2020.12.5,chardet==3.0.4,comtypes==1.1.7,docutils==0.16,idna==2.10,Kivy==2.0.0,kivy-deps.angle,kivy-deps.glew==0.3.0,kivy-deps.sdl2==0.3.1,
Kivy-Garden==0.1.4,Pygments==2.7.3,pypiwin32==223,pyttsx3==2.90,pywin32==300,requests==2.25.0,urllib3==1.26.2

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
