+++
date = '2026-08-21T20:00:00-05:00'
draft = false
title = 'Can a Computer Tell Crowley From Aziraphale?'
+++

### What Makes a Character Sound Like Themselves?
##### ***Warning: Good Omens spoilers***

One of the things that has always interested me about linguistics is how it differentiates us. Even without seeing or hearing someone, we still manage to communicate personality through text, and it is interesting how much of that can become specific to one person.

Authors, especially in fiction, exploit this to make characters distinct. Specific tones and linguistic styles can make us feel like we know a character without ever actually hearing or seeing them. I started thinking about this through *Good Omens*, especially the contrast between Crowley and Aziraphale. They have very different personalities and ways of speaking, but after knowing each other for thousands of years they have also rubbed off on each other.

One of my favorite examples comes near the end of the book when they swap bodies. Their impressions of each other are convincing enough that the reveal actually surprised me. That got me thinking about what the reader has learned about them by that point. We only have the words on the page, so what exactly makes a line feel like something Crowley would say rather than Aziraphale?

That is the question I want to work on for this project: **can I define some of those differences linguistically, and can a computer learn to recognize them too?**

### Starting with the linguistics

I am still very early in this project, so most of what I have been doing so far is reading and trying to work out what I should even measure.

One idea I have been reading about is **keyword analysis**. I originally thought a keyword basically meant an important or common word, but in corpus linguistics it is more specific than that. A word can be considered a keyword when it appears much more or much less often in one text than we would expect when compared with a useful reference text.

That comparison is important. A word appearing five times does not tell me much by itself. If it appears five times in 5,000 words but only ten times in another 100,000 words, suddenly that frequency looks much more unusual. This is where statistical tests such as the chi-square test, sometimes with Yates' correction for a 2x2 table, or Dunning's log-likelihood test can be used to test how surprising that difference actually is.

I am still learning the statistics behind these tests, but I like this idea because it gives me a way to move from something vague like "Crowley sounds more casual" to something I can actually investigate. Maybe Crowley uses certain contractions, discourse markers, words or sentence structures unusually often. Maybe Aziraphale does the same with completely different features. Or maybe some of the differences I think I notice will disappear once I actually count them.

### The computer part

I have also started setting up the coding side, although there is definitely not a finished machine-learning model yet. Right now the useful part is much more basic: deciding how I am going to store the dialogue, label who is speaking, and turn each line into features that a program can count.

Eventually I want to try two slightly different approaches. One model can look at the actual words being used, while another will be more restricted and look at things such as sentence length, punctuation, contractions, pronouns and other stylistic features. If both can tell the characters apart, that would be interesting for different reasons. If the word-based model does much better, it may simply be learning the topics and vocabulary associated with each character rather than their broader style.

For now, though, I am not anywhere near answering the original question. I have mostly ended up with more questions: what should count as a useful stylistic feature, what should the reference text be, how much dialogue do I need, and how do I stop the model from taking shortcuts?

That is probably a better place to start than pretending I already know the answer. Over the next few posts I want to document the process as I learn the linguistics, build the dataset and slowly get the code working.
