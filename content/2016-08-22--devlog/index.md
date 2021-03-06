+++
title = "This Month in ZoC - 2016.08.22"
slug = "2016-08-22--devlog"
+++

(Repost from <https://users.rust-lang.org/t/this-month-in-zone-of-control/6993>)

Hi, comrades! Welcome to the first issue of ZoC's monthly report!

------------------------------------------------------------------------

[ZoC](https://github.com/ozkriff/zoc) is a turn-based hexagonal strategy
game written in Rust.

Core game features are:

-   advanced fog of war
-   slot system (multiple units per tile)
-   reaction fire (xcom-like)
-   morale and suppression

GFX and rusttype
================

[Zgl](https://github.com/ozkriff/zoc/tree/c8b11f4/src/zgl/src)/[stb\_truetype](https://github.com/ozkriff/stb-tt-rs)
were finally replaced with [GFX](https://github.com/gfx-rs/gfx) and
[rusttype](https://github.com/dylanede/rusttype), YAY :-D !!1 -
[\#183](https://github.com/ozkriff/zoc/issues/183)

Android
=======

ZoC is now build with
[cargo-apk](https://github.com/tomaka/android-rs-glue).

There are still some problems with android version though:
<https://github.com/ozkriff/zoc/issues/197> :(

Roads
=====

<https://github.com/ozkriff/zoc/issues/152>

![Simple road](simple-road.png)

Sectors, victory points and game results screen
===============================================

<https://github.com/ozkriff/zoc/issues/124>

<div class="youtube"><iframe
    frameborder="0"
    src="https://www.youtube.com/embed/hI6YmZeuZ3s"
></iframe></div>

![Sectors](sectors.png)

Basic smoke screens
===================

<https://github.com/ozkriff/zoc/issues/160>

![Smoke](smoke.png)

![Smoke screen in action](somke-on-water.png)

<div class="youtube"><iframe frameborder="0" allowfullscreen src="https://www.youtube.com/embed/WJHkuWwAb7A?color=white&rel=0&showinfo=0"></iframe></div>

Water tiles
===========

<https://github.com/ozkriff/zoc/issues/204>

![Water](water-tiles.png)

GUI updates
===========

-   Replaced unit ids with unit type names
-   Added hit chances
-   Added basic unit info to the upper-left corner of the screen

![unit types](unit-types.png)

![hit chances](hit-chances.png)

![basic unit info](basic-unit-info.png)

Fixed switching between normal and wireframe mode for buildings
===============================================================

<https://github.com/ozkriff/zoc/issues/182>

![combined wireframe and normal buildings](combined-wireframe-and-normal-buildings.png)

Other notable changes
=====================

- [Fixed armored units reaction to light reactive fire](https://github.com/ozkriff/zoc/issues/191)
- [Improved error message about missing assets](https://github.com/ozkriff/zoc/issues/211)
- [Made MapText fading to alpha smoothly](https://github.com/ozkriff/zoc/commit/ac2c7c6)
- [Fixed annoying vehicle-in-building pathfinder bug](https://github.com/ozkriff/zoc/commit/1ee698)
- [Added personal independent camera for each human player](https://github.com/ozkriff/zoc/commit/fde38)
- [Fixed AI hangup](https://github.com/ozkriff/zoc/issues/196)

Bonus 1: ZoC on android
=======================

![photo](zoc-on-andoid.jpg)

Bonus 2: memoir44-mockup of smoke demo map
==========================================

![photo](memoir44.jpg)

------------------------------------------------------------------------

Weekly links:
[1](https://users.rust-lang.org/t/whats-everyone-working-on-this-week-31-2016/6747/2),
[2](https://www.reddit.com/r/rust/comments/4wob4b/whats_everyone_working_on_this_week_322016/d68pxx4),
[3](https://www.reddit.com/r/rust/comments/4xrycf/whats_everyone_working_on_this_week_332016/d6i0d1a),
[4](https://www.reddit.com/r/rust/comments/4yzx43/whats_everyone_working_on_this_week_342016/d6rp869).

<https://github.com/ozkriff/zoc>, [@ozkriff on Twitter](https://twitter.com/ozkriff)
