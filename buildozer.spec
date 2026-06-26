[app]
# Nombre y paquete de tu app
title = LabubuNeon
package.name = labubucalc
package.domain = org.alejandro

# Dónde está el código y qué extensiones empaquetar
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Versión y dependencias críticas
version = 0.1
requirements = python3,kivy==2.3.0,kivymd,pillow

# Configuración de pantalla y arquitectura del celular
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
