+++
title = "Zemeroth v0.5: ggez, WASM, itch.io"
slug = "2019-04-14--devlog-zemeroth-v0-5"
+++

Hi, folks! I'm happy to announce Zemeroth v0.5.

[Zemeroth] is a turn-based hexagonal tactical game written in Rust.
You can [download precompiled v0.5 binaries][release v0.5]
for Windows, Linux, and macOS.
Also, now you can **[play an online version](https://ozkriff.itch.io/zemeroth)**
(read more about the web version in the "WASM" section below).

The last release happened about a year ago.
Since then, development haven't been that active,
sometimes even completely stalled for weeks.
But a year is a big period of time anyway, so there're still lots of changes.

Main features of v0.5 release are:
migration to ggez engine, web version, itch.io page, visual updates,
campaign mode, and tests.

[release v0.5]: https://github.com/ozkriff/zemeroth/releases/tag/v0.5.0

## Migration to `ggez` engine

Maintaining your own engine (even a simple and minimalistic 2D one)
turned out to be really not fun for me in practice -
you have to fight a constant stream of a small corner case issues
and platform-specific tweaks and hacks.

So I've surrended: [discontinued my tiny game engine Häte2d][pr247]
and migrated to [ggez],
because ???.
I though that I knew that it's a hard task but it turned out even worse.
(__TODO__: link to ggez's hidpi issues on macos)
(__TODO__: на ровном месте возникает огроомное количество всяких мелочей.
и это даже если делать чисто для себя движок.
а ведь обидно, что его никто не используется.
но делать движок общего назначения еще на порядок сложнее.
это все интересный опыт, но игру я так и за десяток лет не закончил бы).
(__TODO__: add a link to `ggez`'s maintainance issues)
<https://github.com/ggez/ggez/labels/bug>

[pr247]: https://github.com/ozkriff/zemeroth/pull/247
[ggez]: https://github.com/ggez/ggez

It was a long process.
Initially I migrated to ggez v0.4 that was SDL2-based.

As soon as the first RC for ggez v0.5 became aviable
I attempted to migrate to it.

ggez v0.5 is still not released atm,
but the aviable RC2 is stable enough for me.

...

`hate` had a built in basic scene management and GUI systems,
but `ggez` is a minimalistic engine and

Two helper crates were extracted from Häte2d

...

The most serious downside of the engine switch,
[though temporary](https://github.com/ggez/ggez/issues/70),
is that there's no native Android version of the game for now.
But who really needs a native port when you have...

## WASM port

__TODO__: link to Icefoxen's plans about WASM support in ggez

`good-web-game` is mostly source compatible with ggez.

> Note that good-web-game is not really GGEZ's backend,
> but a separate web-targeted engine with a similar API
> that @not-fl3 uses for his prototypes.
>
> Zemeroth uses good-web-game for its web version as a quick-n-dirty
> immediate solution until a proper WASM support arrives to GGEZ
> (there're no plans of making good-web-game some kind of official GGEZ backend).
>
> The currently implemented subset of GGEZ API is quite limited
> and while it may be used for something else that Zemeroth,
> it will probably require a lot of work to do (contributions are welcome ;) ).

A hack to substitute the crate:

```rust
#[cfg(not(target_arch = "wasm32"))]
extern crate ggez;

#[cfg(target_arch = "wasm32")]
extern crate good_web_game as ggez;
```

(__TODO__: why can't I do this in `Cargo.toml`?)

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

A short helper script:

```sh
$ cat utils/wasm/build.sh
#!/bin/sh
cp -r assets static
cp utils/wasm/index.html static
ls static > static/index.txt
cargo web build
```

The script prepares a `static` directory that will be packed by cargo-web.

cargo-web only packs `static` directory, so the script copies the game's assets there.

It also copies the `index.html` template page there.

And adds a good-web-game specific file that lists all resources
that should be loadable by the engine.

__TODO__: ...

[not-fl3/good-web-game](https://github.com/not-fl3/good-web-game)

[example](https://github.com/not-fl3/good-web-game/tree/9b362da6d/examples/simple)

???

![TODO](2019-01-29--web-port-vs-native.jpg)

## itch.io

I've created a page for Zemeroth on itch.io:
[ozkriff.itch.io/zemeroth](https://ozkriff.itch.io/zemeroth)

<https://twitter.com/ozkriff/status/1090615410242785280>

> Created [an itch.io list of Rust games][itch-rust-list].
>
> Also, I've sent a request to itch.io folks to add Rust as an instrument,
> so now a more official list is available:
> [itch.io/games/made-with-rust](https://itch.io/games/made-with-rust).
> Looks like my original list will be deprecated with time but
> it's still useful for now because only authors of the games can add
> an instrument to the metadata.

[itch-rust-list]: https://www.reddit.com/r/rust/comments/arm9dr/a_list_of_itchio_games_written_in_rust

Lots of feedback.

Btw, I've also created an itch.io page for Zone of Control.

## Visual Improvements

Flatten map a little bit and added some shadows

------

Dust effect (jumps) - <https://github.com/ozkriff/zemeroth/pull/390>

> пыль создается одной не очень большой функцией, которая просто создает
> пачку спрайтов и навешивает на них цепочки простых действий перемещения
> и изменения цвета.

------

blood splatters and weapon flashes - <https://github.com/ozkriff/zemeroth/pull/401>

Adds weapon flashes of four types: slash, smash, pierce and claw;
Adds directed dynamic blood splatters.

------

Every agent now has `WeaponType`:

- smash
- slash
- pierce
- claw

For now thay are just a visual information.
They affect only what sprite is used during the attack animation.

> Добавил бойцам параметр WeaponType.
> Пока есть четыре вида: smash, slash, pierce и claw
> и они чисто визуальные - для выбора подходящей текстурки.
> Некоторые спрайты атаки под углами смотрятся странно
> (копейщик, я на тебя смотрю) надо будет потом дополнительные варианты
> добавить и зеркалировать все это хозяйство по ситуации.

(__TODO__: это было в реддите или на гитхабе на английском)

------

Blood splatters.
slowly dissapear in three turns.

Initial draft of the new sprites looked like this:

![__TODO__: description](agents-inkscape-mockup.jpeg)

^ _yeah, Floating Eye and Insecto-snake haven't made it to the master yet._

_Shadows_?

> На макетах выше видно много градиентов. В текущей версии решил отказаться
> от градиентов и всех округлостей, делая акцент на “типа-низкополигональном”
> угловатом стиле. На данный момент игра выглядит вот так: __TODO__.

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

## Game Rules Changes

- Spike traps

- [Updated](https://github.com/ozkriff/zemeroth/pull/351) "Poison" passive ability:
  it can’t, by itself, kill an agent anymore.
  “Poisoned” status is removed when a target’s strength is reduced to 1.
  This should make battles a little bit less frustrating and more dramatic.

- Updates to the "Summon" ability:

  - [Fix 'summon' ability - treat each agent individually](https://github.com/ozkriff/zemeroth/pull/413)

  - [Updated](https://github.com/ozkriff/zemeroth/pull/349) ‘Summon’ ability:
    each use of it now creates one more imp (up to 6).
    It should force the player to be more aggressive.

  - [Changed the summoning algorithm to prefer imp types that are under-presented
    on the map, not just random ones](https://twitter.com/ozkriff/status/1040321852495863808).
    Seems to work fine now - even with increased summon rate imp types
    are balanced in count:

    [img](2018-09-14--map-lines.png)

    This prevents Imp Summoners from being created only a tile away from enemies
    and thus not having any chances to survive.

- __TODO__: Commutative bombs (__TODO__: <https://github.com/ozkriff/zemeroth/pull/296>,
  <https://github.com/ozkriff/zemeroth/issues/286>)

- Teach AI to move closer to targets even if there's no direct path to them

  <https://github.com/ozkriff/zemeroth/pull/308>

## Gameplay Video

So, putting this all together:

__TODO__: _Record a gameplay video_

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

One of the benefits of making a turn-based game is that you can relatively easy
separate the logic from the visuals and cover the former with tests.

Added basic tests scenarios to #Zemeroth and refactored state mutations.

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

## Other Technical Changes

- [Moved all crates to Rust 2018](https://github.com/ozkriff/zemeroth/pull/394);
- [Added a note about 'help-wanted' issues](https://github.com/ozkriff/zemeroth/pull/226)
- [Migrated to `std::time::Duration`](https://github.com/ozkriff/zemeroth/pull/229)
  and added `time_s` helper function (__TODO__: link and explain).
- Fixed a fun bug ([taking control of imp summoners](https://github.com/ozkriff/zemeroth/issues/288))
- [Removed](https://github.com/ozkriff/zemeroth/pull/365) some data duplication
  from [the `.ron` config with objects descriptions][objects_ron]
  using serde's default annotations and helper init functions.
- [Added a `windows_subsystem` attribute](https://github.com/ozkriff/zemeroth/pull/220).
  Don't show cmd window.
- [Fix panic when boulder is pushed into fire/spikes](https://github.com/ozkriff/zemeroth/pull/233);
- [Merge all 'line_height' consts and funcs](https://github.com/ozkriff/zemeroth/pull/431)
- `derive_more::From` for enums and errors;
- [Removed data duplication from `objects.ron`](https://github.com/ozkriff/zemeroth/pull/365)

[objects_ron]: https://github.com/ozkriff/zemeroth_assets/blob/69e6fb34c/objects.ron

## Indikator

[Gave a presentation about Zemeroth][indikator_twit] at 8th Indie-StandUp
at Indikator (previousy known as Indie Space).

__TODO__: What is Indikator? Give a link.

Gave a presentation about Zemeroth at 8th Indie-StandUp in Indie_Space_SPB.

![me presenting Zemeorth at Indikator](2018-11-03--indikator.jpg)

------

[Zemeroth is mentioned on Amit's page about hex math][amit].

[indikator_twit]: https://twitter.com/ozkriff/status/1058359693503070208
[amit]: https://www.redblobgames.com/grids/hexagons/implementation.html

------

## Migrated this devlog from Pelican to Zola

(__TODO__: What is Zola?)

__TODO__: ...

(__TODO__: _link to the twitter thread_)

TLDR:

- Mostly automaticly converted all RestructuredText post sources into Markdown;
- Hyde theme;
- No more disqus comments

------

## Roadmap

What's next?

You can find the roadmap [in the README](__TODO__);

> I want reactions system to be the core of the game. Atm, only basic reactions
> (attacking) is implemented, but I hope to add more interesting behaviors:
> auto-jumping away when an enemy approaches or something
> more aggressive auto-movement (like Muton Berserker from the X-Com).

__TLDR__: Short-term plan is (aka "things I hope to do for v0.6 release):

- improve the GUI;
- [Reduce text overlapping](https://github.com/ozkriff/zemeroth/issues/214)
- ???
- start maintaining a bupic GDD (game design document);
- __TODO__;

------

That's all for today, thanks for reading!

__TODO__:
> I've started a [@rust_gamedev](http://twitter.com/rust_gamedev) twitter account
> in an attempt to create some central point for #rustlang #gamedev stuff on twitter;
> Follow.

**Discussions of this post**:
[/r/rust](__TODO__),
[twitter](__TODO__).

[Zemeroth]: https://github.com/ozkriff/zemeroth
