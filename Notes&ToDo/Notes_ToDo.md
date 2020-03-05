# The To-Do List
### *in order of priority*

## To Do:
* [ ] Enlarge の slightly.
* [ ] Brush up on my Japanese font terminology.
* [ ] Redesign lead-in stroke components.
* [ ] Link all horizontal glyphs to vertical.
* [ ] Adjust hiragana shapes and modify glyphs.
  * [ ] Resize some glyphs (right now they are slightly uneven – は looks big compared to あ, for instance)
* [ ] The lead-in strokes and flicks on some glyphs are small. Compare all and even out.
* [ ] Create Katakana
* [ ] Include U+1b000 (𛀀) and U+1b001 (𛀁) archaic kana glyphs.
* [ ] Make extra punctuation.
* [ ] Link all new horizontal glyphs to vertical.

### Once all full-size glyphs have been created:
* [ ] Make small kana.
* [ ] Make halfwidth glyphs.
* Create 小 verstion (all glyphs slightly scaled down).
  * Then carefully copy kana to the AlbaPrintMincho fonts to make photopolymer-suitable version.
  * Increase contrast on AlbaPrintMincho (predominantly by thinning hairlines)?

## Vertical forms linked so far
「」『』、。

## Finalising
* See the guide:
http://designwithfontforge.com/en-US/Making_Sure_Your_Font_Works_Validation.html

## Uncertainties:
Should the 点 on the ン be bigger?

## To Not Do
* Don't use glyps u10FFDE to u10FFED for vertical glyps.


# Notes

## Glyphs so far that need manual direction editing.
々すむ
u10FFEF

## Positions
Horizontal setting small kana glyphs should be horizontally centred but moved down by 100. 84.5 - 85% size (84.5% and then broaden).

## Shortcuts:
### When finishing editing the font
Ctrl-A
Ctrl-Shift-_
Ctrl-Shift-D

### To remove overlap
Ctrl-Shift-O

#### How To Git
A reminder for myself of how to Git.
git add .
git commit
git push
