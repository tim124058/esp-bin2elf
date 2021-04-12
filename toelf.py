import esp_bin2elf

rom = esp_bin2elf.parse_rom('code.bin', 'code.bin')
section_names = esp_bin2elf.name_sections(rom)
elf = esp_bin2elf.convert_rom_to_elf(rom, section_names, 'out.elf')
