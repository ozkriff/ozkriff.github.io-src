
Разработка Мародера - 2014.03.23
################################

:tags: devlog, marauder
:excerpt:
    Manowar, обновление rustc, Eq для float, мертвый страйк,
    выделение отдельных отрядов в клетке


Сходил на Manowar, о да, нужно больше пафоса. Только теперь
вообще ничего не слышу :) .

Мучал glfw-rs, cgmath-rs и самого мародера, что бы они собирались с
последней версией компилятора. Сложно было :)

Брендан хочет, что бы cgmath-rs был исправлен не таким грубым хаком.
Там могут быть косяки с NaN и +/-Inf.
Но я туплю как сделать правильно. :(

Мой грандиозный страйк помер :(, черт:

|github-streak-fail|


Капельку поковырял текст. Решил, что не буду использовать cmr/hgl-rs,
страшно мне. Лучше все-таки чего-то свое сделаю.

Шрифты, шрифты:

|font-cli|


Сделал выделение отдельных отрядов в клетке:

|color-picking-01|

|color-picking-02|

|color-picking-03|

.. |github-streak-fail| image:: images/2014-03-20--github-streak-fail.png
.. |font-cli| image:: images/2014-03-20--font-cli.png
.. |color-picking-01| image:: images/2014-03-20--color-picking-1.gif
.. |color-picking-02| image:: images/2014-03-20--color-picking-2.png
.. |color-picking-03| image:: images/2014-03-20--color-picking-1.gif

.. vim: set tabstop=4 shiftwidth=4 softtabstop=4 expandtab:
