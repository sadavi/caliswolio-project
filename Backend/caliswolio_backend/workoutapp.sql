-- Table for levels
CREATE TABLE Level(
    Level_ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL
);

-- Table for exercises
CREATE TABLE Exercise(
    Exercise_ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Category TEXT NOT NULL,
    Level_ID INTEGER NOT NULL,
    Description TEXT,
    FOREIGN KEY (Level_ID) REFERENCES Level(Level_ID)
);

-- Table for member account
CREATE TABLE Member_account(
    Member_ID INTEGER PRIMARY KEY,
    Email TEXT NOT NULL,
    Password TEXT NOT NULL,
    Phone_Number TEXT NOT NULL,
    Level_ID INTEGER NOT NULL,
    Birth_Year INTEGER NOT NULL,
    Gender TEXT NOT NULL,
    Zipcode INTEGER NOT NULL,
    FOREIGN KEY (Level_ID) REFERENCES Level(Level_ID)
);

-- Table for workout templates
CREATE TABLE Template_Workout(
    Template_ID INTEGER PRIMARY KEY,
    Member_ID INTEGER NOT NULL,
    Level_ID INTEGER NOT NULL,
    Category TEXT NOT NULL,
    Name TEXT NOT NULL,
    FOREIGN KEY (Level_ID) REFERENCES Level(Level_ID),
    FOREIGN KEY (Member_ID) REFERENCES Member_Account(Member_ID)
);

-- Table for prior workouts
CREATE TABLE Prior_Workout(
    Prior_Workout_ID INTEGER PRIMARY KEY,
    Member_ID INTEGER NOT NULL,
    Level_ID INTEGER NOT NULL,
    Category TEXT NOT NULL,
    When_Completed DATE,
    FOREIGN KEY (Level_ID) REFERENCES Level(Level_ID)
    FOREIGN KEY (Member_ID) REFERENCES Member_Account(Member_ID)
);

-- Table for holding future workouts
CREATE TABLE Future_Workout(
    Future_Workout_ID INTEGER PRIMARY KEY,
    Member_ID INTEGER NOT NULL,
    Level_ID INTEGER NOT NULL,
    Category TEXT NOT NULL,
    Name TEXT NOT NULL,
    Perform_On DATE,
    FOREIGN KEY (Level_ID) REFERENCES Level(Level_ID)
    FOREIGN KEY (Member_ID) REFERENCES Member_Account(Member_ID)
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
    Prior_Workout_ID INTEGER NOT NULL,
    Target_Sets INTEGER,
    Target_Reps INTEGER,
    Position_In_List INTEGER NOT NULL,
    FOREIGN KEY (Exercise_ID) REFERENCES Exercise(ExerciseID),
    FOREIGN KEY (Prior_Workout_ID) REFERENCES Prior_Workout(Prior_Workout_ID)
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

---- ******************************************************************** ----
INSERT INTO Level (Level_ID, Name) 
VALUES
(1, "Beginner"),
(2, "Intermediate"),
(3, "Advanced");

INSERT INTO Exercise (Exercise_ID, Name, Category, Level_ID)
VALUES
(1, "Scapular Pull", "Pull-up", 1),
(2, "Arch hang", "Pull-up", 1),
(3, "Negative Pull-up", "Pull-up", 1),
(4, "Pull-up", "Pull-up", 2),
(5, "Wide Grip Pull-up", "Pull-up", 2),
(6, "L-sit Pull-up", "Pull-up", 3),
(7, "Muscle-up", "Pull-up", 3),
(8, "Vertical Push-up", "Push-up", 3),
(9, "Incline Push-up", "Push-up", 1),
(10, "Push-up", "Push-up", 1),
(11, "Decline Push-up", "Push-up", 1),
(12, "Diamond Push-up", "Push-up", 2),
(13, "Pike Push-up", "Push-up", 2),
(14, "Wall Assisted Handstand Push-up", "Push-up", 2),
(15, "Pseudo-planche Push-up", "Push-up", 2),
(16, "Freestanding Handstand Push-up", "Push-up", 3),
(17, "Decline Pseudo-planche Push-up", "Push-up", 3),
(18, "Planche Push-up", "Push-up", 3),
(19, "Magic Push-up", "Push-up", 3),
(20, "Static Dip Support Hold", "Dip", 1),
(21, "Negative Dip", "Dip", 1),
(22, "Seated Dip", "Dip", 1),
(23, "Parallel Bar Dip", "Dip", 2),
(24, "Straight Bar Dip", "Dip", 2),
(25, "Impossible Dip", "Dip", 3),
(26, "Vertical Row", "Row", 1),
(27, "Incline Row", "Row", 1),
(28, "Horizontal Row", "Row", 2),
(29, "Wide-grip Incline Row", "Row", 2),
(30, "Wide-grip Horizontal Row", "Row", 3),
(31, "Decline Row", "Row", 3),
(32, "Assisted Squat", "Squat", 1),
(33, "Air Squat", "Squat", 1),
(34, "Bulgarian Split Squat", "Squat", 1),
(35, "Beginner Shrimp Squat", "Squat", 2),
(36, "Intermediate Shrimp Squat", "Squat", 2),
(37, "Assisted Pistol Squat", "Squat", 2),
(38, "Advanced Shrimp Squat", "Squat", 3),
(39, "Pistol Squat", "Squat", 3),
(40, "Dragon Pistol Squat", "Squat", 3),
(41, "Romanian Deadlift", "Hinge", 1),
(42, "Single Leg Deadlift", "Hinge", 2),
(43, "Banded Nordic Curl Negative", "Hinge", 2),
(44, "Banded Nordic Curl", "Hinge", 3),
(45, "Nordic Curl", "Hinge", 3),
(46, "Full Plank", "Core", 1),
(47, "Half Plank", "Core", 1),
(48, "L-sit", "Core", 1),
(49, "Hanging Knee-raise", "Core", 1),
(50, "Sit-up", "Core", 1),
(51, "Crunch", "Core", 1),
(52, "Toe-touch", "Core", 1),
(53, "Superman Hold", "Core", 1),
(54, "Mountain Climber", "Core", 1),
(55, "Plank Row", "Core", 2),
(56, "Pseudo-planche Hold", "Core", 2),
(57, "Crow Hold", "Core", 2),
(58, "Leg Raise", "Core", 2),
(59, "Bicycle", "Core", 2),
(60, "Side Plank With Rotation", "Core", 2),
(61, "Banana Roll", "Core", 2),
(62, "Hanging L-sit", "Core", 2),
(63, "Hanging Leg Raise", "Core", 2),
(64, "Reverse Deadlift", "Core", 3),
(65, "Dragon Flag", "Core", 3),
(66, "Front Lever", "Core", 3),
(67, "Single-leg Straight Arm Side Plank", "Core", 3),
(68, "Planche Hold", "Core", 3);