# A small installable module to test how the Fire CLI parses arguments.

This module allows to call a Fire CLI with arguments and prints them and their python type back to the user.

It can be installed with pip via
```
pip install /path/to/pyroprint
```

After installation, a `pyroprint` entry point to the Fire CLI for print_arguments() is setup. This can be used to quickly test argument parsing from the shell, e.g.,
`pyroprint "test string" 5 --var_key "[string1, string2]"`
with output
```
=== Printing arguments ===
Argument 0: 'test string'
Type: <class 'str'>
Argument 1: 5
Type: <class 'int'>
=== Printing keyword arguments ===
var_key: ['string1', 'string2']
Type: <class 'list'>
```
