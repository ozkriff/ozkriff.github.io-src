+++
title = "Разработка Мародера - 2014.04.20"
slug = "2014-04-21--devlog-marauder-008"
description = "Отчет об ошибке, битсквид, текст, verify!"

[taxonomies]
tags = ["devlog", "marauder"]
+++

Отпуск кончился. Хочется умереть :) .

Забыл написать. На прошлой неделе появился первый отчет об ошибке, ура
ура! Правда я хз что с ним делать :( .

Наткнулся на серию классных постов об обработке ошибок в блоге
битсквида.

Сделал кое какое отображение 2д и 3д текста.

Решил возвращать текст в экранных координатах, а для отображения в 3д
сцене его плющить матрицами как надо.

Для поиска всех gl вызовов и вывода только их названий:

    grep -oh 'gl::\w*(' visualizer/* | sort | uniq

Добавил макрос (фу) `verify!`, позаимствованный из kiss3d, для проверки
`gl::GetError` после каждого OpenGL вызова. Нашлась парочка ошибок.
Надеюсь, это поможет запустить мародера на os x, а то неудобно. что
отчет об ошибке столько времени уже висит.

Сделал отображаемый пробел и поддержку нескольких строчек в текстовом
кэше для font\_stash.

Камера в начале боя теперь не где-то с краю, а в центре карты.
