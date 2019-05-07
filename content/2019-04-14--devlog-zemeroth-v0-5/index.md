+++
title = "Zemeroth v0.5: ggez, WASM, itch.io, visuals, AI, campaign, tests"
slug = "2019-04-14--devlog-zemeroth-v0-5"
+++

<!-- markdownlint-disable MD013 -->
<!-- cspell:ignore Berserker Muton kiegel Yururu ldjam devs itchio -->

Hi, folks! I'm happy to announce **Zemeroth v0.5**.
Main features of this release are:
migration to ggez, web version, itch.io page, campaign mode,
AI improvements, visual updates, and tests.

![demo fight](2019-04-29--title-demo.gif)

[Zemeroth] is a turn-based hexagonal tactical game written in Rust.
You can [download precompiled v0.5 binaries][release v0.5]
for Windows, Linux, and macOS.
Also, now you can **[play an online version][itch_zemeroth]**
(_read more about it in the "WebAssembly version" section below_).

![github commits graph](2019-04-27--github-commits.png)

The last release happened about a year ago.
Since then the development mostly happened in irregular bursts,
sometimes it even was completely stalled for weeks.
But a year is a big period of time anyway, so there're still lots of changes.

Lots of text ahead, feel free to skip sections
that you're not interested in particularry.
Here's a table of contents:

- [Migration to the `ggez` game engine](#migration-to-the-ggez-game-engine)
- [WebAssembly version](#webassembly-version)
- [itch.io](#itchio)
- [Visual Improvements](#visual-improvements)
- [Simple campaign mode](#simple-campaign-mode)
- [Hit chances](#hit-chances)
- [Armor](#armor)
- [AI updates](#ai-updates)
- [Other Game Rules Changes](#other-game-rules-changes)
- [Gameplay Video](#gameplay-video)
- [SVG Atlas](#svg-atlas)
- [Tests](#tests)
- [Other Technical Changes](#other-technical-changes)
- [Indikator](#indikator)
- [Migrated this devlog to Zola](#migrated-this-devlog-to-zola)
- [Roadmap](#roadmap)

[release v0.5]: https://github.com/ozkriff/zemeroth/releases/tag/v0.5.0

## Migration to the `ggez` game engine

An experiment with maintaining my own engine
(even a simple and minimalistic 2D one)
turned out to be too exhausting in practice:
you have to fight a constant stream of reports about small corner case issues
and deal with platform-specific tweaks and hacks
(stuff [like this](https://github.com/ggez/ggez/issues/587), for example).
It can consume surprisingly large amounts of time.
But what's is more important for a hobby project,
it also sucks too much fun out of the development process.

And what made it worse in my case is that [Häte2d][docs_hate] intentionally wasn't
a general-purpose game engine (to reduce the scope of work),
so it was sad to know that all this work won't be reused by anyone.
But converting Häte into a real general-purpose engine wasn't an option too,
because it wouldn't have left any time for Zemeroth's development.

So I've surrendered and decided to give away some control over
low-level parts of Zemeroth:
[Häte2d was discontinued][pr247] and replaced by [ggez], the most mature and
actively developed Rust 2d game engine at that time.

![ggez's logo](ggez-logo-maroon-full.svg)

`häte` had some builtin basic
[scene management](https://docs.rs/hate/0.1.0/hate/scene/)
and [GUI](https://docs.rs/hate/0.1.0/hate/gui/) systems,
but ggez is minimalistic by design and has none of this.
So, two helper crates were extracted from Häte2d and rebuilt on top of ggez:

- [ggwp-zscene](https://github.com/ozkriff/zemeroth/tree/721ad06a6/ggwp-zscene)
  is a simple scene/declarative animation manager that provides:
  - Sprites with shared data;
  - Scene and Actions to manipulate sprites;
  - Simple layers;
- [ggwp-zgui](https://github.com/ozkriff/zemeroth/tree/721ad06a6/ggwp-zgui)
  is a tiny and opinionated UI library:
  - Provides only simple labels, buttons and layouts;
  - Handles only basic click event;
  - No custom styles, only the basic one.

Since Icefoxen [asked not to use `ggez-` prefix][ggwp],
I used `ggwp-` ("good game, well played!") to denote that the crate
belongs to ggez's ecosystem, but is not official.

These libraries are still tied to Zemeroth,
not sure how helpful these libraries can be for a project that is not Zemeroth.
You probably won't be able to use them without changes in other games.
But maybe someone will manage ti extract some benefit from them.

These crates are still immature and aren't published on crates.io yet,
while the `rancor` component library was renamed to `zcomponents` and
[is published](https://crates.io/crates/zcomponents).

------

Initially I migrated to ggez v0.4 that was SDL2-based.
But as soon as the first release candidate of [winit]-based ggez v0.5
became available I attempted to migrate to it.
I've filed [a bunch of mostly text-related issues in the process][ggez_issues]
and tried to fix the most critical ones for Zemeroth:
["Remove the generic argument from Drawable::draw"](https://github.com/ggez/ggez/pull/559),
["Drawable::dimensions()"](https://github.com/ggez/ggez/pull/567) (big one!)
and ["Fix Text::dimensions height"](https://github.com/ggez/ggez/pull/593).
These PRs took some time, but then I relatively easy
[ported Zemeroth to ggez v0.5.0-rc.0](https://github.com/ozkriff/zemeroth/pull/426).

ggez v0.5 isn't released yet, so at the moment
Zemeroth uses ggez `0.5.0-rc.1`. It's stable enough for me.

------

![nalgebra logo](2019-05-03--na.png)

Previously, I was using [cgmath] (because it's simple and straightforward).
ggez's "native" math library is nalgebra.
even though ggez v0.5 uses `mint` types for all its public API,
I still migrated to nalgebra, because
of [this](https://users.rust-lang.org/t/cgmath-looking-for-new-maintainers/20406).

------

One downside of the migration is that debug builds are much slower now,
because more code is pure Rust.
Something like 3-5 FPS on my notebook.
But it's ok, I don't need debug builds often,
I prefer debugging through logs anyway.
And even when I really need a debug build to track down something extremely strange,
I can use cargo's yet unstable feature
["profile-overrides" unstable feature][profile_overrides].

```toml
cargo-features = ["profile-overrides"]

[profile.dev.overrides."*"]
opt-level = 2
```

Another serious downside of the engine switch,
[though temporary](https://github.com/ggez/ggez/issues/70),
is that there's no native Android version of the game for now.
But who really needs a native port when you have...

[pr247]: https://github.com/ozkriff/zemeroth/pull/247
[ggez]: https://github.com/ggez/ggez
[docs_hate]: https://docs.rs/hate
[ggwp]: https://github.com/ggez/ggez/issues/373
[winit]: https://github.com/rust-windowing/winit
[cgmath]: https://github.com/rustgd/cgmath
[mint]: https://github.com/kvark/mint
[ggez_issues]: https://github.com/ggez/ggez/issues?q=is%3Aissue+author%3Aozkriff+created%3A%3E2019-01-01
[profile_overrides]: https://doc.rust-lang.org/nightly/cargo/reference/unstable.html#profile-overrides

## WebAssembly version

After ggez v0.5-rc.0 was published, Icefoxen have posted
["The State Of GGEZ 2019"](https://wiki.alopex.li/TheStateOfGGEZ2019),
where among other things he wrote that
a web port is unlikely to happen soon because
a lot of issues in dependencies need to be fixed first.
It could be relatively easy to write a specialized web backend for ggez,
but ggez's philosophy is against having multiple backends.

And that's where [Fedor @not-fl3](https://twitter.com/notfl3) suddenly comes in
with his [good-web-game][good_web_game] WASM/WebGL game engine.

He had been experimenting with 2d web prototypes
([like this one](https://twitter.com/notfl3/status/1079499336243965952))
for some time and used a custom 2d web engine for this.
The API of this engine was heavily inspired by ggez
so he managed to write a partly ggez-compatible wrapper in a weekend.

Colors are slightly off and text rendering if a little bit different,
but otherwise it works nicely and smoothly,
providing the same experience:

[![web version vs native](2019-01-29--web-port-vs-native.jpg)](2019-01-29--web-port-vs-native.jpg)

Zemeroth uses good-web-game for its web version as a quick-n-dirty
immediate solution until a proper WASM support arrives to GGEZ
(there're no plans of making good-web-game some kind of official GGEZ backend
or anything like this).
The currently implemented subset of ggez's API is quite limited
and while it may be used for something else that Zemeroth,
it will probably require a lot of work to do.

You can't use crate renaming in `Cargo.toml` to reuse a name on different platforms,

```toml
# Cargo.toml with this dependencies wouldn't build:

[target.'cfg(not(target_arch = "wasm32"))'.dependencies]
ggez = "0.5.0-rc.1"

[target.'cfg(target_arch = "wasm32")'.dependencies]
ggez = { git = "https://github.com/not-fl3/good-web-game", package = "good-web-game" }
```

So the crate substitution hack is done in `main.rs`
using `extern crate` items in `main.rs`:

```rust
#[cfg(not(target_arch = "wasm32"))]
extern crate ggez;

#[cfg(target_arch = "wasm32")]
extern crate good_web_game as ggez;
```

99.9% of code stays the same,
but I had to use a separate main, because good-web-game
has a different initialization API:

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

Finally, a short helper script `utils/wasm/build.sh` was added:

```sh
#!/bin/sh
cp -r assets static
cp utils/wasm/index.html static
ls static > static/index.txt
cargo web build
```

- [cargo-web] only packs a `static` directory (it's hardcoded),
  so the script copies the game's assets there;
- the `index.html` template page is also copied there;
- all assets should be listed in `index.txt` for good-web-game to be able
  to load them, so this file is created;

You can find a minimal example of good-web-game
[here](https://github.com/not-fl3/good-web-game/tree/9b362da6d/examples/simple).

[good_web_game]: https://github.com/not-fl3/good-web-game
[cargo-web]: https://github.com/koute/cargo-web

## itch.io

The web version needs to be hosted somewhere.
[itch.io](https://itch.io/) is a nice place for this:

__[ozkriff.itch.io/zemeroth][itch_zemeroth]__

it has a nice and simple UI (for both developers and consumers),
it's extremely [easy to upload an web game there](https://itch.io/docs/creators/html5)
and it's a relatively known store for a indie games that can provide
some exposure by itself.

[![screenshot of the itch.io page](2019-05-02--itch-ozkriff.png)](https://ozkriff.itch.io)

------

Note an "Enter fullscreen" button in the bottom right corner
of the game area:

!["enter fullscreen" button](2019-04-26-wasm-fullscreen-button.png)

------

As I've said in the ggez section above,
the web version of the game seems to work fine on most mobile devices:

![web version on android device](2019-05-04--android-wasm.jpg)

------

Created [an itch.io list of Rust games][itch_rust_list].
When I find a Rust game on itch.io I add it there.

Also, I've sent a request to itch.io folks to add Rust as an instrument,
so now a more official list is available:
[itch.io/games/made-with-rust](https://itch.io/games/made-with-rust)
(you can edit a game's instruments here: "edit game" -> "metadata" -> "engines & tools").
Looks like my original list will be deprecated with time but
it's still useful for now because only authors of the games can add
an instrument to the metadata.

------

With a playable version only a click away
I received a lot of fresh feedback:
a lot of people that previously were only following the development
now actually tried to play the game.

The most important things people want to see improved are:

- Improve the GUI: Replace text buttons with icons, show some tooltips, etc;
- Add a tutorial or at least a short guide;
- Randomness is too frustrating: missed attacks should result in some
  little positive effect, like pushing enemies back or reducing their stamina;
- Game lacks ranged attack units, like archers or knife throwers.

------

@Yururu even wrote
[a giant comment](https://itch.io/post/660275) on the itch page!
It's inspiring when
a stranger from the internet breaks through the crude primitive interface,
figures out game mechanics on a quite deep level,
and writes a detailed review of their experience and thoughts.

------

Btw, I've also created [an itch.io page for Zone of Control][itch_zoc].

[wasm_twit]: https://twitter.com/ozkriff/status/1090615410242785280
[itch_rust_list]: https://www.reddit.com/r/rust/comments/arm9dr/a_list_of_itchio_games_written_in_rust
[itch_zoc]: https://ozkriff.itch.io/zoc

## Visual Improvements

[Initial draft](https://twitter.com/ozkriff/status/975827153056075776)
of the new sprites looked like this:

![New style mockup](agents-inkscape-mockup.jpeg)

Tiles are flatten now.
It's less a schematic top-down view as it was before.
"Camera" is moved to the side so the tiles and agents are shown
using the same projection.

There're many gradients in the mockup image above.
Later I decided to get rid of all thegradients and curvy lines
and stick with "pseudo lowpoly" style.

Floating Eye and Insecto-snake from the mockup haven't made it to the master yet.

------

All objects now have a shadow.
It makes the image a little bit more tangible.
Walk and especially throw animations feels better now.

Initially shadow was an ellipse with gradient.
Later it was replaced by two semi-transparent hexagons
for style consistency.

------

(__TODO__: demo gif)

[Dust effect (for jumps and throws)](https://github.com/ozkriff/zemeroth/pull/390)
The dust effect is created by a simple function
that just emits a bunch of half-transparent sprites
and attaches position and color change actions to them.
Sprites' size, velocity and transparacy is a little bit randomized.

------

[Added blood splatters and weapon flashes](https://github.com/ozkriff/zemeroth/pull/401)
to make attacks more dramatic:

(__TODO__: demo gif - _use github's title gif for this_?)

Direction of the blood splatter is opposite of attack's direction.
Number of drops depends on the attack's damage.
Blood slowly disappears into transparency in three turns,
otherwise the battlefield would become a complete and unreadable mess.

Adds weapon flashes of four types: slash, smash, pierce and claw;
Every agent now has `WeaponType`: "smash", "slash", "pierce", and "claw".
For now they are just a visual information.
They affect only what sprite is used during the attack animation.

Same as agent sprites, weapon flash sprites are not yet mirrored horizontally.
That is mostly noticeable with curvy smash sprite.

Also, spearman's "pierce" weapon sprite is horizontal and it looks weird
during vertical attacks.
Either multiple sprites are need or
it should be rotated.

## Simple campaign mode

Basic campaign mod.
It's just a linear sequence of battles with predefined scenarios.
After each battle your survived fighters are carried over to the next battle.
If you loose a battle - campaign is over for you.
If you win a battle, you're shown a transition screen with a list
of your dead fighters, your current squad and possible recruits:

![Campaign screen example](2018-11-15--first-iteration-of-a-campaign-mode.png)

Campaign is defined by a [RON][ron] config file with this structure:

```text
initial_agents: ["swordsman", "alchemist"],
nodes: [
    (
        scenario: (
            map_radius: (4),
            rocky_tiles_count: 8,
            objects: [
                (owner: Some((1)), typename: "imp", line: Front, count: 3),
                (owner: Some((1)), typename: "imp_bomber", line: Middle, count: 2),
            ],
        ),
        award: (
            recruits: ["hammerman", "alchemist"],
        ),
    ),
    (
        scenario: (
            rocky_tiles_count: 10,
            objects: [
                (owner: None, typename: "boulder", line: Any, count: 3),
                (owner: None, typename: "spike_trap", line: Any, count: 3),
                (owner: Some((1)), typename: "imp", line: Front, count: 4),
                (owner: Some((1)), typename: "imp_toxic", line: Middle, count: 2),
                (owner: Some((1)), typename: "imp_bomber", line: Back, count: 1),
                (owner: Some((1)), typename: "imp_summoner", line: Back, count: 2),
            ],
        ),
        award: (
            recruits: ["swordsman", "spearman", "hammerman"],
        ),
    ),
]
```

Here's some real campaign scenario:
[campaign_01.ron](https://github.com/ozkriff/zemeroth_assets/blob/acd9fe9ef/campaign_01.ron)

There's a known bug that you can exit from a battle that is not going well
at any moment to start again.
This will be forbidden - permadeath is the only way :) .

## Hit chances

I've added `attack_accuracy` and `dodge` stats to the `Agent` component and
[used these fields for some basic hit chances math](https://github.com/ozkriff/zemeroth/pull/370).

When you select an agent that can attack
(has an attack point and enemies in range)
a hit chance is shown over all aviable targets.

During the attack animation a hit chance is shown near
the attacker with a smaller font.
This was added in order for player to see how dangerous enemy attacks are.

![Hit chances demo](2018-09-29--old-hit-chances-demo.gif)

^ __TODO__: _this gif needs to be updated!_

------

Also, wounded agents now become less accurate.
Each lost strength point results in -10% hit chance penalty (up to -30%).

Missing strength points (wounds) are shown by almost transparent green dots:
![demo of transparent strength points](2018-10-04--transparent-dots.png)

This gameplay change has two game balance consequences:

- Now it's more important to wound enemies,
  finishing them off is a lower priority most of the time.
  Sometimes wounded enemies even can be helpful to the player,
  because they are not a real threat to player's fighters,
  but can block the path for other enemies;
- Alchemist's "heal" ability become important
  because your agents are less useful when wounded too.

Also, attacks with strength > 1 have additional hit chances - with reduced damage
(each attack strength point gives 10% hit chance improvement).
This emulates the situation when an attacker barely touches their target
but still manages to make some damage to it.

## Armor

Implemented a basic armor system.
Armor points is shown above the agent in one line with strength points
using the yellow dots.
Each armor point deflects one damage point on each attack.
Some weapons can break armor (the `attack_break` parameter).
Fire and poison ignore armor.

Here's a little demo:

![old armor demo](2018-09-16--old-armor-demo.gif)

- an imp can't break armor so he can't deal any damage to the heavy swordsman;
- toxic imp can't deal any direct damage but he poisons the swordsman
  ignoring the armor;
- insecto-snake destroys the armor with a powerful attack.

In the current version of the game only the imp summoner has the armor,
so be carefull with them.

## AI updates

Now, enemies always act in order of remoteness from a player's fighters.
This way melee imps don't trip over each other too much.

------

Non-melee imps (bombers and summoners) are now trying to keep
distance in range.
They need to avoid melee fights but still be able to throw bombs
at a player's fighters or summon new imps nears the frontline.
Summoner have a greater min/max range than bombers.

(__TODO__: add demo gif)

------

AI now moves closer to its targets even if there's no direct path to them:

[![new pathfinding demo](2018-06-04--ai-pathfinding-demo.gif)](https://youtu.be/09ODLL_Nu8w)

^ _click on the image to see the full demo_

------

During the debugging of the abovementioned features
I also wrote a simple helper function `dump_map` that takes a closure
and dumps required map data as an ascii.
In this case, pic 1 shows objects and pic 2 shows available positions:

(__TODO__: gif demo from imgur)

## Other Game Rules Changes

- Spike traps were added.

  (__TODO__: describe how they work)

  (__TODO__: add an image)

- [Updated](https://github.com/ozkriff/zemeroth/pull/351) "Poison" passive ability:
  it can’t, by itself, kill an agent anymore.
  “Poisoned” status is removed when a target’s strength is reduced to 1.
  This should make battles a little bit less frustrating and more dramatic.

- Updates to the "Summon" ability:

  [Fixed 'summon' ability - treat each agent individually](https://github.com/ozkriff/zemeroth/pull/413)

  [Updated](https://github.com/ozkriff/zemeroth/pull/349) ‘Summon’ ability:
  each use of it now creates one more imp (up to 6).
  It should force the player to be more aggressive.

  [Changed the summoning algorithm to prefer imp types that are under-presented
  on the map, not just random ones](https://twitter.com/ozkriff/status/1040321852495863808).
  Seems to work fine now - even with increased summon rate imp types
  are balanced in count: [img](2018-09-14--map-lines.png).
  This prevents Imp Summoners from being created only a tile away from enemies
  and thus not having any chances to survive.

- __TODO__: Commutative bombs (__TODO__: [PR](https://github.com/ozkriff/zemeroth/pull/296),
  [issue](https://github.com/ozkriff/zemeroth/issues/286))

<!-- TODO: spell-checker:disable -->

> [PR  #360 "Don't create agents near enemies"](https://github.com/ozkriff/zemeroth/pull/360)
>
> [PR ##369 "Arrange created objects in 'Line's"](https://github.com/ozkriff/zemeroth/pull/369))
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

<!-- TODO: spell-checker:enable -->

## Gameplay Video

So, putting these gameplay changes together:

(**_TODO: Record a gameplay video. A campaign walkthrough maybe?_**)

## SVG Atlas

And now back to more technical updates.

[![TODO](2018-07-16--svg-atlas-test.png)](2018-07-16--svg-atlas-test.png)

[svg atlas](https://github.com/ozkriff/zemeroth_assets_src/blob/846a45b7c/atlas.svg)

[export.py](https://github.com/ozkriff/zemeroth_assets_src/blob/846a45b7c/export.py)

> 2018.07.16: Testing a simple python export script that extracts named objects
> from an `.svg` atlas. Colored backgrounds are for debug purposes.

...

> Atlas is the "original file" now, so I just edit the sprite here.
> Linking external svg files is surprisingly difficult in inkscape (or svg in general? not sure).

...

<!-- TODO: spell-checker:disable -->

> При реализации атласа пришлось вставить костыль для регулировки размера
> экспортируемых спрайтов: в каждой именнованной группе объектов находится
> обычно невидимый квадрат (прямоугольник для клеток) нужного количества пикселей.
> Для отладки их даже можно временно делать видимыми, бывает удобно: ...

<!-- TODO: spell-checker:enable -->

Resource hashes - md5. Travis check.

<!-- TODO: spell-checker:disable -->

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

<!-- TODO: spell-checker:enable -->

## Tests

One of the benefits of making a turn-based game is that you can relatively easy
separate the logic from the visuals and cover the former with tests.

Added basic tests scenarios to #Zemeroth and refactored state mutations.

Test scenarios are completely deterministic.
Randomness is canceled out with special agent types + special debug flag in
game's state that causes a panic if you try to do anything with uncertain results

Main issue is randomness.

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

[colin-kiegel/rust-pretty-assertions](https://github.com/colin-kiegel/rust-pretty-assertions)

Woo-hoo

## Other Technical Changes

- `derive_more::From` for enums and errors;
- [Moved all crates to Rust 2018](https://github.com/ozkriff/zemeroth/pull/394);
- [Added a note about 'help-wanted' issues](https://github.com/ozkriff/zemeroth/pull/226)
- [Migrated to `std::time::Duration`](https://github.com/ozkriff/zemeroth/pull/229)
  and added `time_s` helper function (__TODO__: link and explain).
- Fixed a fun bug ([taking control of imp summoners](https://github.com/ozkriff/zemeroth/issues/288))
- [Removed](https://github.com/ozkriff/zemeroth/pull/365) some data duplication
  from [the `.ron` config with objects descriptions][objects_ron]
  using serde\`s default annotations and helper init functions.
- [Added a `windows_subsystem` attribute](https://github.com/ozkriff/zemeroth/pull/220).
  Don't show cmd window.
- [Fix panic when boulder is pushed into fire/spikes](https://github.com/ozkriff/zemeroth/pull/233);
- [Merge all 'line_height' consts and functions](https://github.com/ozkriff/zemeroth/pull/431)
- [Removed data duplication from `objects.ron`](https://github.com/ozkriff/zemeroth/pull/365)

[objects_ron]: https://github.com/ozkriff/zemeroth_assets/blob/69e6fb34c/objects.ron

## Indikator

[Gave a presentation about Zemeroth][indikator_twit] at 8th Indie-StandUp
at [Indikator](http://indierocket.ru).
It went pretty good, local indie devs seemed to like the project,
especially considering that it's opensource and uses an interesting tech.
At least one of the devs has visited
[our local rustlang meetup](https://www.meetup.com/spbrust) afterwards. 🦀

![me presenting Zemeroth at Indikator](2018-11-03--indikator.jpg)

Also, [Zemeroth was mentioned on Amit's page about hex math][amit].

[indikator_twit]: https://twitter.com/ozkriff/status/1058359693503070208
[amit]: https://www.redblobgames.com/grids/hexagons/implementation.html

## Migrated this devlog to Zola

Migrated this devlog from Pelican to Zola

(__TODO__: What is Zola?)

__TODO__: ...

[Twitter thread](https://twitter.com/ozkriff/status/1119212330246656002)

TLDR:

- Mostly automatically converted all RestructuredText post sources into Markdown;
- Hyde theme;
- No more Disqus comments

------

<!--

## Roadmap

What's next?

You can find the roadmap [in the README](__TODO__);

> I want reactions system to be the core of the game. Atm, only basic reactions
> (attacking) is implemented, but I hope to add more interesting behaviors:
> auto-jumping away when an enemy approaches or something
> more aggressive auto-movement (like Muton Berserker from the X-Com).

__TLDR__: Short-term plan is (aka "things I hope to do for v0.6 release):

- improve the GUI: replace text buttons with icons (__TODO__: link to an issue);
- [Reduce text overlapping](https://github.com/ozkriff/zemeroth/issues/214)
- ???
- start maintaining a basic GDD (game design document);
- agent upgrade trees (__TODO__: link to an issue);
- __TODO__;

-->

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
[itch_zemeroth]: https://ozkriff.itch.io/zemeroth
[ron]: https://github.com/ron-rs/ron
