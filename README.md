# aoc-2022

## Set Year
- Set `AOC_YEAR` variable in [.env](.env) to current year

## Set Session Token 
- go to https://adventofcode.com/ 
- make sure you are logged in
- open devtools
- copy value of `session` cookie
- paste into `AOC_SESSION` variable in [.env](.env)

## Start New Day
- creates base files for day from templates
- downloads input file from adventofcode.com
```
$ pipenv run new {day}

example:
$ pipenv run new 1
```

## Set Test Data
- create files in the `inputs` folder for each sample data provided
- add the samples to the `sample_files` method in `Day{day}Part{part}Controller` with filepath and expected result:
```python
def sample_files(self) -> list[(str, int)]:
    return [("src/days/day02/inputs/sample01.txt", 18)]
```
Failure to set test data will result in:
```
Exception: No sample files setup. Add these to: Day03PartAController
```
Failure to pass test data will result in:
```
Exception: Test Fail: Sample src/day03/input_sample01.txt, expecting: 0, actual: None
```

## Run Day Part
```
$ pipenv run part {day} {part}

example: 
$ pipenv run part 1 a
```

## Submit Result
```
$ pipenv run submit {day} {part}

example: 
$ pipenv run submit 1 a
```

## Testing
Pytest is used for testing
```
$ pipenv run test
```

## Linting
Flake8 is used for linting
```
$ pipenv run lint
```

## Formatting
Black is used for formatting
```
$ pipenv run fmt
```

## Run all quality checks and auto-format
``` 
$ pipenv run checks 
``` 

## Install Pre-Commit hook to run all checks
```
$ pipenv run setup
```

## CI
Github Actions is used for CI

[CI Workflow on Github Actions](https://github.com/tom-haug/AdventOfCode2017/actions/workflows/ci.yml)

[Pipeline Config](.github/workflows/ci.yml)
