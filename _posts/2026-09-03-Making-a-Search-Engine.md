---
layout: post
title: "i'm making a search engine"
author: "Yusuf Gürdoğan"
tags: search-engine, sofya
---

it's live at [search.sofya.co](https://search.sofya.co), please search for whatever you like and see how the results are. and know that inshallah it's going to be much better than this!

## top 10 search engines by index size
index size is usually not public, so here are the best estimates.

| # | Engine | Best figure |
|---|---|---|
| 1 | **Google** | ~500–600B pages |
| 2 | **Bing** | ~100–200B pages |
| 3 | **Yandex** | ~200B documents |
| 4 | **Perplexity** | 200B+ URLs |
| 5 | **Yep (Ahrefs)** | ~100B pages |
| 6 | **Sogou** | 50B+ pages |
| 7 | **Brave** | 40B+ pages |
| 8 | **Baidu** | 30B+ pages |
| 9 | **Qwant / EUSP** | ~20B pages |
| 10 | **Mojeek** | ~9.2B pages |

what i have is a server with 2x4TB NVMe SSD, 128GB RAM, 24 cores of a brand new AMD EPYC CPU. so it's one big box.

currently the index size of sofya is 744 million. and i believe this server will be able to have an index size of up to 2 billion.

so, does that mean, if i had 9 more servers like this, i can get into the top 10 with a 20B index size?

## metric for success
you are a restaurant owner. you look at your reviews once in a while and see some people say bad things about how the food tastes. then you try to fix that. then 5 months later you realize that bad reviews still keep coming.

better one would be that you eat from your own restaurant every day and see what can be better or what can be fixed. "it tastes much better, what changed?" you could say. and whatever has changed, would be implemented permanently.

now i don't know much about restaurants. but if you ran a competition, like, 10 people cook the same dish, you[^taste] taste each one, pick whichever tastes best, and hire that person, that'd be even better.

[^taste]: if you are not sure if your own taste represents your customers, gotta have better reviewer(s) of food.

is there a single best food, no. but you can definitely increase the general likeability of it, or whatever else that you are evaluating for.

## how to make the best search engine?
some ideas:
- see how the successful ones did it and learn from them.
- make an eval for it. this works: when you make a number, such that, that number represents your success, "make number go up" can become your only goal, and for that, "try out stuff, see what works, double down" just works.
- if sofya could have 80% of their quality while having 1% of their index size, that'd be amazing. currently, it's about 0.1% of their size while getting about half of their result quality on my own benchmark.

## limits of physics is the ceiling
in a search engine, there are so many parts where i could push the limits harder.
- speed of crawling the web (PPS: Pages Per Second)
- index size that fits in a given machine
- query speed

this is where i always believe that the room for growth is massive. i can always try a better algorithm.

a good question to ask is: "how far we are away from the limits of physics in <....>"? the blank part can be anything like crawl speed, index size, query speed... you name it.

a good way to build is, first, make it work.

does it work? yes. now make it faster.

is it faster? is it the fastest? where's the physical limit, and where are we at now in %?

## so many engineering challenges
- how do you know if a site is reputable?
- you have a user query, and among millions of pages to select from, how do you pick the top 10 results, in the fastest way possible?
- how do you know which pages you should crawl?
- how do you rank results well without any user data?
- how to eliminate/punish spammy and SEOmaxxed sites, while not harming the ones that are not?

## some technical stuff
i use Go programming language. and claude code on the same server.

sofya now crawls with a speed of 500 to 1200 pages per second.
every part of the search engine is on a single server now, which is probably inefficient. i think i need to have many servers for crawlers, and perhaps a few for the serving layer as well.

## abuse notifications
making a search engine at this scale gets you a lot of false abuse notifications. people/automated systems think that you are DoSing them. so you have to make the system so that it is always a *nice* actor on the web. and constantly learn and make it nicer over time.

## misc
- before publishing this, i updated this document quite a lot! every number is moving (pps, index size, ...) and i now got another server for crawling.

## so...
it's really fun making this.

since, i believe, claude doesn't have the source code for the best search engines, "hey claude make me a search engine" doesn't work well, so it takes some time to get good results.
