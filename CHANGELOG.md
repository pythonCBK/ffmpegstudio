# Changelog

All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)


## [1.3] - 02-08-2026

### Added
- Multithreading! Finally. No more interface freezes while FFmpeg is running.
- For convenience, the FFmpeg logic is now in a separate file.

### Fixed
- Code optimization and cleanliness.

### Other changes
- Updated the versions format to the original one:
  
  x.x.x → x.x
  
  Sub-versions will be indicated in x.x.x format.

  

## [1.1.2] - 30-07-2026

### Added
- Audio qauality settings.
- Hiding the FFmpeg console while it is running.


  
## [1.1.1] - 26-07-2026

### Added
- Replaced QPlainTextEdit with QLineEdit, improving both the UI appearance and overall application usability.

### Fixed
- Fixed issues related to user input validation.
- Renamed conversion options for better clarity:
  Crop the video → Trim by time
- Fixed the application icon size.

### Other changes
- Updated the application version format:
  x.x → x.x.x



## [1.1] - 24-07-2026

### Added
- Added millisecond-precision video trimming.
- Added status notifications displayed in the status label.
- Added validation for output directory selection and existence.
- Added settings input validation.

### Fixed
- Increased application icon resolution.

### Other changes
- Removed the bundled FFmpeg build (will be added back in the future).


## [1.0] - 23-07-2026

- First version release.

<p align="left">
  <img src="https://media.discordapp.net/attachments/1350892543033872515/1529867075605237760/image.png?ex=6a70057e&is=6a6eb3fe&hm=382a51dbb112119eb44ef571f5f49f2fd96434c2cfc8f169452df66fcda1a600&=&format=webp&quality=lossless&width=1190&height=853" alt="Interface Screenshot" width="750" heigh="400">
</p>
