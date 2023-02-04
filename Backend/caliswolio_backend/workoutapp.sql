
--- First section where we define the five exercise related tables ---

-- -- Table to hold our workout categories
-- CREATE TABLE Workout_Category(
--     Cat_ID INTEGER PRIMARY KEY,
--     Description TEXT NOT NULL,
--     Name TEXT NOT NULL
-- );

-- -- Table for holding the different workout levels
-- CREATE TABLE Workout_Level(
--     Level_ID INTEGER PRIMARY KEY,
--     Description TEXT NOT NULL,
--     Name TEXT NOT NULL
-- );

-- -- Table for exercises
-- CREATE TABLE Exercise(
--     Exercise_ID INTEGER PRIMARY KEY,
--     Ex_Name TEXT NOT NULL,
--     Description TEXT NOT NULL
-- );

-- -- Table to merge Exercise and Workout_Category
-- CREATE TABLE Exercise_Category(
--     Ex_Cat_ID INTEGER PRIMARY KEY,
--     Exercise_ID INTEGER,
--     Cat_ID INTEGER,
--     Num_Of_Exercises TEXT NOT NULL,
--     FOREIGN KEY (Exercise_ID) REFERENCES Exercise(Exercise_ID),
--     FOREIGN KEY (Cat_ID) REFERENCES Workout_Category(Cat_ID)
-- );

-- -- Table to merge Exercise and Workout_Level 
-- CREATE TABLE Exercise_Level(
--     Ex_Level_ID INTEGER PRIMARY KEY,
--     Exercise_ID INTEGER,
--     Level_ID INTEGER,
--     Default_Target_Sets INTEGER NOT NULL,
--     Default_Target_Reps INTEGER NOT NULL,
--     FOREIGN KEY (Exercise_ID) REFERENCES Exercise(Exercise_ID),
--     FOREIGN KEY (Level_ID) REFERENCES Workout_Level(Level_ID)
-- );

--- ******************************************************************** ---


