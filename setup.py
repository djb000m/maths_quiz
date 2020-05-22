from setuptools import setup

setup(
    name="maths_quiz",
    version="0.1",
    author="djb000m",
    description=(
        "A simple python script to randomly generate a maths quiz for children."
    ),
    py_modules=["matsh_quiz"],
    install_requires=[
        "colorama; platform_system=='Windows'",  # Colorama is only required for Windows.
        "click",
        "py_expression_eval",
        "emoji",
    ],
    entry_points="""
        [console_scripts]
        maths_quiz=maths_quiz:cli
    """,
)
