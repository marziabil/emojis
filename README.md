# emojis

### Introduction
Emoji, literally meaning ‘picture-word’ in Japanese, are increasingly being used in written language. This can be observed in the rise in the number of emoji-related tools such as search-by-emoji and Emoji Replacement or prediction features. The emoji language is also considered to be the fastest growing language in the UK; this may be attributable to how a large proportion of 18 to 25-year-olds find it easier to express their feelings through emoji instead of through text (Doble, 2015). However, despite the increasing use of emojis and their rising numbers, there are still several emotional concepts which are not represented visually. This project aims to generate emojis which visually depict these emotions. 

### Process
#### 1. Model emotions computationally
Human emotions are largely subjective and different individuals may react differently to the same stimulus (Fellous, 2007). There are several computational and cognitive models of emotions which stem from multidisciplinary research on the subject such as Ekman’s model of six basic emotions, Wang’s hierarchical model of emotions, the appraisal theory of emotions and Russel’s circumplex model. 
Russel's circumplex model will be used here which comprises two affective dimensions of *arousal* and *valence*. Arousal is the level of energy while valence is the type of experiences such as displeasure and pleasure. The image below shows the two-dimensional circumplex space model which was further adapted by Scherer. I mapped existing emojis onto this model using Emojipedia (https://emojipedia.org/), an emoji reference website. 

![image](https://user-images.githubusercontent.com/94219257/179352214-e595c455-7f4b-4670-bf02-7f2d9fc20bbe.png)

#### 2. Features
After mapping existing emojis to Scherer’s model, I observed that emojis had the below main properties which can be altered to depict different emotions: 
- Eyes 
- Eyebrows
- Mouth 
- Colour of the face
- An additional feature such as hands or a hat

Since the highest number of emojis exists in quadrant 3 where both arousal and valence are negative, I began the process of creating emojis by observing the similarities between emojis in this quadrant. 

#### 3. Setting rules

Based on the coordinates of each emoji, I set conditions for what the features should be like, for example, how highly furrowed the eyebrows should be, whether the eyes are frowning or oval in shape. 

I also listed all the emotions in the circumplex model and did the following two tasks:

##### a. Recreate existing emojis #####

An example is shown below: 

**Emotion**: Worried

![image](https://user-images.githubusercontent.com/94219257/177621356-d7a7eef3-a2d6-437b-80d4-4cd551179203.png)

##### b.  Generate new emojis #####

**Emotion**: Desperate (x and y coordinates: -0.80	-0.50)

![image](https://user-images.githubusercontent.com/94219257/177792300-ca90b5de-c31b-4d44-917b-d0cc70cf1071.png)

A quick Google Image search showed similar expressions as well:

![image](https://user-images.githubusercontent.com/94219257/177792677-cf9b96d7-2b52-4efb-a3f8-3f5ed7cb041b.png)

**Emotion**: Melancholic

![image](https://user-images.githubusercontent.com/94219257/177793571-bbf788b2-2dc2-4eb4-afea-ae6069c6f3a4.png)

### Next steps

Since the features could be the same for particular emotions based on the rules, the next step would be to implement fuzzy rules which would make the reasoning approximate instead of being fixed and exact. This would allow every emoji to be unique based on its coordinates. For instance, the 'furrowness' of the eyebrows would increase slightly as the intensity increases. 

Moreover, the existing work has to be mapped to the next three quadrants as well. Currently, the code only works for emojis with negative x and y coordinates. 

### References
Doble, A., 2015. UK's fastest growing language is... emoji. [online] BBC News. Available at: <https://www.bbc.co.uk/news/newsbeat-32793732> [Accessed 30 June 2022].

Fellous, J., (2007). Models of emotion. Scholarpedia, 2(11), 1453. 


