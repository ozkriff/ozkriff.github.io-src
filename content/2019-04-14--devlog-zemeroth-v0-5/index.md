+++
title = "Zemeroth v0.5: GGEZ and WASM"
+++

Hi, comrades! I'm happy to announce Zemeroth v0.5.

[Zemeroth] is a turn-based hexagonal tactical game written in Rust.

You can **download precompiled binaries** for Windows, Linux, macOS and android here:
<https://github.com/ozkriff/zemeroth/releases/tag/v0.5.0>

__TODO__: you can play an online version _here_

More than a year of lazy work.
Забрасывал разработку.

Lot's of changes.

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

__TODO__: [Drawable::dimensions() #567](https://github.com/ggez/ggez/pull/567)

## WASM

```rust
#[cfg(not(target_arch = "wasm32"))]
extern crate ggez;

#[cfg(target_arch = "wasm32")]
extern crate good_web_game as ggez;
```

```rust
#[cfg(target_arch = "wasm32")]
fn main() -> GameResult {
    ggez::start(
        conf::Conf {
            cache: conf::Cache::Index,
            loading: conf::Loading::Embedded,
            ..Default::default()
        },
        |mut context| {
            let state = MainState::new(&mut context).unwrap();
            event::run(context, state)
        },
    )
}
```

```sh
$ cat utils/wasm/build.sh
#!/bin/sh
cp -r assets static
cp utils/wasm/index.html static
ls static > static/index.txt
cargo web build
```

__TODO__: ...

[not-fl3/good-web-game](https://github.com/not-fl3/good-web-game)

[example](https://github.com/not-fl3/good-web-game/tree/9b362da6d/examples/simple)

???

![TODO](2019-01-29--web-port-vs-native.jpg)

__TODO__: Add a photo from the Indikator

## itch.io

I've created a page for Zemeroth on itch.io:
[ozkriff.itch.io/zemeroth](https://ozkriff.itch.io/zemeroth)

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

Blood splatters.
slowly dissapear in three turns.

![__TODO__: description](agents-inkscape-mockup.jpeg)

_Shadows_

> На макетах выше видно много градиентов. В текущей версии решил отказаться
> от градиентов и всех округлостей, делая акцент на “типа-низкополигональном”
> угловатом стиле. На данный момент игра выглядит вот так: __TODO__.

## SVG Atlas

![TODO](2018-07-16--svg-atlas-test.png)

> 2018.07.16: Testing a simple python export script that extracts named objects
> from an `.svg` atlas. Colored backgrounds are for debug purposes.

> При реализации атласа пришлось вставить костыль для регулировки размера
> экспортируемых спрайтов: в каждой именнованной группе объектов находится
> обычно невидимый квадрат (прямоугольник для клеток) нужного количества пикселей.
> Для отладки их даже можно временно делать видимыми, бывает удобно: ...

Resource hashes - md5. Travis check.

> Хэши ресурсов
>
> После очередного #310 2 добавил таки в ресурсы подсчет md5 хэша.
> Нужный хэш хардкодится прямо в исходник игры,
> что бы при запуске с другой версией все грохалось с понятным сообщением.
>
> В CI хранилища исходников хэш персчитывается и сверяется с записанным в файл,
> а в CI самого Земерота проверяется что в исходниках захардкожен
> самый последний хэш ресурсов.
>
> Да, вот настолько я хочу хранить ресурсы в отдельном репозитории
> и не люблю git submodules. :-p

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

## Other Changes

- [Moved all crates to Rust 2018](https://github.com/ozkriff/zemeroth/pull/394);
- [Added a note about 'help-wanted' issues](https://github.com/ozkriff/zemeroth/pull/226)
- [Migrated to `std::time::Duration`](https://github.com/ozkriff/zemeroth/pull/229)
  and added `time_s` helper function (__TODO__: link and explain).
- Fixed a fun bug ([taking control of imp summoners](https://github.com/ozkriff/zemeroth/issues/288))
- [Removed](https://github.com/ozkriff/zemeroth/pull/365) some data duplication
  from [the `.ron` config with objects descriptions](https://github.com/ozkriff/zemeroth_assets/blob/69e6fb34c/objects.ron)
  using serde's default annotations and helper init functions.
- [Added a `windows_subsystem` attribute](https://github.com/ozkriff/zemeroth/pull/220).
  Don't show cmd window.
- [Fix panic when boulder is pushed into fire/spikes](https://github.com/ozkriff/zemeroth/pull/233);
- [Merge all 'line_height' consts and funcs](https://github.com/ozkriff/zemeroth/pull/431)
- `derive_more::From` for enums and errors;

------

## Devlog migrated from Pelican to Zola

__TODO__: ...

\+ link to twitter posts

------

[Zemeroth is mentioned on Amit's page about hex math][amit].

[amit]: https://www.redblobgames.com/grids/hexagons/implementation.html

------

That's all for today, thanks for reading!

**Discussions**:
[/r/rust](__TODO__),
[twitter](__TODO__) (__TODO__).

[Zemeroth]: https://github.com/ozkriff/zemeroth
