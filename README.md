# Lazy Loading Script

A Python utility that automatically adds `loading="lazy"` attributes to `<img>` and `<video>` tags in HTML files across a directory tree.

## Features

- Recursively processes all HTML files in a directory
- Uses regex to identify tags without lazy loading
- Modifies tags to improve web performance
- Preserves existing attributes

## Usage

1. Set the `directory_path` variable to your target directory
2. Run the script: `python Lazy.py`

## Requirements

- Python 3.x
- `os` and `re` modules (included in standard library)

## Example

```python
directory_path = "/path/to/your/html/files"
```

The script will modify tags like:
```html
<img src="image.jpg">
```
to:
```html
<img src="image.jpg" loading="lazy">
```
