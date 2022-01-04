import datetime
import requests
import regex as re
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from IPython.display import display
import1 = datetime.datetime.now()
import nfl_teams as nfl
from nflplayoffgame import playoff_game
import2 = datetime.datetime.now()
print('import time: ' + str(import2-import1))

time1 = datetime.datetime.now()

'''team1_name_double = 'Rams  Rams'
team1_abb = 'LAR'
team1_abb2 = 'ram'
team2_name_double = 'Cardinals  Cardinals'
team2_abb = 'ARI'
team2_abb2 = 'crd'''

def season(week):
    while week <= 18:
        #global total
        point_total = 0
        # league schedule by week
        print('Week ' + str(week))
        league_sched_page = requests.get("https://www.cbssports.com/nfl/schedule/2021/regular/" + str(week) + '/')
        league_sched_soup = BeautifulSoup(league_sched_page.content, 'lxml')
        league_sched_table = league_sched_soup.find_all('table')
        league_sched_df1 = pd.read_html(str(league_sched_table))[0]
        league_sched_df = league_sched_df1#pd.concat([league_sched_df1, league_sched_df2, league_sched_df3], axis=0)
        #print(len(league_sched_soup.find_all('table')))
        '''print(league_sched_df1)
        print(league_sched_df)'''
        if len(league_sched_soup.find_all('table')) > 1:
            league_sched_df2 = pd.read_html(str(league_sched_table))[1]
            league_sched_df = league_sched_df.append(league_sched_df2)
            if len(league_sched_soup.find_all('table')) > 2:
                league_sched_df3 = pd.read_html(str(league_sched_table))[2]
                league_sched_df = league_sched_df.append(league_sched_df3)
                if len(league_sched_soup.find_all('table')) > 3:
                    league_sched_df4 = pd.read_html(str(league_sched_table))[3]
                    league_sched_df = league_sched_df.append(league_sched_df4)
                    if len(league_sched_soup.find_all('table')) > 4:
                        league_sched_df5 = pd.read_html(str(league_sched_table))[4]
                        league_sched_df = league_sched_df.append(league_sched_df5)
        league_sched_df = league_sched_df.iloc[:30, :2]
        display(league_sched_df)
        rows = int(league_sched_df.shape[0])
        #print(rows)
        row = 0
        while row < rows:
            team1_label = str(league_sched_df.iloc[row, 0])
            team2_label = str(league_sched_df.iloc[row, 1])
            global team1_name_double, team1_abb, team2_name_double, team2_abb, team1_abb2, team2_abb2, team1_c, team2_c
            team1_name_double = nfl.abb(team1_label)[0]
            team1_abb = nfl.abb(team1_label)[1]
            team2_name_double = nfl.abb(team2_label)[0]
            team2_abb = nfl.abb(team2_label)[1]
            team1_abb2 = nfl.abb(team1_label)[2]
            team2_abb2 = nfl.abb(team2_label)[2]
            team1_c = nfl.abb(team1_label)[3]
            team2_c = nfl.abb(team2_label)[3]

            class Team1_Drive():
                def __init__(self, td_perc, fga_perc, fg_made_perc, fg_miss_perc, xp_made_perc, xp_miss_perc, tov_perc, punt_perc, tov_on_downs_perc, time_dr):
                    self.td_perc = td_perc
                    self.fga_perc = fga_perc
                    self.fg_made_perc = fg_made_perc
                    self.fg_miss_perc = fg_miss_perc
                    self.xp_made_perc = xp_made_perc
                    self.xp_miss_perc = xp_miss_perc
                    self.tov_perc = tov_perc
                    self.punt_perc = punt_perc
                    self.tov_on_downs_perc = tov_on_downs_perc
                    self.time_dr = time_dr

            class Team2_Drive():
                def __init__(self, td_perc, fga_perc, fg_made_perc, fg_miss_perc, xp_made_perc, xp_miss_perc, tov_perc, punt_perc, tov_on_downs_perc, time_dr):
                    self.td_perc = td_perc
                    self.fga_perc = fga_perc
                    self.fg_made_perc = fg_made_perc
                    self.fg_miss_perc = fg_miss_perc
                    self.xp_made_perc = xp_made_perc
                    self.xp_miss_perc = xp_miss_perc
                    self.tov_perc = tov_perc
                    self.punt_perc = punt_perc
                    self.tov_on_downs_perc = tov_on_downs_perc
                    self.time_dr = time_dr

            def get_sec(time_string):
                m, s = time_string.split(':')
                return int(m) * 60 + int(s)

            LOGIN_URL = "https://www.footballoutsiders.com/user/login?destination=home"

            # Start the session
            session = requests.Session()

            # Create the payload
            payload = {'name':'tylerchasse',
                      'pass':'patriots77',
                       'form_id':'user_login_form' #authenticity_token
                     }
            # Post the payload to the site to log in
            s = session.post("https://www.footballoutsiders.com/user/login?destination=home", data=payload, headers = dict(referer = LOGIN_URL))

            # Navigate to the next page and scrape the data
            s = session.get('https://www.footballoutsiders.com/stats/nfl/overall-drive-statsoff/2021')

            soup = BeautifulSoup(s.content, 'lxml')
            # drives, tov/dr, time of possession/dr
            fo1_table = soup.find('table')
            fo1_df = pd.read_html(str(fo1_table))[0]
            fo1_df = fo1_df.iloc[:32, 0:18]
            fo1_df = fo1_df.drop(fo1_df.columns[[2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16]], axis=1)
            '''pd.set_option('display.max_columns', None)'''
            #display(fo1_df)

            '''# team 1 tov/dr
            team1_tov_dr_df = fo1_df[fo1_df["Team"] == team1_abb]
            team1_tov_dr = team1_tov_dr_df.iloc[0, 2]
            
            # team 2 tov/dr
            team2_tov_dr_df = fo1_df[fo1_df["Team"] == team2_abb]
            team2_tov_dr = team2_tov_dr_df.iloc[0, 2]'''

            # team 1 top/dr
            team1_top_dr_df = fo1_df[fo1_df["Team"] == team1_abb]
            team1_top_dr = team1_top_dr_df.iloc[0, 3]
            team1_top_dr = str(team1_top_dr)
            team1_top_dr = team1_top_dr.replace('.', ':')
            team1_top_dr = get_sec(team1_top_dr) + 45


            # team 2 top/dr
            team2_top_dr_df = fo1_df[fo1_df["Team"] == team2_abb]
            team2_top_dr = team2_top_dr_df.iloc[0, 3]
            team2_top_dr = str(team2_top_dr)
            team2_top_dr = team2_top_dr.replace('.', ':')
            team2_top_dr = get_sec(team2_top_dr) + 45
            #print(team1_tov_dr, team2_tov_dr, team1_top_dr, team2_top_dr)

            '''# drives, td/dr, fg/dr, punts/dr
            fo2_table = soup.find_all('table')#, style='margin-left: -42px;')
            fo2_df = pd.read_html(str(fo2_table))[1]
            fo2_df = fo2_df.iloc[:32, 0:18]
            fo2_df = fo2_df.drop(fo2_df.columns[[2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]], axis=1)
            print('\n')
            display(fo2_df)
            
            # team 1 td/dr
            team1_td_dr_df = fo2_df[fo2_df["Team"] == team1_abb]
            team1_td_dr = team1_td_dr_df.iloc[0, 2]
            
            # team 2 td/dr
            team2_td_dr_df = fo2_df[fo2_df["Team"] == team2_abb]
            team2_td_dr = team2_td_dr_df.iloc[0, 2]
            
            # team 1 punts/dr
            team1_punts_dr_df = fo2_df[fo2_df["Team"] == team1_abb]
            team1_punts_dr = team1_punts_dr_df.iloc[0, 4]
            
            # team 2 punts/dr
            team2_punts_dr_df = fo2_df[fo2_df["Team"] == team2_abb]
            team2_punts_dr = team2_punts_dr_df.iloc[0, 4]
            #print(team1_td_dr, team2_td_dr, team1_punts_dr, team2_punts_dr)'''

            s = session.get('https://www.footballoutsiders.com/stats/nfl/overall-drive-statsdef/2021')

            soup = BeautifulSoup(s.content, 'lxml')
            # opp drives, tov/dr, time of possession/dr
            opp_fo1_table = soup.find('table')
            opp_fo1_df = pd.read_html(str(opp_fo1_table))[0]
            opp_fo1_df = opp_fo1_df.iloc[:32, 0:18]
            opp_fo1_df = opp_fo1_df.drop(opp_fo1_df.columns[[2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16]], axis=1)
            pd.set_option('display.max_columns', None)
            '''print('\n')
            display(opp_fo1_df)'''

            '''# team 1 opp_tov/dr
            team1_opp_tov_dr_df = opp_fo1_df[opp_fo1_df["Team"] == team1_abb]
            team1_opp_tov_dr = team1_opp_tov_dr_df.iloc[0, 2]
            
            # team 2 opp_tov/dr
            team2_opp_tov_dr_df = opp_fo1_df[opp_fo1_df["Team"] == team2_abb]
            team2_opp_tov_dr = team2_opp_tov_dr_df.iloc[0, 2]'''

            # team 1 opp_top/dr
            team1_opp_top_dr_df = opp_fo1_df[opp_fo1_df["Team"] == team1_abb]
            team1_opp_top_dr = team1_opp_top_dr_df.iloc[0, 3]
            team1_opp_top_dr = str(team1_opp_top_dr)
            team1_opp_top_dr = team1_opp_top_dr.replace('.', ':')
            team1_opp_top_dr = get_sec(team1_opp_top_dr)

            # team 2 opp_top/dr
            team2_opp_top_dr_df = opp_fo1_df[opp_fo1_df["Team"] == team2_abb]
            team2_opp_top_dr = team2_opp_top_dr_df.iloc[0, 3]
            team2_opp_top_dr = str(team2_opp_top_dr)
            team2_opp_top_dr = team2_opp_top_dr.replace('.', ':')
            team2_opp_top_dr = get_sec(team2_opp_top_dr)
            #print(team1_opp_tov_dr, team2_opp_tov_dr, team1_opp_top_dr, team2_opp_top_dr)

            '''# opp drives, td/dr, fg/dr, punts/dr
            opp_fo2_table = soup.find_all('table')#, style='margin-left: -42px;')
            opp_fo2_df = pd.read_html(str(opp_fo2_table))[1]
            opp_fo2_df = opp_fo2_df.iloc[:32, 0:18]
            opp_fo2_df = opp_fo2_df.drop(opp_fo2_df.columns[[2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]], axis=1)
            print('\n')
            display(opp_fo2_df)
            
            # team 1 opp_td/dr
            team1_opp_td_dr_df = opp_fo2_df[opp_fo2_df["Team"] == team1_abb]
            team1_opp_td_dr = team1_opp_td_dr_df.iloc[0, 2]
            
            # team 2 opp_td/dr
            team2_opp_td_dr_df = opp_fo2_df[opp_fo2_df["Team"] == team2_abb]
            team2_opp_td_dr = team2_opp_td_dr_df.iloc[0, 2]
            
            # team 1 opp_punts/dr
            team1_opp_punts_dr_df = opp_fo2_df[opp_fo2_df["Team"] == team1_abb]
            team1_opp_punts_dr = team1_opp_punts_dr_df.iloc[0, 4]
            
            # team 2 opp_punts/dr
            team2_opp_punts_dr_df = opp_fo2_df[opp_fo2_df["Team"] == team2_abb]
            team2_opp_punts_dr = team2_opp_punts_dr_df.iloc[0, 4]
            #print(team1_opp_td_dr, team2_opp_td_dr, team1_opp_punts_dr, team2_opp_punts_dr)'''

            # fgm, fga
            fg_page = requests.get("https://www.nfl.com/stats/team-stats/special-teams/field-goals/2021/reg/all")
            fg_soup = BeautifulSoup(fg_page.content, 'lxml')
            fg_table = fg_soup.find('table')
            fg_df = pd.read_html(str(fg_table))[0]
            fg_df = fg_df.iloc[:32, :3]
            #print('\n')
            #display(fg_df)

            # team1 fg missed
            team1_fgm_df = fg_df[fg_df["Team"] == team1_name_double]
            team1_fgm = team1_fgm_df.iloc[0, 1]
            team1_fga = team1_fgm_df.iloc[0, 2]
            team1_fg_missed = int(team1_fga) - int(team1_fgm)

            # team2 fg missed
            team2_fgm_df = fg_df[fg_df["Team"] == team2_name_double]
            team2_fgm = team2_fgm_df.iloc[0, 1]
            team2_fga = team2_fgm_df.iloc[0, 2]
            team2_fg_missed = int(team2_fga) - int(team2_fgm)
            #print(team1_fg_missed, team2_fg_missed)

            # 4th down att, made
            fourth_page = requests.get("https://www.nfl.com/stats/team-stats/offense/downs/2021/reg/all")
            fourth_soup = BeautifulSoup(fourth_page.content, 'lxml')
            fourth_table = fourth_soup.find('table')
            fourth_df = pd.read_html(str(fourth_table))[0]
            fourth_df = fourth_df.iloc[:32, :5]
            fourth_df = fourth_df.drop(fourth_df.columns[[1, 2]], axis=1)
            #print('\n')
            #display(fourth_df)

            # team1 4th fails
            team1_fourth_df = fourth_df[fourth_df["Team"] == team1_name_double]
            team1_fourth_made = team1_fourth_df.iloc[0, 2]
            team1_fourth_att = team1_fourth_df.iloc[0, 1]
            team1_fourth_missed = int(team1_fourth_att) - int(team1_fourth_made)

            # team2 4th fails
            team2_fourth_df = fourth_df[fourth_df["Team"] == team2_name_double]
            team2_fourth_made = team2_fourth_df.iloc[0, 2]
            team2_fourth_att = team2_fourth_df.iloc[0, 1]
            team2_fourth_missed = int(team2_fourth_att) - int(team2_fourth_made)
            #print(team1_fourth_missed, team2_fourth_missed)

            # opp 4th down att, made
            opp_fourth_page = requests.get("https://www.nfl.com/stats/team-stats/defense/downs/2021/reg/all")
            opp_fourth_soup = BeautifulSoup(opp_fourth_page.content, 'lxml')
            opp_fourth_table = opp_fourth_soup.find('table')
            opp_fourth_df = pd.read_html(str(opp_fourth_table))[0]
            opp_fourth_df = opp_fourth_df.iloc[:32, :5]
            opp_fourth_df = opp_fourth_df.drop(opp_fourth_df.columns[[1, 2]], axis=1)
            #print('\n')
            #display(opp_fourth_df)

            # team1 4th fails
            team1_opp_fourth_df = opp_fourth_df[opp_fourth_df["Team"] == team1_name_double]
            team1_opp_fourth_made = team1_opp_fourth_df.iloc[0, 2]
            team1_opp_fourth_att = team1_opp_fourth_df.iloc[0, 1]
            team1_opp_fourth_missed = int(team1_opp_fourth_att) - int(team1_opp_fourth_made)

            # team2 4th fails
            team2_opp_fourth_df = opp_fourth_df[opp_fourth_df["Team"] == team2_name_double]
            team2_opp_fourth_made = team2_opp_fourth_df.iloc[0, 2]
            team2_opp_fourth_att = team2_opp_fourth_df.iloc[0, 1]
            team2_opp_fourth_missed = int(team2_opp_fourth_att) - int(team2_opp_fourth_made)
            #print(team1_opp_fourth_missed, team2_opp_fourth_missed)

            # team1 tds, tovs, opp tds, opp tovs
            team1_page = requests.get("https://www.pro-football-reference.com/teams/" + team1_abb2 + "/2021.htm")
            team1_soup = BeautifulSoup(team1_page.content, 'lxml')

            cleantext = re.sub('<!--\n\n', '\n', str(team1_soup))
            cleanertext = re.sub('\n-->\n', '\n', str(cleantext))
            html = BeautifulSoup(cleanertext, 'lxml')

            team1_table = html.find('table', id='team_stats')
            team1_df = pd.read_html(str(team1_table))[0]
            team1_df = team1_df.iloc[0:2, 5:18]
            team1_df = team1_df.drop(team1_df.columns[[1, 2, 3, 4, 5, 7, 8, 9, 10, 11]], axis=1)
            pd.set_option('display.max_columns', None)
            #print('\n')
            #display(team1_df)

            # team1 tds, tovs, opp td, tovs
            team1_tds = team1_df.iloc[0, 1] + team1_df.iloc[0, 2]
            team1_tovs = team1_df.iloc[0, 0]
            team1_opp_tds = team1_df.iloc[1, 1] + team1_df.iloc[1, 2]
            team1_opp_tovs = team1_df.iloc[1, 0]
            #print(team1_tds, team1_tovs, team1_opp_tds, team1_opp_tovs)

            # team1 punts, opp punts
            team1_kicking_table = html.find('table', id='kicking')
            team1_kicking_df = pd.read_html(str(team1_kicking_table))[0]
            kicking1_rows = len(team1_kicking_df.index)
            team1_kicking_df = team1_kicking_df.iloc[(kicking1_rows-2):kicking1_rows, 16:29]
            team1_kicking_df = team1_kicking_df.drop(team1_kicking_df.columns[[2, 7, 8, 9, 10, 11]], axis=1)
            pd.set_option('display.max_columns', None)
            #print('\n')
            #display(team1_kicking_df)

            # team1 fga, fg%, punts, opp punts
            team1_fg_made_perc = team1_kicking_df.iloc[0, 2]
            team1_fg_made_perc = str(team1_fg_made_perc).replace('%', '')
            team1_fg_made_perc = float(team1_fg_made_perc)
            team1_fg_made_perc = float(team1_fg_made_perc) / 100
            team1_fg_miss_perc = 1 - team1_fg_made_perc
            team1_opp_fga = team1_kicking_df.iloc[1, 0]
            team1_punts = team1_kicking_df.iloc[0, 6]
            team1_opp_punts = team1_kicking_df.iloc[1, 6]
            team1_xp_made_perc = team1_kicking_df.iloc[0, 5]
            team1_xp_made_perc = str(team1_xp_made_perc).replace('%', '')
            team1_xp_made_perc = float(team1_xp_made_perc)
            team1_xp_made_perc = float(team1_xp_made_perc) / 100
            team1_xp_miss_perc = 1 - team1_xp_made_perc
            if team1_fg_made_perc == 1:
                team1_fg_made_perc -= .01
                team1_fg_miss_perc += .01
            if team1_xp_made_perc == 1:
                team1_xp_made_perc -= .01
                team1_xp_miss_perc += .01
            #print(team1_xp_made_perc, team1_xp_miss_perc, team1_punts, team1_opp_punts)

            # team2 tds, tovs, opp tds, opp tovs
            team2_page = requests.get("https://www.pro-football-reference.com/teams/" + team2_abb2 + "/2021.htm")
            team2_soup = BeautifulSoup(team2_page.content, 'lxml')

            cleantext = re.sub('<!--\n\n', '\n', str(team2_soup))
            cleanertext = re.sub('\n-->\n', '\n', str(cleantext))
            html = BeautifulSoup(cleanertext, 'lxml')

            team2_table = html.find('table', id='team_stats')
            team2_df = pd.read_html(str(team2_table))[0]
            team2_df = team2_df.iloc[0:2, 5:18]
            team2_df = team2_df.drop(team2_df.columns[[1, 2, 3, 4, 5, 7, 8, 9, 10, 11]], axis=1)
            pd.set_option('display.max_columns', None)
            #print('\n')
            #display(team2_df)

            # team2 tds, tovs, opp td, tovs
            team2_tds = team2_df.iloc[0, 1] + team2_df.iloc[0, 2]
            team2_tovs = team2_df.iloc[0, 0]
            team2_opp_tds = team2_df.iloc[1, 1] + team2_df.iloc[1, 2]
            team2_opp_tovs = team2_df.iloc[1, 0]
            #print(team2_tds, team2_tovs, team2_opp_tds, team2_opp_tovs)

            # team2 punts, opp punts
            team2_kicking_table = html.find('table', id='kicking')
            team2_kicking_df = pd.read_html(str(team2_kicking_table))[0]
            kicking2_rows = len(team2_kicking_df.index)
            team2_kicking_df = team2_kicking_df.iloc[(kicking2_rows - 2):kicking2_rows, 16:29]
            team2_kicking_df = team2_kicking_df.drop(team2_kicking_df.columns[[2, 7, 8, 9, 10, 11]], axis=1)
            pd.set_option('display.max_columns', None)
            #print('\n')
            #display(team2_kicking_df)

            # team2 fga, fg%, punts, opp punts
            team2_fg_made_perc = team2_kicking_df.iloc[0, 2]
            team2_fg_made_perc = str(team2_fg_made_perc).replace('%', '')
            team2_fg_made_perc = float(team2_fg_made_perc)
            team2_fg_made_perc = float(team2_fg_made_perc) / 100
            team2_fg_miss_perc = 1 - team2_fg_made_perc
            team2_opp_fga = team2_kicking_df.iloc[1, 0]
            team2_punts = team2_kicking_df.iloc[0, 6]
            team2_opp_punts = team2_kicking_df.iloc[1, 6]
            team2_xp_made_perc = team2_kicking_df.iloc[0, 5]
            team2_xp_made_perc = str(team2_xp_made_perc).replace('%', '')
            team2_xp_made_perc = float(team2_xp_made_perc)
            team2_xp_made_perc = float(team2_xp_made_perc) / 100
            team2_xp_miss_perc = 1 - team2_xp_made_perc
            if team2_fg_made_perc == 1:
                team2_fg_made_perc -= .01
                team2_fg_miss_perc += .01
            if team2_xp_made_perc == 1:
                team2_xp_made_perc -= .01
                team2_xp_miss_perc += .01
            #print(team2_xp_made_perc, team2_xp_miss_perc, team2_punts, team2_opp_punts)

            team1_drives = team1_tds + team1_fga + team1_tovs + team1_punts + team1_fourth_missed
            team2_drives = team2_tds + team2_fga + team2_tovs + team2_punts + team2_fourth_missed
            team1_opp_drives = team1_opp_tds + team1_opp_fga + team1_opp_tovs + team1_opp_punts + team1_opp_fourth_missed
            team2_opp_drives = team2_opp_tds + team2_opp_fga + team2_opp_tovs + team2_opp_punts + team2_opp_fourth_missed

            team1_td_dr = team1_tds / team1_drives
            team1_fga_dr = team1_fga / team1_drives
            team1_tovs_downs_dr = team1_fourth_missed / team1_drives
            team1_tov_dr = team1_tovs / team1_drives
            team1_punts_dr = team1_punts / team1_drives
            team1_opp_td_dr = team1_opp_tds / team1_opp_drives
            team1_opp_fga_dr = team1_opp_fga / team1_opp_drives
            team1_opp_tov_downs_dr = team1_opp_fourth_missed / team1_opp_drives
            team1_opp_tov_dr = team1_opp_tovs / team1_opp_drives
            team1_opp_punts_dr = team1_opp_punts / team1_opp_drives

            team2_td_dr = team2_tds / team2_drives
            team2_fga_dr = team2_fga / team2_drives
            team2_tovs_downs_dr = team2_fourth_missed / team2_drives
            team2_tov_dr = team2_tovs / team2_drives
            team2_punts_dr = team2_punts / team2_drives
            team2_opp_td_dr = team2_opp_tds / team2_opp_drives
            team2_opp_fga_dr = team2_opp_fga / team2_opp_drives
            team2_opp_tov_downs_dr = team2_opp_fourth_missed / team2_opp_drives
            team2_opp_tov_dr = team2_opp_tovs / team2_opp_drives
            team2_opp_punts_dr = team2_opp_punts / team2_opp_drives
            #print(((int(team1_top_dr) + int(team2_opp_top_dr)) / 2), (int(team2_top_dr) + int(team1_opp_top_dr)) / 2)

            # td/dr, fga/dr, fgmade%, fgmissed%, xpmade%, xpmissed%, tov/dr, punt/dr, tov on downs/dr,
            Team1_Dr = Team1_Drive((team1_td_dr + team2_opp_td_dr) / 2, (team1_fga_dr + team2_opp_fga_dr) / 2, team1_fg_made_perc, team1_fg_miss_perc, team1_xp_made_perc, team1_xp_miss_perc, (team1_tov_dr + team2_opp_tov_dr) / 2, (team1_punts_dr + team2_opp_punts_dr) / 2, (team1_tovs_downs_dr + team2_opp_tov_downs_dr) / 2, (int(team1_top_dr) + int(team2_opp_top_dr)) / 2)
            Team2_Dr = Team1_Drive((team2_td_dr + team1_opp_td_dr) / 2, (team2_fga_dr + team1_opp_fga_dr) / 2, team2_fg_made_perc, team2_fg_miss_perc, team2_xp_made_perc, team2_xp_miss_perc, (team2_tov_dr + team1_opp_tov_dr) / 2, (team2_punts_dr + team1_opp_punts_dr) / 2, (team2_tovs_downs_dr + team1_opp_tov_downs_dr) / 2, (int(team2_top_dr) + int(team1_opp_top_dr)) / 2)
            '''print(vars(Team1_Dr))
            print(vars(Team2_Dr))'''

            team1_statlist = ('1_td', '1_fga', '1_tov', '1_punt', '1_tov_downs')
            team2_statlist = ('2_td', '2_fga', '2_tov', '2_punt', '2_tov_downs')

            def drive(poss):
                if poss == 1:
                    outcome = np.random.choice(team1_statlist, 1, p=[Team1_Dr.td_perc, Team1_Dr.fga_perc, Team1_Dr.tov_perc, Team1_Dr.punt_perc, Team1_Dr.tov_on_downs_perc])
                    return outcome
                if poss == 2:
                    outcome = np.random.choice(team2_statlist, 1, p=[Team2_Dr.td_perc, Team2_Dr.fga_perc, Team2_Dr.tov_perc, Team2_Dr.punt_perc, Team2_Dr.tov_on_downs_perc])
                    return outcome

            def fga(poss):
                if poss == 1:
                    make_or_miss = np.random.choice(('make', 'miss'), 1, p=[Team1_Dr.fg_made_perc, Team1_Dr.fg_miss_perc])
                    return make_or_miss
                if poss == 2:
                    make_or_miss = np.random.choice(('make', 'miss'), 1, p=[Team2_Dr.fg_made_perc, Team2_Dr.fg_miss_perc])
                    return make_or_miss

            def xp(poss):
                if poss == 1:
                    make_or_miss = np.random.choice(('make', 'miss'), 1, p=[Team1_Dr.xp_made_perc, Team1_Dr.xp_miss_perc])
                    return make_or_miss
                if poss == 2:
                    make_or_miss = np.random.choice(('make', 'miss'), 1, p=[Team2_Dr.xp_made_perc, Team2_Dr.xp_miss_perc])
                    return make_or_miss

            def nflgame():
                global team1_win, team2_win, team1_1st_drive, team2_1st_drive, tie, team1_score, team2_score
                home_team_advantage = 2 # adds about 2% per point
                quarter = 0
                time = 900
                team1_score = 0
                team2_score = 0
                poss = np.random.choice((1, 2))
                if poss == 1:
                    second = 2
                if poss == 2:
                    second = 1
                team1_win = False
                team2_win = False
                tie = False
                team1_1st_drive = False  ########### for if field goal will win game in OT
                team2_1st_drive = False
                while quarter < 5:# or (team1_score > team2_score and team2_1st_drive == False) or (team2_score > team1_score and team1_1st_drive == False):# and quarter == 5):
                    quarter += 1
                    if time <= 0:
                        time = 900
                        if quarter == 5:
                            time = 600
                    if quarter == 3:
                        poss = second
                    while time > 0 and quarter <= 4:
                        #print('There is ' + str(time) + ' seconds left in quarter ' + str(quarter))
                        if poss == 1:
                            time -= Team1_Dr.time_dr
                            #print(team1_abb + ' has possession')
                        elif poss == 2:
                            time -= Team2_Dr.time_dr
                            #print(team2_abb + ' has possession')
                        outcome = drive(poss)
                        #print(outcome)
                        if outcome == ['1_td']:
                            team1_score += 6
                            extra = xp(1)
                            if extra == ['make']:
                                team1_score += 1
                                #print(team1_abb + ' scored a touchdown and made the extra point for 7 points!')
                                poss = 2
                            if extra == ['miss']:
                                #print(team1_abb + ' scored a touchdown but missed the extra point for 6 points')
                                poss = 2
                        if outcome == ['1_fga']:
                            fg = fga(1)
                            #print(team1_abb + ' is attempting a field goal')
                            if fg == ['make']:
                                team1_score += 3
                                #print(team1_abb + ' made the field goal!')
                                poss = 2
                            if fg == ['miss']:
                                #print(team1_abb + ' missed the field goal!')
                                poss = 2
                        if outcome == ['1_tov']:
                            #print(team1_abb + ' turned over the ball!')
                            poss = 2
                        if outcome == ['1_punt']:
                            #print(team1_abb + ' punts')
                            poss = 2
                        if outcome == ['1_tov_downs']:
                            #print(team1_abb + ' turns the ball over on downs')
                            poss = 2
                        if outcome == ['2_td']:
                            team2_score += 6
                            extra = xp(2)
                            if extra == ['make']:
                                team2_score += 1
                                poss = 1
                                #print(team2_abb + ' scored a touchdown and made the extra point for 7 points!')
                            if extra == ['miss']:
                                #print(team2_abb + ' scored a touchdown but missed the extra point for 6 points')
                                poss = 1
                        if outcome == ['2_fga']:
                            fg = fga(2)
                            #print(team2_abb + ' is attempting a field goal')
                            if fg == ['make']:
                                team2_score += 3
                                poss = 1
                                #print(team2_abb + ' made the field goal!')
                            if fg == ['miss']:
                                #print(team2_abb + ' missed the field goal!')
                                poss = 1
                        if outcome == ['2_tov']:
                            #print(team2_abb + ' turned over the ball!')
                            poss = 1
                        if outcome == ['2_punt']:
                            #print(team2_abb + ' punts')
                            poss = 1
                        if outcome == ['2_tov_downs']:
                            #print(team2_abb + ' turns the ball over on downs')
                            poss = 1
                        #print(team1_abb + ': ' + str(team1_score) + ' - ' + team2_abb + ': ' + str(team2_score) + '\n')
                        ###team1_score = team2_score ###
                    if quarter == 5 and team1_score == team2_score:
                        poss = np.random.choice((1, 2))
                        game_over = False
                        while time > 0 and game_over == False:# or (time > 0 and team1_score > team2_score and team2_1st_drive == False) or (time > 0 and team2_score > team1_score and team1_1st_drive == False):
                            if poss == 1:
                                team1_1st_drive = True
                            if poss == 2:
                                team2_1st_drive = True
                            if team1_1st_drive and team2_score > team1_score:
                                game_over = True
                            if team2_1st_drive and team1_score > team2_score:
                                game_over = True
                            #print('There is ' + str(time) + ' seconds left in overtime')
                            if poss == 1:
                                time -= Team1_Dr.time_dr
                                #print(team1_abb + ' has possession')
                            elif poss == 2:
                                time -= Team2_Dr.time_dr
                                #print(team2_abb + ' has possession')
                            outcome = drive(poss)
                            # print(outcome)
                            if outcome == ['1_td']:
                                team1_score += 6
                                #print(team1_abb + ' scored a touchdown to win the game!')
                                game_over = True
                                poss = 2
                            if outcome == ['1_fga']:
                                fg = fga(1)
                                #print(team1_abb + ' is attempting a field goal')
                                if fg == ['make']:
                                    team1_score += 3
                                    #print(team1_abb + ' made the field goal!')
                                    poss = 2
                                    if team2_1st_drive == True:
                                        game_over = True
                                if fg == ['miss']:
                                    #print(team1_abb + ' missed the field goal!')
                                    poss = 2
                            if outcome == ['1_tov']:
                                #print(team1_abb + ' turned over the ball!')
                                poss = 2
                            if outcome == ['1_punt']:
                                #print(team1_abb + ' punts')
                                poss = 2
                            if outcome == ['1_tov_downs']:
                                #print(team1_abb + ' turns the ball over on downs')
                                poss = 2
                            if outcome == ['2_td']:
                                team2_score += 6
                                #print(team2_abb + ' scored a touchdown to win the game!')
                                game_over = True
                                poss = 1
                            if outcome == ['2_fga']:
                                fg = fga(2)
                                #print(team2_abb + ' is attempting a field goal')
                                if fg == ['make']:
                                    team2_score += 3
                                    #print(team2_abb + ' made the field goal!')
                                    poss = 1
                                    if team1_1st_drive == True:
                                        game_over = True
                                if fg == ['miss']:
                                    #print(team2_abb + ' missed the field goal!')
                                    poss = 1
                            if outcome == ['2_tov']:
                                #print(team2_abb + ' turned over the ball!')
                                poss = 1
                            if outcome == ['2_punt']:
                                #print(team2_abb + ' punts')
                                poss = 1
                            if outcome == ['2_tov_downs']:
                                #print(team2_abb + ' turns the ball over on downs')
                                poss = 1
                            #print(team1_abb + ': ' + str(team1_score) + ' - ' + team2_abb + ': ' + str(team2_score) + '\n')
                            if time <= 0:
                                game_over = True
                team2_score += home_team_advantage
                if team1_score > team2_score:
                    print(team1_abb + ' beat ' + team2_abb + ' ' + str(team1_score) + '-' + str(team2_score))
                    team1_win = True
                if team2_score > team1_score:
                    print(team2_abb + ' beat ' + team1_abb + ' ' + str(team2_score) + '-' + str(team1_score))
                    team2_win = True
                if team1_score == team2_score:
                    print(team1_abb + ' tied ' + team2_abb + ' ' + str(team1_score) + '-' + str(team2_score))
                    tie = True
                '''point_total += team1_score
                point_total += team2_score'''
            nflgame()
            point_total += team1_score
            point_total += team2_score
            if team1_win == True:
                nfl.team_names[team1_c].wins += 1
                nfl.team_names[team2_c].losses += 1
            if team2_win == True:
                nfl.team_names[team2_c].wins += 1
                nfl.team_names[team1_c].losses += 1
            if tie == True:
                nfl.team_names[team2_c].ties += 1
                nfl.team_names[team1_c].ties += 1
            print(team1_abb + ': ' + str(nfl.team_names[team1_c].wins) + '-' + str(nfl.team_names[team1_c].losses))
            print(team2_abb + ': ' + str(nfl.team_names[team2_c].wins) + '-' + str(nfl.team_names[team2_c].losses))
            row += 1
        #print(point_total / (rows*2))
        week += 1
        print('\n')
    print('\n')
    Carolina_record = [int(nfl.team_names[0].wins), nfl.abb('Carolina')]
    Tampa_Bay_record = [int(nfl.team_names[1].wins), nfl.abb('Tampa Bay')]
    Chicago_record = [int(nfl.team_names[2].wins), nfl.abb('Chicago')]
    Minnesota_record = [int(nfl.team_names[3].wins), nfl.abb('Minnesota')]
    Cincinnati_record = [int(nfl.team_names[4].wins), nfl.abb('Cincinnati')]
    Cleveland_record = [int(nfl.team_names[5].wins), nfl.abb('Cleveland')]
    Dallas_record = [int(nfl.team_names[6].wins), nfl.abb('Dallas')]
    Philadelphia_record = [int(nfl.team_names[7].wins), nfl.abb('Philadelphia')]
    Green_Bay_record = [int(nfl.team_names[8].wins), nfl.abb('Green Bay')]
    Detroit_record = [int(nfl.team_names[9].wins), nfl.abb('Detroit')]
    Indianapolis_record = [int(nfl.team_names[10].wins), nfl.abb('Indianapolis')]
    Jacksonville_record = [int(nfl.team_names[11].wins), nfl.abb('Jacksonville')]
    New_England_record = [int(nfl.team_names[12].wins), nfl.abb('New England')]
    Miami_record = [int(nfl.team_names[13].wins), nfl.abb('Miami')]
    New_Orleans_record = [int(nfl.team_names[14].wins), nfl.abb('New Orleans')]
    Atlanta_record = [int(nfl.team_names[15].wins), nfl.abb('Atlanta')]
    NY_Jets_record = [int(nfl.team_names[16].wins), nfl.abb('N.Y. Jets')]
    Buffalo_record = [int(nfl.team_names[17].wins), nfl.abb('Buffalo')]
    Pittsburgh_record = [int(nfl.team_names[18].wins), nfl.abb('Pittsburgh')]
    Baltimore_record = [int(nfl.team_names[19].wins), nfl.abb('Baltimore')]
    Tennessee_record = [int(nfl.team_names[20].wins), nfl.abb('Tennessee')]
    Houston_record = [int(nfl.team_names[21].wins), nfl.abb('Houston')]
    Washington_record = [int(nfl.team_names[22].wins), nfl.abb('Washington')]
    NY_Giants_record = [int(nfl.team_names[23].wins), nfl.abb('N.Y. Giants')]
    Kansas_City_record = [int(nfl.team_names[24].wins), nfl.abb('Kansas City')]
    Denver_record = [int(nfl.team_names[25].wins), nfl.abb('Denver')]
    LA_Chargers_record = [int(nfl.team_names[26].wins), nfl.abb('L.A. Chargers')]
    Las_Vegas_record = [int(nfl.team_names[27].wins), nfl.abb('Las Vegas')]
    Seattle_record = [int(nfl.team_names[28].wins), nfl.abb('Seattle')]
    Arizona_record = [int(nfl.team_names[29].wins), nfl.abb('Arizona')]
    San_Francisco_record = [int(nfl.team_names[30].wins), nfl.abb('San Francisco')]
    LA_Rams_record = [int(nfl.team_names[31].wins), nfl.abb('L.A. Rams')]

    # printing team records:
    print('Carolina Record: ' + str(nfl.team_names[0].wins) + '-' + str(nfl.team_names[0].losses) + '-' + str(nfl.team_names[0].ties))
    print('Tampa Bay Record: ' + str(nfl.team_names[1].wins) + '-' + str(nfl.team_names[1].losses) + '-' + str(nfl.team_names[1].ties))
    print('Chicago Record: ' + str(nfl.team_names[2].wins) + '-' + str(nfl.team_names[2].losses) + '-' + str(nfl.team_names[2].ties))
    print('Minnesota Record: ' + str(nfl.team_names[3].wins) + '-' + str(nfl.team_names[3].losses) + '-' + str(nfl.team_names[3].ties))
    print('Cincinnati Record: ' + str(nfl.team_names[4].wins) + '-' + str(nfl.team_names[4].losses) + '-' + str(nfl.team_names[4].ties))
    print('Cleveland Record: ' + str(nfl.team_names[5].wins) + '-' + str(nfl.team_names[5].losses) + '-' + str(nfl.team_names[5].ties))
    print('Dallas Record: ' + str(nfl.team_names[6].wins) + '-' + str(nfl.team_names[6].losses) + '-' + str(nfl.team_names[6].ties))
    print('Philadelphia Record: ' + str(nfl.team_names[7].wins) + '-' + str(nfl.team_names[7].losses) + '-' + str(nfl.team_names[7].ties))
    print('Green Bay Record: ' + str(nfl.team_names[8].wins) + '-' + str(nfl.team_names[8].losses) + '-' + str(nfl.team_names[8].ties))
    print('Detroit Record: ' + str(nfl.team_names[9].wins) + '-' + str(nfl.team_names[9].losses) + '-' + str(nfl.team_names[9].ties))
    print('Indianapolis Record: ' + str(nfl.team_names[10].wins) + '-' + str(nfl.team_names[10].losses) + '-' + str(nfl.team_names[10].ties))
    print('Jacksonville Record: ' + str(nfl.team_names[11].wins) + '-' + str(nfl.team_names[11].losses) + '-' + str(nfl.team_names[11].ties))
    print('New England Record: ' + str(nfl.team_names[12].wins) + '-' + str(nfl.team_names[12].losses) + '-' + str(nfl.team_names[12].ties))
    print('Miami Record: ' + str(nfl.team_names[13].wins) + '-' + str(nfl.team_names[13].losses) + '-' + str(nfl.team_names[13].ties))
    print('New Orleans Record: ' + str(nfl.team_names[14].wins) + '-' + str(nfl.team_names[14].losses) + '-' + str(nfl.team_names[14].ties))
    print('Atlanta Record: ' + str(nfl.team_names[15].wins) + '-' + str(nfl.team_names[15].losses) + '-' + str(nfl.team_names[15].ties))
    print('NY Jets Record: ' + str(nfl.team_names[16].wins) + '-' + str(nfl.team_names[16].losses) + '-' + str(nfl.team_names[16].ties))
    print('Buffalo Record: ' + str(nfl.team_names[17].wins) + '-' + str(nfl.team_names[17].losses) + '-' + str(nfl.team_names[17].ties))
    print('Pittsburgh Record: ' + str(nfl.team_names[18].wins) + '-' + str(nfl.team_names[18].losses) + '-' + str(nfl.team_names[18].ties))
    print('Baltimore Record: ' + str(nfl.team_names[19].wins) + '-' + str(nfl.team_names[19].losses) + '-' + str(nfl.team_names[19].ties))
    print('Tennessee Record: ' + str(nfl.team_names[20].wins) + '-' + str(nfl.team_names[20].losses) + '-' + str(nfl.team_names[20].ties))
    print('Houston Record: ' + str(nfl.team_names[21].wins) + '-' + str(nfl.team_names[21].losses) + '-' + str(nfl.team_names[21].ties))
    print('Washington Record: ' + str(nfl.team_names[22].wins) + '-' + str(nfl.team_names[22].losses) + '-' + str(nfl.team_names[22].ties))
    print('NY Giants Record: ' + str(nfl.team_names[23].wins) + '-' + str(nfl.team_names[23].losses) + '-' + str(nfl.team_names[23].ties))
    print('Kansas City Record: ' + str(nfl.team_names[24].wins) + '-' + str(nfl.team_names[24].losses) + '-' + str(nfl.team_names[24].ties))
    print('Denver Record: ' + str(nfl.team_names[25].wins) + '-' + str(nfl.team_names[25].losses) + '-' + str(nfl.team_names[25].ties))
    print('LA Chargers Record: ' + str(nfl.team_names[26].wins) + '-' + str(nfl.team_names[26].losses) + '-' + str(nfl.team_names[26].ties))
    print('Las Vegas Record: ' + str(nfl.team_names[27].wins) + '-' + str(nfl.team_names[27].losses) + '-' + str(nfl.team_names[27].ties))
    print('Seattle Record: ' + str(nfl.team_names[28].wins) + '-' + str(nfl.team_names[28].losses) + '-' + str(nfl.team_names[28].ties))
    print('Arizona Record: ' + str(nfl.team_names[29].wins) + '-' + str(nfl.team_names[29].losses) + '-' + str(nfl.team_names[29].ties))
    print('San Francisco Record: ' + str(nfl.team_names[30].wins) + '-' + str(nfl.team_names[30].losses) + '-' + str(nfl.team_names[30].ties))
    print('LA Rams Record: ' + str(nfl.team_names[31].wins) + '-' + str(nfl.team_names[31].losses) + '-' + str(nfl.team_names[31].ties))

    global afc, nfc, nfc_north, nfc_east, nfc_south, nfc_west, afc_north, afc_east, afc_south, afc_west
    nfc = [Carolina_record, Tampa_Bay_record, Chicago_record, Minnesota_record, Dallas_record, Philadelphia_record,
            Green_Bay_record, Detroit_record, New_Orleans_record, Atlanta_record, Washington_record, NY_Giants_record,
            Seattle_record, Arizona_record, San_Francisco_record, LA_Rams_record]
    nfc_north = [Green_Bay_record, Minnesota_record, Chicago_record, Detroit_record]
    nfc_east = [Dallas_record, NY_Giants_record, Washington_record, Philadelphia_record]
    nfc_south = [Tampa_Bay_record, New_Orleans_record, Carolina_record, Atlanta_record]
    nfc_west = [Arizona_record, LA_Rams_record, San_Francisco_record, Seattle_record]
    afc = [Cincinnati_record, Cleveland_record, Indianapolis_record, Jacksonville_record, New_England_record, Miami_record,
            NY_Jets_record, Buffalo_record, Pittsburgh_record, Baltimore_record, Tennessee_record,
            Houston_record, Kansas_City_record, Denver_record, LA_Chargers_record, Las_Vegas_record]
    afc_north = [Pittsburgh_record, Baltimore_record, Cincinnati_record, Cleveland_record]
    afc_east = [New_England_record, Miami_record, Buffalo_record, NY_Jets_record]
    afc_south = [Houston_record, Tennessee_record, Jacksonville_record, Indianapolis_record]
    afc_west = [Kansas_City_record, Las_Vegas_record, LA_Chargers_record, Denver_record]
    afc = sorted(afc, key=lambda team: team[0], reverse=True)
    afc_north = sorted(afc_north, key=lambda team: team[0], reverse=True)
    afc_east = sorted(afc_east, key=lambda team: team[0], reverse=True)
    afc_south = sorted(afc_south, key=lambda team: team[0], reverse=True)
    afc_west = sorted(afc_west, key=lambda team: team[0], reverse=True)
    nfc_north = sorted(nfc_north, key=lambda team: team[0], reverse=True)
    nfc_east = sorted(nfc_east, key=lambda team: team[0], reverse=True)
    nfc_south = sorted(nfc_south, key=lambda team: team[0], reverse=True)
    nfc_west = sorted(nfc_west, key=lambda team: team[0], reverse=True)
    nfc = sorted(nfc, key=lambda team: team[0], reverse=True)
    return afc, nfc, nfc_north, nfc_east, nfc_south, nfc_west, afc_north, afc_east, afc_south, afc_west
#season(1) # 4 weeks took 5 mins
#nflgame()

def playoffs(week, numofseasons, numofplayoffs):
    seasonsnum = 0
    while seasonsnum < numofseasons:
        season(week)  ###### sim each game multiple times and use average wins per season for seeding?
        seasonsnum += 1
    '''print(afc_north)
    print(afc_east)
    print(afc_south)
    print(afc_west)
    print(nfc_north)
    print(nfc_east)
    print(nfc_south)
    print(nfc_west)'''
    afc_div_winners = [afc_north[0], afc_east[0], afc_south[0], afc_west[0]]
    nfc_div_winners = [nfc_north[0], nfc_east[0], nfc_south[0], nfc_west[0]]
    afc_new = [i for i in afc if i not in afc_div_winners]
    nfc_new = [i for i in nfc if i not in nfc_div_winners]
    afc_div_winners = sorted(afc_div_winners, key=lambda team: team[0], reverse=True)
    nfc_div_winners = sorted(nfc_div_winners, key=lambda team: team[0], reverse=True)
    afc_1 = afc_div_winners[0]
    afc_2 = afc_div_winners[1]
    afc_3 = afc_div_winners[2]
    afc_4 = afc_div_winners[3]
    afc_5 = afc_new[0]
    afc_6 = afc_new[1]
    afc_7 = afc_new[2]
    afc_8 = afc_new[3]
    afc_9 = afc_new[4]
    afc_10 = afc_new[5]
    afc_11 = afc_new[6]
    afc_12 = afc_new[7]
    afc_13 = afc_new[8]
    afc_14 = afc_new[9]
    afc_15 = afc_new[10]
    afc_16 = afc_new[11]
    nfc_1 = nfc_div_winners[0]
    nfc_2 = nfc_div_winners[1]
    nfc_3 = nfc_div_winners[2]
    nfc_4 = nfc_div_winners[3]
    nfc_5 = nfc_new[0]
    nfc_6 = nfc_new[1]
    nfc_7 = nfc_new[2]
    nfc_8 = nfc_new[3]
    nfc_9 = nfc_new[4]
    nfc_10 = nfc_new[5]
    nfc_11 = nfc_new[6]
    nfc_12 = nfc_new[7]
    nfc_13 = nfc_new[8]
    nfc_14 = nfc_new[9]
    nfc_15 = nfc_new[10]
    nfc_16 = nfc_new[11]

    print('\nThe NFL Regular Season Simulation is Over, Here are the Results:\n')
    print('East Seed #1: ' + afc_1[1][1])
    print('East Seed #2: ' + afc_2[1][1])
    print('East Seed #3: ' + afc_3[1][1])
    print('East Seed #4: ' + afc_4[1][1])
    print('East Seed #5: ' + afc_5[1][1])
    print('East Seed #6: ' + afc_6[1][1])
    print('East Seed #7: ' + afc_7[1][1])
    print('East Seed #8: ' + afc_8[1][1])
    print('East Seed #9: ' + afc_9[1][1])
    print('East Seed #10: ' + afc_10[1][1])
    print('East Seed #11: ' + afc_11[1][1])
    print('East Seed #12: ' + afc_12[1][1])
    print('East Seed #13: ' + afc_13[1][1])
    print('East Seed #14: ' + afc_14[1][1])
    print('East Seed #15: ' + afc_15[1][1])
    print('East Seed #16: ' + afc_16[1][1])
    print('\n')
    print('West Seed #1: ' + nfc_1[1][1])
    print('West Seed #2: ' + nfc_2[1][1])
    print('West Seed #3: ' + nfc_3[1][1])
    print('West Seed #4: ' + nfc_4[1][1])
    print('West Seed #5: ' + nfc_5[1][1])
    print('West Seed #6: ' + nfc_6[1][1])
    print('West Seed #7: ' + nfc_7[1][1])
    print('West Seed #8: ' + nfc_8[1][1])
    print('West Seed #9: ' + nfc_9[1][1])
    print('West Seed #10: ' + nfc_10[1][1])
    print('West Seed #11: ' + nfc_11[1][1])
    print('West Seed #12: ' + nfc_12[1][1])
    print('West Seed #13: ' + nfc_13[1][1])
    print('West Seed #14: ' + nfc_14[1][1])
    print('West Seed #15: ' + nfc_15[1][1])
    print('West Seed #16: ' + nfc_16[1][1])

    time2 = datetime.datetime.now()
    print('season time: ' + str(time2 - time1))
    playoffnum = 0
    while playoffnum < numofplayoffs:
        playofftime1 = datetime.datetime.now()
        print('\nNFL Playoffs Start Now\n')
        '''afc_1_out = False
        afc_2_out = False
        afc_3_out = False
        afc_4_out = False
        afc_5_out = False
        afc_6_out = False
        afc_7_out = False'''
        afc_playoff_teams = [afc_1, afc_2, afc_3, afc_4, afc_5, afc_6, afc_7]
        nfc_playoff_teams = [nfc_1, nfc_2, nfc_3, nfc_4, nfc_5, nfc_6, nfc_7]
        #print(afc_playoff_teams, nfc_playoff_teams)
        # afc rnd 1
        print('AFC Round 1:\n')
        afc_2_7 = playoff_game(afc_2[1][0], afc_2[1][1], afc_2[1][2], afc_7[1][0], afc_7[1][1], afc_7[1][2])
        #print(afc_2_7)
        if afc_2_7:
            afc_playoff_teams.remove(afc_7)
        else:
            afc_playoff_teams.remove(afc_2)
        afc_3_6 = playoff_game(afc_3[1][0], afc_3[1][1], afc_3[1][2], afc_6[1][0], afc_6[1][1], afc_6[1][2])
        #print(afc_3_6)
        if afc_3_6:
            afc_playoff_teams.remove(afc_6)
        else:
            afc_playoff_teams.remove(afc_3)
        afc_4_5 = playoff_game(afc_4[1][0], afc_4[1][1], afc_4[1][2], afc_5[1][0], afc_5[1][1], afc_5[1][2])
        #print(afc_4_5)
        if afc_4_5:
            afc_playoff_teams.remove(afc_5)
        else:
            afc_playoff_teams.remove(afc_4)

        # nfc rnd 1
        print('\nNFC Round 1:\n')
        nfc_2_7 = playoff_game(nfc_2[1][0], nfc_2[1][1], nfc_2[1][2], nfc_7[1][0], nfc_7[1][1], nfc_7[1][2])
        #print(nfc_2_7)
        if nfc_2_7:
            nfc_playoff_teams.remove(nfc_7)
        else:
            nfc_playoff_teams.remove(nfc_2)
        nfc_3_6 = playoff_game(nfc_3[1][0], nfc_3[1][1], nfc_3[1][2], nfc_6[1][0], nfc_6[1][1], nfc_6[1][2])
        #print(nfc_3_6)
        if nfc_3_6:
            nfc_playoff_teams.remove(nfc_6)
        else:
            nfc_playoff_teams.remove(nfc_3)
        nfc_4_5 = playoff_game(nfc_4[1][0], nfc_4[1][1], nfc_4[1][2], nfc_5[1][0], nfc_5[1][1], nfc_5[1][2])
        #print(nfc_4_5)
        if nfc_4_5:
            nfc_playoff_teams.remove(nfc_5)
        else:
            nfc_playoff_teams.remove(nfc_4)
        #print(afc_playoff_teams, nfc_playoff_teams)
        # afc rnd 2
        print('\nAFC Round 2:\n')
        afc_rnd2_1 = playoff_game(afc_playoff_teams[0][1][0], afc_playoff_teams[0][1][1], afc_playoff_teams[0][1][2], afc_playoff_teams[3][1][0], afc_playoff_teams[3][1][1], afc_playoff_teams[3][1][2])
        afc_rnd2_2 = playoff_game(afc_playoff_teams[1][1][0], afc_playoff_teams[1][1][1], afc_playoff_teams[1][1][2], afc_playoff_teams[2][1][0], afc_playoff_teams[2][1][1], afc_playoff_teams[2][1][2])
        #print(afc_rnd2_1, afc_rnd2_2)
        if afc_rnd2_1 and afc_rnd2_2:
            afc_playoff_teams.pop(3)
            afc_playoff_teams.pop(2)
        elif afc_rnd2_1 and not afc_rnd2_2:
            afc_playoff_teams.pop(3)
            afc_playoff_teams.pop(1)
        elif afc_rnd2_2 and not afc_rnd2_1:
            afc_playoff_teams.pop(0)
            afc_playoff_teams.pop(1)
        else:
            afc_playoff_teams.pop(0)
            afc_playoff_teams.pop(0)

        # nfc rnd 2
        print('\nNFC Round 2:\n')
        nfc_rnd2_1 = playoff_game(nfc_playoff_teams[0][1][0], nfc_playoff_teams[0][1][1], nfc_playoff_teams[0][1][2], nfc_playoff_teams[3][1][0], nfc_playoff_teams[3][1][1], nfc_playoff_teams[3][1][2])
        nfc_rnd2_2 = playoff_game(nfc_playoff_teams[1][1][0], nfc_playoff_teams[1][1][1], nfc_playoff_teams[1][1][2], nfc_playoff_teams[2][1][0], nfc_playoff_teams[2][1][1], nfc_playoff_teams[2][1][2])
        #print(nfc_rnd2_1, nfc_rnd2_2)
        if nfc_rnd2_1 and nfc_rnd2_2:
            nfc_playoff_teams.pop(3)
            nfc_playoff_teams.pop(2)
        elif nfc_rnd2_1 and not nfc_rnd2_2:
            nfc_playoff_teams.pop(3)
            nfc_playoff_teams.pop(1)
        elif nfc_rnd2_2 and not nfc_rnd2_1:
            nfc_playoff_teams.pop(0)
            nfc_playoff_teams.pop(1)
        else:
            nfc_playoff_teams.pop(0)
            nfc_playoff_teams.pop(0)
        #print(afc_playoff_teams, nfc_playoff_teams)
        # afc champs
        print('\nAFC Championship:\n')
        afc_champs = playoff_game(afc_playoff_teams[0][1][0], afc_playoff_teams[0][1][1], afc_playoff_teams[0][1][2], afc_playoff_teams[1][1][0], afc_playoff_teams[1][1][1], afc_playoff_teams[1][1][2])
        #print(afc_champs)
        if afc_champs:
            afc_playoff_teams.pop(1)
        else:
            afc_playoff_teams.pop(0)

        # nfc champs
        print('\nNFC Championship:\n')
        nfc_champs = playoff_game(nfc_playoff_teams[0][1][0], nfc_playoff_teams[0][1][1], nfc_playoff_teams[0][1][2],
                                  nfc_playoff_teams[1][1][0], nfc_playoff_teams[1][1][1], nfc_playoff_teams[1][1][2])
        #print(nfc_champs)
        if nfc_champs:
            nfc_playoff_teams.pop(1)
        else:
            nfc_playoff_teams.pop(0)
        #print(afc_playoff_teams, nfc_playoff_teams)
        # superbowl
        print('\nSuperbowl:\n')
        superbowl = playoff_game(afc_playoff_teams[0][1][0], afc_playoff_teams[0][1][1], afc_playoff_teams[0][1][2], nfc_playoff_teams[0][1][0], nfc_playoff_teams[0][1][1], nfc_playoff_teams[0][1][2], True)
        #print(superbowl)
        if superbowl:
            print(afc_playoff_teams[0][1][1] + ' beat ' + nfc_playoff_teams[0][1][1] + ' in the Superbowl')
        else:
            print(nfc_playoff_teams[0][1][1] + ' beat ' + afc_playoff_teams[0][1][1] + ' in the Superbowl')
        playofftime2 = datetime.datetime.now()
        print('playoff time: ' + str(playofftime2-playofftime1))
        playoffnum += 1

'''def sims(week, seasons, Playoffs):
    playoffs_num = 0
    while playoffs_num < Playoffs:
        playoffs(week, seasons)
        playoffs_num += 1'''
### (18, 3, 1) import: 1:15, seasons: 4:30, playoffs: 3:10
playoffs(18, 10, 10)
