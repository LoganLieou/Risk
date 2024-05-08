---
author: Logan Jackson
date: \today{}
title: Risk Assessment Model for Arbitrage in Eve Online
header-includes: |
    \usepackage{geometry}
    \geometry{margin=0.5in}
---

## Introduction

In real life arbitrage is the act exploiting price differences across markets. Typically, the problems associated with
arbitrage are identifying these prices differences and executing trades as quickly as possible. In Eve
Online however, the game tells you exactly where these opportunities are available and in what markets, speed is also
not much of a concern as you must physically travel in game to the station (market) where this opportunity exists. The
main issue arises from the physically traveling part. Identifying good opportunities for arbitrage then becomes an
assessment of risk, as in the game you can be attacked by other players and lose everything you have. In this paper
I propose a model for assessing the risk associated with a given run.

## Broad Overview

In this paper I assume risk is the expected conditional profit $\pi{}$ want to
find $\pi{}(S_0, t | \gamma{}, k)$ where $k$ is capital invested $S_0$ the
initial profit at time $t = 0$ and $t$ is expected time to end finally,
$\gamma{}$ is the joint pdf representing the likelihood a player will die to a
gank on a given route. Note, $\pi{}$ is not a joint pdf but rather refers to a
pdf conditioned only on random variable $t$ where $S_0$ is constant, the only
reason I'm including $S_0$ is for future reference, as the model is built out.
Additionally, note that this is only a starting point and a further more
complex model should be built on top of this to get an even more accurate
picture of the risk.

## Further Research Currently Required to Complete the Paper
 - At what rate does the security level across null sec change
 - What is $\lambda{}$ for jumps
 - What is a good function for $r \propto{} k$
 - Pilot quantifiers
 - Weights for gank pdf

