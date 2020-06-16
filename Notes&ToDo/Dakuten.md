# Dakuten and Handakuten

In both Japanese kana syllabaries, the *dakuten*, two small dots (゛), and *handakuten*, a small circle (゜), are used to represent a change to the consonant sounds of some letters. Historically once optional, these are now a vital part of writing hiragana and katakana. Here, I'd like to give a brief explanation of one problem I have encountered with these symbols in printed form and a possible solution.

## The Issue

One thing I have noticed with great frequency when reading Japanese, especially at small sizes such as in ruby (振り仮名) lettering, is the difficulty in differentiating between these marks. They can look surprisingly similar, espexially on pixelated screens or in bad printing conditions, this can make an impact on the ease of reading a novel or webpage, or on finding a word in a dictionary. In some cases, context makes the distinction clear, but just as often trying to figure out a word becomes a process of trial and error, especially for those new to the language. Some typefaces have attempted to overcome this problem by making the *dakuten* bigger or the *handakuten* a thinner ring, but even then it's a more difficult task than I believe necessary to tell the two marks apart.

## A New Approach

In Alba Mincho Kana, I'd like to take another approach, which I will make optionally available as an OpenType feature. Rather than simply scaling the mark, I'd like to realign the two dots of the *dakuten* entirely so as to cause no confusion, skewing the placement to a more traditionally calligraphic offset so that the resulting shape is discernible even at very small sizes or in bad printing conditions.

## Examples

Here are some examples of my experiments so far with modifying the shape of *dakuten*. These images were generated in Inkscape, applying blur to simulate bad printing and screen pixelation.

![濁点](https://github.com/fontfish/AlbaMinchoKana/blob/master/Testing/Dakuten/d1-medium.png)
![半濁点](https://github.com/fontfish/AlbaMinchoKana/blob/master/Testing/Dakuten/hd-medium.png)
![ずらした濁点](https://github.com/fontfish/AlbaMinchoKana/blob/master/Testing/Dakuten/d2-medium.png)
