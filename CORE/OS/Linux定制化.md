`sudo apt install gnome-shell-extension-manager gir1.2-gtop-2.0 lm-sensors`


# 主题


# 触摸板手势

## fusuma 基于xdotool的触摸屏配置

[fusuma github](https://github.com/iberianpig/fusuma)

1. 安装xdotool

2. 配置触摸板手势：
`mkdir -p ~/.config/fusuma/config.yml`
结合系统快捷键进行配置

```yml
swipe:
  3: 
    left: 
      command: 'xdotool key shift+super+Left'
    right: 
      command: 'xdotool key shift+super+Right'
    up: 
      command: 'xdotool key super'
    down: 
      command: 'xdotool key super+a'
  4:
    left: 
      command: 'xdotool key ctrl+alt+Down'
    right: 
      command: 'xdotool key ctrl+alt+Up'
    up: 
      command: 'xdotool key ctrl+alt+Down'
    down: 
      command: 'xdotool key super+l'
pinch:
  in:
    command: 'xdotool keydown ctrl click 4 keyup ctrl'
  out:
    command: 'xdotool keydown ctrl click 5 keyup ctrl'
hold:
  4:
    command: 'xdotool key super' # Activit
```


3. 开机启动：
配置desktop文件
/usr/share/applications
```desktop
[Desktop Entry]
Encoding=UTF-8
Name=fusuma
Comment=fusuma
Exec=/usr/local/bin/fusuma --config=/home/piper/.config/fusuma/config.yml
Icon=/usr/share/icons/gnome-logo-text.svg

Terminal=false
Type=Application
Categories=Application;Development;
```
在tweak中配置开机启动
