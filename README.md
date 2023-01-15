# The Mansion - Python adventure game.

Live link to the application can be found here: [The Mansion](https://project-3-python-game.herokuapp.com/)

Link to repository on GitHub can be found [here](https://github.com/adrian-cucuet/project3-python-game)

## How to play

* The overall aim of the project is to create and adventure game, where the player is has to solve several quests in order to find the killer.
* The game starts by asking the user to input a name.

![Game intro](/images/game-intro.png)

* The user has to follow the story and find clues around the mansion.
* Every quest has a story and possible answers. The user need to decide what answer to choose.
* If the user is coming to a dead end, the game will automatically bring him back to the last quest.

![Dead end](/images/dead-end.png)

## Planning

![Flowchart](/images/plan.png)

## Validator

* No errors identified from syntax check online [infoheap](https://infoheap.com/python-lint-online/)

* Project code passed through the CI Python Linter with no issues. The only issues were related to longer code, but that has to do with the emoji codes.

![CI Python Linter](/images/CI-linter.png)

## Bugs fixed

* During testing I found the input is case sensitive. I fixed the issue by using .lower() on the users answers. 

![Case Sensitive](/images/case-sensitive.png)

* I created an error message highlighted in red. The user is prompt with an error message about what answer is expected.

![Error Message](/images/error-message.png)

## Unfixed Bugs

* No unfixed Bugs.

## Deployment

The project was deployed using Heroku. The steps to deploy are as follows:

  1. Go to Heroku
  2. Go to 'New' and select 'Create a new app'
  3. Input your app name and create app.
  4. Navigate to 'Settings'
  5. Install the needed buildpacks. Select Python and install and then node.js and 
     install and then click save. They must be in this order.
  6. Navigate to the 'Deploy' section.
  7. Connect to GitHub, search for your repo and confirm.
  8. Choose branch to deploy.
  9. Your app should now be available to see. You can choose whether to have your app 
     automatically redeploy with every push or to keep it manual.

## Languages used 

 * Python

## Technologies used

 * Github 

 * Gitpod

 * Heroku

 * Code Institute template

 ## Future Expansion

 * Create an option to choose the difficulty level for the game. Have two difficulties for the game (basically having two separate games).

 ## Credits

 * Code Institute for the template and GUI.

 * [FIGlet](http://www.figlet.org/) for the pyfiglet ASCII art fonts module.

 * [Emoji](https://carpedm20.github.io/emoji/docs/) for the emoji module.

 * [Termcolor](https://pypi.org/project/termcolor/) for the text color module.
