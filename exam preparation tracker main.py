
"""Exam Preparation Tracker - main menu."""

from exam_tracker import storage
from exam_tracker.planner import days_left
from exam_tracker.report import show_plan, show_report
from exam_tracker.tracker import Tracker
from exam_tracker.validators import ask_date, ask_number


def choose_subject(tracker):
    names = tracker.subject_names()
    print("\nSubjects:")

    i = 1
    for name in names:
        print(f"  {i}. {name}")
        i = i + 1

    choice = ask_number("Choose subject: ", 1, len(names))
    return names[choice - 1]


def choose_topic(tracker):
    subject = choose_subject(tracker)
    topics = tracker.get_topics(subject)

    print(f"\nTopics in {subject}:")

    i = 1
    for topic in topics:
        print(f"  {i}. {topic.name}")
        i = i + 1

    choice = ask_number("Choose topic: ", 1, len(topics))
    return topics[choice - 1]


def mark_studied(tracker):
    topic = choose_topic(tracker)
    topic.mark_studied()
    print(f"  '{topic.name}' marked as studied.")


def rate_confidence(tracker):
    topic = choose_topic(tracker)
    confidence = ask_number(
        "Confidence (1 = low, 5 = high): ", 1, 5
    )
    topic.set_confidence(confidence)
    print(f"  Confidence for '{topic.name}' saved.")


def add_score(tracker):
    topic = choose_topic(tracker)

    score = ask_number(
        "Practice test score (0 to 10): ", 0, 10
    )

    topic.add_score(score)

    print(
        f"  Score added. Average for "
        f"'{topic.name}' is {topic.average_score():.1f}/10."
    )


def set_exam_date(tracker):
    subject = choose_subject(tracker)

    date_text = ask_date("Exam date (DD-MM-YYYY): ")

    tracker.exam_dates[subject] = date_text

    if days_left(date_text) < 0:
        print("  Note: this date has already passed.")

    print(f"  Exam date for {subject} saved.")


def main():
    tracker = Tracker()
    storage.load(tracker)

    print("=" * 62)
    print("            EXAM PREPARATION TRACKER")
    print("=" * 62)

    while True:
        print("\nMAIN MENU")
        print("  1. View progress report")
        print("  2. Mark a topic as studied")
        print("  3. Rate confidence in a topic")
        print("  4. Add a practice test score")
        print("  5. Set exam date")
        print("  6. Show study plan")
        print("  7. Exit")

        choice = ask_number("Enter your choice: ", 1, 7)

        if choice == 1:
            show_report(tracker)

        elif choice == 2:
            mark_studied(tracker)

        elif choice == 3:
            rate_confidence(tracker)

        elif choice == 4:
            add_score(tracker)

        elif choice == 5:
            set_exam_date(tracker)

        elif choice == 6:
            show_plan(tracker)

        else:
            storage.save(tracker)
            print("Progress saved. Good luck for your exams!")
            break

        if choice in (2, 3, 4, 5):
            storage.save(tracker)


if __name__ == "__main__":
    main()
