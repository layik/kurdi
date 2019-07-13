# kurdi
There are some hopefully useful files/scripts/chunks etc to share with Kurdi developers. 

1. kurdi_words.txt: a list of Kurdish words (currently 29014), unique and alphabetically ordered (thanks to @dolanskurd).
2. unicode_list.txt: list of unicode values for Kurdish alphabet (Arabic script) standard accepted and published on http://unicode.ekrg.org/ku_unicodes.html
3. ku.po for Drupal. Most of the translations come from https://localize.drupal.org/translate/languages/ku (now almost dead
4. KRG health institutions throughout KRG (see health)

Now that we have some good unique nad cleaned up wordlist. We can do some statistics on them (in R for now):

```r
ku = readLines("corpus/kurdi_words.txt")
ku_v = readLines("corpus/letters_lines.txt")
letters_used = sapply(ku_v, function(x){
  length(grep(x, ku))
})
library(ggplot2)
ggplot() + geom_bar(aes(x=names(letters_used),y=letters_used), stat='identity') + xlab('x') + ylab('y')
```

The answer would be:

<img src="https://user-images.githubusercontent.com/408568/61165158-8e7d0e00-a514-11e9-8e1a-919b24a016bb.png" width="100%">
