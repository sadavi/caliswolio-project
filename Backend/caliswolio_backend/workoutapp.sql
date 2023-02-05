
---- First section where we define the five exercise related tables ----

-- Table to hold workout categories
CREATE TABLE Workout_Category(
    Cat_ID INTEGER PRIMARY KEY,
    Description TEXT NOT NULL,
    Name TEXT NOT NULL
);

-- Table to hold workout levels
CREATE TABLE Workout_Level(
    Level_ID INTEGER PRIMARY KEY,
    Description TEXT NOT NULL,
    Name TEXT NOT NULL
);

-- Table for exercises
CREATE TABLE Exercise(
    Exercise_ID INTEGER PRIMARY KEY,
    Ex_Name TEXT NOT NULL,
    Description TEXT NOT NULL
);

-- Table for exercise categories
CREATE TABLE Exercise_Category(
    Ex_Cat_ID INTEGER PRIMARY KEY,
    Exercise_ID INTEGER NOT NULL,
    Cat_ID INTEGER NOT NULL,
    Num_Of_Exercises TEXT NOT NULL,
    FOREIGN KEY (Exercise_ID) REFERENCES Exercise(Exercise_ID),
    FOREIGN KEY (Cat_ID) REFERENCES Workout_Category(Cat_ID)
);

-- Table for exercise levels 
CREATE TABLE Exercise_Level(
    Ex_Level_ID INTEGER PRIMARY KEY,
    Exercise_ID INTEGER NOT NULL,
    Level_ID INTEGER NOT NULL,
    Default_Target_Sets INTEGER NOT NULL,
    Default_Target_Reps INTEGER NOT NULL,
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
    Target_Sets INTEGER NOT NULL,
    Target_Reps INTEGER NOT NULL,
    FOREIGN KEY (Exercise_ID) REFERENCES Exercise(Exercise_ID),
    FOREIGN KEY (Template_ID) REFERENCES Template_Workout(Template_ID)
);

-- Table for prior workout exercises
CREATE TABLE Prior_Workout_Exercises(
    Prior_Workout_Ex_ID INTEGER PRIMARY KEY,
    Exercise_ID INTEGER NOT NULL,
    Workout_ID INTEGER NOT NULL,
    Target_Sets INTEGER NOT NULL,
    Target_Reps INTEGER NOT NULL,
    Actual_Sets INTEGER NOT NULL,
    Actual_Reps INTEGER NOT NULL,
    Position_In_List INTEGER NOT NULL,
    FOREIGN KEY (Exercise_ID) REFERENCES Exercise(ExerciseID),
    FOREIGN KEY (Workout_ID) REFERENCES Prior_Workout(Workout_ID)
);

-- Table for future workout exercises
CREATE TABLE Future_Workout_Exercises(
    Future_Workout_Ex_ID INTEGER PRIMARY KEY,
    Future_Workout_ID INTEGER NOT NULL,
    Exercise_ID INTEGER NOT NULL,
    Target_Sets INTEGER NOT NULL,
    Target_Reps INTEGER NOT NULL,
    Position_In_List INTEGER NOT NULL,
    FOREIGN KEY (Exercise_ID) REFERENCES Exercise(Exercise_ID),
    FOREIGN KEY (Future_Workout_ID) REFERENCES Future_Workout(Future_Workout_ID)
);

-- Table for workout templates
CREATE TABLE Template_Workout(
    Template_ID INTEGER PRIMARY KEY,
    Member_ID INTEGER NOT NULL,
    Level_ID INTEGER NOT NULL,
    Category_ID TEXT NOT NULL,
    Name TEXT NOT NULL,
    FOREIGN KEY (Level_ID) REFERENCES Member_Account(Level_ID),
    FOREIGN KEY (Member_ID) REFERENCES Member_Account(Member_ID)
);

-- Table for prior workouts
CREATE TABLE Prior_Workout(
    Workout_ID INTEGER PRIMARY KEY,
    Member_ID INTEGER NOT NULL,
    Level_ID INTEGER NOT NULL,
    Category_ID TEXT NOT NULL,
    When_Completed DATE,
    FOREIGN KEY (Level_ID) REFERENCES Member_Account(Level_ID),
    FOREIGN KEY (Member_ID) REFERENCES Member_Account(Member_ID)
);

-- Table for holding future workouts
CREATE TABLE Future_Workout(
    Future_Workout_ID INTEGER PRIMARY KEY,
    Member_ID INTEGER NOT NULL,
    Level_ID INTEGER NOT NULL,
    Category_ID TEXT NOT NULL,
    Name TEXT NOT NULL,
    Perform_On DATE,
    FOREIGN KEY (Level_ID) REFERENCES Member_Account(Level_ID),
    FOREIGN KEY (Member_ID) REFERENCES Member_Account(Member_ID)
);