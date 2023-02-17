# British Premier League Home Win Predictor
## Project at a glance
- Collected data from https://www.football-data.co.uk/englandm.php Seasons 2000-2021
- Light Data Exploration to see distribution and scatter plots of different statistics
- Trained KNearest Neighbot, Random Forests, XGBoost, SVC, and Naive Bayes 
- Built Web application
#### 📌 [See the web app in action here](https://jacobh310-soccer-betting-app-frontend-game-predictions-cty251.streamlit.app)
## Resources
- https://www.kaggle.com/datasets/saife245/english-premier-league?select=2020-2021.csv


## Introduction
The Sports Betting market is worth $74.2 billion dollars as of 2021 and is expected to reach $129.3 billion by 2028 according to Global News Wire There is no question that your average sports gambler is competing against companies that put millions into having the best algorithims to price their odds all with the goal of making money of the average sports bettor. I tried to tilt the odds back to the sports bettor's favor by training a machine learning algorithm that predicts the home teams winning probability. **The goal of this project is to build a tool sports better can leverage to make more informed betting decisions**

## Data Collection
In-game statistics from the Premier League seasons 2000-2021 were collected from https://www.football-data.co.uk/englandm.php. Each season has its own CSV file and has a plethora of different games. But it also has odds from different bookmakers for each game. This will come into play when evaluating the models. The rows were matches and the columns were game statistics. A row would contain the teams playing each other the respective stats for that game. 
#### Example
Home Team | Away Team | Home Shots | Away Shots| Home Goals| Away Goals| etc

The British premier league has 20 teams and each team plays the other twice. There would be a total of 380 matches each season which equals the number of rows for each CSV file

## Data Cleaning and Preprocessing
As mentioned above, each row only contained what happened in that game. I created a preprocessing function that would take the rolling sum of each stat for each team and divide it by the match week to get the average. Then I removed the first 4 games of each season so the average stats can stabilize. Each season was its own CSV file so the above processing was done in a data frame for each season and then appended together to make one large data set for seasons 2000-2021

Since the model is going to predict home team wins, labels were made where 1 indicates a home team win and 0 indicates a draw or a home team loss.

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
From the chart below you can see that home wins are almost split down the middle with the home team winning approximately 45% of the time. Having an unbalanced dataset is going to be a problem
<p ><img align="center" src="https://raw.githubusercontent.com/jacobh310/soccer_betting/main/Images/Home_win_barchart.png"
    title="App Architecture" width="500"/></p>
The chart below dissects the match outcome (Home win, draw, away win) by season. You can see that the home team wins a majority of the time except for 2021 where the away team won more. This comes into effect when we evaluate the profitability of the models. The model struggles to make money when the home team is winning less. More on that later.
<p ><img align="center" src="https://raw.githubusercontent.com/jacobh310/soccer_betting/main/Images/Wins%20by%20season.png"
    title="App Architecture" width="900"/></p>
The chart below dissects each home and away goal by season. You can see that the home team outscores the away team by a pretty large quantity every season except for 2021 where the home and away teams scored almost the same amount of goals. That contributed to home teams winning at a lower rate than usual  

A home team usually has the advantage because they are played with home fans. The intimidation and yelling at the away team make it harder for them to lose. But in 2021 a majority of the games were played without fans because of the covid-19 pandemic which equaled the playing field. This just goes to show you how fans play a huge 
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
The model will only predict only home wins. The baseline is going to be the home team winning percentage for each data set (Train and Dev). This is going to emulate betting on the home team to win every game. 

#### Train Home Win Percentage: 46.73%
#### Dev Home Win Percentage: 48.26%

### Correlation

I dropped the bottom 4 features with the least correlation which are HTY, HTR, ATY, ATR. These are the average red and yellow cards per game for the home and away team
<p ><img align="center" src="https://raw.githubusercontent.com/jacobh310/soccer_betting/main/Images/correlation.png"
    title="App Architecture" width="500"/></p>

**Features:** Average stats for each team split by home and away  
**Labels:**  
1: Home team win  
0: Draw or home team loss  
**Output:** Probability out of 100% of the home team winning

## Evaluate Model Performance
### Classification Metrics
<p ><img align="center" src="https://raw.githubusercontent.com/jacobh310/soccer_betting/main/Images/model%20scores.png"
    title="App Architecture" width="500"/></p>

### Profit/Loss
These classification metrics should serve as a guideline but the ultimate goal is to make money from the predictions by placing bets on the model. We tested two betting strategies: Home Team Win and Positive Expected Value

#### Home Win
This strategy is simple. If the model gives the home team a greater than 50% of winning then we are going to place a mock $100 dollar bet. If the model is right, the payout is calculated using the odds and added to the current balance. If the model is wrong then we are going to subtract $100 from the current balance

#### Results
In the first column, you have the Dev set Profit and in the second column, you have the Dev+Test profit. This combines both dev and test.
The baseline of just betting on the home team every game actually made you money on just the dev set. It was actually the second most profitable model. Once you add the test set you can see that it actually loses you money. The common theme, as seen from the graph too, is that all the models made money at first but slowly started to lose money. This could be due to the pandemic season where home teams started to lose more often.
<p ><img align="center" src="https://raw.githubusercontent.com/jacobh310/soccer_betting/main/Images/HW_pl_table.png"
    title="App Architecture" width="300"/></p>
    
<p ><img align="center" src="https://raw.githubusercontent.com/jacobh310/soccer_betting/main/Images/hw_pl.png"
    title="App Architecture" width="700"/></p>


#### Positive Expected Value
To explain this strategy, I am going to need to go over some basic sports betting terminology. 
**Decimal Odds:** The payout if a bet is won. Decimal odds of 2 means that if you bet $10 you would receive $20. $10 of the original bet and $10 profit. The higher the decimal odds the higher the pay  
**Implied Probability:** The probability implied by the decimal odds line. Implied probability = 1/Decimal Odds. A decimal odds of 2 has an implied probability of 50%. The higher the odds the lower the probability. Meaning low probably events have a higher payout.  

Without getting too much into it, the home odds for each game are converted to implied probability and will be compared to the model's predicted probability. If the model has a higher probability than the bookmakers implied probability, then that signals to bet on the home team. The current balances are going to be calculated like in the Home Win strategy. 

#### Results
The expected value strategy is more profitable on both the Dev set and the dev + test set. The common theme prevails that 3 quarters through the data all the models start to lose money. This is worth investigating further.

<p ><img align="center" src="https://raw.githubusercontent.com/jacobh310/soccer_betting/main/Images/EV_pl_table.png"
    title="App Architecture" width="300"/></p>
    
<p ><img align="center" src="https://raw.githubusercontent.com/jacobh310/soccer_betting/main/Images/ev_pl.png"
    title="App Architecture" width="700"/></p>

## Conclusion and Next Steps
The goal was achieved to make a model that would help the average sports bettor make money. However, there is still much room for improvement 
- Add data from other soccer leagues for better generalization and prevent overfitting
- Add rolling average to important statistics to capture a temporal element 
- Experiment with temporal neural networks like LSTM
- Remove the seasons where games were played with no audience
- Outlier analysis of features
