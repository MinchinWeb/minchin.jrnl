<!--<p align="center">
<a href="https://jrnl.sh">
<img align="center" src="https://github.com/MinchinWeb/minchin.jrnl/blob/develop/docs_theme/assets/readme-header.png"/>
</a>
</p>-->

*minchin.jrnl*
==============

 [![Testing](https://github.com/MinchinWeb/minchin.jrnl/workflows/Testing/badge.svg)](https://github.com/MinchinWeb/minchin.jrnl/actions?query=workflow%3ATesting)
 [![Downloads](https://pepy.tech/badge/minchin.jrnl)](https://pepy.tech/project/minchin.jrnl)
 [![Version](http://img.shields.io/pypi/v/minchin.jrnl.svg?style=flat)](https://pypi.python.org/pypi/minchin.jrnl/)

*To get help, [submit an
issue](https://github.com/MinchinWeb/minchin.jrnl/issues/new/choose) on
Github.*

`minchin.jrnl` is a simple journal application for the command line.

You can use it to easily create, search, and view journal entries. Journals are
stored as human-readable plain text, and can also be encrypted using  [AES
encryption](http://en.wikipedia.org/wiki/Advanced_Encryption_Standard).

## In a Nutshell

To make a new entry, just enter

``` sh
jrnl yesterday: Called in sick. Used the time to clean the house and write my
book.
```

`yesterday:` is  interpreted by `minchin.jrnl` as a timestamp. Everything until
the first sentence ending (either `.`, `?`, or `!`) is interpreted as the
title, and the rest as the body. In your journal file, the result will look
like this:

    [2012-03-29 09:00] Called in sick.
    Used the time to clean the house and write my book.

If you just call `jrnl`, you will be prompted to compose your entry - but you
can also configure _minchin.jrnl_ to use your external editor.

<!--For more information, please read the
[documentation](https://jrnl.sh).-->

## Contributors

### Maintainers

Our maintainers help keep the lights on for the project:

* William Minchin ([minchinweb](https://github.com/MinchinWeb))

Please thank them if you like `minchin.jrnl`!

### Code Contributors

This project is made with love by the many fabulous people who have contributed.
`minchin.jrnl` couldn't exist without each and every one of you!

<!--
<a href="https://github.com/MinchinWeb/minchin.jrnl/graphs/contributors"><img
src="https://opencollective.com/minchin.jrnl/contributors.svg?width=890&button=false"
/></a>
-->

If you'd also like to help make `minchin.jrnl` better, please see our
[contributing documentation](CONTRIBUTING.md).

<!--
### Financial Backers

Another way show support is through direct financial contributions. These funds
go to covering our costs, and are a quick way to show your appreciation for
`jrnl`.

[Become a financial contributor](https://opencollective.com/jrnl/contribute)
and help us sustain our community.

<a href="https://opencollective.com/jrnl"><img
src="https://opencollective.com/jrnl/individuals.svg?width=890"></a>
-->
