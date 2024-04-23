CREATE DATABASE ChildMuseum;

USE ChildMuseum;

CREATE TABLE Exhibit (
    ExhibitID INT,
    ExhibitName VARCHAR(100) PRIMARY KEY,
    Location VARCHAR(100)
);

CREATE TABLE Activities (
    ActivityID INT PRIMARY KEY,
    ActivityName VARCHAR(100),
    Category VARCHAR(50),
    Subcategory VARCHAR(100),
    Description TEXT,
    ExhibitName VARCHAR(100),
    FOREIGN KEY (ExhibitName) REFERENCES Exhibit(ExhibitName)

);

CREATE TABLE Users(
    UserID INT PRIMARY KEY,
    Username VARCHAR(100),
    Email VARCHAR(100),
    Password VARCHAR(100)
);

CREATE TABLE Children (
    ChildID INT PRIMARY KEY,
    ChildName VARCHAR(100),
    Age INT,
    ParentUserID INT,
    FOREIGN KEY (ParentUserID) REFERENCES Users(UserID)
);

CREATE TABLE TypeOfPlay (
    TypeID INT PRIMARY KEY,
    TypeName VARCHAR(100),
    Description TEXT
);

CREATE TABLE ChildInteraction(
    InteractionID INT PRIMARY KEY,
    ChildID INT,
    ExhibitName VARCHAR(100),
    ActivityID INT,
    InteractionDate DATE,
    InteractionTime TIME,
    DurationMinutes INT,
    FOREIGN KEY (ChildID) REFERENCES Children(ChildID),
    FOREIGN KEY (ExhibitName) REFERENCES Exhibit(ExhibitName),
    FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID)
);

CREATE TABLE TimeStamp(
    TimeStampID INT PRIMARY KEY,
    CurrentTime TIMESTAMP,
    DateTime DATETIME,
    UserID INT,
    ChildID INT,
    ExhibitName VARCHAR(100),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (ChildID) REFERENCES Children(ChildID),
    FOREIGN KEY (ExhibitName) REFERENCES Exhibit(ExhibitName)
);

INSERT INTO Exhibit (ExhibitID, ExhibitName, Location)
VALUES
    (0, 'Art Smart', 'Level 2'),
    (1, 'Big John', 'Level 3'),
    (2, 'Central Bank', 'Level 2 (Safety Village)'),
    (3, 'Engineers Workshop', 'Level 2'),
    (4, 'Farm', 'Level 2'),
    (5, 'Firehouse', 'Level 2 (Safety Village)'),
    (6, 'Global Cafe', 'Level 1'),
    (7, 'Ice Cream Parlor', 'Level 2 (Safety Village)'),
    (8, 'KidsPort', 'Level 1'),
    (9, 'Light Cloud', 'Level 1'),
    (10, 'Pizza Place', 'Level 2 (Safety Village)'),
    (11, 'Publix', 'Level 2 (Safety Village)'),
    (12, 'St. Josephs Children Hospital', 'Level 2 (Safety Village)'),
    (13, 'Tugboats Tots', 'Level 1'),
    (14, 'Twinkle Stars Theater', 'Level 2'),
    (15, 'Vet Clinic', 'Level 2 (Safety Village)'),
    (16, 'Water''s Journey', 'Level 2'),
    (17, 'All Exhibits', 'Level 1, 2, & 3');

INSERT INTO Activities (ActivityID, ActivityName, Category, Subcategory, Description, ExhibitName)
VALUES
    (1, 'Make Me a Pizza', 'Physical', 'Spreading food on pizza', 'By spreading food on pizza, children engage in fine motor skills development', 'Pizza Place'),
    (2, 'Shall We Dance?', 'Physical', 'Dancing', 'Through dancing, children learn gross motor movement and body coordination', 'Twinkle Stars Theater'),
    (3, 'Time to Draw!', 'Physical', 'Drawing', 'Drawing helps children develop fine motor skills and creative expression', 'Art Smart'),
    (4, 'Who is faster?', 'Physical', 'Racing', 'Engaging in races helps children develop logic and physical coordination', 'Tugboats Tots'),
    (5, 'At the Races', 'Physical', 'Racing', 'Participating in races aids in prediction skills and physical activity', 'Tugboats Tots'),
    (6, 'Stop that Ball!', 'Physical', 'Moving', 'Playing games like "Stop that Ball!" helps in gross motor skills and coordination', 'Tugboats Tots'),
    (7, 'Lego Activity', 'Physical', 'Building Lego', 'Playing with Legos promotes fine motor skills and creativity', 'All Exhibits'),
    (8, 'Where will it go?', 'Physical', 'Drawing', 'Drawing activities like "Where will it go?" develop spatial awareness and planning', 'Art Smart'),
    (9, 'Piloting a Boat', 'Physical', 'Piloting a boat', 'Practicing boat piloting enhances motor skills and spatial awareness', 'KidsPort'),

    (10, 'I’m Here to Help', 'Social-emotional', 'Morality', 'Engaging in moral activities like "I’m Here to Help" encourages empathy and cooperation', 'St. Josephs Children Hospital'),
    (11, 'Kaleidoscope', 'Social-emotional', 'Theory of mind', 'Activities like "Kaleidoscope" foster theory of mind understanding and perspective taking', 'Twinkle Stars Theater'),
    (12, 'Counting Quickly', 'Social-emotional', 'Sharing', 'Counting activities promote sharing and cooperative behavior', 'All Exhibits'),
    (13, 'Lego Activity', 'Social-emotional', 'Egocentrism', 'Playing with Legos helps children understand egocentrism and social interaction', 'All Exhibits'),
    (14, 'Twinkle Star Theater', 'Social-emotional', 'Acting', 'Participating in theater activities like "Twinkle Star Theater" fosters creativity and social skills', 'Twinkle Stars Theater'),

    (15, 'Eating the Rainbow', 'Sensory', 'Food', 'Exploring different foods helps children develop sensory experiences and dietary awareness', 'Global Cafe'),
    (16, 'Kaleidoscope', 'Sensory', 'Colors', 'Using a kaleidoscope promotes sensory exploration of colors and patterns', 'Twinkle Stars Theater'),
    (17, 'Time to Draw!', 'Sensory', 'Drawing', 'Drawing activities provide sensory input and encourage creativity', 'Art Smart'),
    (18, 'Ahoy, There!', 'Sensory', 'Vision-size constancy', 'Engaging in activities like "Ahoy, There!" develops visual perception and size constancy', 'All Exhibits'),

    (19, 'Bilingual Activity', 'Cognitive', 'Foreign language', 'Participating in bilingual activities helps in language acquisition and cognitive flexibility', 'All Exhibits'),
    (20, 'Nutrition', 'Cognitive', 'Sorting into categories', 'Sorting foods into categories aids in cognitive development and dietary awareness', 'Farm'),
    (21, 'Money', 'Cognitive', 'Math/counting', 'Engaging in activities involving money promotes math skills and financial literacy', 'Central Bank'),
    (22, 'Sorting', 'Cognitive', 'Sorting by size', 'Sorting objects by size enhances cognitive skills and categorization abilities', 'All Exhibits'),
    (23, 'Bones', 'Cognitive', 'Symbolic play', 'Engaging in symbolic play with bones promotes imagination and understanding of abstract concepts', 'Big John'),
    (24, 'Eating the Rainbow', 'Cognitive', 'Food', 'Exploring different foods promotes sensory experiences and dietary awareness', 'Global Cafe'),
    (25, 'Going to the Doctor', 'Cognitive', 'Mapping', 'Role-playing activities like "Going to the Doctor" enhance spatial awareness and social understanding', 'St. Josephs Children Hospital'),
    (26, 'Make Me a Pizza', 'Cognitive', 'Math/counting', 'Engaging in pizza-making activities involves math skills and counting', 'Pizza Place'),
    (27, 'Advanced Pizza Making', 'Cognitive', 'Advanced math', 'Activities like "Advanced Pizza Making" develop more complex math skills and problem-solving', 'Pizza Place'),
    (28, 'Order up!', 'Cognitive', 'Memory', 'Memory games like "Order up!" enhance cognitive skills and recall abilities', 'Pizza Place'),
    (29, 'Planning a Party', 'Cognitive', 'Planning skills', 'Planning activities like "Planning a Party" develop organizational skills and foresight', 'KidsPort'),
    (30, 'Fire Fighter!', 'Cognitive', 'Symbolic play', 'Engaging in symbolic play as a firefighter promotes imagination and problem-solving', 'FireHouse'),
    (31, 'Kaleidoscope', 'Cognitive', 'Theory of mind', 'Activities like "Kaleidoscope" foster theory of mind understanding and perspective taking', 'Twinkle Stars Theater'),
    (32, 'Counting Quickly', 'Cognitive', 'Counting', 'Counting activities promote numeracy and cognitive development', 'All Exhibits'),
    (33, 'How the Mind Wanders', 'Cognitive', 'Memory', 'Activities like "How the Mind Wanders" enhance memory and attention abilities', 'All Exhibits'),
    (34, 'Time to Draw!', 'Cognitive', 'Representation', 'Drawing activities promote creativity and visual-spatial skills', 'Art Smart'),

    (35, 'Bilingual Activity', 'Communication', 'Foreign language', 'Engaging in bilingual activities helps in language acquisition and cultural understanding', 'All Exhibits'),
    (36, 'Letters', 'Communication', 'Recognizing letters', 'Letter recognition activities promote literacy skills and phonemic awareness', 'All Exhibits'),
    (37, 'The Case of the Missing Letter', 'Communication', 'Word completion', 'Word completion activities enhance vocabulary and language comprehension', 'All Exhibits'),
    (38, 'Surely You’re Joking', 'Communication', 'Metaphor', 'Engaging in metaphorical expressions promotes linguistic creativity and understanding', 'All Exhibits');

INSERT INTO TypeOfPlay (TypeID, TypeName, Description)
VALUES
    (1, 'Physical', 'Activities that involve physical movement and coordination.'),
    (2, 'Social-emotional', 'Activities that promote social interaction, empathy, and emotional development.'),
    (3, 'Sensory', 'Activities that engage the senses such as touch, sight, smell, and taste.'),
    (4, 'Cognitive', 'Activities that stimulate cognitive development including problem-solving, memory, and reasoning.'),
    (5, 'Communication', 'Activities that focus on language development, including speaking, listening, and understanding.');






