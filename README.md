# emojis

### Introduction
Emoji, literally meaning ‘picture-word’ in Japanese, are increasingly being used in written language. This can be observed in the rise in the number of emoji-related tools such search-by-emoji and Emoji Replacement or prediction features. The emoji language is also considered to be the fastest growing language in the UK; this may be attributable to how a large proportion of 18 to 25-year-olds find it easier to express their feelings through emoji instead of through text (Chollet, 2017). However, despite the increasing use of emoji and their rising numbers, there are still several emotional concepts which are not represented visually. This project aims to generate emojis which visually depict these emotions. 

### Process
#### 1. Model emotions computationally
Human emotions are largely subjective and different individuals may react differently to the same stimulus (Fellous, 2007). There are several computational and cognitive models of emotions which stem from multidisciplinary research on the subject such as Ekman’s model of six basic emotions, Wang’s hierarchical model of emotions, the appraisal theory of emotions and Russel’s circumplex model. 
Russel's circumplex model will be used here which comprises of two affective dimsensions of *arousal* and *valence*. Arousal is the level of energy while valence is the type of experience such as displeasure and pleasure. The image below shows the two-dimesnional circumplex space model which was further adapted by Scherer. I mapped existing emojis onto this model using Emojipedia (https://emojipedia.org/), an emoji reference website. 

![image](https://user-images.githubusercontent.com/94219257/177370656-0daa8d2c-86a8-4879-85c6-324f4aa3d926.png)

#### 2. Features
After mapping existing emojis to Scherer’s model, I observed that emojis had the below main properties which can be altered to depict different emotions: 
- Eyes 
- Eyebrows
- Mouth 
- Colour of the face
- An additional feature such as hands or a hat

Since the highest number of emojis exist in quadrant 3 where both arousal and valence are negative, I began the process of creating emojis by observing the similarities between emojis in this quadrant. 

#### 3. Setting rules

Based on the coordinates of each emoji, I set conditions for what the features should be like, for example, how highly furrowed the eyebrows should be, whether the eyes are frowning or oval in shape:

![image](https://user-images.githubusercontent.com/94219257/177615249-1e1fd97f-5866-403a-bc7d-7af09d05a866.png)

![image](https://user-images.githubusercontent.com/94219257/177615293-d3a52028-34ae-4015-be78-0d1aaeb75a38.png)

![image](https://user-images.githubusercontent.com/94219257/177615344-1330770d-331f-4155-a68b-b97a5f62d53b.png)

I also listed all the emotions in the circumplex model and did the following two tasks:

1. Recreate existing emojis
An example is shown below: 
Worried: ![image](https://user-images.githubusercontent.com/94219257/177621356-d7a7eef3-a2d6-437b-80d4-4cd551179203.png)


2.  Generate new emojis

