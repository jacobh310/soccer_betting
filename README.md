# British Premier League Home Win Predictor
## Project at a glance
- Collected data from https://www.football-data.co.uk/englandm.php Seasons 2000-2021
- Light Data Exploration to see distrubtution and scatter plots of different statistcis
- Trained KNearest Neighbot, Random Forests, XGBoost, and Naive Bayes 
- Built Web application
#### 📌 [See the web app in action here](https://jacobh310-soccer-betting-app-frontend-game-predictions-cty251.streamlit.app)

## Data Collection
In game statistics from the Premier league seasons 2000-2021 were collected from https://www.football-data.co.uk/englandm.php. Each season has its own CSV file. The rows were mathces and the columns were game statitistcis. A row would contain the teams playing each other the respective stats for that game. 
#### Example
Home Team | Away Team | Home Shots | Away Shots| Home Goals| Away Goals| etc

A the british premier league has 20 teams and each team plays eachother twice. There would be a total of 380 matches each season which equals the amount of rows for each CSV file

## Data Cleaning and Preprocessing
As mentioned above, each row only contained what happened in that game. I created a preprocessing function that would take the rolling sum of each stats for each team and the divide by the matchweek to get the average. Then I removed the first 4 games of each season so the averae stats can stabilize. Each season was its own csv file so the above preocessing was done in a data frame for each season then appending together to make one large data set for seasons 2000-2021

#### Feature Engineering
The following features were engineered and added to the data set
- HTP: Home Team Points
- ATP: Away Team Points
- HTFormPts: Home points in the last 5 games
- ATFormPts: Aeay points in the last 5 games
- HTGD: Home Total Goals Difference
- HTSD: Home Total Shots Difference
- HTTSD: Home Total Target Shots Difference
- ATGD: Away Total Goals Difference
- ATSD: Away Total Shots Difference
- ATTSD: Away Total Target Shots Difference
- FPD: Form Points Difference

## Exploratory Data Analysis
