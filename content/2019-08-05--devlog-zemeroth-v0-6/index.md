+++
title = "Zemeroth v0.6: Renown, Upgrades and Effect Icons"
slug = "2019-08-12--devlog-zemeroth-v0-6"
+++

_**TODO**: move all the images to this repository_

_**TODO**: `.editorconfig`?_

<!-- markdownlint-disable MD013 -->
<!-- cspell:ignore editorconfig reddit -->

Hi, folks! I'm happy to announce **Zemeroth v0.6**.
Main features of this release are:
renown, agent upgrades, visual improvements,
status effect icons, logo
(**TODO**).

**TODO**: _Title GIF demo (or a video)_

[Zemeroth] is my hobby turn-based hexagonal tactics game written in Rust.
You can [download precompiled v0.6 binaries][release v0.6]
for Windows, Linux, and macOS
or [play the online version on itch.io][itch_zemeroth].

**TODO**: some preface

<!-- The last release happened about a year ago.
Since then the development mostly happened in irregular bursts,
sometimes it even was completely stalled for weeks.
But a year is a big period of time anyway, so there're still lots of changes.

Lots of text ahead, feel free to skip sections
that you're not interested in particularly.
Here's a table of contents: -->

I've experimented with weekly logs,
but I failed to make them regularly.
So I decided to at least make releases more often.

Removed planned versions from the roadmap.

It has been seven weeks since the previous devlog video and
so far my plan to make a new devlog video every few weeks totally failed.
Partly because I was on vacation in Germany for a few weeks,
but mostly because I just procrastinate a lot.

But the project still moves on.

[Zemeroth]: https://github.com/ozkriff/zemeroth
[itch_zemeroth]: https://ozkriff.itch.io/zemeroth
[release v0.6]: https://github.com/ozkriff/zemeroth/releases/tag/v0.6.0

## Smaller Releases

_**TODO**: Do I need this section? What should be moved here from the preface?_

readme roadmap removed versions.

Experimented with forum and weekly videos.

I don't really need all of this, I just need to make smaller releases.

<!-- 
Here's my first video devlog ever (_[/r/rust_gamedev discussion](https://www.reddit.com/r/rust_gamedev/comments/bwquqy/zemeroth_dev_vlog_1/)_):

<https://youtu.be/EDoxb7vbqgg>

I hope to keep these videos short and release them every week or two.
-->

## Renown and Upgrades

"Renown" (the term is obviously borrowed from [Banner Saga])
is the currency of the campaign mode.

It's received when you win battles.

The amount that you receive is encoded in [assets/campaign_0.ron]:

![campaign_0.ron content](https://i.imgur.com/PTpdqgP.png)

Recruit options are still hard-coded in the campaign.

Renown is spent between the battles on upgrading your fighters or recruiting new ones.

![TODO](https://i.imgur.com/du8NkAr.png)

Costs and upgrade options are described in a [assets/agent_campaign_info.ron]
config:

^ **TODO**: upgrade used commit (use v0.6's final commit)

```ron
{
    "swordsman": (
        cost: 10,
        upgrades: ["heavy_swordsman", "elite_swordsman"],
    ),
    "elite_swordsman": (
        cost: 15,
    ),
    "heavy_swordsman": (
        cost: 14,
    ),
    "spearman": (
        cost: 11,
        upgrades: ["heavy_spearman", "elite_spearman"],
    ),
    "elite_spearman": (
        cost: 15,
    ),
    . . .
```

Each new fighter costs more. (**TODO**: _how? why? explain more about it_)

If you don't like upgrade options

**TODO**: {show png images and/or inkscape}

and only features "heavy" and "elite" (unbalanced) variations of swordsman and spearman for now.

TODO: heavy_hammerman, healer, firer

heavy variants move slower (only two move points)

TODO: one upgrade path per agent

![upgrade trees](https://i.imgur.com/MYGESBv.png)

TODO: Describe what different properties do they have.

"elite" variants are generally faster and have more abilities or
can use them more often.

"Heavy-*" variants move slower (they have 2 move points instead of 3),
don't have any additional attacks.

Old fighters:

- "hammerman" - becomes a little bit weaker and loses "heavy strike"
  passive ability
- "alchemist" - loses all bombs except for pushing bomb

New fighters:

- "heavy hammerman" - more health, stronger but rarer attacks

    Balance Club ability: reduce duration and remove FlyOff effect

- "healer" - heals better and can throw only poison bomb

- "firer" - can't heal, but can throw bombs & firebombs

TODO: firer: now explosions destroy armor.

THe idea is that the player should never have enough renown to buy everything.

[Banner Saga]: https://bannersaga.gamepedia.com/Renown
[assets/campaign_0.ron]: https://github.com/ozkriff/zemeroth_assets/blob/e3886c064/campaign_01.ron
[assets/agent_campaign_info.ron]: https://github.com/ozkriff/zemeroth_assets/blob/e3886c064/agent_campaign_info.ron

## Visual Improvements

<!-- I've been mostly working on small visual improvements. -->

There're many small visual improvements.

![demo of the tile highlighting](https://i.imgur.com/laN1eaW.gif)

First, a tile under the cursor is highlighted now.
Highlighting is disabled though on touch devices
(by ignoring an event if its delta movement is zero).

![scene with flipped agents](https://i.imgur.com/JDeOhSK.png)

Next, agents now [can be flipped horizontally][pr473]
to match their action's direction.
I've wanted to add this for a long time because sometimes
units were attacking each other backwards and it was weird.

**TODO**: - Small change: Flip weapon flashes horizontally;

![TODO](https://i.imgur.com/XjRMRcd.gif)

[Added][pr471] simple dodge animations when an attack misses

![TODO](https://i.imgur.com/M0C203X.gif)

A helper message is [now shown][pr472]
when an agent's move is interrupted.

![demo](https://i.imgur.com/LydFrfq.gif)

Now [agents have special sprite frames for some abilities][pr476].
It's a compromise between having real animations and only having static pieces.

Also, spearman will get special directional attack frames soon,
because he can attack enemies two tiles away from him
and it looks weird with completely static sprite sometimes.

[pr471]: https://github.com/ozkriff/zemeroth/pull/471
[pr472]: https://github.com/ozkriff/zemeroth/pull/472
[pr473]: https://github.com/ozkriff/zemeroth/pull/473
[pr476]: https://github.com/ozkriff/zemeroth/pull/476

## Agent's Info Screen

Added a basic agent info screen to Zemeroth.
Now you can look up some stats before recruiting or upgrading a fighter.

![agent info screen](https://i.imgur.com/X8iP7Ww.png)

![TODO: description](https://i.imgur.com/IjSu3Ut.png)

**TODO**: Small `[i]` buttons.

## Explosion Ground Marks

Decorative explosion ground marks were added:

![explosion ground marks demo](https://i.imgur.com/EauSc3J.gif)

Same as blood, they're slowly disappearing into transparency in three turns.
To avoid making the battlefield too noisy and unreadable.

## Status Effect Icons

Effect icons were added.

- poisoned (skull)
- stunned (spiral)

![status effect icons demo](https://i.imgur.com/AOf0E1X.png)

I'm hoping to rework how the brief stats are displayed with dots someday,
but for now...

## External Contributions

There were a few PRs from external contributors:

- by [@debris](github.com/debris):
  - ["Bump ggez to version 0.5.0-rc.2"][pr485];
  - ["Highlight buttons on mouse over"][pr490];
  - ["Load sprites from sprites.ron file"][pr486];
- by [@ltfschoen](github.com/ltfschoen):
  - ["docs: Fix logic of insert within zcomponents"][pr491];
  - ["Update readme with instructions to add missing dependencies"][pr488].

[pr485]: https://github.com/ozkriff/zemeroth/pull/485
[pr490]: https://github.com/ozkriff/zemeroth/pull/490
[pr486]: https://github.com/ozkriff/zemeroth/pull/486
[pr491]: https://github.com/ozkriff/zemeroth/pull/491
[pr488]: https://github.com/ozkriff/zemeroth/pull/488

Thanks, folks!

## Other changes

- AI of the Summoner and Bomber imps is tweaked to **TODO** smaller distances;
  "Decrease distance ranges for summoners and bombers";
  Chasing summoners through the whole map with slow heavy fighters isn't fun.
  [pr508]

- "Add a mostly empty explicit rustfmt.toml file" - [pr495]

  [Motivation][i492]

- **TODO**: check PRs

[pr495]: https://github.com/ozkriff/zemeroth/pull/495
[i492]: https://github.com/ozkriff/zemeroth/issues/492
[pr508]: https://github.com/ozkriff/zemeroth/pull/508

## Logo

![TODO: err msg](https://i.imgur.com/nKS1fNv.png)

The game now has a text logo.
It's a manually "low poly vectorized" text written with the Old London font.
Not sure if it really fits the game, but it'll do for now.

## Spreading the Word

There're a couple of non-code updates.

I've added [a "Roadmap" section][roadmap] to the readme
to show in which direction the project moves.

^^^ **TODO**: _this was a part of 0.5 release, isn't it?_

I also added [a new "Inspiration" section][inspiration]
with a list of games that inspire me to work on Zemeroth.

I got the [ozkriff.games](https://ozkriff.games) domain
and move my devlog there.

**TODO**: _actually, I've moved the blo there now_

[fb.com/ozkriff.games] and [vk.com/ozkriff.games] pages were created.

And I've revived my Patreon page: [patreon.com/ozkriff]

_**TODO**: What I'm going to do with it and what are my expectations?_

[fb.com/ozkriff.games]: https://fb.com/ozkriff.games
[vk.com/ozkriff.games]: https://vk.com/ozkriff.games
[patreon.com/ozkriff]: https://patreon.com/ozkriff
[roadmap]: https://github.com/ozkriff/zemeroth/blob/master/README.md#roadmap
[inspiration]: https://github.com/ozkriff/zemeroth/blob/0e789a546/README.md#inspiration

## Bonus

**TODO**: {piece of the video from Indikator} - Visited indikator.

**TODO**: _also, photos were uploaded_

------

(**TODO**: _Don't forget to use some cool final image:
Reddit will use it as a preview_)

That's all for today, thanks for reading!

If you're interested in this project you can follow
[@ozkriff on Twitter][@ozkriff] for fresh news.

Also, if you're interested in Rust game development in general,
you may want to check [@rust_gamedev on Twitter][@rust_gamedev].

<!--
TODO: uncomment when the post is published
**Discussions of this post**:
[/r/rust](TODO),
[twitter](TODO).
-->

[@ozkriff]: https://twitter.com/ozkriff
[@rust_gamedev]: https://twitter.com/rust_gamedev
