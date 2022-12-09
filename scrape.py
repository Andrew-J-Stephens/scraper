

from selenium import webdriver
from selenium.webdriver.common.by import By

# specify the URL of the page you want to scrape
web = "https://www.888sport.ca/basketball/nba/"
path = 'Downloads'
driver = webdriver.Chrome(
    executable_path=path,
    options=webdriver.ChromeOptions()
)
driver.get(web)

driver.implicitly_wait(5)

class Game:
    def __init__(self, team1, team2, moneyLine1, moneyLine2):
        self.team1 = team1
        self.team2 = team2
        self.moneyLine1 = moneyLine1
        self.moneyLine2 = moneyLine2
    def __str__(self):
        return f'The {self.team1} are facing the {self.team2} with payouts: {self.moneyLine1} & {self.moneyLine2}'


games888 = []

# find all elements with class name "bet-card__bet-buttons"
bet_cards = driver.find_elements(By.CLASS_NAME, "bet-card")

# loop through each bet-card element
i = 0
for card in bet_cards:
    # find the elements with class name "bet-card__bet-buttons" and "featured-matches-widget__event-text featured-matches-widget__event-competitor" inside the current bet-card
    bet_buttons = card.find_elements(By.CLASS_NAME, "bet-card__bet-buttons")
    # event_competitor = card.find_elements(By.CLASS_NAME, "featured-matches-widget__event-text featured-matches-widget__event-competitor")
    event_competitors = card.find_elements(By.XPATH, "//span[contains(@class,'featured-matches-widget__event-text featured-matches-widget__event-competitor')]")

    # for event_competitor in event_competitors:
        # print(event_competitor.get_attribute("innerHTML"))

    # print the text of each element
    for button in bet_buttons:
        print("i: " + str(i))
        games888.append(Game(str(event_competitors[i].get_attribute("innerHTML").replace("@", "").replace(" ", "")),str(event_competitors[i+1].get_attribute("innerHTML").replace(" ", "")),(float(button.text.split("\n")[5])), (float(button.text.split("\n")[4]))))

    i = i + 2
        
    
i = 0
for i in games888:
    print(i)

# close the webdriver instance
driver.close()

web2 = "https://www.northstarbets.ca/sportsbook#sports-hub/basketball/nba"
path = 'Downloads'
driver = webdriver.Chrome(
    executable_path=path,
    options=webdriver.ChromeOptions()
)
driver.get(web2)

driver.implicitly_wait(8)

gamesBetway = []

# find all elements with class name "bet-card__bet-buttons"
bet_cards = driver.find_elements(By.CLASS_NAME, "KambiBC-bet-offer__outcomes")
print("bet_card: " + str(len(bet_cards)))

# loop through each bet-card element
i = 0
for card in bet_cards:
    # find the elements with class name "bet-card__bet-buttons" and "featured-matches-widget__event-text featured-matches-widget__event-competitor" inside the current bet-card
    # bet_buttons = card.find_elements(By.CLASS_NAME, "KambiBC-bet-offer__outcomes")
    # event_competitor = card.find_elements(By.CLASS_NAME, "featured-matches-widget__event-text featured-matches-widget__event-competitor")
    event_competitors = card.find_elements(By.XPATH, "//div[contains(@class,'KambiBC-event-participants__name')]")

    # for event_competitor in event_competitors:
        # print(event_competitor.get_attribute("innerHTML"))

    # print the text of each element
    for button in bet_cards:
        gamesBetway.append(Game(str(event_competitors[i].get_attribute("innerHTML").replace("@", "").replace(" ", "")),str(event_competitors[i+1].get_attribute("innerHTML").replace(" ", "")),(float(button.text.split("\n")[5])), (float(button.text.split("\n")[4]))))

    i = i + 2
        
    
i = 0
for i in gamesBetway:
    print(i)

# close the webdriver instance
driver.close()
