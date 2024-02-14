# Practicing Bioinformatics-related Problems

Problems are taken from the [Rosalind.info](https://rosalind.info/problems/locations/) website.

Individual files can be run through the console via `python3 <file location>`

### Notes
-------------------------------------------
** Modules **
- While creating the file `Bioinfo_Armory/genbank_to_fasta.py` I ran into an issue while trying to run the file via the command line because the file __imported a util function from a module__ found in an adjacent folder. I found that, as the linked post states, `python cannot import files from upper directory of your working directory unless you add them to PATH`. Thus, to run this file, instead of using the usual `python3 Bioinfo_Armory/genbank_to_fasta` command I needed to use
 ```
python3 -m Bioinfo_Armory.genbank_to_fasta
```
- An important element of this solution is the `-m`, which tells Python to treat the subsequent file as a module, rather than executing the given file as a script.

- [Google Gemini explanation of the -m flag](https://g.co/gemini/share/93f79b12a64a)
- [Stack Overflow post on python modules](https://stackoverflow.com/questions/72878837/importerror-attempted-relative-import-with-no-known-parent-package-still-no-sol)