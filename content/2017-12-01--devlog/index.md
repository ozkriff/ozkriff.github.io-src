+++
title = "Zemeroth v0.0.3: Jokers, Rancor, Blood and more"
slug = "2017-12-01--devlog"
+++

Hi, comrades! Welcome to the second issue of Zemeroth's devlog.

[Zemeroth] is a turn-based hexagonal tactical game written in Rust.

It slowly grows into a middle-sized project:
[Zemeroth] has [4.3k LoCs] and 82🌟 now.
Though I still can't find enough free time to work on it on daily basis
and I have to take weeks-long breaks sometimes.

So, the progress is quite slow 🐌 but still,
I've managed to do some amount of useful stuff during last three months.
Here's a short video of how the game looks right now:

<div class="youtube"><iframe frameborder="0" allowfullscreen src="https://www.youtube.com/embed/XrC4eCqspUo?rel=0&showinfo=0"></iframe></div>

Ok, let's talk about what exactly have I done for the project during this autumn.

[Zemeroth]: https://github.com/ozkriff/zemeroth
[4.3k LoCs]: https://github.com/Aaronepower/tokei

## [Pre-built binaries][i56]

The most important change for anyone who wants to try out Zemeroth
and don't want to compile it from the source
is auto-deployed pre-built binaries.

**You can download them here:**
**[zemeroth/releases](https://github.com/ozkriff/zemeroth/releases)**

They are compiled and deployed to Github's releases
by CI servers (Travis, Appveyor and CircleCI) on every tag.

[The latest release at the time of writing is `v0.0.3`][v0.0.3]:

[![v.0.0.3 release page](v-0-0-3-release-page.png)][v0.0.3]

Linux/Windows and OSX versions are not that interesting - they are
built exactly like [it was done for ZoC][zoc_i242].

Deploying Android `apk`s is a more interesting story.

I've stolen basic apk-building script for CircleCI from [@tomaka]
(thanks again!) - <https://github.com/tomaka/glutin/pull/919> -
and it worked straight out of the box.

Deploying `apk`s is harder:
circle-ci doesn't provide a built-in convenient way of deploying to Github,
so you have to wield some curl/github_api magic.

[All the magic is packed in .circleci/upload_apk_to_github_releases.sh script][upload_script]
(which is based on [this gist]).

Also, some [strange branch magic is required][branch magic]
if you don't want to run both `build` and `deploy` targets
on _every_ commit.

[branch magic]: https://github.com/ozkriff/zemeroth/blob/efc36eb08/.circleci/config.yml#L20-L33

------

Btw, old badges were not that clear of what do they mean:

![build: passing, build: passing, passed - wtf?](old-badges.png)

Most programmers know that travis's badge usually means
Linux/OSX builds and appveyor is for Windows builds.
But what does the third one?

To fix this
[I've added custom labels to the badges through shields.io][commit with badges]:

```md
https://img.shields.io/travis/ozkriff/zemeroth/master.svg?label=Linux|OSX
https://img.shields.io/appveyor/ci/ozkriff/zemeroth.svg?label=Windows
https://img.shields.io/circleci/project/github/ozkriff/zemeroth/master.svg?label=Android
```

Looks a little bit better now:

![uniform new badges](new-badges.png)

------

_And there're two yet-to-be-solved issues:_

- _[`apk`s are built in the debug mode][i136]_
- _[Deploy precompiled versions of the latest commit to a special release][i161]_

[i56]: https://github.com/ozkriff/zemeroth/issues/56
[i136]: https://github.com/ozkriff/zemeroth/issues/136
[v0.0.3]: https://github.com/ozkriff/zemeroth/releases/tag/v0.0.3
[upload_script]: https://github.com/ozkriff/zemeroth/blob/efc36eb08/.circleci/upload_apk_to_github_releases.sh
[@tomaka]: https://github.com/tomaka
[zoc_i242]: https://github.com/ozkriff/zoc/issues/242
[this gist]: https://gist.github.com/stefanbuck/ce788fee19ab6eb0b4447a85fc99f447
[commit with badges]: https://github.com/ozkriff/zemeroth/pull/158/commits/1f0fc2b75
[i161]: https://github.com/ozkriff/zemeroth/issues/161

## Decorations: Grass and Blood Pools

The [**Grass**][i73] is just a randomly-placed decoration,
but [**Blood Pools**][i42] are also an additional indicator
of a successful attack:

![two tiles of grass](grass.png)
![pool of blood](bool-of-blood.png)

[i42]: https://github.com/ozkriff/zemeroth/issues/42
[i73]: https://github.com/ozkriff/zemeroth/issues/73

## Jokers and Strength

Now, some actual gameplay changes!

To make Zemeroth a little bit more tactical
[**Jokers were added**][i59]. They can be used either as Attacks or Moves.

In the previous version, units were dying from a single hit.
That doesn't work well with reaction attacks as they were dying too quickly:
fighters should have some kind of basic hit points.

[So **Strength** was added.][i63]

This name is stolen from [Banner Saga]:
as I'm going to use this property also as a basic attack modifier.
Right now every successful attack deals a damage of one strength
but later a much more fine-grained battle math will be implemented.

[Banner Saga]: http://store.steampowered.com/app/237990/The_Banner_Saga

## Dots

To show the most important dynamic information about units on the map
[**"Dots"** were added][i95].

![thee agents with different stats showed by color dots](info-dots.png)

The current legend is:

- "Strength" - green;
- "Attacks" - red;
- "Moves" - blue;
- "Jokers" - purple.

------

[@LPGhatguy] [pointed me out on twitter] to a problem with colors:

> With the amount of red/green in the game so far,
> you should try it with a Deuteranopia filter!

I've googled a simulator:
[etre.com/tools/colourblindsimulator](https://www.etre.com/tools/colourblindsimulator).
Here's an example of its output:

![Example of output. Dots are hard to read now](color-issue.png)

And, yeah, that doesn't look readable at all.
[It's clear that I should change the colors and shapes][i98]
in the near future.

*Btw, <http://gameaccessibilityguidelines.com> is a very interesting resource.
I've never thought about a lot of issues raised and explained there.*

[i59]: https://github.com/ozkriff/zemeroth/issues/59
[i63]: https://github.com/ozkriff/zemeroth/issues/63
[i95]: https://github.com/ozkriff/zemeroth/issues/95
[i98]: https://github.com/ozkriff/zemeroth/issues/98
[@LPGhatguy]: https://github.com/LPGhatguy
[pointed me out on twitter]: https://twitter.com/LPGhatguy/status/902800456082001920

## [Info panel with selected unit's stats][i92]

Dots can show only a small portion of the dynamic information about units.
Other less important dynamic or static information goes into the side panel.

![info panel showing imp's stats using text](info-panel.png)

Btw, [now you can select enemy units][i100] to see their move range and stats
in the info panel.

_NOTE: additionally, a deselection of any unit on the second click was added._

[i100]: https://github.com/ozkriff/zemeroth/pull/100
[i92]: https://github.com/ozkriff/zemeroth/pull/92

## [Spearman](https://github.com/ozkriff/zemeroth/issues/65)

![closeup of a spearman](spearman.png)

Another important gameplay change is
an addition of third fighter type: "Spearman".

He has an attack radius of two tiles and
can control with reaction attacks a big area of 18 tiles around him.

![spearman can attack distant enemies](spearman-controls-territory.png)

On the picture above the spearman has only one Joker point:
this is not an attack unit, he's almost useless during his own turn.

But if spearman hasn't used its Joker during his own turn,
he has _four_ reaction attacks during enemy's turn:

![example of a spearman with 4 reactive attacks](spearman-many-reaction-attacks.png)

And that's a lot considering that reaction attacks can interrupt enemy's movement.

Also, this unit has only three Strength points to accent his defence role.

## [Rancör][i141] - a Stupid Component System

Previously, Zemeroth's units were represented by a single struct
holding all the stuff as its fields.
Not a very adaptable solutions and it was impossible
to create a non-unit type of objects.

It's the end of 2017 so the solution to this problem is obviously _components_.

With a component system, I should be able to implement:
[Boulders](https://github.com/ozkriff/zemeroth/issues/142),
[Bombs](https://github.com/ozkriff/zemeroth/issues/69),
Fire,
[Poison stuff](https://github.com/ozkriff/zemeroth/issues/154),
[Corpses](https://github.com/ozkriff/zemeroth/issues/108),
etc.

I don't think Zemeroth needs a full-featured ECS solution
(like [specs](https://github.com/slide-rs/specs)) as the game is turn-based.
A bunch of `HashMap<ObjId, ComponentType>` will do the work fine.

So.. I've reinvented another ~~[bicycle 🚲]~~ square wheel! \o/

[Meet **Rancör** - a simple macro-based component system][i141].
I'm not calling this an ECS because it has no systems, it's just a storage.

Nothing fancy, you just declare some usual structs for components
and create a hidden `HashMap`-based monster-struct using a friendly macro:

```rust
rancor_storage!(Parts<ObjId>: {
    strength: component::Strength,
    pos: component::Pos,
    meta: component::Meta,
    belongs_to: component::BelongsTo,
    agent: component::Agent,
});
```

And then use individual fields:

```rust
parts.agent.insert(id, agent);
...
let agent = self.state.parts().agent.get(id);
if agent.moves == Moves(0) && agent.jokers == Jokers(0) { ... }
...
parts.agent.remove(id);
```

Or call `parts.remove(id);` to completely wipe-out the entity.

------

Rancor seems to work fine, but I see two issues:

- Too many braces in RON file with prototypes
- [Duplication of data between initial values and their base values][duplication]

As I do not expect anyone to use it, this carte lives in the Zemeroth's repo.

*Btw, see <https://gridbugs.org/programming-languages-make-terrible-game-engines>
and <https://gridbugs.org/modifying-entity-component-system-for-turn-based-games>
articles about component systems and turn-based games in Rust.*

[i141]: https://github.com/ozkriff/zemeroth/issues/141
[bicycle 🚲]: https://www.reddit.com/r/rust/comments/6zdvza/my_experience_participating_in_highload_cup_re/dmulhzj
[duplication]: (https://github.com/ozkriff/zemeroth/issues/105#issuecomment-335439037)

## [TOML -> RON](https://github.com/ozkriff/zemeroth/pull/67)

Rust community kinda loves TOML, but I'm not a fan of this format.
TOML is not _that_ bad, but I find its tables too strange for anything
but simple configs.

And I've decided to try to use **[RON]** format for Zemeroth.

_([RON's readme][RON] has a pretty good list of reasons
of why you may not want to use other formats)_

Thanks to [@kvark] for starting this project originally
and thanks to [@torkleyy] for resurrecting the project
[for Amethyst's needs][amethyst_pr269].

[RON]: https://github.com/ron-rs/ron
[@kvark]: https://github.com/kvark
[@torkleyy]: https://github.com/torkleyy
[amethyst_pr269]: https://github.com/amethyst/amethyst/pull/269

## Boulders and Rocks

To make tactics a little bit more interesting
and to prototype non-agent objects using Rancör
I've [added some tile-blocking **Boulders**][i142].
This is a first non-agent object type in the game.

It's a little bit strange that I have different terrain types
support for a long time, but not actually using them in the game at all.
[Meet randomly-placed tiles of **TileType::Rocks** type][pr164].
You can move through these tiles, but it requires 3 move points and not 1.

![a map with some boulders and rock tiles](rocks.png)

Rock tiles and boulders work together with blood and grass to make
the battlefield look a little bit less boring.

_(Yes, I know that it'll be better to use a different texture for Rocks tiles,
not just a darker color)_

[i142]: https://github.com/ozkriff/zemeroth/issues/142
[pr164]: https://github.com/ozkriff/zemeroth/pull/164

## [Logging: `log` & `env_logger`][i83]

I'm tired of adding a special-cased `println`s to debug
something small and removing them before the commit.

As I don't have much experience with slog, I decided
to replace `println`s with a classic [env_logger].
It seems to work, for now,
the source code is filled with all kinds of `info!` and `debug!` calls. :)

[i83]: https://github.com/ozkriff/zemeroth/issues/83
[env_logger]: https://docs.rs/env_logger

## Häte: [Examples](https://github.com/ozkriff/zemeroth/pull/131)

Some news about [my silly game engine][hate's announcement].

[hate's announcement]: https://ozkriff.github.io/2017-08-17--devlog.html#hate2d

It's important to decouple Häte from Zemeroth.
First, Häte was extracted to a separate crate inside the repo.
The next step is to separate example/test screens.

These screens do nothing game-specific so they belong to the engine.

There was a bunch of tasks needed to be solved before extracting the examples:

- [Baked GLSL shaders into Häte's source][i129].
  They are supposed to be dead-simple & tightly coupled with
  the engine - what's the point of having them in user's assets dir?

- [Baked a default font into Häte's source][i130].
  I've used the smallest font from this article:
  <http://oxfordshireweb.com/smallest-file-size-google-web-fonts>.
  `Karla-Regular.ttf` is 17kib only.

- [`Settings::default`][i138]. Simplified the examples.

- [Check assets dir from every `fs::load` call][i32].

[i138]: https://github.com/ozkriff/zemeroth/issues/138
[i129]: https://github.com/ozkriff/zemeroth/issues/129
[i130]: https://github.com/ozkriff/zemeroth/issues/130
[i32]: https://github.com/ozkriff/zemeroth/issues/32

## Häte: [Cache Text Textures][i96]

[ZoC] was almost unusable in debug builds:
[it may take more than 10 seconds to start a game on some machines][zoc_i264]
and now I'm trying to keep Zemeroth's debug builds fast enough.

One of the common problems is that [Rusttype] is very slow in debug builds,
especially on Android.
As a text in Häte is rendered by creating a separate texture for
every string the simplest solution was to cache these textures.

Caching is a little bit sloppy solution, but we have no other choice
until <https://github.com/rust-lang/cargo/issues/1359> is implemented.

_**NOTE**: Btw, there's a [cool hack] from [@matklad],
but you have to compile an outdated cargo from his dev-branch._

[i96]: https://github.com/ozkriff/zemeroth/issues/96
[zoc_i264]: https://github.com/ozkriff/zoc/issues/264
[ZoC]: https://github.com/ozkriff/zoc
[Rusttype]: https://github.com/redox-os/rusttype
[cool hack]: https://github.com/rust-lang/cargo/issues/1359#issuecomment-329653216
[@matklad]: https://github.com/matklad

## "Game Development in Rust"

![me presenting a talk about zoc and zemeroth on spb meetup](spb-meetup.jpg)

There was [a local meetup][meetup] in Saint-Petersburg this September where

- [@not-fl3] talked about his experience as a [SHAR]'s developer
- [@vitvakatu] talked about [three-rs]
- and I talked about the history of [ZoC] and [Zemeroth].

Everything is in Russian, but here are the links anyway, just in case:

- [full video](https://www.youtube.com/watch?v=BCsPcsmRhOM)
- [my slides](https://docs.google.com/presentation/d/19-Vc2VOpmB2r42u5arMVdKXfOPzozNjY5drjhbyIw3E)

![overview of the slides](slides-overview.png)

Thanks to [JetBrains](https://intellij-rust.github.io) for hosting the event!

[meetup]: https://meetup.com/Rust-в-Питере/events/242219775
[@not-fl3]: https://github.com/not-fl3
[@vitvakatu]: https://github.com/vitvakatu
[shar]: https://twitter.com/BringerShar
[three-rs]: https://github.com/three-rs/three

## Short-Range Plans

### RestructuredText -> Markdown

For a long time, I was trying to avoid the use of MD.

Mostly [because MD has no built-in support for extensions and
is MD is forever tied to HTML][MD bad].

I was mostly hoping for RST to become popular enough.
There was a chance, [but doc team decided to stay with MD][no RST for you]
and now Rust community doesn't care about RST at all. :(

[CommonMark] solves the standardization problem to some degree.
Though, it's still glued to HTML and is not easily extensible.

Anyway, I'm not going to use these documents anywhere except in the web browser,
so... [I'm going to migrate this blog to some rust blog generator][i157]
from Pelican. This post is written in MD already.

[MD bad]: https://eli.thegreenplace.net/2017/restructuredtext-vs-markdown-for-technical-documentation
[no RST for you]: https://internals.rust-lang.org/t/rustdoc-restructuredtext-vs-markdown/356
[CommonMark]: http://commonmark.org
[i157]: https://github.com/ozkriff/zemeroth/issues/157

### Abilities and Lasting Effects

A skirmish game is unimaginable without [special abilities]
and some interesting [instant] and [lasting effects] of the actions.

So, here are some previews of what I'm working right now:

- <https://youtu.be/Egfyd4VX2YU> - jump & [knockback](https://github.com/ozkriff/zemeroth/issues/102)
- <https://youtu.be/TilgaGspTJk> - [self-explode](https://github.com/ozkriff/zemeroth/issues/69)
- <https://youtu.be/Yg38yeno3sE> - [poison](https://github.com/ozkriff/zemeroth/issues/154)

[special abilities]: https://github.com/ozkriff/zemeroth/issues/110
[instant]: https://github.com/ozkriff/zemeroth/issues/102
[lasting effects]: https://github.com/ozkriff/zemeroth/issues/154

------

_Whew! That was the longest piece of text in English that I've ever written O.o._

That's all for today! :)

**Discussions**:
[/r/rust](https://www.reddit.com/r/rust/comments/7gy3wx/zemeroths_devlog_2_jokers_rancor_blood_and_more/),
[twitter](https://twitter.com/ozkriff/status/936708540168884224).
