Ubuntu 22.04 ROS2 Humble Hawksbill
Сборка происходила с помощью ament_python

Робот состоит из пяти звеньев (не считая base_link и платформы) и трёх подвижных вращающихся шарниров.

launch-файлы запуска находится в папке launch: один с запуском jsp-gui, второй - без gui
есть неработающая нода публикации в топик /joint_states
ВАЖНО! Для запуска на стороннем устройстве необходимо установить два дополнительных пакета:
1) urdf_launch (стандартный пакет, на который ссылаются, чтобы не засорять кучей настроек launch файл собственного проекта)
2) joint_state_publisher (и joint_state_publisher_gui)

URDF-файл находится в папке models

Видео работы представлено в файле video.webm
Дерево преобразований представлено в файле frames_2024-09-17_18.18.54.pdf
