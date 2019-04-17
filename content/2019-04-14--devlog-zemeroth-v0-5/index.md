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

> [Ported Zemeroth to ggez v0.5.0-rc.0](https://github.com/ozkriff/zemeroth/pull/426),
> filed [a bunch of mostly text-related issues in the process](https://github.com/ggez/ggez/issues?utf8=%E2%9C%93&q=is%3Aissue+author%3Aozkriff+created%3A%3E2019-01-01)
> (sorry, /u/icefoxen!) and tried to fix the most critical ones for Zemeroth:
> ["Remove the generic argument from Drawable::draw"](https://github.com/ggez/ggez/pull/559),
> ["Drawable::dimensions()"](https://github.com/ggez/ggez/pull/567) (big one!)
> and ["Fix Text::dimensions height"](https://github.com/ggez/ggez/pull/593).
>
> Now, [when GGEZ v0.5.0-rc.1 is out](https://www.reddit.com/r/rust_gamedev/comments/auexbj/ggez_050rc1_released/),
> I can switch to it and try to [merge a WASM version of Zemeroth into master](https://github.com/ozkriff/zemeroth/issues/178).

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

> RIP [Häte2d](https://docs.rs/hate), you were a fun experiment,
> but using ggez is much more practical.
>
> The most serious downside of the engine switch,
> [though temporary](https://github.com/ggez/ggez/issues/70),
> is that there's no Android version of the game for now.
> And I don't like that much
> [SDL2 native dependency](https://github.com/ozkriff/zemeroth/blob/d36340e17/.travis.yml#L29-L40).

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

ggwp?

> "__What does `ggwp-` prefix mean?__"
>
> As Icefoxen asked to [not use `ggez-` prefix][ggwp]
> I use `ggwp-` ("good game, well played!") to denote that the crate
> belongs to ggez ecosystem, but is not official.

[ggwp]: https://github.com/ggez/ggez/issues/373#issuecomment-390461696

old note:

> но в целом я 90% hate'а поверх ggez просто реализовал,
> так что код самого проекта не так уж и сильно зацепило.
> ядро с логикой вообще не тронуто, в визуализаторе больше всего
> геморроя из-за перехода с cgmath на nalgebra :-\

__TODO__: [Drawable::dimensions() #567](https://github.com/ggez/ggez/pull/567)

> [Ported Zemeroth to ggez v0.5.0-rc.0](https://github.com/ozkriff/zemeroth/pull/426),
> filed [a bunch of mostly text-related issues in the process](https://github.com/ggez/ggez/issues?utf8=%E2%9C%93&q=is%3Aissue+author%3Aozkriff+created%3A%3E2019-01-01)
> (sorry, /u/icefoxen!) and tried to fix the most critical ones for Zemeroth:
> ["Remove the generic argument from Drawable::draw"](https://github.com/ggez/ggez/pull/559),
> ["Drawable::dimensions()"](https://github.com/ggez/ggez/pull/567) (big one!) and
> ["Fix Text::dimensions height"](https://github.com/ggez/ggez/pull/593).
>
> Now, [when GGEZ v0.5.0-rc.1 is out](https://www.reddit.com/r/rust_gamedev/comments/auexbj/ggez_050rc1_released),
> I can switch to it and try to
> [merge a WASM version of Zemeroth into master](https://github.com/ozkriff/zemeroth/issues/178).

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

![me presenting Zemeorth at Indikator](2018-11-03--indikator.jpg)

## itch.io

I've created a page for Zemeroth on itch.io:
[ozkriff.itch.io/zemeroth](https://ozkriff.itch.io/zemeroth)

<https://twitter.com/ozkriff/status/1090615410242785280>

> Created [an itch.io list of Rust games](https://www.reddit.com/r/rust/comments/arm9dr/a_list_of_itchio_games_written_in_rust).
>
> Also, I've sent a request to itch.io folks to add Rust as an instrument,
> so now a more official list is available:
> [itch.io/games/made-with-rust](https://itch.io/games/made-with-rust).
> Looks like my original list will be deprecated with time but
> it's still useful for now because only authors of the games can add
> an instrument to the metadata.

Lot's of feedback.

> Обратной связи целый вагон, тут расписывать подробно поленюсь,
> но чаще всего повторялось, что нужен более человечный GUI,
> хоть какое-то руководство как в это играть и слишком сильный рандом -
> главное направление действий после окончания миграции на ggez 0.5 ясно.
>
> Отдельно отмечу, что отхватил на итче [огромный отзыв](https://itch.io/post/660275).
> Прям очень круто, что кто-то незнакомый продрался через супер-сырой интерфейс,
> позалипал в игру, разобрался в большей части механик,
> и не поленился написать развернутую и мотивирующую конструктивную критику.

## Simple campaign mode

"Basic campaign mode with a carryover of the survivor fighters"

> Представляет из себя просто цепочку боев с заранее заданными сценариями.
> Если проигрываешь в бою - все, кампания для тебя закончилась, начинай сначала.
> Если выигрываешь, то тебе показывается переходный экран со списком погибших,
> текущим составом группы и вариантами кого ты можешь “докупить” в награду.
>
> Поскольку экран боя создается в экране главного меню или экране кампании,
> а затем складывается в виде типаж-объекта на стек экранов,
> возврат результата боя получилось организовать только через [канал](__TODO__).
> Немного костыльно, но сойдет.
>
> Сейчас есть косяк с тем что если бой пошел неудачно,
> то можно в любой момент выйти из него в меню кампании и начать бой заново.
> Уже завел [задачу](https://github.com/ozkriff/zemeroth/issues/387)
> на то, что бы пресечь это безобразие - “вечная смерть” наше все.

Win and Loose screens.

![Campaign screen example](2018-11-15--first-iteration-of-a-campaign-mode.png)

> Still working on a campaign mode with a carryover of the fighters
> from one battle to the next.

[campaign_01.ron](https://github.com/ozkriff/zemeroth_assets/blob/acd9fe9ef/campaign_01.ron)

------

__TODO__: Not sure if this piece belongs to this section:

> <https://github.com/ozkriff/zemeroth/pull/360>
>
> <https://github.com/ozkriff/zemeroth/pull/369>
>
> Добавлены зоны начального построения (lines) и генератор
> больше не создает агентов в упор к врагам.
>
> С последним все просто - если рядом с клеткой стоит враг,
> то она считается непригодной для начальной позиции.
> Это помогает избежать дурацких ситуаций на первом ходу,
> например когда важный дальнобойный боец оказывается по случайности
> связан рукопашныи боем - теперь всегда есть возможность его отвести
> куда-то и перегруппироваться.
>
> А насчет зон, добавлено перечисление
> `pub enum Line { Any, Front, Middle, Back },`
> позволяющее указывать в сценарии где мы какие виды агентов хотим видить.
> Теперь демоны-вызываетли всегда сощдаются в дальнем конце карты за жвым щитом,
> т.е. застрахованы от быстрой расправы на первом ходу.
>
> Снимок тестовой карты, в которую специально нагнана прям куча демонов что бы
> четко были видны зоны и отступы: ...

## Hit chances

...

[Implemented hit chances](https://github.com/ozkriff/zemeroth/pull/370).
Added `attack_accuracy`  and  `dodge`  stats to  `Agent`  component
and used these fields for some basic hit chances math.

Attacks with strength > 1 have additional hit chances - with reduced damage
(each strength point gives 10% hit chance improvement).

Wounded agents become less accurate.

In the current implementation, it's based on attacker's accuracy and target's
dodge stats. The hit chance is reduced when attacker is wounded.

![Hit chances demo](2018-09-29--old-hit-chances-demo.gif)
(__TODO__: needs an update)

> Из визуала:
>
> - При выделении готового к атаке бойца поверх врагов
>   показываются шансы попасть по ним;
> - Во время атаки под атакующим ненадолго появляется вероятность успеха атаки.
>   Нужно, в первую очередь, что бы было понятнее насколько враги опасны.
>
> Пока я два недостатка описанной выше схемы знаю:
>
> - Сходу в ней не показать оружие, у которого нет градации урона.
>   Хз что это именно за оружие должно быть и нужно ли оно мне (вряд ли),
>   но штуки вида “или попал и нанес 4 урона, или не попал совсем”
>   непредставимы без дополнительных костылей.
> - Отравляющий демон наносит 0 урона при атках - т.е. его шанс попасть
>   ниже остальных демонов.
>   Тут вбил костыль в виде повышения его точности атаки.
>
> Какие изменния случились с балансом:
>
> - Теперь первоочередная цель это ранить врага,
>   добивать уже может быть меньшим приоритетом - иногда удобно,
>   что бы практически неспособный попасть по твоим бойцам враг
>   занимал клетку и не давал его более здоровым друзьям подойти;
> - Важность способности лечения у алхимика возросла, потому что толку
>   от своих раненных бойцов становится сильно меньше.

[Show missing strength points as transparent dots](https://github.com/ozkriff/zemeroth/pull/343)

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

Dust effect (jumps) - <https://github.com/ozkriff/zemeroth/pull/390>

> пыль создается одной не очень большой функцией, которая просто создает
> пачку спрайтов и навешивает на них цепочки простых действий перемещения
> и изменения цвета.

------

blood splatters and weapon flashes - <https://github.com/ozkriff/zemeroth/pull/401>

Adds weapon flashes of four types: slash, smash, pierce and claw;
Adds directed dynamic blood splatters.

------

> Добавил бойцам параметр WeaponType.
> Пока есть четыре вида: smash, slash, pierce и claw
> и они чисто визуальные - для выбора подходящей текстурки.
> Некоторые спрайты атаки под углами смотрятся странно
> (копейщик, я на тебя смотрю) надо будет потом дополнительные варианты
> добавить и зеркалировать все это хозяйство по ситуации.

------

Blood splatters.
slowly dissapear in three turns.

![__TODO__: description](agents-inkscape-mockup.jpeg)

_Shadows_?

> На макетах выше видно много градиентов. В текущей версии решил отказаться
> от градиентов и всех округлостей, делая акцент на “типа-низкополигональном”
> угловатом стиле. На данный момент игра выглядит вот так: __TODO__.

## SVG Atlas

![TODO](2018-07-16--svg-atlas-test.png)

[svg atlas](https://github.com/ozkriff/zemeroth_assets_src/blob/846a45b7c/atlas.svg)

[export.py](https://github.com/ozkriff/zemeroth_assets_src/blob/846a45b7c/export.py)

> 2018.07.16: Testing a simple python export script that extracts named objects
> from an `.svg` atlas. Colored backgrounds are for debug purposes.

...

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

Test scenarios are completely deterministic.
Randomness is canceled out with special agent types + special debug flag in
game's state that causes a panic if you try to do anything with uncertain results

> it can be mitigated with special unit types with unrealistic stats
> (for example, accuracy = 999, strength = 1) that allows them
> to always pass required tests (for example, always hits or always dies).
>
> and an additional `no_random` flag in the game state, that causes a panic
> if agent's stats during the "dice roll" may result in non-determined results
> (basically, it checks that the coefficients are large or low enough
> to shut off any dice value fluctuations).

`pretty_assertions` crate is super-useful when you need to debug
failing assert comparisons of big hierarchical objects
(some of which may be many screens long in my case)

<https://github.com/colin-kiegel/rust-pretty-assertions>

Woo-hoo

One of the benefits of making a turn-based game is that you can relatively easy
separate the logic from the visuals and cover the former with tests.

Added basic tests scenarios to #Zemeroth and refactored state mutations:

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

  This prevents Imp Summoners from being created only a tile away from enemies
  and thus not having any chances to survive.

- Teach AI to move closer to targets even if there's no direct path to them

  <https://github.com/ozkriff/zemeroth/pull/308>

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
- [Removed data duplication from `objects.ron`](https://github.com/ozkriff/zemeroth/pull/365)

------

> started [@rust_gamedev](http://twitter.com/rust_gamedev) twitter account in
> an attempt to create some central point for #rustlang #gamedev stuff on twitter;

------

## Devlog migrated from Pelican to Zola

__TODO__: ...

\+ link to twitter posts

------

[gave a presentation about Zemeroth project at 8th Indie-StandUp](https://twitter.com/ozkriff/status/1058359693503070208).

------

[Zemeroth is mentioned on Amit's page about hex math][amit].

[amit]: https://www.redblobgames.com/grids/hexagons/implementation.html

------

__TODO__: Bonus: stress testing screenshots? Not sure the post really needs them.

------

## Roadmap

What's next?

You can find the roadmap [in the README](__TODO__);

> I want reactions system to be the core of the game. Atm, only basic reactions (attacking) is implemented, but I hope to add more interesting behaviors: auto-jumping away when an enemy approaches or something more aggressive auto-movement (like Muton Berserker from the X-Com).

Short-term plans are:

- GUI improvements
- [Reduce text overlapping](https://github.com/ozkriff/zemeroth/issues/214)
- xxx
- __TODO__;

------

That's all for today, thanks for reading!

**Discussions**:
[/r/rust](__TODO__),
[twitter](__TODO__) (__TODO__).

[Zemeroth]: https://github.com/ozkriff/zemeroth
