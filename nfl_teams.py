import requests
import regex as re
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import display

def records(name):
    league_standings_page = requests.get("https://www.cbssports.com/nfl/standings/")
    league_standings_soup = BeautifulSoup(league_standings_page.content, 'lxml')

    league_standings_soup = re.sub(' - e', '', str(league_standings_soup))
    league_standings_soup = re.sub(' - y', '', str(league_standings_soup))
    league_standings_soup = re.sub(' - x', '', str(league_standings_soup))
    league_standings_soup = re.sub(' - z', '', str(league_standings_soup))
    league_standings_soup = re.sub(' - *', '', str(league_standings_soup))
    #league_standings_soup = re.sub(' *', '', str(league_standings_soup))
    league_standings_soup = BeautifulSoup(league_standings_soup, 'lxml')

    league_standings_table = league_standings_soup.find_all('table')
    league_standings_df = pd.read_html(str(league_standings_table))[0]
    league_standings_df = league_standings_df.iloc[:30, :4]

    #league_standings2_table = league_standings_soup.find('table', id='TableBase-2')
    league_standings2_df = pd.read_html(str(league_standings_table))[1]
    league_standings2_df = league_standings2_df.iloc[:30, :4]

    league_standings_df = league_standings_df.append(league_standings2_df)
    league_standings_df = league_standings_df.drop(league_standings_df.index[[4, 5, 10, 11, 16, 17]], axis=0)
    league_standings_df = league_standings_df.replace('Green Bay*', 'Green Bay')
    #league_standings_df = league_standings_df.replace('Green Bay*', 'Green Bay')
    #display(league_standings_df)
    '''for row in league_standings_df:
        league_standings_df.iloc(row, 0).replace('- e', '')'''
    pd.set_option('display.max_rows', None)
    #return(league_standings_df)
    team_record_df = league_standings_df[league_standings_df['Unnamed: 0_level_0', 'East'] == name]
    current_wins = int(team_record_df.iloc[0, 1])
    current_losses = int(team_record_df.iloc[0, 2])
    current_ties = int(team_record_df.iloc[0, 3])
    team_record = (current_wins, current_losses, current_ties)
    return current_wins, current_losses, current_ties
    #return league_standings_df

def abb(name):
    if name == 'Carolina':
        name = 'Panthers'
        name = (name + '  ' + name)
        abb = 'CAR'
        abb2 = 'car'
        c = 0
        return name, abb, abb2, c
    if name == 'Tampa Bay':
        name = 'Buccaneers'
        name = name + '  ' + name
        abb = 'TB'
        abb2 = 'tam'
        c = 1
        return name, abb, abb2, c
    if name == 'Chicago':
        name = 'Bears'
        name = name + '  ' + name
        abb = 'CHI'
        abb2 = 'chi'
        c = 2
        return name, abb, abb2, c
    if name == 'Minnesota':
        name = 'Vikings'
        name = name + '  ' + name
        abb = 'MIN'
        abb2 = 'min'
        c = 3
        return name, abb, abb2, c
    if name == 'Cincinnati':
        name = 'Bengals'
        name = name + '  ' + name
        abb = 'CIN'
        abb2 = 'cin'
        c = 4
        return name, abb, abb2, c
    if name == 'Cleveland':
        name = 'Browns'
        name = name + '  ' + name
        abb = 'CLE'
        abb2 = 'cle'
        c = 5
        return name, abb, abb2, c
    if name == 'Dallas':
        name = 'Cowboys'
        name = name + '  ' + name
        abb = 'DAL'
        abb2 = 'dal'
        c = 6
        return name, abb, abb2, c
    if name == 'Philadelphia':
        name = 'Eagles'
        name = name + '  ' + name
        abb = 'PHI'
        abb2 = 'phi'
        c = 7
        return name, abb, abb2, c
    if name == 'Green Bay':
        name = 'Packers'
        name = name + '  ' + name
        abb = 'GB'
        abb2 = 'gnb'
        c = 8
        return name, abb, abb2, c
    if name == 'Detroit':
        name = 'Lions'
        name = name + '  ' + name
        abb = 'DET'
        abb2 = 'det'
        c = 9
        return name, abb, abb2, c
    if name == 'Indianapolis':
        name = 'Colts'
        name = name + '  ' + name
        abb = 'IND'
        abb2 = 'clt'
        c = 10
        return name, abb, abb2, c
    if name == 'Jacksonville':
        name = 'Jaguars'
        name = name + '  ' + name
        abb = 'JAX'
        abb2 = 'jax'
        c = 11
        return name, abb, abb2, c
    if name == 'New England':
        name = 'Patriots'
        name = name + '  ' + name
        abb = 'NE'
        abb2 = 'nwe'
        c = 12
        return name, abb, abb2, c
    if name == 'Miami':
        name = 'Dolphins'
        name = name + '  ' + name
        abb = 'MIA'
        abb2 = 'mia'
        c = 13
        return name, abb, abb2, c
    if name == 'New Orleans':
        name = 'Saints'
        name = name + '  ' + name
        abb = 'NO'
        abb2 = 'nor'
        c = 14
        return name, abb, abb2, c
    if name == 'Atlanta':
        name = 'Falcons'
        name = name + '  ' + name
        abb = 'ATL'
        abb2 = 'atl'
        c = 15
        return name, abb, abb2, c
    if name == 'N.Y. Jets':
        name = 'Jets'
        name = name + '  ' + name
        abb = 'NYJ'
        abb2 = 'nyj'
        c = 16
        return name, abb, abb2, c
    if name == 'Buffalo':
        name = 'Bills'
        name = name + '  ' + name
        abb = 'BUF'
        abb2 = 'buf'
        c = 17
        return name, abb, abb2, c
    if name == 'Pittsburgh':
        name = 'Steelers'
        name = name + '  ' + name
        abb = 'PIT'
        abb2 = 'pit'
        c = 18
        return name, abb, abb2, c
    if name == 'Baltimore':
        name = 'Ravens'
        name = name + '  ' + name
        abb = 'BAL'
        abb2 = 'rav'
        c = 19
        return name, abb, abb2, c
    if name == 'Tennessee':
        name = 'Titans'
        name = name + '  ' + name
        abb = 'TEN'
        abb2 = 'oti'
        c = 20
        return name, abb, abb2, c
    if name == 'Houston':
        name = 'Texans'
        name = name + '  ' + name
        abb = 'HOU'
        abb2 = 'htx'
        c = 21
        return name, abb, abb2, c
    if name == 'Washington':
        name = 'Football Team'
        name = name + '  ' + name
        abb = 'WAS'
        abb2 = 'was'
        c = 22
        return name, abb, abb2, c
    if name == 'N.Y. Giants':
        name = 'Giants'
        name = name + '  ' + name
        abb = 'NYG'
        abb2 = 'nyg'
        c = 23
        return name, abb, abb2, c
    if name == 'Kansas City':
        name = 'Chiefs'
        name = name + '  ' + name
        abb = 'KC'
        abb2 = 'kan'
        c = 24
        return name, abb, abb2, c
    if name == 'Denver':
        name = 'Broncos'
        name = name + '  ' + name
        abb = 'DEN'
        abb2 = 'den'
        c = 25
        return name, abb, abb2, c
    if name == 'L.A. Chargers':
        name = 'Chargers'
        name = name + '  ' + name
        abb = 'LAC'
        abb2 = 'sdg'
        c = 26
        return name, abb, abb2, c
    if name == 'Las Vegas':
        name = 'Raiders'
        name = name + '  ' + name
        abb = 'LV'
        abb2 = 'rai'
        c = 27
        return name, abb, abb2, c
    if name == 'Seattle':
        name = 'Seahawks'
        name = name + '  ' + name
        abb = 'SEA'
        abb2 = 'sea' ########
        c = 28
        return name, abb, abb2, c
    if name == 'Arizona':
        name = 'Cardinals'
        name = name + '  ' + name
        abb = 'ARI'
        abb2 = 'crd'
        c = 29
        return name, abb, abb2, c
    if name == 'San Francisco':
        name = '49ers'
        name = name + '  ' + name
        abb = 'SF'
        abb2 = 'sfo'
        c = 30
        return name, abb, abb2, c
    if name == 'L.A. Rams':
        name = 'Rams'
        name = name + '  ' + name
        abb = 'LAR'
        abb2 = 'ram'
        c = 31
        return name, abb, abb2, c

class team_records():
    def __init__(self, wins, losses, ties):
        self.wins = wins
        self.losses = losses
        self.ties = ties

team_names = ['Carolina','Tampa Bay','Chicago','Minnesota','Cincinnati','Cleveland','Dallas','Philadelphia','Green Bay','Detroit','Indianapolis','Jacksonville','New England','Miami','New Orleans','Atlanta','N.Y. Jets','Buffalo','Pittsburgh','Baltimore','Tennessee','Houston','Washington','N.Y. Giants','Kansas City','Denver','L.A. Chargers','Las Vegas','Seattle','Arizona','San Francisco','L.A. Rams']
c = 0
while c < 32:
    team_names[c] = team_records(records(team_names[c])[0], records(team_names[c])[1], records(team_names[c])[2])
    c += 1
