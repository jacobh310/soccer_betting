# British Premier League Home Win Predictor
## Project at a glance
- Collected data from https://www.football-data.co.uk/englandm.php Seasons 2000-2021
- Light Data Exploration to see distrubtution and scatter plots of different statistcis
- Trained KNearest Neighbot, Random Forests, XGBoost, and Naive Bayes 
- Built Web application
#### 📌 [See the web app in action here](https://jacobh310-soccer-betting-app-frontend-game-predictions-cty251.streamlit.app)

## Introduction
The Sports Betting market is worth $74.2 billion dolalrs as of 2021 and is expexted to reach $129.3 billion by 2028 according to Global News Wire There is no question that your average sports gambler is competeting against companies that put in millions into having the best algorithims to price their odds all with the goal of making money of the average sports bettor. I tried to tilt the odds back to the sports bettor favor by training a machine learning algorithim that predicts the home teams winning probability. **The goal of this project is to build a tool sports better can leverage to make more informed betting decisions**

## Data Collection
In game statistics from the Premier league seasons 2000-2021 were collected from https://www.football-data.co.uk/englandm.php. Each season has its own CSV file and has a plethora of different in game. But is also has odds from different bookmkaers for each game. This will come into play when evaluating the models. The rows were mathces and the columns were game statitistcis. A row would contain the teams playing each other the respective stats for that game. 
#### Example
Home Team | Away Team | Home Shots | Away Shots| Home Goals| Away Goals| etc

A the british premier league has 20 teams and each team plays eachother twice. There would be a total of 380 matches each season which equals the amount of rows for each CSV file

## Data Cleaning and Preprocessing
As mentioned above, each row only contained what happened in that game. I created a preprocessing function that would take the rolling sum of each stats for each team and the divide by the matchweek to get the average. Then I removed the first 4 games of each season so the averae stats can stabilize. Each season was its own csv file so the above preocessing was done in a data frame for each season then appending together to make one large data set for seasons 2000-2021

Since the model is going to predict home team wins, labels were made where 1 indicates home team win and 0 indicates draw or home team loss.

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
### Categorical Variables
From the chart below you can see that home wins are almot split down the middile with the home team winning apporiximately 45% of the time. Having a unbalanced dataset is going to be problem
<p ><img align="center" src="https://raw.githubusercontent.com/jacobh310/soccer_betting/main/Images/Home_win_barchart.png"
    title="App Architecture" width="500"/></p>
The chart below dissects the match outcome (Home win, draw, away win) by season. You can see that the home team weins a majority of the time excet for 2021 where the away team won more.This comes into effect when we evaluating the profitability of the models. The model struggles to make money when the home team is winning less. More on that later.
<p ><img align="center" src="https://raw.githubusercontent.com/jacobh310/soccer_betting/main/Images/Wins%20by%20season.png"
    title="App Architecture" width="900"/></p>
The chart below dissects each home and away goals by season. You can see that the home team outscores the away team by a pretty large quantity every season except for 2021 where the home and away teams scored almost the same amount of goals. That contributed to home teams winning at a lower rate than usual  

A home team usually has the advantage becasue they are played with home fans. The intimidation and yelling at the away team makes it harder for them to lose. But in 2021 a majority of the games were played without fans becasue of the covid-19 pandemic which equaled the playing field. This just goes to show you how fans play a huge 
role in the outcome of the game. Next time, I will discard the 2021 season from the data set so the algorithims do not pick up on the pattern. 

<p ><img align="center" src="https://raw.githubusercontent.com/jacobh310/soccer_betting/main/Images/Goals%20by%20season.png"
    title="App Architecture" width="900"/></p>

### Numerical Variables

Most of the data looks normally distributed with some plots having significant 0 values 
<p ><img align="center" src="https://raw.githubusercontent.com/jacobh310/soccer_betting/main/Images/histograms.png"
    title="App Architecture" width="900"/></p>
    

#### I have interactive scatter and bar charts in the web app I deployed for this project. [Check it out here](https://jacobh310-soccer-betting-app-frontend-game-predictions-cty251.streamlit.app/Exploratory_Data_Analysis)

## Model Building

### Establishing a baseline
The model will only predict only home wins. The baseline is going to be home team winning percentage for each data set (Train and Dev). This is going to emulate betting on the hometeam to win very game. 

### Correlation

I dropped the bottom 4 features with the least correlation which are HTY, HTR, ATY, ATR. These are the average red and yellow cards per game for the home and away team
<p ><img align="center" src="https://raw.githubusercontent.com/jacobh310/soccer_betting/main/Images/correlation.png"
    title="App Architecture" width="500"/></p>

#### Train Home Win Percentae: 46.73%
#### Dev Home Win Percentage: 48.26%

**Features:** Average stats for each team split by home and away  
**Labels:**  
1: Home team win  
0: Draw or home team loss  
**Ouput:** Probability out of 100% of home team winning

## Evaluate Model Performance
### Classfication Metrics
<p ><img align="center" src="https://raw.githubusercontent.com/jacobh310/soccer_betting/main/Images/model%20scores.png"
    title="App Architecture" width="500"/></p>

### Profit/Loss
These classification metrics should serve as a guideline but the ultimate goal is to make money from the predictions by placing bets on the model. We tested two betting strateies: Home Team Win and Positive Expevted Value

#### Home Win
This stratey is simple. If the model gives the home team a greater than 50% of winning then we are going to place a mock $100 dollar bet. If the model is right, the payout is calculated using the odds and added to the current balance. If the model is wrong then we are going to subtract $100 from the current balance
<p ><img align="center" src="https://raw.githubusercontent.com/jacobh310/soccer_betting/main/Images/HW_pl_table.png"
    title="App Architecture" width="300"/></p>
    
<p ><img align="center" src="https://raw.githubusercontent.com/jacobh310/soccer_betting/main/Images/hw_pl.png"
    title="App Architecture" width="700"/></p>



#### Positive Expected Value
To explain this strategy, I am going to need to go over some basic sports betting terminology. 
**Decimal Odds:** The payout if a bet is won. Decmal odds of 2 means that if you bet $10 you would recieve $20. $10 of the original bet and $10 profit. The higher the decimal odds the higher the pay  
**Implied Probability:** The probability implied by the decmial odds line. Implied probability = 1/Decimal Odds. A decimal odds of 2 has an implied probability of 50%. The higher the odds the lower the probability. Meaning low proably events have a higher payout.  

Without getting to much into it, the home odds for each game are converted to implied probability and will be compared to the model's predicted probability. If the model has a higher probability than the bookmkaers implied probability, then that signals to bet on the home team. The current balances are going to be calculated like in the Home Win strategy. 

<p ><img align="center" src="https://raw.githubusercontent.com/jacobh310/soccer_betting/main/Images/EV_pl_table.png"
    title="App Architecture" width="300"/></p>
    
<p ><img align="center" src="https://raw.githubusercontent.com/jacobh310/soccer_betting/main/Images/ev_pl.png"
    title="App Architecture" width="700"/></p>

## Conclusion and Next Steps





