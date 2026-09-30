# Exam Preparation Tracker

A simple console project in Python that helps a first-semester student track exam preparation for **Calculus**, **Python** and **Environmental Sustainability**.

## Overview
The student can mark topics as studied, rate confidence, save practice test scores, set exam dates and get a study plan that shows the weakest topics first. Everything is saved in a JSON file, so progress is not lost when the program is closed. No database is used.

## Features
- Progress report with progress bars for every subject
- Mark a topic as studied
- Rate confidence in a topic (1 to 5)
- Add practice test scores (0 to 10) and see the average
- Set exam dates and see days left and topics to study per day
- Study plan that lists the weakest topics first
- Input validation for numbers and dates
- Progress is saved automatically after every change

## Syllabus Covered
| Subject | Topics |
|---|---|
| Calculus | Limit, Continuity, Partial Derivative |
| Python | List, Dictionary, Array |
| Environmental Sustainability | Photochemical Smog, Air Pollution, Water Pollution |

## Technologies Used
- Python 3.8 or above (only the standard library: `array`, `json`, `datetime`, `os`, `unittest`)
- Git and GitHub for version control

## Project Structure
```
exam_prep_tracker/
├── main.py                  # menu and program flow
├── exam_tracker/
│   ├── __init__.py
│   ├── syllabus.py          # subjects and topics (dictionary)
│   ├── topic.py             # Topic class (uses array for scores)
│   ├── tracker.py           # Tracker class (keeps all topics)
│   ├── planner.py           # days left, weakest topics
│   ├── report.py            # progress report and study plan
│   ├── storage.py           # save and load JSON file
│   └── validators.py        # input checking
├── tests/
│   └── test_tracker.py      # unit tests
├── data/                    # progress.json is created here
├── docs/                    # diagrams and project report
├── README.md
└── statement.md
```

## How to Install and Run
1. Install Python 3 from python.org (no extra libraries are needed).
2. Download or clone this repository:
   ```
   git clone <your-repository-link>
   cd exam_prep_tracker
   ```
3. Run the program:
   ```
   python main.py
   ```
   (Use `python3 main.py` on Mac/Linux.)

## How to Use
Type the number of an option in the main menu and press Enter.

```
MAIN MENU
  1. View progress report
  2. Mark a topic as studied
  3. Rate confidence in a topic
  4. Add a practice test score
  5. Set exam date
  6. Show study plan
  7. Exit
```
Dates must be written as `DD-MM-YYYY`, for example `15-12-2026`.

## Sample Output
```
Python   [######----] 66%
  Topic                 Studied   Confidence  Avg Score
  List                  Yes       4           -
  Dictionary            Yes       -           9.0/10
  Array                 No        -           -
```

## Testing
Run all unit tests from the project folder:
```
python -m unittest discover tests -v
```
The tests check the Topic and Tracker classes, input validation, the planner and saving/loading of the file (15 tests).

## Author
Made as part of the VITyarthi "Build Your Own Project" evaluation for Python Essentials.
