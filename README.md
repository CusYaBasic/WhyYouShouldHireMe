# WhyYouShouldHireMe
An app for tcgroup to demostrate personality and techincal skills

## Programming Principles Demonstrated
* Clean code organisation
* Reusable components
* Separation of concerns
* Event-driven programming
* Encapsulation
* Code maintainability
* Debugging and problem solving
* Building software from concept to finished product

## Python Development
* Built a complete desktop application using Python
* Object-oriented programming (OOP)
* Created reusable classes and custom widgets
* Structured a project using modules/packages
* Used inheritance to extend Qt widgets
* Implemented signals and slots for communication between components
* Managed application state and page navigation

## PySide6 / Qt Framework
* Developed a custom GUI application using PySide6
* Created custom widgets:
  - Rounded image labels
  - Custom buttons
  - Animated buttons
  - Custom title bar
  - Interactive menu cards
  - Built a frameless application window
  - Created a custom Windows-style title bar
* Implemented:
  - Hover events
  - Click events
  - Mouse event handling
  - Widget positioning
  - Layout management

## User Interface / UX Design
* Designed a complete interactive portfolio experience
Created:
  - Home screen
  - Section menu
  - Presentation/slideshow pages
  - Interactive demos
  - Final recruitment screen
* Implemented consistent UI styling with Qt Style Sheets (QSS)
Created:
  - Rounded corners
  - Borders
  - Hover effects
  - Disabled states
  - Text outlines
  - Image overlays
* Designed responsive layouts using:
  - QVBoxLayout
  - QHBoxLayout
  - QGridLayout
  - QStackedWidget


## Animation Systems
* Created custom UI animations using Qt animations
Implemented:
  - Sliding images
  - Moving text bubbles
  - Animated troll face
  - Jesus hover animation
* Escaping "No" button
Used:
  - QPropertyAnimation
  - QEasingCurve
  - Timers

## Multimedia Integration
* Added audio playback using Qt Multimedia
Implemented:
  - Button click sounds
  - Animation sound effects
* Victory sounds
Managed:
  - QMediaPlayer
  - QAudioOutput
  - Local media assets

## Game Development
Built a playable mini-game inside the application:

Catch Game
* Player selection system
Multiple user profiles:
  - Stuart
  - David
  - Yas
  - Robyn
* Keyboard controls:
  - WASD
  - Arrow keys
* Collision detection
* Score tracking
* Lives system
* High scores
* Increasing difficulty
* Random object spawning
* Game restart functionality

## Data / State Management
* Created unlock progression system
* Locked/unlocked content based on completion
* Managed application progression
* Maintained page state between navigation
* Implemented page resetting functionality

## Interactive Features
* Created a "Mind Reader" trolling game
* Created an interactive recruitment ending:
  - "Would you hire Lewis?"
  - Confetti celebration
  - Victory animation
  - Moving "No" button
  - Created humorous user interactions through animations and events

## Software Architecture
* Separated code into:
  - Pages
  - Widgets
  - Main application controller
* Built reusable components
* Avoided duplicated UI code
* Created modular slideshow system reusable for:
  - Why Hire Me
  - Strengths
  - Weaknesses
  - Previous Work
  - Programming Principles

## File / Asset Management
* Managed:
  - Images
  - Sounds
  - UI assets
* Created organised project structure

## Notes
A few things were made by AI that I feel I should mention

path.py:
When building the application into a .exe, Images were not showing. I used Pycharm IDE and although the pathing worked in there, It did not in the build. AI created the path.py script and I simply updated any QPixmaps to use the AI created resource path.

confetti_widget.py:
This one scratched my brain a bit, So I asked AI a few questions and it generated me this script without asking, so out of curiosity I used it too see what it was like and it was better than expected so I left it in.

title_bar.py:
I wanted to bind to the Windows Title Bar buttons but according to AI that isn't a possibility so once again AI generated this script and out of curiosity I just rolled with it. I also had an issue with the jesus easter egg only showing on one page, So AI made it a part of this class.
