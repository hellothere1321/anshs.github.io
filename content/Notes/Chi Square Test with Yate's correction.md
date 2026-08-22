
Here is an example of a chi square test with examples

|                    | Right | Rest of the words |
| ------------------ | ----- | ----------------- |
| **Your text**      | 5     | 5000              |
| **Reference text** | 10    | 100000            |

The essence of the test is to add the total amount of instance of the word "Right" up, along with how many total words there are, across both texts. Then you divide the amount of instances of "Right" by the total amount of other words, and see how many instances of ""Right""  are expected versus how many there are. Here there are 15 instances of right with 105,000 words thus meaning there should be less than one "right" in your text, but there are actually 5, which means there is a significant discrepancy.


