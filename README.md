# Ascii Lines
Copyright (c) 2019 MacKenzie K. Cooper

## What is it and what does it do?

This is the first homework assignment for CS 561 (Open Source Software) at Portland State University, Summer 2019. 

The program takes a file path to a .tvg file as an argument and parses that tvg file to output an ascii canvas to the user. The lines from the .tvg file are parsed sequentially and so can overwrite previous lines.

## Example Usage

With the file [`tests/test1.tvg`](https://github.com/mackkcooper/asciilines/blob/master/tests/test1.tvg) as input,

```
3 4
* 1 -1 h 5
# -1 1 v 5
```

the output should be:

```
.#..
*#**
.#..
```

## Build & Run

This program was written using Python (3.7.1).

## Bugs, Defects, Failing Tests, Etc.

The program should fail on any .tvg file that has formatting errors.

## License

This program is licensed under the "MIT License".  Please
see the file [`LICENSE`](https://github.com/mackkcooper/asciilines/blob/master/LICENSE) in the source distribution of this
software for license terms.

## Acknowledgments

Tests and outputs 1-3 from [http://gitlab.com/pdx-cs-oss/asciilines-resources](http://gitlab.com/pdx-cs-oss/asciilines-resources).