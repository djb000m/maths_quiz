# Maths Quiz!

A simple python script to randomly generate a maths quiz for children.

## Install

1. Clone the repository to your computer

```
  git clone git@bitbucket.org:djb000m/maths_quiz.git
```

2. Create a new python virtual environment:

```
  python -m venv {environment_location}

```

3. Activate the virtual environment and Use pip to install the script:

```
  cd {script_directory}
  source {environment_location}/bin/activate
  pip install .
```

4. Run the script:

```
  Usage: maths_quiz [OPTIONS]

    A simple Maths Quiz python application for children

  Options:
    -q, --questions INTEGER  The number of question you want in your quiz,
                            default is 10

    -d, --difficulty TEXT    The difficulty level for the quiz; Easy, Medium or
                            Hard. Default is Easy

    --help                   Show this message and exit.

```

> #### Notes:
>
> _If **--number** is not specified then 10 questions will be generated._
