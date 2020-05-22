#!/usr/bin/env python

## Maths Quiz!
## A simple maths quiz for young children. Randomly generates a number of simple maths sums
## and checks the answers.

## TODO: Change colours depending on results (20%, 40%, 60%, 80%, 100%)
## TODO: Change colours of check and cross marks (green & red)
## TODO: Add a simple prompt menu system instead of defaults for setting up quiz
## TODO: Error Handling!!!!!!(!)
## TODO: Persistent Users and High Scores (generate score based on accuracy and speed)
## TODO: Add a multiplication option
## TODO: Add a division option
## TODO: Add a choice for types of quiz (e.g. mixed, adding, subtracting etc.)
## TODO: add a times tables mode (user picks the number)
## TODO: Get the Emojis working!


import click
import time
import random
import emoji
from py_expression_eval import Parser
from question import Question


@click.command()
@click.option(
    "--questions",
    "-q",
    help="The number of question you want in your quiz, default is 10",
    default=10,
)
@click.option(
    "--difficulty",
    "-d",
    help="The difficulty level for the quiz; Easy, Medium or Hard. Default is Easy",
    default="easy",
)
def cli(questions, difficulty):
    """
    A simple Maths Quiz python application for children

    Args:
        questions (Int): The number of questions desired in the quiz
        difficulty (String): The difficulty level of the quiz questions, defined in d_value below
    """

    # clear the screen
    click.clear()

    # define the difficulty level values - these are used as maximum values for addition & subtraction
    d_value = {"easy": 10, "medium": 30, "hard": 100}

    if difficulty not in d_value:
        difficulty = "easy"

    maths_quiz(
        questions,
        {"easy": easy_difficulty, "medium": medium_difficulty, "hard": hard_difficulty}[
            difficulty.lower()
        ](d_value[difficulty.lower()]),
    )


def maths_quiz(num_q, d_value):
    """
    Main function that creates the quiz object and calls helpers to populate it.
    Prints the questions, takes a user input then compares against the answer

    Args:
        num_q ([Int]): The number of questions to generate for the quiz
        d_value ([String]): The difficulty of the questions. Easy, Medium or Hard
    """

    # Create the quiz dictionary and populate it with question instances
    quiz = create_quiz(num_q, d_value)

    # correct answers, zero to start with ;)
    q_correct = 0
    quiz_results = {}

    for q in quiz:
        question = f"Q{q+1}: {quiz[q].question_text}?    "
        answer = input(question)

        # snapshot of time after 1st question is answered (it's for kids!)
        if q == 0:
            t0 = time.time()

        # handle any non-numerical answers
        # the quiz is timed, so just give -1 as the answer
        try:
            if int(answer) == quiz[q].question_answer:
                q_correct += 1
                quiz_results[question] = answer + "   ✓".rjust(6)
            else:
                quiz_results[question] = answer + "   ✗".rjust(6)
        except ValueError:
            quiz_results[question] = emoji.emojize(":zany face:") + "   ✗".rjust(6)

    # snapshot of time after last question
    t1 = time.time()

    # calculate total elapsed time
    total_time = t1 - t0

    click.clear()

    # print results summary with time (two decimal places)
    print(f"You got {q_correct} out of {num_q} right in {total_time:.2f} seconds\n")

    # print results
    for q, a in quiz_results.items():
        print(q.ljust(15) + str(a).rjust(10))

    # for looks
    print("\n")


def easy_difficulty(d_value):
    """
    Prints a motivational message and returns the value that is supplied with no modification.
    A bit hacky, but does the job at the moment
    TODO: Improve this?

    Args:
        d_value (Int): Difficulty value for the quiz (defined at runtime)

    Returns:
        Int: Just returns the same value that was supplied
    """
    click.secho(
        f"\nEasy Difficulty\nThis should be a piece of cake!\n",
        fg="green",
        blink=False,
        underline=False,
        bold=True,
    )
    return d_value


def medium_difficulty(d_value):
    """
    Prints a motivational message and returns the value that is supplied with no modification.
    A bit hacky, but does the job at the moment
    TODO: Improve this?

    Args:
        d_value (Int): Difficulty value for the quiz (defined at runtime)

    Returns:
        Int: Just returns the same value that was supplied
    """
    click.secho(
        f"\nMedium Difficulty\nGo on, try your best!\n",
        fg="yellow",
        blink=False,
        underline=False,
        bold=True,
    )
    return d_value


def hard_difficulty(d_value):
    """
    Prints a motivational message and returns the value that is supplied with no modification.
    A bit hacky, but does the job at the moment
    TODO: Improve this?

    Args:
        d_value (Int): Difficulty value for the quiz (defined at runtime)

    Returns:
        Int: Just returns the same value that was supplied
    """
    click.secho(
        f"\nHard Difficulty!", fg="red", blink=True, underline=False, bold=True,
    )
    click.secho(
        f"Up for a Challenge? Let's go!\n",
        fg="red",
        blink=False,
        underline=False,
        bold=True,
    )
    return d_value


def type_of_sum():
    """
    Returns a type of sum to create - addition or subtraction

    Returns:
        String: String description of the type of sum to create
    """
    sums = {0: "+", 1: "-", 3: "*", 4: "/"}

    return sums.get(random.randint(0, 1))


def create_question(d_value):
    # create Parser object from py_expression eval in order to parse maths strings
    parser = Parser()

    # set qanswer to -1 to start the loop
    qanswer = -1

    # Loop until we have a positive value
    while qanswer < 0:
        qsum = f"{random.randint(0,d_value)}{type_of_sum()}{random.randint(0,d_value)}"
        qanswer = parser.parse(qsum).evaluate({})

    return (qsum, qanswer)


def create_quiz(num_q, d_value):
    """
    Create and return a quiz dictionary

    Args:
        num_q (Int): Size of quiz to generate
        difficulty (String): Difficulty to questions to generate. Easy, Medium or Hard
    """

    # create dictionary to hold the quiz question objects
    quiz = {}

    for i in range(num_q):
        q = create_question(d_value)
        quiz[i] = Question(q[0], q[1])

    return quiz
