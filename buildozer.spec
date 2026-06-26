[app]
# Nombre y paquete de tu app
title = LabubuNeon
package.name = labubucalc
package.domain = org.alejandro

# Dónde está el código y qué extensiones empaquetar
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Versión y dependencias — versiones fijas para evitar conflictos
version = 0.1
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow

# Android SDK / NDK — versiones estables y probadas
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license = True

# Configuración de pantalla y arquitectura
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
