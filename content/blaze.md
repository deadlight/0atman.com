Title: Blaze: A lightweight literate programing preprocessor
Date: 2017-09-12 20:40
Category: tools

I've been playing with many literate programming tools since this technique of document-first programming came into my life two years ago.

[Literate programming](https://en.wikipedia.org/wiki/Literate_programming) (LP), a concept that has been around since at least the 80s, is back in the spotlight since the [Eve](http://witheve.com/) language (released by the eve team headed by Chris Granger of [Light Table](http://lighttable.com) fame) was released to the public in 2015.

While LP's original concept aimed to create a document-first system whereby the building blocks of the actual code could be read (by the human or compiler) in any order (as it is in Eve), the contemporary state of the art is focused on creating the document-first model with existing procedural languages.

There are two main kinds of tool in the modern LP category:

 1. Tools that write beautiful documentation based on comments in source code, such as [Docco](http://ashkenas.com/docco/) and (a personal favourite) [Marginalia](https://github.com/gdeer81/marginalia)
 2. Tools that allow you to execute code-fenced source code within some markup, such as [Literate](https://github.com/zyedidia/Literate), [litpro](https://github.com/jostylr/litpro), and tiny [lit](https://github.com/vijithassar/lit).
 
The first is an evolution of the documentation processors you will be familiar with, no real innovation has happened in this space since [Javadoc](https://en.wikipedia.org/wiki/Javadoc). (Much though I love [Sphynx](http://www.sphinx-doc.org/en/stable/index.html) et al)

The second category I think is worth exploring.

It is into this backdrop I present [Blaze](https://gist.github.com/0atman/5ea526a3ae26409da50dd7697eb700e8).

## Blaze is Tiny:

<script src="https://gist.github.com/0atman/2a96b82ab05d7f02c28109cc9de28ebf.js"></script>

But what it gives you is the ability to execute your markdown files as though they were scripts: It is a drop-in replacement for `/usr/bin/env`:

<script src="https://gist.github.com/0atman/491f0aeda776c9cbbdf0a30f872e2199.js"></script>

It also allows as many paramaters to be passed to your interpreter as you like (unlike normal shebangs), which means you can use tools like [pex](https://github.com/pantsbuild/pex):

<script src="https://gist.github.com/0atman/f673844a92ac3e24ab24b3fe45b299aa.js"></script>

(Note that we are able to use pex's ephemeral venv trick to run python with any requirements pre-installed)

Blaze's REAL trick, is that if it is called with a `.md` file, it only executes code inside triple-backtick codefences, as in this all-encompasing example of a literate program with built-in requirements:

<script src="https://gist.github.com/0atman/c9ebb7e7256d7a144ac3587c1ad7bfec.js"></script>

Magic, right?

## Overhead
Blaze introduces minimal startup overhead, somewhere between 5-20ms, an almost zero runtime overhead (`sh` is running, I suppose).

### Python Shebang
```shell
λ ./py-test.py
hi
./py-test.py  0.02s user 0.00s system 94% cpu 0.025 total
```

### Blaze Shebang
```shell
λ ./blaze-test.py
hi
./blaze-test.py  0.02s user 0.00s system 67% cpu 0.030 total
```

## Prior Art / Acknowledgements

Blaze is currently a hacked-together LP tool that is only suitable for one-off scripts. I borrowed the awk code-fence-stripping code from [@trauber](https://gist.github.com/trauber/4955706).
