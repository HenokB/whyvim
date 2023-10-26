<p align="center">
<h1>WhyVim</h1>
<h3>⚠️A work in progress. Adding more features everyday</h3>
</p>


This Python script offers a collection of functionalities for GitHub analytics and local directory management. It provides the ability to fetch user statistics from GitHub, compare GitHub users, get detailed analytics on repositories, compare repository branches, and manage directories on your local system.



# Features:
Local Directory Management:
```bash
show_dir_tree(): Displays the current directorys tree.
make_dir(name): Creates a directory with the given name.
change_dir(name): Change to a specified directory.
go_up(): Navigate up to the parent directory.
run_git_command(git_command): Execute Git commands.
```

## Compare to GitHub users.

You can compare two users and it will do a visualization of the users stats and output it like below.

#### Demo

```bash
>>> compare
Enter first GitHub username: HenokB
Enter second GitHub username: rauchg
```

![compare](https://github.com/HenokB/whyvim/assets/46082799/cf8e9b34-1f0a-4c8b-ab0f-5a4e075dc58c)


## GitHub User Analytics:
```bash
show_github_stats(): Displays detailed GitHub statistics for a given username. This includes repositories, stars, top languages, and contact information.
```
#### Demo
```bash
>>> showgithub
Enter the GitHub username: 🧑‍💻 HenokB
🔍 Repositories of HenokB (Page 1) 🔍
📦 100-nlp-papers | ⭐ 0 | ⚙️ None
📦 Algorithms-in-Amharic | ⭐ 2 | ⚙️ None
📦 alx-low_level_programming | ⭐ 0 | ⚙️ C
📦 alx-onboarding | ⭐ 0 | ⚙️ None
📦 alx-pre_course | ⭐ 0 | ⚙️ Shell
📦 alx-system_engineering-devops | ⭐ 0 | ⚙️ Shell
📦 alx-zero_day | ⭐ 0 | ⚙️ Shell
📦 Amharic-BMI-calculator- | ⭐ 2 | ⚙️ Dart
📦 amharicprocessor | ⭐ 0 | ⚙️ None
📦 amnlp | ⭐ 0 | ⚙️ None
📦 awesome-github-profiles | ⭐ 1 | ⚙️ None
📦 Donut | ⭐ 1 | ⚙️ Python
📦 ethionlp.github.io | ⭐ 0 | ⚙️ None
📦 file-converter | ⭐ 0 | ⚙️ Python
📦 fine-tuning-BERT | ⭐ 0 | ⚙️ Jupyter Notebook
📦 flask-app | ⭐ 1 | ⚙️ Python
📦 Fractals-with-Python | ⭐ 1 | ⚙️ Python
📦 Fun-with-Cpp | ⭐ 1 | ⚙️ C++
📦 Functional-Programming | ⭐ 1 | ⚙️ Haskell
📦 getting-started | ⭐ 0 | ⚙️ None
📦 glossary | ⭐ 0 | ⚙️ HTML
📦 GPU-Puzzles | ⭐ 0 | ⚙️ Jupyter Notebook
📦 Grafo | ⭐ 1 | ⚙️ JavaScript
📦 Hack-the-Runway | ⭐ 0 | ⚙️ JavaScript
📦 hackathon-participants-March-2022 | ⭐ 0 | ⚙️ None
📦 HackerRank-30-Days-of-Code | ⭐ 1 | ⚙️ C++
📦 HackerRank-C-Practice-solutions | ⭐ 1 | ⚙️ C
📦 Hacking-Birthday-Bash | ⭐ 1 | ⚙️ Python
📦 Hacktoberfest-2021 | ⭐ 1 | ⚙️ Jupyter Notebook
📦 HenokB | ⭐ 0 | ⚙️ None
📦 henokb.github.io | ⭐ 0 | ⚙️ None
📦 hypershift | ⭐ 0 | ⚙️ None
📦 ihp | ⭐ 0 | ⚙️ None
📦 InterviewPrep | ⭐ 1 | ⚙️ Python
📦 Jest | ⭐ 0 | ⚙️ None
📦 kubernetes | ⭐ 0 | ⚙️ None
📦 Learn-Go | ⭐ 3 | ⚙️ Go
📦 learningReact | ⭐ 0 | ⚙️ None
📦 lotus | ⭐ 0 | ⚙️ Python
📦 masakhane-mt | ⭐ 0 | ⚙️ None
📦 mdanalysis | ⭐ 0 | ⚙️ None
📦 Member.json | ⭐ 1 | ⚙️ None
📦 Merge-Sort | ⭐ 2 | ⚙️ C++
📦 mindsdb | ⭐ 0 | ⚙️ None
📦 MinnHacks | ⭐ 0 | ⚙️ JavaScript
📦 MLH-Local-Hack-Day- | ⭐ 1 | ⚙️ Python
📦 mlh-mascot | ⭐ 1 | ⚙️ HTML
📦 movie_land | ⭐ 0 | ⚙️ CSS
📦 NeurIPS-2022 | ⭐ 1 | ⚙️ None
📦 nlp-tutorial | ⭐ 0 | ⚙️ None
📦 Peace-Out-Hacks | ⭐ 1 | ⚙️ CSS
📦 prep-portfolio-22.OCT.PREP.2 | ⭐ 0 | ⚙️ HTML
📦 prep-project-22.OCT.PREP.2 | ⭐ 0 | ⚙️ None
📦 Project-Euler | ⭐ 1 | ⚙️ Python
📦 puzzle.github.io | ⭐ 0 | ⚙️ HTML
📦 pydatastructs | ⭐ 0 | ⚙️ None
📦 pysis | ⭐ 0 | ⚙️ Python
📦 raspy | ⭐ 0 | ⚙️ None
📦 react-practice | ⭐ 1 | ⚙️ None
📦 React-todo-list | ⭐ 1 | ⚙️ HTML
📦 roadmaps | ⭐ 0 | ⚙️ None
📦 scikit-llm | ⭐ 0 | ⚙️ None
📦 Secure_Health | ⭐ 0 | ⚙️ JavaScript
📦 Simple-Movie-Recommendation-with-Machine-Learning | ⭐ 1 | ⚙️ Jupyter Notebook
📦 snakesandhackers | ⭐ 0 | ⚙️ None
📦 Startups-in-Ethiopia | ⭐ 4 | ⚙️ None
📦 summer-of-haskell | ⭐ 0 | ⚙️ None
📦 Teacher-Aid | ⭐ 3 | ⚙️ JavaScript
📦 TeachMeCLikeIm5 | ⭐ 1 | ⚙️ None
📦 team_planet | ⭐ 1 | ⚙️ Python
📦 Tensor-Puzzles | ⭐ 0 | ⚙️ None
📦 TheHackTrical | ⭐ 0 | ⚙️ None
📦 Tic-Tac-Toe- | ⭐ 1 | ⚙️ Python
📦 vaxman- | ⭐ 0 | ⚙️ Python
📦 whyvim | ⭐ 0 | ⚙️ Python
📦 WildHacks | ⭐ 1 | ⚙️ JavaScript
📦 Wonder | ⭐ 0 | ⚙️ JavaScript
📦 zero_day | ⭐ 0 | ⚙️ None

📊 Total Repos: 78
🌟 Total Stars: 41
🔝 Top 3 Languages:
Python (14 repos)
JavaScript (7 repos)
HTML (5 repos)

💼 Contact Information for HenokB 💼
🐦 Twitter: https://twitter.com/henokademtew
```

Repository Analytics: display_repository_analytics(): Provides commit activity and contributor stats for a given user's repository.
compare_branches(): Compares two branches of a repository and fetches detailed analytics.
Utilities:
```

Functions like fetch_user_details(), fetch_user_repos(), fetch_commit_activity(), and fetch_contributors_stats() assist in fetching relevant data from the GitHub API for the above functionalities.

## Visualization:
Uses matplotlib to generate bar and pie charts for visual comparison.
Requirements:
Python 3.x
requests: For making API requests to GitHub.
matplotlib: For visualizing data.
numpy: Required for operations with matplotlib.
Usage:
Run the script in your preferred Python environment. Depending on the feature you wish to use, call the appropriate function. For instance:

```python

show_github_stats()
#Will prompt you for a GitHub username and then display detailed statistics about the user.
```
### Notes:
Ensure you have the required libraries installed using ```pip install requests matplotlib numpy```.
As this script uses the GitHub API, there's a limit to the number of requests you can make in a given time period. Make sure to consider this when making multiple or frequent calls.


**Contribution**
Feel free to contribute to this project by adding more features or optimizing the existing ones. Pull requests are welcome!

Henok Ademtew 2023