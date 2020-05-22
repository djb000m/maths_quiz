#!/usr/bin/env python


class Question:
    def __init__(
        self, question_text="question text", question_answer="question answer"
    ):
        self.__question_text = question_text
        self.__question_answer = question_answer

    def __str__(self):
        return f"Q: {self.__question_text}?\nA: {self.__question_answer}"

    ## Properties
    @property
    def question_text(self):
        return self.__question_text

    @question_text.setter
    def question_text(self, txt):
        self.__question_text = txt

    @property
    def question_answer(self):
        return self.__question_answer

    @question_answer.setter
    def question_answer(self, txt):
        self.__question_answer = txt
