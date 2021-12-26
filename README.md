# Jawa

[![Python package](https://github.com/GiantTreeLP/jawa-fixed/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/GiantTreeLP/jawa-fixed/actions/workflows/python-package.yml)
[![License](https://img.shields.io/github/license/GiantTreeLP/jawa-fixed.svg?style=for-the-badge)](LICENSE)

Jawa is a human-friendly library for assembling, disassembling, and exploring
JVM class files. It's highly suitable for automation tasks.

*NOTE*: The assembler does _not_ currently implement Stack Maps, an
artificially complex requirement for ClassFiles generated for Java 7 and
above to properly verify (unless you turn it off with -XX:-UseSplitVerifier).
However, assembled files targeting Java 6 will still work with 7 and above.

## Documentation

API documentation & examples are available at http://jawa.tkte.ch

## Why `jawa-fixed`?

The current version of `jawa` is not maintained anymore, as work is currently in progress for its' replacement: [`lawu`](https://github.com/TkTech/Lawu).
As such this project serves as a way to improve on the currently working library for Java bytecode manipulation.

## Licence

Jawa is available under the MIT licence. See LICENCE.
