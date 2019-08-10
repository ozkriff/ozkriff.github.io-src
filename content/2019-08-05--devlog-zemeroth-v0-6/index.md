+++
title = "Zemeroth v0.6: Renown, Upgrades and Effect Icons"
slug = "2019-08-12--devlog-zemeroth-v0-6"
+++

<!-- markdownlint-disable MD013 -->
<!-- cspell:ignore Berserker Muton kiegel Yururu ldjam devs itchio PNGs -->

Hi, folks! I'm happy to announce **Zemeroth v0.6**.
Main features of this release are:
**TODO**.

**TODO**: _Title GIF demo (or a video)_

**TODO**: merge two intros

[Zemeroth] is my hobby turn-based tactics game.
It's an open-source project that lives on GitHub and is written in the Rust programming language.
You can download latest development builds or play the online version on itch.io.

[Zemeroth] is a turn-based hexagonal tactical game written in Rust.
You can [download precompiled v0.6 binaries][release v0.6]
for Windows, Linux, and macOS.
Also, now you can **[play an online version][itch_zemeroth]**.
s
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

**TODO**: _table of contents_

[release v0.6]: https://github.com/ozkriff/zemeroth/releases/tag/v0.6.0

It has been seven weeks since the previous devlog video and
so far my plan to make a new devlog video every few weeks totally failed.
Partly because I was on vacation in Germany for a few weeks,
but mostly because I just procrastinate a lot.

But the project still moves on.

## Renown and Upgrades

"Renown" (the term is obviously borrowed from [Banner Saga](https://bannersaga.gamepedia.com/Renown))
is the currency of the campaign mode.

It's received when you win battles.

The amount that you receive is encoded in [assets/campaign_0.ron](https://github.com/ozkriff/zemeroth_assets/blob/e3886c064/campaign_01.ron):

![campaign_0.ron content](https://i.imgur.com/PTpdqgP.png)

Recruit options are still hard-coded in the campaign.

Renown is spent between the battles on upgrading your fighters or recruiting new ones.

![TODO](https://i.imgur.com/du8NkAr.png)

Costs and upgrade options are described in a [assets/agent_campaign_info.ron](https://github.com/ozkriff/zemeroth_assets/blob/e3886c064/agent_campaign_info.ron) config:

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

Each new fighter costs more.

If you don't like upgrade options

{show png images and/or inkscape}

and only features "heavy" and "elite" (unbalanced) variations of swordsman and spearman for now.

TODO: heavy_hammerman, healer, firer

heavy variants move slower (only two move points)

TODO: one upgrade path per agent

![upgrade trees](https://i.imgur.com/MYGESBv.png)

TODO: Describe what different properties do they have.

"elite" variants are generally faster and have more abilities or can use them more often.

"Heavy-*" variants move slower (they have 2 move points instead of 3),
don't have any additional attacks.

Old fighters:

- "hammerman" - becomes a little bit weaker and loses "heavy strike" passive ability
- "alchemist" - loses all bombs except for pushing bomb

New fighters:

- "heavy hammerman" - more health, stronger but rarer attacks

    Balance Club ability: reduce duration and remove FlyOff effect

- "healer" - heals better and can throw only poison bomb

- "firer" - can't heal, but can throw bombs & firebombs

TODO: firer: now explosions destroy armor.

THe idea is that the player should never have enough renown to buy everything.

## First video devlog, visual updates, spreading the word (TODO: remove?)

Here's my first video devlog ever (_[/r/rust_gamedev discussion](https://www.reddit.com/r/rust_gamedev/comments/bwquqy/zemeroth_dev_vlog_1/)_):

<https://youtu.be/EDoxb7vbqgg>

I hope to keep these videos short and release them every week or two.

## Visual Improvements

I've been mostly working on small visual improvements.

![TODO](https://i.imgur.com/laN1eaW.gif)

First, a tile under the cursor is highlighted now.
Highlighting is disabled though on touch devices
(by ignoring an event if its delta movement is zero).

![TODO](https://i.imgur.com/JDeOhSK.png)

Next, agents now [can be flipped horizontally](https://github.com/ozkriff/zemeroth/pull/476)
to match their action's direction.
I've wanted to add this for a long time because sometimes
units were attacking each other backwards and it was weird.

![TODO](https://i.imgur.com/XjRMRcd.gif)

[Added](https://github.com/ozkriff/zemeroth/pull/471)
simple dodge animations when an attack misses

![TODO](https://i.imgur.com/M0C203X.gif)

A helper message is [now shown](https://github.com/ozkriff/zemeroth/pull/472)
when an agent's move is interrupted.

![demo](https://i.imgur.com/LydFrfq.gif)

Now [agents have special sprite frames for some abilities](https://github.com/ozkriff/zemeroth/pull/476).
It's a compromise between having real animations and only having static pieces.

Also, spearman will get special directional attack frames soon,
because he can attack enemies two tiles away from him
and it looks weird with completely static sprite sometimes.

## Spreading the Word

There're a couple of non-code updates.

I've added [a "Roadmap" section](https://github.com/ozkriff/zemeroth/blob/master/README.md#roadmap)
to the readme to show in which direction the project moves.

I also added [a new "Inspiration" section](https://github.com/ozkriff/zemeroth/blob/0e789a546/README.md#inspiration) with a list of games that inspire me to work on Zemeroth.

![TODO: err msg](https://i.imgur.com/nKS1fNv.png)

The game now has a text logo. It's a manually "low poly vectorized" text written with the Old London font. Not sure if it really fits the game, but it'll do for now.

I got the [ozkriff.games](http://ozkriff.games) domain (but haven't created a landing page there yet, so it redirects to the devlog for now).

[fb.com/ozkriff.games](https://fb.com/ozkriff.games) and [vk.com/ozkriff.games](https://vk.com/ozkriff.games) pages were created.

And I've revived my Patreon page:

<https://patreon.com/ozkriff>

That's all news for today. :)

## Agent's Info Screen

Added a basic agent info screen to Zemeroth. Now you can look up some stats before recruiting or upgrading a fighter.

![agent info screen](https://i.imgur.com/X8iP7Ww.png)

**TODO**: Small `[i]` buttons. (TODO: image)

**TODO**: ![TODO: description](https://i.imgur.com/IjSu3Ut.png)

## Explosion Ground Marks

Decorative explosion ground marks were added.

Same as blood, they're slowly disappearing into transparency in three turns.
To avoid making the battlefield too noisy and unreadable.

![explosion ground marks demo](https://i.imgur.com/EauSc3J.gif)

## Status Effect Icons

Effect icons were added.

- poisoned (skull)
- stunned (spiral)

![TODO](https://i.imgur.com/AOf0E1X.png)

I'm hoping to rework how the brief stats are displayed with dots someday, but for now...

## PRs from External Contributors

There're a few PRs from external contributors:

- by [@debris](github.com/debris):
  - ["Bump ggez to version 0.5.0-rc.2"](https://github.com/ozkriff/zemeroth/pull/485);
  - ["Highlight buttons on mouse over"](https://github.com/ozkriff/zemeroth/pull/490);
  - ["Load sprites from sprites.ron file"](https://github.com/ozkriff/zemeroth/pull/486);
- by [@ltfschoen](github.com/ltfschoen):
  - ["docs: Fix logic of insert within zcomponents"](https://github.com/ozkriff/zemeroth/pull/491);
  - ["Update readme with instructions to add missing dependencies"](https://github.com/ozkriff/zemeroth/pull/488);

Thanks, folks!

## Other changes

- AI of the Summoner and Bomber imps is tweaked to **TODO** smaller distances;
  "Decrease distance ranges for summoners and bombers";
  Chasing summoners through the whole map with slow heavy fighters isn't fun.
  <https://github.com/ozkriff/zemeroth/pull/508>

- Small change: Flip weapon flashes horizontally;
- "Add a mostly empty explicit rustfmt.toml file" - <https://github.com/ozkriff/zemeroth/pull/495>

  Motivation: <https://github.com/ozkriff/zemeroth/issues/492>

- **TODO**: check PRs

## Bonus

{piece of the video from Indikator} - Visited indikator.

------

That's all for today, thanks for reading!

If you're interested in this project you can follow
[@ozkriff on Twitter](https://twitter.com/ozkriff) for more news.

Also, if you're interested in Rust game development in general,
you may want to check [@rust_gamedev on Twitter](http://twitter.com/rust_gamedev).

**Discussions of this post**:
[/r/rust](TODO),
[twitter](TODO).

[Zemeroth]: https://github.com/ozkriff/zemeroth
[itch_zemeroth]: https://ozkriff.itch.io/zemeroth
[ron]: https://github.com/ron-rs/ron
