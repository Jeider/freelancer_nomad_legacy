# Pythonlancer agent instructions

## DATA writes

Pythonlancer may write to the game's DATA directory only through
`tools.data_folder`. Extend `DataFolder` with the necessary methods for new
content. Generators and installers must not write, copy, move or delete DATA
files directly. Use the same entry point for staged DATA output and rollback.
Direct reads are allowed.
