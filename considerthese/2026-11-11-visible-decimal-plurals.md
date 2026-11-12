# Kotoba: plural selection can depend on visible decimals

CLDR's English cardinal rule changed between [23.1](https://github.com/unicode-org/cldr/blob/release-23-1/common/supplemental/plurals.xml) and [24](https://github.com/unicode-org/cldr/blob/release-24/common/supplemental/plurals.xml): numeric unity became insufficient; the singular category also required no visible fractional digits.

The [LDML Numbers specification](https://unicode.org/reports/tr35/tr35-numbers.html#Operands) distinguishes numeric magnitude from decimal presentation. Its operands separately describe integer digits, fractional digits and visible precision, including or excluding trailing zeros. Equal numeric values can therefore select different categories.

For localized prompt templates, preserve decimal presentation until plural selection; numeric conversion can erase required precision. Record locale, cardinal versus ordinal rules, data version and formatting policy together. A category identifies a message branch, not a complete translation or universal grammatical rule.

Primary-source reading; no implementation tested. Unicode's repository license distinguishes restricted public copying of LDML from data licensing; historical files point to Unicode terms. Original commentary only, no copied rules or examples. Unassimilated.

Reviewed 2026-11-11. Destination: VeigaPunk/kotoba-shokunin, master, considerthese/2026-11-11-visible-decimal-plurals.md.
