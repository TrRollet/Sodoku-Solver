# Sodoku Solver

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

## How to use
- **Parameters:**
    - `-p <file_name>` to print the solution into a file
    - `-f <file_name">` to solve a sodoku from a file (check exemple_file)

- **Format of sodoku file:**
    - 9 lines of 9 numbers
    - . for empty cell
    - 1 to 9 for filled cell
    - __Example:__
    ```
        2..8.4..6
        ..6...5..
        .74...92.
        3...4...7
        ...3.5...
        4...6...9
        .19...74.
        ..8...2..
        5..6.8..1
    ```

- **Example of use:**
    - `python3 main.py -f exemple_file` <br>
    <img src="https://i.imgur.com/8s5H0He.png"
         alt="Exemple 1"
         style="margin-right: 10px;
                margin-bottom: 10px;
                margin-top: 25px;
                width: 45%;" />

    - `python3 main.py -f exemple_file -p solution_file` <br>
    <img src="https://i.imgur.com/x61auWq.png"
         alt="Exemple 2"
         style="margin-right: 10px;
                margin-bottom: 10px;
                margin-top: 25px;
                width: 45%;" />
        
    - `python3 main.py` <br>
    <img src="https://i.imgur.com/ZfpSfy1.png"
         alt="Exemple 3"
         style="margin-right: 10px;
                margin-bottom: 10px;
                margin-top: 25px;
                width: 75%;" />


[contributors-shield]: https://img.shields.io/github/contributors/TrRollet/Sodoku-Solver.svg?style=for-the-badge
[contributors-url]: https://github.com/TrRollet/Sodoku-Solver/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/TrRollet/Sodoku-Solver.svg?style=for-the-badge
[forks-url]: https://github.com/TrRollet/Sodoku-Solver/network/members
[stars-shield]: https://img.shields.io/github/stars/TrRollet/Sodoku-Solver.svg?style=for-the-badge
[stars-url]: https://github.com/TrRollet/Sodoku-Solver/stargazers
[issues-shield]: https://img.shields.io/github/issues/TrRollet/Sodoku-Solver.svg?style=for-the-badge
[issues-url]: https://github.com/TrRollet/Sodoku-Solver/issues
[license-shield]: https://img.shields.io/github/license/TrRollet/Sodoku-Solver.svg?style=for-the-badge
[license-url]: https://github.com/TrRollet/Sodoku-Solver/blob/main/LICENSE
