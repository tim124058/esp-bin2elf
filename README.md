# esp-bin2elf

### Usage:

```sh
$ python2 ./toelf.py
select a unique name for each section in the rom.
sensible defaults are available for the following common names:
 .rodata .bootrom.text .bss .irom0.text .shstrtab .data .text .symtab
 if defaults are unavailable for a name, generic values will be used.
     enter a name for 0x40201010> .irom0.text
     enter a name for 0x40100000> .text
     enter a name for 0x3ffe8000> .data
     enter a name for 0x3ffe8560> .rodata
```

