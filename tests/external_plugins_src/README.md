# Rot13 Custom Exporter for Jrnl

This is a custom exporter to demostrate how to write customer exporters for
[minchin.jrnl](https://github.com/MinchinWeb/minchin.jrnl). It is also used by
*minchin.jrnl* in its tests to ensure the feature works as expected.

This plugin applies a [Caeser
cipher](https://en.wikipedia.org/wiki/Caesar_cipher) (specifically the
[ROT13](https://en.wikipedia.org/wiki/ROT13)) to output text.
