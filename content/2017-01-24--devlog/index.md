+++
title = "This Month in ZoC - 2017.01.24"
slug = "2017-01-24--devlog"
+++

(Repost from <https://users.rust-lang.org/t/this-month-in-zone-of-control/6993>)

Hi, everyone! :)

It has been four months since the first post, sorry. I'm struggling to
find enough time for the project plus I was busy with [porting glutin to
winit](https://github.com/tomaka/glutin/issues/813) for about a month
around October.

Helicopters
===========

<https://github.com/ozkriff/zoc/issues/111>

![helicopters](helicopters.png)

-   Helicopters can fly above any terrain or ground units, but can't
    capture sectors

-   Most units can't attack helicopters - WeaponType got
    `max_air_distance: Option<i32>;` field

-   Helicopters can be seen by enemies even in non-visible tiles

-   Helicopters have a different field of view rules - their FoV have no
    'obstacle shadows':

    ![comparison of land and air field of views](air-vs-ground-fov.png)

IDLE animation:

<div class="youtube"><iframe
    frameborder="0"
    allowfullscreen
    src="https://www.youtube.com/embed/wj8ldf7sBRc?color=white&rel=0&showinfo=0"
></iframe></div>

It's not easy for ground units to catch up with a helicopter :) :

<div class="youtube"><iframe
    frameborder="0"
    allowfullscreen
    src="https://www.youtube.com/embed/u5yNCP_1G4M?color=white&rel=0&showinfo=0"
></iframe></div>

Haven't got around to implement
[AA-guns](https://github.com/ozkriff/zoc/issues/226) and
[Manpads](https://github.com/ozkriff/zoc/issues/226) yet so the main
AA-defence for now is just jeep's machinegun.

Reinforcements
==============

<https://github.com/ozkriff/zoc/issues/208>

Players have no starting forces now - everything is bought in
reinforcement sectors for reinforcement points.

The upper-left corner displays the amount of reinforcement points that
current player has and their per-turn increment:

![Reinforcements](reinforcements.png)

Reinforcement sectors are marked by two circles in player's color:

![Circle marks](circle-marks.png)

There's an additional "reinforcements" item in the context menu: when
clicked it opens a list of available units:

![Main context menu](main-context-menu.png)

This opens a list of available units:

![Context sub-menu](context-sum-menu.png)

There must be enough reinforcement points and enough room for the unit.
Units have no move or attack points at their first turn.

And, by the way, AI has been taught to buy units too.

Map selection
=============

<https://github.com/ozkriff/zoc/issues/213>

After the implementation of reinforcements it became possible to add map
selection.

You can change map by clicking on the current map's name in the main
menu screen:

![Main menu](main-menu.png)

It was mostly needed for testing/debugging purposes so most of the maps
look like this for now:

![Debugging map](debug-map.png)

Tests however are in early prototype phase and are not in the repo yet.
Right now they use special maps but I intend to implement some ASCII-DSL
like the following:

```
let map = "
    ... ... ... ...
      ... ... ... ...
    ... ... t.. r..
      t.. t.. r.. ..B
    r.A r.. r.. ..C
      ... t.. ... ...
";
```

where 't' is a 'trees', 'r' is a road and 'ABC' are positions.

Tests work by sending hardcoded commands and waiting for specified
events in response. I can't test anything that depends on RNG (attacks
mostly) but the movements, FoW, etc are more or less testable. It can't
help with errors in visualizer but it makes it easier for me to refactor
the Core.

Auto-deploy to github releases
==============================

<https://github.com/ozkriff/zoc/pull/246>

[@Gordon-F](https://github.com/Gordon-F) has implemented auto-deploy of
releases for travis and appveyor.

Now you can download windows, linux and osx builds for tagged releases
here from the [github releases
page](https://github.com/ozkriff/zoc/releases).

Android is totally different story with all its SDKs/NDKs and is still
built and uploaded manually.

Wreckages
=========

<https://github.com/ozkriff/zoc/issues/247>

Now destroyed vehicles leave wreckages.

![Wreckages](wreckages.png)

They only obstruct movement for now. Later they'll be used by infantry
as protective covering.

When particle system will be implemented wreckages will emit smoke and
fire.

Towing
======

<https://github.com/ozkriff/zoc/issues/161>

There're two new items in context menu: "attach" and "detach".

You can't chain attachments or attach WholeTile-sized units.

Towing system is mostly important for quick reposition of field guns but
it can also help with clearing roads from wrecked vehicles. The latter
reason will become more important when partial damage for vehicles gets
implemented.

<div class="youtube"><iframe
    frameborder="0"
    allowfullscreen
    src="https://www.youtube.com/embed/WEBmAvGUMGU?color=white&rel=0&showinfo=0"
></iframe></div>

Smoothly fading to alpha Fog of War
===================================

<https://github.com/ozkriff/zoc/issues/210>

<div class="youtube"><iframe
    frameborder="0"
    allowfullscreen
    src="https://www.youtube.com/embed/eNwlOO_tTqs?color=white&rel=0&showinfo=0"
></iframe></div>

Opening FoW is a very common action so it deserves to be a little more
pretty :)

It was easy though I had to rework the FoW rendering code to make it use
a lot of independently colored scene nodes instead of a single big mesh.

Fixed an old error with units moving into invisible enemies
===========================================================

<https://github.com/ozkriff/zoc/issues/106>

This change caused some refactorings in the codebase:

- Added a new event type: Reveal, similar to ShowUnit but generated by
  Core itself and not by the filtering system
- Merge all `*State` structs and `GameState` trait into one universal
  State struct - [#255](https://github.com/ozkriff/zoc/issues/255)
- Added a proper FoW layer for air units

Other changes
=============

-   [The short-term roadmap was translated into English and updated](https://github.com/ozkriff/zoc/issues/159)

-   [AI was taught to capture sectors](https://github.com/ozkriff/zoc/issues/205)

    AI is still in poor state and crashes once in a while. I need to
    implement replays to reproduce and fix these errors. It's either AI
    sometimes issues orders to units that are already dead or there are
    bugs in the event filtering system.

-   [Android memory alignment errors are finally gone](https://github.com/ozkriff/zoc/issues/197), thanks to
    @not-fl3, @tomaka, @brendanzab and @mhintz.

    [Though android port is still not very stable](https://github.com/ozkriff/zoc/issues/248).

-   [Fixed bridge slots count](https://github.com/ozkriff/zoc/issues/214). Now bridges are
    real strategic points which can be controlled or blocked easily.

-   [Do not reduce unit morale if the attack was harmless](https://github.com/ozkriff/zoc/issues/220)

-   Added "zoom in/out" buttons:

    ![zoom in-out buttons](zoom-buttons.png)

    because it's simpler than handling multi-touch gestures on android :)

Gameplay screenshots
====================

![gameplay screenshot 1](gameplay-screenshot-1.png)

![gameplay screenshot 2](gameplay-screenshot-2.png)

[@ozkriff on Twitter](https://twitter.com/ozkriff)
