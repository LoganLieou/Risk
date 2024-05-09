---
author: Logan Jackson
date: \today{}
title: Optimal Selection Model for Arbitrage in Eve Online
header-includes: |
    \usepackage{geometry}
    \geometry{margin=1in}
---

## Introduction

Arbitrage in Eve Online is an interesting problem because imagine you were to
buy a TV on Facebook Marketplace to sell on Ebay for 20% more but instead of
going to pick up the TV and driving home with it there was a high liklihood you
get carjacked and robbed on the way home the question then becomes when is it a
good idea to go pick up the TV.

## Broad Overview

There's four parts to a model for arbitrage in Eve Online first, we need to
identify canidates i.e. what are potentially profitable trades? Second there's
some amount of time it will take to execute the trade, so we need to have some
idea of future price, in Eve trades take quite a while, we can estimate the
time given path length $n$ and the rate parameter $\lambda{}$ (time to jump
follows a poisson distrobution) after this we can construct a 98% confidence
interval for the price of the asset at time $t$ using the asset's variance
retrieved from historic data, monte carlo simulation, and geometric brownian
motion. Third we need to calculate the probability of failure, as of right now
this is somewhat hard to do it's possible to use machine learning here as a
truly accurate picture will need to pull data from the player themselves as
it's somewhat difficult to quantify a pilot's skill, so for now I have a fairly
generic function $P(F) = P(g) * P(d)$ where $g$ is probability of getting
ganked and $P(d)$ is the probability of dying to a gank. Lastly since the
result of failure is total loss of all invested capital the problem is somewhat
similar to something like gambling, hence I use the kelly criterion here to
estimate the maximum ratio of net capital to invest in a given run, plugging in
the previous values we calculated: $f^* = (1 - P(F)) - \frac{P(F)}{b}$ where
$b$ is our payout in this case expected profit $\pi{}$ which is estimated in
the second step.

## Research Currently Required to Complete the Paper
 - At what rate does the security level across null sec change
 - What is $\lambda{}$ for jumps

## Notes

Death function $d$ is related to capital $k$ and gank function $\gamma{}$ is
related to security level $s$ these two functions we assume are independent
i.e. weather or not you get ganked is not related to how likely you are to die
to a gank (this is probably not true since both should be dependent on $k$) I
think $\gamma{} \propto{} \frac{1}{s}$ and $d \propto{} -k^2$ I think you can
use MLE to estimate $d$ as well with a general shape and some parameters.

