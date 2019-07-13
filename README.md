# kurdi
There are some hopefully useful files/scripts/chunks etc to share with Kurdi developers. 

1. kurdi_words.txt: a list of Kurdish words (currently 29014), unique and alphabetically ordered (thanks to @dolanskurd).
2. unicode_list.txt: list of unicode values for Kurdish alphabet (Arabic script) standard accepted and published on http://unicode.ekrg.org/ku_unicodes.html
3. ku.po for Drupal. Most of the translations come from https://localize.drupal.org/translate/languages/ku (now almost dead
4. KRG health institutions throughout KRG (see health)

Now that we have some good unique nad cleaned up wordlist. We can do some statistics on them (in R for now):

```r
ku_alphabet = "ئبپتجچحخدرڕزژسشعغفڤقکگلڵمنهاەوۆوویێ"
ku_v = c()
for (i in 1:nchar(ku_alphabet)) {
  ku_v = c(ku_v, substring(ku_alphabet, i, i))
}
# writeLines(ku_v, "/corpus/letters_lines.txt")
letters_used = sapply(ku_v, function(x){
  length(grep(x, ku))
})
plot(letters_used, xaxt="n")
axis(1,at=1:35,labels=names(letters_used))
```

The answer would be و:

<img src="https://user-images.githubusercontent.com/408568/61164188-2249dc80-a50b-11e9-8d12-7cb7821cec9f.png" width="100%">
