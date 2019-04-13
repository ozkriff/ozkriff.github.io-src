+++
title = "Zemeroth v0.5: GGEZ and WASM"
+++

Hi, comrades! I'm happy to announce Zemeroth v0.5.

[Zemeroth] is a turn-based hexagonal tactical game written in Rust.

You can **download precompiled binaries** for Windows, Linux, macOS and android here:
<https://github.com/ozkriff/zemeroth/releases/tag/v0.5.0>

__TODO__: you can play an online version _here_

## Häte2d -> GGEZ

<https://github.com/ozkriff/zemeroth/pull/247>

Maintaining your own engine isn't that fan in practice.
(__TODO__: add a link to GGEZ's maintainance issues)

__TODO__: ...

- ggwp-zgui
- ggwp-zscene

Btw, zcomponents crate now lives on crates.io.

No native Android version, but the web port works fine on mobile.

Debug builds are super-slow now.
I'm using nightly cargo feature to hack around this when I really need a debug build.

cgmath -> nalgebra
(see [this](https://users.rust-lang.org/t/cgmath-looking-for-new-maintainers/20406))

This PR:

> - kills `häte` crate :cry: 
> - renames `rancor` crate to `zcomponents`
> - extracts `ggwp-zgui` and `ggwp-zscene` crates from `häte`'s dead body
> - updates some deps
> - renames `game_view` mod to `battle_view`
> - removes all android stuff (circleci config, readme info, `do_android` script,
>   Cargo.toml metadata, etc)
> - install SDL2 on CI
> - removes deployment step from CI
> - adds `time_s` helper func
> - changes bg color
> - ton of other small tweaks
>
> The most serious downside of the engine switch, though temporary,
> is that there's no Android version of the game now.

old note:

> но в целом я 90% hate'а поверх ggez просто реализовал,
> так что код самого проекта не так уж и сильно зацепило.
> ядро с логикой вообще не тронуто, в визуализаторе больше всего
> геморроя из-за перехода с cgmath на nalgebra :-\

## WASM

__TODO__: ...

???

![TODO](2019-01-29--web-port-vs-native.jpg)

__TODO__: Add a photo from the Indikator

## Simple campaign mode

Win and Loose screens.

![Campaign screen example](2018-11-15--first-iteration-of-a-campaign-mode.png)

> Still working on a campaign mode with a carryover of the fighters
> from one battle to the next.

## Hit chances

...

[Implemented hit chances](https://github.com/ozkriff/zemeroth/pull/370).
Added `attack_accuracy`  and  `dodge`  stats to  `Agent`  component
and used these fields for some basic hit chances math.

Attacks with strength > 1 have additional hit chances - with reduced damage
(each strength point gives 10% hit chance improvement).

Wounded agents become less accurate.

![Hit chances demo](2018-09-29--old-hit-chances-demo.gif)
(__TODO__: needs an update)

## Armor

Implemented basic armor system.
Each armor point deflects one damage point.
Some weapons can break armor.
Fire and poison ignore armor.

> Each armor point deflects one damage point.
> Some weapons can break armor and fire/poison/etc ignore armor.

![old armor demo](2018-09-16--old-armor-demo.gif)
(__TODO__: replace with a local image. and update?)

## AI updates

__TODO__: gifs (record new?)

Keep distance in the range.

## Graphics

> flatten map a little bit and added some shadows

Dust effect (jumps)

Blood platters

![__TODO__: description](agents-inkscape-mockup.jpeg)

## SVG Atlas

![TODO](2018-07-16--svg-atlas-test.png)

> 2018.07.16: Testing a simple python export script that extracts named objects
> from an `.svg` atlas. Colored backgrounds are for debug purposes.

Resource hashes - md5. Travis check.

## Tests

Woo-hoo

## Game Rules Changes

- Spike traps

- [Updated](https://github.com/ozkriff/zemeroth/pull/351) "Poison" passive ability:
  it can’t, by itself, kill an agent anymore.
  “Poisoned” status is removed when a target’s strength is reduced to 1.
  This should make battles a little bit less frustrating and more dramatic.

- [Updated](https://github.com/ozkriff/zemeroth/pull/349) ‘Summon’ ability:
  each use of it now creates one more imp (up to 6).
  It should force the player to be more aggressive.

- __TODO__: Commutative bombs (__TODO__: <https://github.com/ozkriff/zemeroth/pull/296>,
  <https://github.com/ozkriff/zemeroth/issues/286>)

- [Changed the summoning algorithm to prefer imp types that are under-presented
  on the map, not just random ones](https://twitter.com/ozkriff/status/1040321852495863808).
  Seems to work fine now - even with increased summon rate imp types
  are balanced in count:
  [img](2018-09-14--map-lines.png)

## Smaller Changes

- [Added a note about 'help-wanted' issues](https://github.com/ozkriff/zemeroth/pull/226)
- [Migrated to `std::time::Duration`](https://github.com/ozkriff/zemeroth/pull/229)
  and added `time_s` helper function (__TODO__: link and explain).
- Fixed a fun bug (__TODO__: taking control of imp summoners)
- [Removed](https://github.com/ozkriff/zemeroth/pull/365) some data duplication
  from [the `.ron` config with objects descriptions](https://github.com/ozkriff/zemeroth_assets/blob/69e6fb34c/objects.ron)
  using serde's default annotations and helper init functions.
- [Added a `windows_subsystem` attribute](https://github.com/ozkriff/zemeroth/pull/220).
  Don't show cmd window.
- [Fix panic when boulder is pushed into fire/spikes](https://github.com/ozkriff/zemeroth/pull/233)

------

That's all for today, thanks for reading!

**Discussions**:
[/r/rust](__TODO__),
[twitter](__TODO__) (__TODO__).

[Zemeroth]: https://github.com/ozkriff/zemeroth
