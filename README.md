# minify-js-html-watcher
Real-time code minification tool.

### Description:

This Python script automatically monitors a specified directory for changes in `.js`, `.css`, and `.html` files. When a file is modified, the script minifies the content and appends it to an output file, complete with metadata headers that include the total character count, the file name, and the current timestamp. This facilitates real-time code minification during development, making it a useful tool for web developers.

### Features:

- **File Watcher**: Uses `watchdog` to observe changes in files and directories in real-time.
- **Minification**: Minifies `.js`, `.css`, and `.html` files using the `terser` tool and built-in Python libraries.
- **Multi-Threading**: Efficiently handles file modification events and queue processing through multithreading.
- **Custom Headers**: Appends metadata headers including character count, file name, and timestamp to the minified output.
- **Keyboard Exit**: Allows the user to safely exit the script by pressing a specified key ('e').

### How to Use:

1. Install required Python packages:
   ```
   pip install watchdog tiktoken css-html-js-minify
   ```

2. Run the script in the directory you want to watch:
   ```
   python3 minify_watcher.py
   ```

3. Press 'e' to exit the script.
