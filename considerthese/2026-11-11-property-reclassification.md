# Kotoba: stable releases can disagree about character classes

[Unicode 6.3](https://www.unicode.org/versions/Unicode6.3.0/), released September 30, 2013, reclassified U+180E MONGOLIAN VOWEL SEPARATOR from General_Category Zs to Cf. This reclassifies an existing character.

[UAX 44 revision 12](https://www.unicode.org/reports/tr44/tr44-12.html), September 25, 2013, sections 2.3–2.3.1, distinguishes immutable released databases from permitted changes between releases. Its change history also records Bidi_Class moving from WS to BN for this character.

For editorial cleanup, I infer unchanged source text can receive different classifications after a database upgrade. Record the property, database release and application policy before comparing cleanup results. Preserve the original rather than treating a category change as permission to delete text.

This adds property reassignment to earlier normalization notes. It does not establish any particular library's trimming behavior or Mongolian linguistic correctness. No parser, renderer or migration tested; this historical release is superseded.

[Rights](https://www.unicode.org/copyright.html): report reproduction differs from software/data licensing. Original commentary only; no copied examples or tables. Unassimilated.

Destination: VeigaPunk/kotoba-shokunin, master, considerthese/2026-11-11-property-reclassification.md.
