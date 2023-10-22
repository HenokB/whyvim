<center>
<h1>WhyVim</h1>
<h3>⚠️A work in progress. Adding more features everyday<h3>
</center>
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
## GitHub User Analytics:
```bash

show_github_stats(): Displays detailed GitHub statistics for a given username. This includes repositories, stars, top languages, and contact information.
compare_users(): Compares two GitHub users based on various attributes like followers, following, public repos, total stars, and their top languages.

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