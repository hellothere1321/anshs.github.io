
The paper is about the empirical approach to quantifying the subsection of ==stylistics== aka characterization, specifically through keyword analysis. The paper goes through how he finds keywords using tools, why they relate to "==style markers==", its limitations as a field but also its effectiveness.

==**Style definitions and measuring==:** Since style looks at frequencies of linguistic items, it must be compared to another item in a given context, thus ==contextual probability== is found, since its probability based on the texts close comparisons. This ties in to the next point, to make an analysis of a passage, you have to compare not to any item but one with a direct connection to the passage, and is also regular or a norm in the field (No point in getting something so different from the norm as your comparison bc that would skew your results).

==**Style markers**:== 
Basically, they are words that are at drastically different frequencies in some passages than in the norm. They have their own connotation even without context, like chuck(colloquial) vs cast(biblical) because of their high frequency in either the colloquial and biblical registers which sets them up to be style markers.

**==Keywords:==** Another word for style markers, essentially they are used in a program called wordsmith tools, which is able to identify them directly by comparing a wordlist with a reference wordlist, to find words that are less or more frequent than normal.

***Statistical tests:*** 

Classic [[Chi Square Test with Yate's correction]] with Yates correction for a 2 * 2

Dunning's log likelihood test, gives an even better estimate especially with long texts or a whole genre against the reference.

***Preparing and doing stuff with the text:*** 

Generally there is a lot of work to be done with preparing a text to be analyzed since different editions have separate spelling variations and are more or less faithful to original translations. The concern comes from how original texts will have spelling variation associated with Elizabethan English which some computers can't take into account. Depending on the tool tagging for characters in a way that the program recognizes is important, with the author opting to use the \<SAM>Gregory, o’ my word, we’ll not carry coals.<\SAM> format.

As for how many words that are needed per character to analyze it, there seems to be no definitive formula, but depending on the context, interactions and more it will vary but 1000 words is what the author chose.

Along with that when analyzing the data set you have to check the keyness value is high enough that it isn't just the fact that the word isn't in the reference corpus aka like Proper nouns, and while Proper nouns have this effect called [[Hapax legomena]] that is associated with them but it doesn't really help with characterizing them.

Next he goes on to check the keyness and then analyze so lets see that.

***Analyze(Pre-keyword):***

He first starts by comparing words and their frequencies for each character making a top 10 for all of the characters. The issue with a black and white top 10 is that most of the words for each character will be similar, a product of the actual authors writing and common diction, with words like and being very common for all the characters. He also compares each character to present day written and spoken English frequencies, and upon seeing similarities between some characters and written and spoken English, noting their flowery rhetorical style of dialogue or maybe their blunt and normal conversation as indicated by their connection with modern day English. Also you can use discrepancies here to further analyze characters tendencies, for example he cites the nurse who has o' in her 10th slot as more emotional given that she clearly has more expressions of shock in the story. Some people do remove grammatical words and phrases from the analysis to create a more interesting top 10 but in some ways grammatical words are great conveyers of information.

***Analyze(with keywords):***

After this point he actually goes over all their characters and their key words with both positive and negative value (negative is when a word is less prevalent than in the reference corpus and generally less likely than positive. Also when using keywords one must be aware that some may just be a reference to an event that they face, like Mercutio saying banished a lot when Romeo is banished. One method to combat this is to look at frequencies given that low freqencies can usually pretty easily be confined to one act while high frequencies are general character features instead of a response to an event (not a confirmed thing just helpful generally). 

|  | *Romeo* | *Juliet* | *Capulet* | *Nurse* | *Mercutio* | *Friar L.* |
|---|---|---|---|---|---|---|
| ***Positive keywords*** | Beauty (10)<br>Blessed (5)<br>Love (46)<br>Eyes (14)<br>More (26)<br>Mine (14)<br>Rich (7)<br>Dear (13)<br>Yonder (5)<br>Farewell (11)<br>Me (73)<br>Sick (6)<br>Lips (9)<br>Stars (5)<br>Fair (15)<br>Thine (7)<br>Hand (11)<br>Banished (9) | If (31)<br>Or (25)<br>Sweet (16)<br>Be (59)<br>News (9)<br>My (92)<br>Night (27)<br>I (138)<br>Would (20)<br>Yet (18)<br>Thou (71)<br>Words (5)<br>Name (11)<br>Nurse (20)<br>Tybalt’s (6)<br>Send (7)<br>Husband (7)<br>That (82)<br>Swear (5) | Go (24)<br>Wife (10)<br>Thank (5)<br>Ha (5)<br>You (49)<br>T (5)<br>Thursday (7)<br>Her (29)<br>Child (7)<br>Welcome (5)<br>We (15)<br>Haste (6)<br>Gentlemen (5)<br>Tis (11)<br>Our (13)<br>Make (10)<br>Now (15)<br>Daughter (5)<br>Well (13) | Day (22)<br>He’s (9)<br>You (55)<br>Quoth (5)<br>Woeful (6)<br>God (12)<br>Warrant (7)<br>Madam (10)<br>Lord (11)<br>Lady (16)<br>Hie (5)<br>It (39)<br>Your (21)<br>Faith (7)<br>Said (6)<br>Ay (90)<br>She (21)<br>About (5)<br>Ever (5)<br>Sir (13)<br>Marry (7)<br>Ah (6)<br>Fall (5)<br>Well (13) | A (85)<br>Hare (5)<br>Very (11)<br>Of (57)<br>He (20)<br>The (85)<br>O’er (5) | Thy (51)<br>From (23)<br>Thyself (5)<br>Mantua (6)<br>Part (7)<br>Heaven (10)<br>Forth (5)<br>Her (30)<br>Alone (6)<br>Time (10)<br>Married (7)<br>Letter (5) |
| ***Negative keywords*** | You (14)<br>Romeo (5)<br>He (11)<br>Go (7) | Her (5)<br>The (84)<br>You (27)<br>And (104)<br>Go (6) | Thou (7)<br>That (13)<br>The (37)<br>Of (21)<br>And (48) | With (12)<br>Thou (11) | My (13)<br>I (31)<br>What (5) | I (32)<br>You (16)<br>A (33)<br>Have (5)<br>My (26) |

Looking at Romeo we see that he has beauty, love, and body parts in his positive keywords. The author analyzed this as a concern for the physical, given that is a lot of what Romeo does do.

On the other hand Juliet's most positive keyword is "if" and another big key word is "yet" showing Juliet's uncertainty throughout the play.

Capulet has the keyword "go" showing how he commands the other characters a lot and displaying that aspect of his 

Overall there are a couple more examples of how interpretation of other characters can go but I think that's more to internalize and less to write down.


***Pronominal patterns in the keyword:*** (to do with pronouns)

| Person | Juliet | Romeo | Capulet | Nurse | Mercutio | Friar L. |
|---|---|---|---|---|---|---|
|  | 1st (2nd) | 1st (2nd) | 2nd (1st) | 3rd (2nd) | 3rd | 2nd (3rd) |
| 1st person singular/plural | S | S | P | - | - | - |
| Thou/you | T | T | Y | Y | - | T |

You see that Juliet and Romeo being the leads have more first person pronouns, but Juliet uses the word "I" more (table not listed), than Romeo who instead uses the word "me", which shows how Juliet has to carry the burden of her own soul while Romeo is more conscious of his role as a lover and how his circumstances effect him. 

The nurse has a lot of he's but it is localized to when she is reacting to his death which displays how some stuff doesn't show patterns.

Also in terms of thou vs you, you is more aloof so the main characters being very emotional generally instead use thou. 

This paper as a whole was a breakthrough in making empirical way of establishing lexical and grammatical patterns using the new tagging system analyzing the dialogue for keywords.

***Paper limitations:***

As a whole it displays statistical deviation but not deviation from absolute rules since that is pretty infrequent with writing, also it separates contractions and doesn't lemmatize the word forms thus loves and love would have been separate given that they may have differences in meaning.

***Future:***
The possibilities for future research are numerous. One area is to consider is
relationships between keywords. Scott (1999) has developed, for example, the
notion of ‘key-keywords’ (keywords that are keywords in a number of different
files, i.e. they are generally key across the body of data), and ‘associates’
(keywords that have a statistical association with other keywords). I was not able
to pursue these notions in my data, on account of the small number of words in
each character file, but this clearly would be an avenue to pursue with larger
quantities of data. Another obvious area for development is to apply keywords
analysis to other kinds of data, such as particular registers, dialects, media,
documents or writings. (Culpeper 28)