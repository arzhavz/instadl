# InstaDL

**InstaDL** is a simple and powerful command-line tool to download Instagram Reels and Photos by bypassing standard restrictions. Perfect for those who want quick and reliable media downloads directly from Instagram links.

---

## Features

- 🎞️ Download Instagram **Reels**
- 📷 Download Instagram **Photos**
- 📥 Support for **multiple URLs at once**
- 📁 Custom save folder support
- ✅ Clean CLI experience with progress bars

---

## Installation

1. Download the latest release from the [Releases Page](https://github.com/arzhavz/instadl/releases).
2. Extract the `.rar` file.
3. Open **PowerShell** or **Command Prompt** in the extracted folder.

---

## Usage

### Download Instagram Reels

```sh
.\instadl.exe reel -u "https://www.instagram.com/reel/your_reel_url"
```

To download multiple Reels:

```sh
.\instadl.exe reel -u "https://www.instagram.com/reel/url1, https://www.instagram.com/reel/url2"
```

### Download Instagram Photos

```sh
.\instadl.exe photo -u "https://www.instagram.com/p/your_photo_url"
```

To download multiple Photos:

```sh
.\instadl.exe photo -u "https://www.instagram.com/p/url1,https://www.instagram.com/p/url2"
```

### Save to a Specific Folder

```sh
.\instadl.exe reel -u "your_url" -s "MyFolder"
```

---

## Help

```sh
.\instadl.exe --help
```

---

## Notes

1. This tool does not require an Instagram login.
2. All downloads are saved in the current directory by default unless specified otherwise.
3. Ensure you have a stable internet connection during downloads.

---

## Author

Created by **Arzha** (me)