from plyer import notification
from time import sleep

facts = {
    1: "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
    2: "A group of flamingos is called a 'flamboyance.'",
    3: "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",
    4: "The Eiffel Tower can be 15 cm taller during the summer due to the expansion of the iron in the heat.",
    5: "A day on Venus is longer than a year on Venus. Venus has an extremely slow rotation on its axis.",
    6: "The world's largest desert is not the Sahara but Antarctica.",
    7: "Honeybees can recognize human faces.",
    8: "The total weight of ants on Earth is comparable to the total weight of all the humans on Earth.",
    9: "The first recorded game of baseball was played in 1846 in Hoboken, New Jersey.",
    10: "A group of crows is called a 'murder.'",
    11: "There are more possible iterations of a game of chess than there are atoms in the observable universe.",
    12: "Octopuses have three hearts. Two pump blood to the gills, while the third pumps it to the rest of the body.",
    13: "The Great Wall of China is not visible from space with the naked eye, despite a popular myth.",
    14: "There's a town in Norway called Hell.",
    15: "The Sahara Desert was once lush and green, with lakes and rivers.",
    16: "A group of owls is called a 'parliament.'",
    17: "Bananas are berries, but strawberries are not.",
    18: "The Great Barrier Reef is the world's largest living structure.",
    19: "Polar bears' skin is black, not white.",
    20: "Cows have best friends and can become stressed when separated from them.",
    21: "The longest hiccuping spree lasted for 68 years.",
    22: "Hippopotamuses secrete a red, oily substance often referred to as 'blood sweat.'",
    23: "Starfish don't have a brain.",
    24: "A flock of geese in flight is called a 'skein.'",
    25: "The world's largest known snowflake was 15 inches wide.",
    26: "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",
    27: "Antarctica is the world's largest desert.",
    28: "The total weight of ants on Earth is comparable to the total weight of all the humans on Earth.",
    29: "The first recorded game of baseball was played in 1846 in Hoboken, New Jersey.",
    30: "A group of crows is called a 'murder.'",
    31: "There are more possible iterations of a game of chess than there are atoms in the observable universe.",
    32: "Octopuses have three hearts. Two pump blood to the gills, while the third pumps it to the rest of the body.",
    33: "The Great Wall of China is not visible from space with the naked eye, despite a popular myth.",
    34: "Honeybees can recognize human faces.",
    35: "There's a town in Norway called Hell.",
    36: "The Sahara Desert was once lush and green, with lakes and rivers.",
    37: "A group of owls is called a 'parliament.'",
    38: "Bananas are berries, but strawberries are not.",
    39: "The Great Barrier Reef is the world's largest living structure.",
    40: "Polar bears' skin is black, not white.",
    41: "Cows have best friends and can become stressed when separated from them.",
    42: "The longest hiccuping spree lasted for 68 years.",
    43: "Hippopotamuses secrete a red, oily substance often referred to as 'blood sweat.'",
    44: "Starfish don't have a brain.",
    45: "A flock of geese in flight is called a 'skein.'",
    46: "The world's largest known snowflake was 15 inches wide.",
    47: "Banging your head against a wall burns 150 calories per hour.",
    48: "A group of flamingos is called a 'flamboyance.'",
    49: "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
    50: "A day on Venus is longer than a year on Venus. Venus has an extremely slow rotation on its axis.",
}

i = 0
while True:
    i += 1
    notification.notify(
        title="did you know?",
        message=facts[i],
        app_icon="D:\\Finished Projects\\Python projects\\Python_projects\\assets\\icon.ico",

    )
    sleep(10)
