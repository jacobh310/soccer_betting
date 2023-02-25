
def home_win_pl(odds_line, labels, features, odds_df, models):

    pl_df = odds_df.reset_index()[[odds_line]]
    pl_df['HW'] = 1
    pl_df['Actual'] = labels



    bet_amt = 100
    money = []
    count = 0

    for i,j in pl_df.iterrows():
        if j['HW'] == j['Actual']:
            count = (count + (bet_amt*j[odds_line])-bet_amt)
            money.append(count)
        else: 
            count = count -bet_amt
            money.append(count)

    pl_df['Baseline PL'] = money

    for model in models:
        pl_df[f'{model} Pred'] = models[model].predict(features)

        bet_amt = 100
        money = []
        count = 0

        for i,j in pl_df.iterrows():
            if j[f'{model} Pred'] == 1:
                if j[f'{model} Pred'] == j['Actual']:
                    count = (count + (bet_amt*j[odds_line])-bet_amt)
                    money.append(count)
                else:
                    count = count -bet_amt
                    money.append(count)

            else:
                if len(money) == 0:
                    count = 0
                    money.append(count)
                else:
                    money.append(money[i-1])

        pl_df[f'{model} PL'] = money
  
    return pl_df


def ev_pl(odds_line, labels, features, odds_df, models):

    pl_df = odds_df.reset_index()[[odds_line]]
    pl_df['Win Prob'] = 1/pl_df[odds_line]
    pl_df['HW'] = 1
    pl_df['Actual'] = labels


    bet_amt = 100
    money = []
    count = 0

    for i,j in pl_df.iterrows():
        if j['HW'] == j['Actual']:
            count = (count + (bet_amt*j[odds_line])-bet_amt)
            money.append(count)
        else: 
            count = count -bet_amt
            money.append(count)

    pl_df['Baseline PL'] = money

    for model in models:
        pl_df[f'{model} Prob'] = models[model].predict_proba(features)[:,1]
        pl_df[f'{model} Bet'] = (pl_df[f'{model} Prob'] > pl_df['Win Prob']).astype('int')
        
        bet_amt = 100
        money = []
        count = 0

        for i,j in pl_df.iterrows():
            if j[f'{model} Bet'] == 1:
                if j[f'{model} Bet'] == j['Actual']:
                    count = (count + (bet_amt*j[odds_line])-bet_amt)
                    money.append(count)
                else:
                    count = count -bet_amt
                    money.append(count)

            else:
                if len(money) == 0:
                    count = 0
                    money.append(count)
                else:
                    money.append(money[i-1])

        pl_df[f'{model} PL'] = money
    
    return pl_df