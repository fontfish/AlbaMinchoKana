# The To-Do List
### *in order of priority*

## To Do:
* [ ] Brush up on my Japanese font terminology.
* [x] Enlarge の slightly. (Not strictly necessary.)
* [ ] Enlarge う just slightly. (Lengthen, to be more precise.)
* [x] The top stroke of the hiragana こ has a misaligned brush return. This should essentially be similar to an *uroko* (うろこ), typographically speaking, but is not currently. Fix it.
  * [ ] Take a second look. Adjust again if necessary.
  * [ ] Write up a brief explanation of how an understanding of calligraphic influence and the calligraphic origins are import in understanding letter design, using this as an example.
* [ ] Rotate dakuten (濁点 = ゙) slightly. It currently feels very vertical.
* [ ] The lead-in strokes and flicks on some glyphs are small. Redesign. (Getting there!)
  * [ ] Check *all* glyphs for consistency of those components. Compare and even out.
* [ ] Adjust hiragana shapes and modify glyphs.
  * [ ] Resize some glyphs (right now they are slightly uneven – は looks big compared to あ, for instance)
* [ ] Link all horizontal glyphs to vertical.
* [ ] Create Katakana.
* [ ] Include U+1b000 (𛀀) and U+1b001 (𛀁) archaic kana glyphs.
* [ ] Make extra punctuation (and add fullwidth quote marks).
* [ ] Link all new horizontal glyphs to vertical.
* [ ] The Python3 test file shows an error somewhere – the vertical spacing of glyphs is uneven. Find out why and fix.
* [ ] Add へのへのもへじ face as an OpenType feature ligature.

### Once all full-size glyphs have been created:
* [ ] Make small kana.
* [ ] Make modified dakuten (濁点 = ゙) glyphs for ease of reading at small sizes.
* [ ] Make halfwidth glyphs.
* Create 小 verstion (all glyphs slightly scaled down).
  * Then carefully copy kana to the AlbaPrintMincho fonts to make photopolymer-suitable version.
  * Increase contrast on AlbaPrintMincho (predominantly by thinning hairlines)?

## Finalising
* See the guide:
http://designwithfontforge.com/en-US/Making_Sure_Your_Font_Works_Validation.html

## Uncertainties:
Should the 点 on the ン be bigger?

## To Not Do
* Don't use glyps u10FFDE to u10FFED for vertical glyps.


# Notes

## Glyphs so far that need manual direction editing.
々すむロ
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
git add . (or git add -A)
git commit
git push
