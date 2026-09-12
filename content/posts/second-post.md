+++
date = '2026-08-08T02:07:18-05:00'
draft = false
title = 'How do you even analyze a pdf'
+++

### What Makes a Character Sound Like Themselves?
### Part 2: How do you even analyze a pdf
##### ***Warning, Good Omens Spoilers***

Last time I decided on the question I wanted to answer: what differentiates the dynamic duo in Good Omens. Since then I've been working on looking more into how the could be defined linguistically, with their speech and how they live in situations within prose. More importantly, I also looked deeper into how I could turn all this into something I could measure.

After reading a lot more about how one could linguistically define a character, whether it came from their actual speech or how they reacted to situations, i realized my first step would be actually getting a text that would work. While perusing the options I decided I would try and choose whether I use the play-book for good omens or the actual novel. In keeping in the spirit of the system I decided to read the actual novel, buying an online copy and using it to parse for dialogue as well. 

Parsing for dialogue was easier said than done, I found that most of the dialogue had the character it was associated with within 8 words of the quotes. So to start I used regex, to look for the symbols "", and then expanded the words captured to 8 words before, to 8 words after keeping the words in quotes as the actual dialogue. Initially I thought I could just look for the correct name, but with compact nature of dialogue I realized that would not be foolproof as there could be two names mentioned with only one being the person speaking. Thus instead of doing that I started thinking about linguistic patterns for speech. By using a combination of speech keywords, like "said", and aliases for the characters like "the angel" for Aziraphale, I would be able to find most of the quotes and classify them. Later on I decided to try and spend some time hashing out a system for detecting pronouns, but it massively slowed down my system and was particularly ineffective as it had to track every character mentioned and look through huge lists to see if they were the actual person who was going to talk next or being talked about.

Doing that I have achieved a pretty good milestone for myself learning more about typical situation and how linguistics combined with the scenario can provide a lot of information about a character and how they act, and allowed to me to even consider using something such to classify my characters beyond just looking at their most key words.

At this point I'm feeling a lot better with my approach, I will finish the rest of cleanup and do a quick review to check the tagging isn't wrong in a sample, then start planning and programming a system to actually, linguistically define Crowley and Aziraphale. From there by a blog post or two at the very least, I want to be able to test whether those patterns are actually strong enough to distinguish characters and then refining the process and moving further with the project .