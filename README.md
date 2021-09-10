![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)
[![View My Profile](https://img.shields.io/badge/View-My_Profile-green?logo=GitHub)](https://github.com/ndleah)
[![View Repositories](https://img.shields.io/badge/View-My_Repositories-blue?logo=GitHub)](https://github.com/ndleah?tab=repositories)


# Currency Converter

<p align="center">
  <img src="https://forthebadge.com/images/badges/built-with-love.svg">
  <img src="https://forthebadge.com/images/badges/made-with-python.svg">
</p>

The app is built for performing currency conversion using data fetched from an open-source API: https://www.frankfurter.app/.

## ⚙️ Usage

In the project directory, you can run:
```bash
python main.py AUD EUR
```

If you are using `Pipenv`, then you can run:

```bash 
pipenv python main.py AUD EUR
```

## 🎒 Package Dependencies

```bash
import requests
```

## 🏗️ Structure
```
├── api.py             <- script contains the code for calling API endpoints 
├── currency.py        <- contains the code for checking if currency code is valid, store results and format final output
├── main.py            <- main program used for entering the input parameters (currency codes) and display the results
├── Pipfile            <- contain information for the dependencies of the project
├── Pipfile.lock       <- specify, based on the packages present in Pipfile
├── README.md          <- a markdown file containing student details, a description of this project, listing of all Python functions and classes and instructions for running the code
├── test_api.py        <- python script for testing code from api.py
└── test_currency.py   <- python script for testing code from currency.py
```

## ✨ Contribution

Contributions, issues, and feature requests are welcome!

To contribute to this project, see the GitHub documentation on **[creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)**.


## 👏 Support

Give a ⭐️ if you like this project!


## 👩‍💻 Author
Leah Nguyen

___________________________________

<p>&copy; 2021 Leah Nguyen</p>