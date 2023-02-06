---- First section where we define the five exercise related tables ----

-- Table to hold workout categories
CREATE TABLE Workout_Category(
    Cat_ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL
);

-- Table to hold workout levels
CREATE TABLE Workout_Level(
    Level_ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL
);

-- Table for exercises
CREATE TABLE Exercise(
    Exercise_ID INTEGER PRIMARY KEY,
    Ex_Name TEXT NOT NULL,
    Description TEXT
);

-- Table for exercise categories
CREATE TABLE Exercise_Category(
    Ex_Cat_ID INTEGER PRIMARY KEY,
    Exercise_ID INTEGER NOT NULL,
    Cat_ID INTEGER NOT NULL,
    FOREIGN KEY (Exercise_ID) REFERENCES Exercise(Exercise_ID),
    FOREIGN KEY (Cat_ID) REFERENCES Workout_Category(Cat_ID)
);

-- Table for exercise levels 
CREATE TABLE Exercise_Level(
    Ex_Level_ID INTEGER PRIMARY KEY,
    Exercise_ID INTEGER NOT NULL,
    Level_ID INTEGER NOT NULL,
    Default_Target_Sets INTEGER,
    Default_Target_Reps INTEGER,
    FOREIGN KEY (Exercise_ID) REFERENCES Exercise(Exercise_ID),
    FOREIGN KEY (Level_ID) REFERENCES Workout_Level(Level_ID)
);

---- ******************************************************************** ----


---- Second section where we finish out the rest of the database ----

-- Table for member account
CREATE TABLE Member_account(
    Member_ID INTEGER PRIMARY KEY,
    Email TEXT NOT NULL,
    Password TEXT NOT NULL,
    Phone_Number TEXT NOT NULL,
    Level_ID INTEGER NOT NULL,
    Birth_Year INTEGER NOT NULL,
    Gender TEXT NOT NULL,
    Zipcode INTEGER NOT NULL
);

-- Table for exercise template exercises
CREATE TABLE Template_Exercises(
    Template_Ex_ID INTEGER PRIMARY KEY,
    Template_ID INTEGER NOT NULL,
    Exercise_ID INTEGER NOT NULL,
    Target_Sets INTEGER,
    Target_Reps INTEGER,
    FOREIGN KEY (Exercise_ID) REFERENCES Exercise(Exercise_ID),
    FOREIGN KEY (Template_ID) REFERENCES Template_Workout(Template_ID)
);

-- Table for prior workout exercises
CREATE TABLE Prior_Workout_Exercises(
    Prior_Workout_Ex_ID INTEGER PRIMARY KEY,
    Exercise_ID INTEGER NOT NULL,
    Workout_ID INTEGER NOT NULL,
    Target_Sets INTEGER,
    Target_Reps INTEGER,
    Actual_Sets INTEGER,
    Actual_Reps INTEGER,
    Position_In_List INTEGER NOT NULL,
    FOREIGN KEY (Exercise_ID) REFERENCES Exercise(ExerciseID),
    FOREIGN KEY (Workout_ID) REFERENCES Prior_Workout(Workout_ID)
);

-- Table for future workout exercises
CREATE TABLE Future_Workout_Exercises(
    Future_Workout_Ex_ID INTEGER PRIMARY KEY,
    Future_Workout_ID INTEGER NOT NULL,
    Exercise_ID INTEGER NOT NULL,
    Target_Sets INTEGER,
    Target_Reps INTEGER,
    Position_In_List INTEGER NOT NULL,
    FOREIGN KEY (Exercise_ID) REFERENCES Exercise(Exercise_ID),
    FOREIGN KEY (Future_Workout_ID) REFERENCES Future_Workout(Future_Workout_ID)
);

-- Table for workout templates
CREATE TABLE Template_Workout(
    Template_ID INTEGER PRIMARY KEY,
    Member_ID INTEGER NOT NULL,
    Level_ID INTEGER NOT NULL,
    Category_ID INTEGER NOT NULL,
    Name TEXT NOT NULL,
    FOREIGN KEY (Level_ID) REFERENCES Member_Account(Level_ID),
    FOREIGN KEY (Member_ID) REFERENCES Member_Account(Member_ID)
);

-- Table for prior workouts
CREATE TABLE Prior_Workout(
    Workout_ID INTEGER PRIMARY KEY,
    Member_ID INTEGER NOT NULL,
    Level_ID INTEGER NOT NULL,
    Category_ID INTEGER NOT NULL,
    When_Completed DATE,
    FOREIGN KEY (Level_ID) REFERENCES Member_Account(Level_ID),
    FOREIGN KEY (Member_ID) REFERENCES Member_Account(Member_ID)
);

-- Table for holding future workouts
CREATE TABLE Future_Workout(
    Future_Workout_ID INTEGER PRIMARY KEY,
    Member_ID INTEGER NOT NULL,
    Level_ID INTEGER NOT NULL,
    Category_ID INTEGER NOT NULL,
    Name TEXT NOT NULL,
    Perform_On DATE,
    FOREIGN KEY (Level_ID) REFERENCES Member_Account(Level_ID),
    FOREIGN KEY (Member_ID) REFERENCES Member_Account(Member_ID)
);

---- ******************************************************************** ----

INSERT INTO Exercise (Exercise_ID, Ex_Name)
VALUES (1, "Scapular Pull"), (2, "Arch hang"), 
(3, "Negative Pull-up"), (4, "Pull-up"),
(5, "Wide Grip Pull-up"), (6, "L-sit Pull-up"),
(7, "Muscle-up"), (8, "Vertical Push-up"),
(9, "Incline Push-up"), (10, "Push-up"),
(11, "Decline Push-up"), (12, "Diamond Push-up"),
(13, "Pike Push-up"), (14, "Wall Assisted Handstand Push-up"),
(15, "Pseudo-planche Push-up"), (16, "Freestanding Handstand Push-up"),
(17, "Decline Pseudo-planche Push-up"), (18, "Planche Push-up"),
(19, "Magic Push-up"), (20, "Static Dip Support Hold"),
(21, "Negative Dip"), (22, "Seated Dip"),
(23, "Parallel Bar Dip"), (24, "Straight Bar Dip"),
(25, "Impossible Dip"), (26, "Vertical Row"),
(27, "Incline Row"), (28, "Horizontal Row"),
(29, "Wide-grip Incline Row"), (30, "Wide-grip Horizontal Row"),
(31, "Decline Row"), (32, "Assisted Squat"),
(33, "Air Squat"), (34, "Bulgarian Split Squat"),
(35, "Beginner Shrimp Squat"), (36, "Intermediate Shrimp Squat"),
(37, "Assisted Pistol Squat"), (38, "Advanced Shrimp Squat"),
(39, "Pistol Squat"), (40, "Dragon Pistol Squat"),
(41, "Romanian Deadlift"), (42, "Single Leg Deadlift"),
(43, "Banded Nordic Curl Negative"), (44, "Banded Nordic Curl"),
(45, "Nordic Curl"), (46, "Full Plank"),
(47, "Half Plank"), (48, "L-sit"),
(49, "Hanging Knee-raise"), (50, "Sit-up"),
(51, "Crunch"), (52, "Toe-touch"),
(53, "Superman Hold"), (54, "Mountain Climber"),
(55, "Plank Row"), (56, "Pseudo-planche Hold"),
(57, "Crow Hold"), (58, "Leg Raise"),
(59, "Bicycle"), (60, "Side Plank With Rotation"),
(61, "Banana Roll"), (62, "Hanging L-sit"),
(63, "Hanging Leg Raise"), (64, "Reverse Deadlift"),
(65, "Dragon Flag"), (66, "Front Lever"),
(67, "Single-leg Straight Arm Side Plank"), (68, "Planche Hold");

INSERT INTO Workout_Category (Cat_ID, Name)
VALUES (1, "Pull-up"), (2, "Push-up"),
(3, "Dip"), (4, "Row"),
(5, "Squat"), (6, "Hinge"),
(7, "Core");

INSERT INTO Workout_Level (Level_ID, Name)
VALUES (1, "Beginner"), (2, "Intermediate"),
(3, "Advanced");