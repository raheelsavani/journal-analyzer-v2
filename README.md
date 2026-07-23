# journal-analyzer v2

This is a reimplementation of [journal-analyzer v1](https://github.com/raheelsavani/journal-analyzer), rebuilt using **Object-Oriented Programming (classes)** instead of the original procedural style.

See v1's README for full project context and base functionality.

## What's new in this version

- **`Entry` class** — journal entries are now built from a blueprint (`__init__`) that sets `content`, an optional `title`, an optional `mood`, and an auto-generated `date` (timestamp of creation). A `view()` method displays a single entry, skipping title/mood if they weren't provided.
- **Persistent timestamps** — each entry's creation date/time is now saved to `entries.txt` alongside title, mood, and content, formatted as `mm/dd/yy hh:mm AM/PM` via `.strftime()`. Previously, the date only existed in memory and was lost on restart.
- **Placeholder text at display time** — a standalone `place_holder()` function returns a friendly message (e.g. `"title not provided"`) for any blank title/mood field when entries are viewed, rather than storing placeholder text in the file itself.
- **Delimiter-based storage** — each entry is stored as one line in `entries.txt`, with fields joined by a `_|_` delimiter: `timestamp_|_title_|_mood_|_content`.

### Concepts learned in this version

- Defining and instantiating classes (`__init__`, instance attributes, methods)
- Working with the `datetime` module and `.strftime()` for custom date/time formatting
- Designing a delimiter-based flat-file format and handling optional fields consistently across write and read