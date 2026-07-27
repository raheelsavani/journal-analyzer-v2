# journal-analyzer v2

This is a reimplementation of [journal-analyzer v1](https://github.com/raheelsavani/journal-analyzer), rebuilt using **Object-Oriented Programming (classes)** instead of the original procedural style.

See v1's README for full project context and base functionality.

## What's new in this version

- **`Entry` class** — journal entries are now built from a blueprint (`__init__`) that sets `content`, an optional `title`, an optional `mood`, and an auto-generated `date` (timestamp of creation). A `view()` method displays a single entry, skipping title/mood if they weren't provided.
- **Persistent timestamps** — each entry's creation date/time is now saved to `entries.txt` alongside title, mood, and content, formatted as `mm/dd/yy hh:mm AM/PM` via `.strftime()`. Previously, the date only existed in memory and was lost on restart.
- **Delimiter-based storage** — each entry is stored as one line in `entries.txt`, with fields joined by a `_|_` delimiter: `timestamp_|_title_|_mood_|_content`.
- **`Entry.from_line()`** — a `@classmethod` that reconstructs an `Entry` object from a saved, `_|_`-delimited line, so entries can be rebuilt from disk instead of manually split and printed.
- **`view()` handles both blank-field origins** — treats *either* `None` or `""` as "not provided" for `title`/`mood`, since blank fields arrive as `None` when built fresh (Add Entry) but as `""` when rebuilt from a saved line (`from_line()`). This replaced the old standalone `place_holder()` function, which has been removed.
- **Option 2 (View Entries)** now uses `Entry.from_line()` + `entry.view()` instead of manually splitting and printing fields.
- **Option 3 (Keyword Search)** now converts each line to an `Entry` via `from_line()` and checks the keyword against `title`, `mood`, and `content`, displaying matches with `.view()` instead of printing raw lines. A blank keyword is now rejected with a message instead of matching every entry (since `"" in any_string` is always `True`).
- **Option 4 (Analyze)** now converts each line to an `Entry` via `from_line()` instead of reading raw lines. `word_count()` and `longest_line()` were narrowed to each do one job on a single entry's `content` string (word count of one entry; whitespace-cleaned version of one entry), returning a value rather than reading the file themselves. The Option 4 block now owns the file loop and accumulates results across all entries — a running total (`+=`) for word count, and a compare-and-replace pattern for the longest entry.

### Concepts learned in this version

- Defining and instantiating classes (`__init__`, instance attributes, methods)
- Working with the `datetime` module and `.strftime()` for custom date/time formatting
- Designing a delimiter-based flat-file format and handling optional fields consistently across write and read
- `@classmethod` as an alternative constructor pattern (building an object from saved data rather than fresh input)
- `continue` for skipping the rest of a loop iteration and returning to the top (used to guard against blank keyword input)
- Narrowing a function's responsibility to a single calculation on a single input, moving file I/O and cross-item accumulation out to the calling loop